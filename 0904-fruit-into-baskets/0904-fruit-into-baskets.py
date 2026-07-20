class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        maxi=0
        l=0
        r=0
        mydict={}
        n=len(fruits)
        while  r<n:
            mydict[fruits[r]]=mydict.get(fruits[r],0)+1
            if len(mydict)>2:
                mydict[fruits[l]]-=1
                if mydict[fruits[l]]==0:
                    del mydict[fruits[l]]

                l+=1
            if len(mydict)<=2:
                maxi=max(maxi,r-l+1)
            r+=1    
        return maxi                