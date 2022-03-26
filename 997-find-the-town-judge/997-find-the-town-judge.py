class Solution:
    def findJudge(self, n, trust):

        if len(trust)==0:
            return -1 if n>1 else 1
        hmap={}
        l=set()
        for trusti in trust:
            l.add(trusti[0])
            hmap[trusti[1]]=hmap.get(trusti[1],0)+1
        print(hmap)    
        for ele in hmap:
            if hmap[ele]==n-1  :
                if ele not in l:
                    return ele
                else:
                    return -1
        return -1