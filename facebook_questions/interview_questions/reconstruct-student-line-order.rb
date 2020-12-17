# You are given a set of students represented by a tuple of (relative_height, # of students taller than student ahead in line)
# In other words, the first value of the tuple represents the relative height
# of the student in the class with 1 being the shortest, and the second value
# is the number of other students ahead of the given student that are taller
# than them. Each student only knows how many students are taller.

# Given this set, reconstruct the original line order and return the order in an array with
# the first element being the front of the line.

# Example:

# Input: Set({(4,1), (3,0), (5,1), (2,3), (1,3)})
# Output: This pretty much will give away the algorithm, but below is an example:

# [3, 5, 4, 1, 2]
