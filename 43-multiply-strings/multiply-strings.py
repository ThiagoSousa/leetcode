class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        if len(num2)>len(num1):
            aux = num1
            num1 = num2
            num2 = aux

        partials = []
        for i in range(len(num2)-1, -1, -1):

            rest = 0
            product = []
            for j in range(len(num1)-1, -1, -1):
                d = int(num1[j])*int(num2[i]) + rest
                rest = int(d/10)
                product.append(d%10)
            if rest>0:
                product.append(rest)
            partials.append(product[::-1]+[0]*(len(num2)-i-1))

        # print(partials)
        
        result = [0]*len(partials[-1])
        for num in partials:
            if len(num)<len(result):
                num = [0]*(len(result)-len(num)) + num
            # print(num)
            rest = 0
            for i in range(len(num)-1, -1, -1):
                result[i] += num[i]+rest
                rest = int(result[i]/10)
                result[i] %= 10
            if rest>0:
                if i-1>=0:
                    result[i-1] = rest
                else:
                    result = [rest]+result
            # print(result)
        i = 0
        while i<len(result) and result[i] == 0:
            i += 1
        result = "".join([str(d) for d in result[i:]])
        if result == "":
            return "0"
        return result
