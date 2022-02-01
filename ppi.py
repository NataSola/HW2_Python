from cmath import pi
import math

def pi_chudnovsky(one=1000000):
    """
    Calculate pi using Chudnovsky's series

    This calculates it in fixed point, using the value for one passed in
    """
    k = 1
    a_k = one
    a_sum = one
    b_sum = 0
    C = 640320
    C3_OVER_24 = C**3 // 24
    while 1:
        a_k *= -(6*k-5)*(2*k-1)*(6*k-1)
        a_k //= k*k*k*C3_OVER_24
        a_sum += a_k
        b_sum += k * a_k
        k += 1
        if a_k == 0:
            break
    total = 13591409*a_sum + 545140134*b_sum
    pi = (426880*sqrt(10005*one, one)*one) // total
    return pi

def sqrt(n, one):
     """
     Return the square root of n as a fixed point number with the one
     passed in.  It uses a second order Newton-Raphson convergence.  This
     doubles the number of significant figures on each iteration.
     """
     # Use floating point arithmetic to make an initial guess
     floating_point_precision = 10**16
     n_float = float((n * floating_point_precision) // one) / floating_point_precision
     x = (int(floating_point_precision * math.sqrt(n_float)) * one) // floating_point_precision
     n_one = n * one
     while 1:
         x_old = x
         x = (x + n_one // x) // 2
         if x == x_old:
             break
     return x

print(pi_chudnovsky(one=10000000000000))
print(pi)