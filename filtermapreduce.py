from functools import reduce

nums = [2,3,4,6,9,8,6,2,4]

evens = list(filter(lambda n: n%2 == 0, nums))

doubles = list (map(lambda n: n*2, evens))

print(doubles)

sum = reduce(lambda a,b: a+b, doubles)


print(sum)