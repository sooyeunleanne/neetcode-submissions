class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        res, curr = [], []
        candidates.sort()

        def bt(start, remaining):
            if remaining == 0:
                res.append(curr[:])
                return
            
            for j in range(start, len(candidates)):
                # skip duplicates
                if j > start and candidates[j] == candidates[j-1]:
                    continue
                
                # too big
                if candidates[j] > remaining:
                    break
                
                curr.append(candidates[j])
                bt(j + 1, remaining - candidates[j])

                curr.pop()
        
        bt(0, target)

        return res
