class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        d={}
        for i in cpdomains:
            c,dom=i.split(" ")
            d[dom]=d.get(dom,0)+int(c)
            while(len(dom.split(".",1))>1):
                dom=dom.split(".",1)[1]
                d[dom]=d.get(dom,0)+int(c)
        ans=[]
        for k,i in d.items():
            ans.append(str(i)+" "+k)
        return ans