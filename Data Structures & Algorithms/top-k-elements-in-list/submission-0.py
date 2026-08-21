class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        number_frequency = {}

        for num in nums:
            number_frequency[num] = number_frequency.get(num, 0) + 1
        
        # lambda item: number_frequency[item] is an anonymous function (a function without a name).
        # It takes each item in the list (which is a number/key in your dictionary) and returns its frequency from the dictionary.
        sorted_by_frequency = list(sorted(number_frequency.keys(), key=lambda item: number_frequency[item], reverse=True))

        return sorted_by_frequency[0:k]