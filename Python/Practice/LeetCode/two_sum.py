nums = [3, 2, 4]
target = 6

def main(): 
    index = 0 
    for number_1 in nums:
        for number_2 in nums: 
            if (number_1 + number_2) == target:
                        index_2 = getIndex(number_2, nums)
                        if index != index_2:
                            answer = [index, index_2]
                            print(answer)
        index += 1


def getIndex(number, numbers):
    index = 0 
    for num in numbers:
        if num == number: 
            return index
        index += 1

main()