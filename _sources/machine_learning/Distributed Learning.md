# Distributed Learning
Learn how the training of deep models can be distributed across multiple machines.
Map Reduce
Map Reduce can be described on the following steps:

1. Split your training set, in batches (ex: divide by the number of workers on your farm: 4)
2. Give each machine of your farm 1/4th of the data
3. Perform Forward/Backward propagation, on each computer node (All nodes share the same model)
4. Combine results of each machine and perform gradient descent
5. Update model version on all nodes.