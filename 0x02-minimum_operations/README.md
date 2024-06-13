# Minimum Operations

Exercise to practice for interviews

## Context

### 0. Minimum Operations

In a text file, there is a single character `H`. Your text editor can execute only two operations in this file: `Copy All` and `Paste`. Given a number `n`, write a method that calculates the fewest number of operations needed to result in exactly `n` `H` characters in the file.

* Prototype: `def minOperations(n)`
* Returns an integer
* If `n` is impossible to achieve, return 0

```
$ cat 0-main.py
#!/usr/bin/python3
"""
Main file for testing
"""

minOperations = __import__('0-minoperations').minOperations

n = 4
print("Min number of operations to reach {} characters: {}".format(n, minOperations(n)))

n = 12
print("Min number of operations to reach {} characters: {}".format(n, minOperations(n)))

$ ./0-main.py
Min number of operations to reach 4 characters: 4
Min number of operations to reach 12 characters: 7
$
```

### Example:

n = 9

H => Copy All => Paste => HH => Paste =>HHH => Copy All => Paste => HHHHHH => Paste => HHHHHHHHH

Number of operations: 6

## Approach1
Think Greedily.
We can get n by copying the current number of Hs and pasting it (n / current Hs) times.
but to do that n must be divisible by the current number of Hs.
As we start with 1, we can get any n,
but we want to get n with the minimum number of operations,
so we need to copy when the condition is met. else we can only paste the current Hs until we get n.


## Approach2
The min number of operations is the sum of the prime factors of n.
because if you want to double the number of Hs, you need to copy all the Hs and paste them 1 time
=> x2 = +2 operations.
and so
if you want to triple the number of Hs, you need to copy the Hs and paste them 2 time => x3 = +3 operations.
and
if you want to multiply the number of Hs by 5, you need to copy the Hs and paste them 4 time => x5 = +4 operations. and so on.
For example,
9 = (1) * 3 * 3, so the answer is 3 + 3 = 6.
We start with 1 H, to triple it we need 3 ops, and to triple it again we need 3 ops, so 3 + 3 = 6.

4 = (1) * 2 * 2, so the answer is 2 + 2 = 4.
We start with 1 H, to double it we need 2 ops, and to double it again we need 2 ops, so 2 + 2 = 4.

12 = (1) * 2 * 2 * 3, so the answer is 2 + 2 + 3 = 7.
