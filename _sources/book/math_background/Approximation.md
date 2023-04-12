# Approximation
An approximation is anything that is intentionally similar but not exactly equal to something else.

## In Mathematics

Approximation theory is a branch of mathematics, a quantitative part of functional analysis. Diophantine approximation deals with approximations of real numbers by rational numbers.

Approximation usually occurs when an exact form or an exact numerical number is unknown or difficult to obtain. However some known form may exist and may be able to represent the real form so that no significant deviation can be found. For example, 1.5 × 106 means that the approximation 1,500,000 has been measured to the nearest hundred thousand (the actual value is somewhere between 1,450,000 and 1,550,000), this is in contrast to the notation 1.500 × 106 which measures 1,500,000 to the nearest thousand (therefore giving a true value somewhere between 1,499,500 and 1,500,500).

It also is used when a number is not rational, such as the number π, which often is shortened to 3.14159, or 1.414 as the shortened form of √2.

Numerical approximations sometimes result from using a small number of significant digits. Calculations are likely to involve rounding errors and other approximation errors. Log tables, slide rules and calculators produce approximate answers to all but the simplest calculations. The results of computer calculations are normally an approximation expressed in a limited number of significant digits, although they can be programmed to produce more precise results.[3] Approximation can occur when a decimal number cannot be expressed in a finite number of binary digits.

Related to approximation of functions is the asymptotic value of a function, i.e. the value as one or more of a function's parameters becomes arbitrarily large. For example, the sum (k/2)+(k/4)+(k/8)+...(k/2^n) is asymptotically equal to k. No consistent notation is used throughout mathematics and some texts use ≈ to mean approximately equal and ~ to mean asymptotically equal whereas other texts use the symbols the other way around.

## Optimal polynomials
Once the domain (typically an interval) and degree of the polynomial are chosen, the polynomial itself is chosen in such a way as to minimize the worst-case error. That is, the goal is to minimize the maximum value of 
∣
�
(
�
)
−
�
(
�
)
∣{\displaystyle \mid P(x)-f(x)\mid }, where P(x) is the approximating polynomial, f(x) is the actual function, and x varies over the chosen interval. For well-behaved functions, there exists an Nth-degree polynomial that will lead to an error curve that oscillates back and forth between 
+
�+\varepsilon  and 
−
�-\varepsilon  a total of N+2 times, giving a worst-case error of 
�\varepsilon . It is seen that there exists an Nth-degree polynomial that can interpolate N+1 points in a curve. That such a polynomial is always optimal is asserted by the equioscillation theorem. It is possible to make contrived functions f(x) for which no such polynomial exists, but these occur rarely in practice.

For example, the graphs shown to the right show the error in approximating log(x) and exp(x) for N = 4. The red curves, for the optimal polynomial, are level, that is, they oscillate between 
+
�+\varepsilon  and 
−
�-\varepsilon  exactly. Note that, in each case, the number of extrema is N+2, that is, 6. Two of the extrema are at the end points of the interval, at the left and right edges of the graphs.


Error P(x) − f(x) for level polynomial (red), and for purported better polynomial (blue)
To prove this is true in general, suppose P is a polynomial of degree N having the property described, that is, it gives rise to an error function that has N + 2 extrema, of alternating signs and equal magnitudes. The red graph to the right shows what this error function might look like for N = 4. Suppose Q(x) (whose error function is shown in blue to the right) is another N-degree polynomial that is a better approximation to f than P. In particular, Q is closer to f than P for each value xi where an extreme of P−f occurs, so

    |Q(x_{i})-f(x_{i})|<|P(x_{i})-f(x_{i})|.

When a maximum of P−f occurs at xi, then
    Q(x_{i})-f(x_{i})\leq |Q(x_{i})-f(x_{i})|<|P(x_{i})-f(x_{i})|=P(x_{i})-f(x_{i}),

And when a minimum of P−f occurs at xi, then
    f(x_{i})-Q(x_{i})\leq |Q(x_{i})-f(x_{i})|<|P(x_{i})-f(x_{i})|=f(x_{i})-P(x_{i}).

So, as can be seen in the graph, [P(x) − f(x)] − [Q(x) − f(x)] must alternate in sign for the N + 2 values of xi. But [P(x) − f(x)] − [Q(x) − f(x)] reduces to P(x) − Q(x) which is a polynomial of degree N. This function changes sign at least N+1 times so, by the Intermediate value theorem, it has N+1 zeroes, which is impossible for a polynomial of degree N.


## Chebyshev approximation
One can obtain polynomials very close to the optimal one by expanding the given function in terms of Chebyshev polynomials and then cutting off the expansion at the desired degree. This is similar to the Fourier analysis of the function, using the Chebyshev polynomials instead of the usual trigonometric functions.

If one calculates the coefficients in the Chebyshev expansion for a function:


and then cuts off the series after the 
�
�
T_{N} term, one gets an Nth-degree polynomial approximating f(x).

The reason this polynomial is nearly optimal is that, for functions with rapidly converging power series, if the series is cut off after some term, the total error arising from the cutoff is close to the first term after the cutoff. That is, the first term after the cutoff dominates all later terms. The same is true if the expansion is in terms of bucking polynomials. If a Chebyshev expansion is cut off after 
�
�
T_{N}, the error will take a form close to a multiple of 
�
�
+
1
T_{{N+1}}. The Chebyshev polynomials have the property that they are level – they oscillate between +1 and −1 in the interval [−1, 1]. 
�
�
+
1
T_{{N+1}} has N+2 level extrema. This means that the error between f(x) and its Chebyshev expansion out to 
�
�
T_{N} is close to a level function with N+2 extrema, so it is close to the optimal Nth-degree polynomial.

In the graphs above, note that the blue error function is sometimes better than (inside of) the red function, but sometimes worse, meaning that it is not quite the optimal polynomial. The discrepancy is less serious for the exp function, which has an extremely rapidly converging power series, than for the log function.

Chebyshev approximation is the basis for Clenshaw–Curtis quadrature, a numerical integration technique.

## Remez's algorithm

## Taylor approximation

## Exponential series

## Logarithmic approximation

## Universal approximation