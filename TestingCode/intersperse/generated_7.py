from typing import List 

def intersperse(numbers: List[int], delimeter: int) -> List[int]: 
    """ Insert a number \'delimeter\' between every two consecutive elements of input list `numbers\' >>> intersperse([], 4) [] >>> intersperse([1, 2, 3], 4) [1, 4, 2, 4, 3] """ 
    return [numbers[0]] + [numbers[i] for i in range(1, len(numbers), 2)] + [delimeter] + [numbers[i] for i in range(2, len(numbers), 2)] if len(numbers) > 1 else [numbers[0]] if len(numbers) == 1 else [] 