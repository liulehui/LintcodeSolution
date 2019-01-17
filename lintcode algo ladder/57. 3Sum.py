# coding:utf-8
def threeSum(numbers):
        # write your code here
        numbers.sort()
        results = []
        length = len(numbers)
        for i in range(0, length - 2):
            if i and numbers[i] == numbers[i - 1]:
                continue
            target = -numbers[i]
            left, right = i + 1, length - 1
            while left < right:
                if numbers[left] + numbers[right] == target:
                    results.append([numbers[i], numbers[left], numbers[right]])
                    right -= 1
                    left += 1
                    while left < right and numbers[left] == numbers[left - 1]:
                        left += 1
                    while left < right and numbers[right] == numbers[right + 1]:
                        right -= 1
                elif numbers[left] + numbers[right] > target:
                    right -= 1
                else:
                    left += 1
        return results