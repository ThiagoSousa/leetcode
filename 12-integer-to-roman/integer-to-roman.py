class Solution:



    def intToRoman(self, num: int) -> str:

        if num == 0:
            return ""
        
        symbol_map = [(1,"I"), (5, "V"), (10, "X"), (50, "L"), (100, "C"), (500, "D"), (1000, "M")]

        i = 0
        while i<len(symbol_map):
            if symbol_map[i][0]>num:
                break
            i += 1

        print(num, i)

        if str(num)[0] not in ["4", "9"]:
            print("\t", symbol_map[i-1][1])
            return symbol_map[i-1][1]+self.intToRoman(num-symbol_map[i-1][0])
        elif str(num)[0]=="4":
            print("\t", symbol_map[i-1][1]+symbol_map[i][1])
            return symbol_map[i-1][1]+symbol_map[i][1]+self.intToRoman(num-symbol_map[i-1][0]*int(str(num)[0]))
        elif str(num)[0]=="9":
            print("\t", symbol_map[i-2][1]+symbol_map[i][1])
            return symbol_map[i-2][1]+symbol_map[i][1]+self.intToRoman(num-symbol_map[i-2][0]*int(str(num)[0]))
        


        