from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]

    return

"""
#for testing
if __name__ == "__main__":
    example_nums = [3,3]
    example_target = 6
    
    print(f"Input: {example_nums}, target = {example_target}")
    result = twoSum(example_nums, example_target)
    print(f"Output: {result}")
    
"""