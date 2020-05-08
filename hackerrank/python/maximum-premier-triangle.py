#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations


# Complete the maximumPerimeterTriangle function below.
def maximumPerimeterTriangle(sticks):
    a = list(combinations(sticks, 3))
    ans = [(-1,)]
    s=-1
    for i in range(len(a)):
        if a[i][0] + a[i][1] > a[i][2]:
            sa=a[i][0]+a[i][1]+a[i][2]
            if s<sa:
                ans=[]
                ans.append(a[i])
                s=sa
    return ans[0]

if __name__ == '__main__':

    n = int(input())

    sticks = list(map(int, input().rstrip().split()))
    sticks.sort()
    result =maximumPerimeterTriangle(sticks)
    print(result)
    print(' '.join(map(str, result)))
