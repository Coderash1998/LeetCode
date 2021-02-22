class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        a=[]
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                if prices[i]>=prices[j]:
                    a.append(prices[i]-prices[j])
                    break
                elif j==len(prices)-1:
                    a.append(prices[i])
        a.append(prices[len(prices)-1])
        return a