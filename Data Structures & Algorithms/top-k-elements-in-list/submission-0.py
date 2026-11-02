class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''Use the Umpire method
        Understand: 
        Inputs - an array of integers, and a single integer representing the kth most frequent 
        integers in the array.
        Output - a list of the kth most frequent integers in the array; order does not matter. i.e [4,1,3]
        Match:
        - hashmap can track the element and its frequency
        - An array of arrays (buckets) can represent the frequencies, array[2] = [2, 3, 4] means that the
            elements 2, 3, 4 have frequencies of 2
        '''
        frequencies = {}
        buckets = [[] for _ in range(len(nums) +1 )]
        for num in nums:
            frequencies[num] = frequencies.get(num, 0) + 1
        
        for num, count in frequencies.items():
            buckets[count].append(num)
        
        results = []
        for index in range(len(buckets) -1, 0, -1):
            for num in buckets[index]:
                results.append(num)
                if len(results) == k:
                    return results
        


