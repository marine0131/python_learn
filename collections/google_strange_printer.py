#! /usr/bin/env python

import numpy as np
import math
import sys

class Solution():
    def __init__(self, s):
        if not s or len(s) == 0:
            print 0

        n = len(s)

        f = np.zeros((n,n))
        for i in range(n):
            f[i][i] = 1

        for l in range(2, n+1):
            for i in range(0, n - l + 1):
                j = i + l - 1
                f[i][j] = 1 + f[i+1][j]
                for k in range(i+1, j):
                    if s[i] == s[k]:
                        f[i][j] = min(f[i][j], f[i+1][k]+f[k+1][j])

                if s[i] == s[j]:
                    f[i][j] = min(f[i][j], f[i+1][j])

        print s + ':' + str(int(f[0][n-1]))

if __name__ == '__main__':
    s = sys.argv[1]
    Solution(s)
