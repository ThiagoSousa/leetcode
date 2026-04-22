class Solution:
    def toHex(self, num: int) -> str:
        hex_map = {10: "a", 11:"b", 12:"c", 13:"d", 14:"e", 15:"f"}
        if num == 0:
            return "0"
        if num<0:
            num += 4294967296

        hex_num = []
        while num>=1:
            hex_num.append(int(num%16))
            num /= 16

        hex_num = [str(i) if i<10 else hex_map[i] for i in hex_num[::-1]]
        return "".join(hex_num)