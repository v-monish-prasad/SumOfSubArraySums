# OBSERVATIONS
#
# [1, 2, 3]
#
# MANUAL
# 1
# 2
# 3
# 12
# 23
# 123
#
# TRACING
# res += 1 * 1 * 3 = 3
# res += 2 * 2 * 2 = 3 + 8 = 11
# res += 3 * 3 * 1 = 11 + 9 = 20
#
# [2, 1, 3]
#
# MANUAL
# 2
# 1
# 3
# 21
# 13
# 213
#
# TRACING
# res += 2 * 1 * 3 = 6
# res += 1 * 2 * 2 = 6 + 4 = 10
# res += 3 * 3 * 1 = 10 + 9 = 19


def findSumOfSubArraySum(array, length):
    if not array:
        return "Empty Array."

    resultSum = 0

    for i in range(length):
        resultSum += array[i] * (i + 1) * (length - i)  # this represents the number of occurrences of an element in all sub-arrays

    return resultSum


if __name__ == "__main__":
    array = list(map(int, input().strip('[').strip(']').split(',')))
    length = len(array)
    print(findSumOfSubArraySum(array, length))
