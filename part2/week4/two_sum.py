import os.path

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "data/two_sum.txt")

numbers = []
with open(filename) as f:
    for line in f:
        numbers.append(int(line))

numbers.sort()
lo = 0
hi = len(numbers)-1

lower_bound = -10000
upper_bound = 10000

sum_set = set()
while lo < hi:
    target_sum = numbers[lo] + numbers[hi]
    if target_sum < lower_bound:
        lo += 1
    elif target_sum > upper_bound:
        hi -= 1
    else:
        temp_lo = lo
        temp_sum = numbers[temp_lo] + numbers[hi]
        while lower_bound <= temp_sum and temp_sum <= upper_bound:
            sum_set.add(temp_sum)
            temp_lo += 1
            temp_sum = numbers[temp_lo] + numbers[hi]
        hi -= 1
print(len(sum_set))