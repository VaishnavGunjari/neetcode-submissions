class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        res=[]
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        f=sorted(d.values(), reverse=True)
        for key,value in d.items():
            if value >= f[k-1]:
                res.append(key)
        return res[:k]
