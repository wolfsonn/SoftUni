from collections import deque


def list_manipulator(numbers, *args):
    nums = numbers
    for argument in args:
        argument = [x for x in args]
        if "add" in argument and "beginning" in argument:
            nums = argument[2:] + nums
            return nums
        elif "add" in argument and "end" in argument:
            nums = nums + argument[2:]
            return nums
        elif "remove" in argument and "beginning" in argument:
            if len(argument) == 2:
                nums = nums[1:]
            else:
                nums = nums[argument[2]:]
            return nums
        elif "remove" in argument and "end" in argument:
            if len(argument) == 2:
                nums = nums[:-1]
            else:
                nums = nums[:-argument[2]]
            return nums


print(list_manipulator([1, 2, 3], "remove", "end"))
print(list_manipulator([1, 2, 3], "remove", "beginning"))
print(list_manipulator([1, 2, 3], "add", "beginning", 20))
print(list_manipulator([1, 2, 3], "add", "end", 30))
print(list_manipulator([1, 2, 3], "remove", "end", 2))
print(list_manipulator([1, 2, 3], "remove", "beginning", 2))
print(list_manipulator([1, 2, 3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1, 2, 3], "add", "end", 30, 40, 50))
