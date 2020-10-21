from case2 import nums, target
import sys

delta = [target - n for n in nums]

for i, n in enumerate(nums):
    if n in delta:
        if delta.index(n) != i:
            print([i, delta.index(n)])
            sys.exit()
