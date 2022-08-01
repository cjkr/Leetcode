# There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

# Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

# The test cases are generated so that the answer will be less than or equal to 2 * 109.

m = 3
n = 7
output = 28

# m = 3
# n = 2
# output = 3


def uniquePaths(m, n):

    grid = []

    for i in range(m):
        l = []
        for j in range(n):
            left_val = 1 if j == 0 else l[j - 1]
            top_val = 0 if i == 0 else grid[i - 1][j]
            val = 1 if j == 0 else top_val + left_val
            l.append(val)
        grid.append(l)

    return grid[-1][-1]


print(uniquePaths(m, n))
