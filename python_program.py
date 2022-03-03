from typing import List


def sum67(nums):
    """
    Gets the sum of the numbers in the array, except ignore sections of numbers starting with a 6
    and extending to the next 7
     param: nums(list): A list of numbers.
    return: Number of sum
    """
    new_list = []
    while 6 in nums:
        index_six = nums.index(6)
        new_list.extend(nums[:index_six])
        nums = nums[index_six:]
        nums = nums[nums.index(7) + 1:]
    new_list.extend(nums)
    print("blablabla - new changes")
    return sum(new_list)

def new_very_important_feature(input_list: List[int]):
    return input_list[::-1]


def main():
    print(sum67(new_very_important_feature([1, 2, 3, 4, 5, 6, 7, 2, 3, 6, 2, 3, 7, 0, 1])))
    print(sum67([]))


if __name__ == "__main__":
    main()
