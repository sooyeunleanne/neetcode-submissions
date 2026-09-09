class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            if num not in freq:
                freq[num] = 0
            
            freq[num] += 1
        
        freq = list(sorted(freq.items(), key = lambda x : x[1], reverse = True))
        
        answer = []
        for i in range(k):
            answer.append(freq[i][0])
        
        return answer