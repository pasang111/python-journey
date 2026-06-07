# Range

# what is range and how can we use it in loops?
# range() is used to generate a sequence of numbers.

for i in range(4):
    print(i)

# range(4) starts from 0 and stops before 4
# output: 0 1 2 3

for num in range(3):
    print(num)

for nums in range(1, 5):
    print(nums)

# starts from 1 and stops before 5
# output: 1 2 3 4

for num in range(2, 11, 2):
    print(num)

# start from 2
# stop before 11
# move 2 steps each time

for j in range(2, 33, 4):
    print(j)

for k in range(11, 2, -1):
    print(k)

# -1 means move backwards
# start from 11 and stop before 2