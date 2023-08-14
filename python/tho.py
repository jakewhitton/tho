"""Given an array of intervals where intervals[i] = [starti, endi], merge all
overlapping intervals, and return an array of the non-overlapping intervals
that cover all the intervals in the input.

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
"""

def jake_merge_intervals(intervals):
    
    # Adding a new interval [a, b] into a list of disjoint intervals has a few cases
    #   1. The new interval is disjoint already, just insert it
    #   2. The interval overlaps with exactly one interval but is disjoint with
    #      all others, extend that interval to include the new region
    #   3. The interval overlaps with more than one interval, 

    merged_intervals = []
    for interval in intervals:
        pass
        

    return merged_intervals
    
def tho_merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0]) # sort based on the start of each interval
    max_end = 0 # keep track of max interval end so far
    merged_result =[]
    for start, end in intervals:
        
        if start <= max_end and merged_result:
            last_interval = merged_result.pop()
            print("last interval: ", last_interval)
            new_start = min(start, last_interval[0])
            new_end = max(end, last_interval[1])
            max_end = new_end
            print("out:", (new_start, new_end))
            merged_result.append([new_start, new_end])
        else:
            max_end = end
            merged_result.append([start, end])
    
    
    return merged_result


test_cases = [
    {
        "input": [[1,3], [2,6], [8,10], [15,18]],
        "output": [[1,6], [8,10], [15,18]]
    },
    {
        "input": [[1,4], [4,5]],
        "output": [[1,5]]
    },
    {
        "input": [[2,3], [4,5], [6,7], [8,9], [1,10]],
        "output": [[2,3], [4,5], [6,7], [1,10]]
    }  
]

for author, solution in [('Tho', tho_merge_intervals), ('Jake', jake_merge_intervals)]:
    print(f'{author}:')
    
    for i, test_case in enumerate(test_cases):
        
        # Fetch solution output
        actual_output = None
        try:
            actual_output = solution(test_case["input"])
        except:
            pass

        expected_output = test_case["output"]
        if actual_output == expected_output:
            print(f'  test {i}...pass!')
        else:
            print(f'  test {i}...fail!')
            print(f'    expected_output = {expected_output}')
            print(f'    actual_output = {actual_output}')

        print()
    print()