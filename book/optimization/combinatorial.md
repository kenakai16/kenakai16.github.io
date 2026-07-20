# Combinatorial Optimization & Scheduling

Unlike continuous optimization where variables can take any decimal value, **Combinatorial Optimization** deals with problems where the variables are discrete (e.g., integers, binary choices, or ordering permutations). 

Many of these problems are **NP-hard**, meaning they cannot be solved to absolute perfection in polynomial time for large datasets. Instead, we use solvers and heuristics.

---

## 1. The Traveling Salesperson Problem (TSP)

In the **Traveling Salesperson Problem (TSP)**, a salesperson must visit a set of cities exactly once and return to the starting city. The goal is to find the **shortest possible route**.

### Formulation
Given a distance matrix $D$ where $d_{ij}$ is the distance from city $i$ to city $j$, we want to find a permutation of cities $\pi$ that minimizes:

$$\text{minimize} \quad \sum_{i=1}^{n-1} d_{\pi(i)\pi(i+1)} + d_{\pi(n)\pi(1)}$$

TSP is a classic routing problem used in logistics, package delivery, and microchip manufacturing.

---

## 2. The Job Shop Scheduling Problem (JSSP)

The **Job Shop Scheduling Problem (JSSP)** is one of the most famous scheduling problems in industrial engineering and operations research.

### Problem Definition:
- We have a set of **Jobs** (e.g., manufacturing specific products).
- Each Job consists of a sequence of **Tasks** that must be executed in a strict order.
- Each Task must be processed on a specific **Machine** for a given **duration**.
- **Constraints**:
  1. A machine can only process one task at a time (no overlap).
  2. Tasks of a single job must be processed in sequence.
- **Objective**: Minimize the **makespan** (the total time to complete all jobs).

---

## 3. Python Implementation: Solving JSSP with Google OR-Tools

We can use Google's **OR-Tools** (Constraint Programming CP-SAT solver) to solve a small JSSP instance.

### Instance Definition:
- **Job 0**: 
  - Task 1: Machine 0, duration 3
  - Task 2: Machine 1, duration 2
  - Task 3: Machine 2, duration 2
- **Job 1**:
  - Task 1: Machine 0, duration 2
  - Task 2: Machine 2, duration 1
  - Task 3: Machine 1, duration 4
- **Job 2**:
  - Task 1: Machine 1, duration 4
  - Task 2: Machine 2, duration 3

```python
from ortools.sat.python import cp_model

# 1. Initialize CP-SAT model
model = cp_model.CpModel()

# 2. Define data
jobs_data = [
    [(0, 3), (1, 2), (2, 2)],  # Job 0
    [(0, 2), (2, 1), (1, 4)],  # Job 1
    [(1, 4), (2, 3)]           # Job 2
]

num_machines = 3
all_machines = range(num_machines)
all_jobs = range(len(jobs_data))

# Find horizon (upper bound of makespan)
horizon = sum(task[1] for job in jobs_data for task in job)

# 3. Create variables
all_tasks = {}
machine_to_intervals = {m: [] for m in all_machines}

for job_id, job in enumerate(jobs_data):
    for task_id, task in enumerate(job):
        machine = task[0]
        duration = task[1]
        suffix = f"_{job_id}_{task_id}"
        
        start_var = model.NewIntVar(0, horizon, f"start{suffix}")
        end_var = model.NewIntVar(0, horizon, f"end{suffix}")
        interval_var = model.NewIntervalVar(start_var, duration, end_var, f"interval{suffix}")
        
        all_tasks[job_id, task_id] = (start_var, end_var, interval_var)
        machine_to_intervals[machine].append(interval_var)

# 4. Add overlap constraints (no two tasks on the same machine can overlap)
for machine in all_machines:
    model.AddNoOverlap(machine_to_intervals[machine])

# 5. Add precedence constraints (tasks of a job must run sequentially)
for job_id, job in enumerate(jobs_data):
    for task_id in range(len(job) - 1):
        model.Add(all_tasks[job_id, task_id + 1][0] >= all_tasks[job_id, task_id][1])

# 6. Define makespan objective (minimize the maximum end time)
makespan = model.NewIntVar(0, horizon, "makespan")
model.AddMaxEquality(makespan, [all_tasks[job_id, len(job) - 1][1] for job_id, job in enumerate(jobs_data)])
model.Minimize(makespan)

# 7. Solve
solver = cp_model.CpSolver()
status = solver.Solve(model)

if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
    print(f"Optimal Makespan: {solver.ObjectiveValue()}")
    for job_id, job in enumerate(jobs_data):
        for task_id, task in enumerate(job):
            start = solver.Value(all_tasks[job_id, task_id][0])
            print(f"Job {job_id}, Task {task_id} starts at {start}")
```

---

## Exercises

```{admonition} Exercise 1
:class: tip
Consider a JSSP with 2 machines ($M_0, M_1$) and 1 job. The job has 2 tasks:
- Task 0: requires $M_0$, duration = 4.
- Task 1: requires $M_1$, duration = 3.
What is the minimum makespan if Task 1 must follow Task 0?
```

```{admonition} Solution — Exercise 1
:class: dropdown
Since there is only one job, and Task 1 must wait for Task 0 to finish:
- Task 0 starts at $t=0$, ends at $t=4$.
- Task 1 starts at $t=4$ (earliest possible), ends at $t=4+3=7$.
The minimum makespan is **7**.
```
