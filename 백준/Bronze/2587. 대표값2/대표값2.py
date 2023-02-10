# 대표값 2

numbers = []
for _ in range(5) :
    numbers += [int(input())]
numbers.sort()

print(int(sum(numbers)/5))
print(numbers[2])