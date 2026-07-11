class Solution:
    def solve(self,ind,total,subset,nums,target,result):
        if total ==target:
            result.append(subset.copy())
            return
        elif total>target:
            return
        if ind>=len(nums):
            return  
        Sum=total+nums[ind]
        subset.append(nums[ind])
        self.solve(ind,Sum,subset,nums,target,result)
        Sum=total
        subset.pop()
        self.solve(ind+1,Sum,subset,nums,target,result)      
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result=[]
        self.solve(0,0,[],candidates,target,result)
        return result
        