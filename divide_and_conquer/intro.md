# Divide and conquer (DAC)
Is an algorithm design paradigm.

Is a programming technique, can be divided in:
1.  **Divide**: This involves dividing the problem into smaller sub-problems
2. **Conquer**: Solve sub-problems by calling resursively until solved
3. **Combine**:Combine the subproblems to get the final solution of the whole problem

Some DAC algorithms:
1. Quicksort
2. Mergesort
3. Closest Pair of Points
4. Strassen9s algorithm (matrices multiplications)
5. Cooley-Turkey Fast Fourir Transform (FFT) algorithm:
6. Karatsuba algorithm for fast multiplication

Scheme of a DAC

```
DAC(a, i, j)
{
    if(small(a, i, j))
      return(Solution(a, i, j))
    else 
      mid = divide(a, i, j)               // f1(n)
      b = DAC(a, i, mid)                 // T(n/2)
      c = DAC(a, mid+1, j)            // T(n/2)
      d = combine(b, c)                 // f2(n)
   return(d)
}
```

Then the recurrence is in the form $T(n)=aT(n/b)+D(n)+C(n)$