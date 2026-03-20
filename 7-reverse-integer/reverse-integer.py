class Solution:
    def reverse(self, x: int) -> int:
        str_x = str(x)
        is_negative = True if "-" in str_x else False
        if is_negative:
            str_x = str_x[1:]
        str_x = str_x[::-1]
        if is_negative:
            lower_range = "2147483648"
            if len(str_x)>len(lower_range):
                return 0
            elif len(str_x)<len(lower_range):
                return int(str_x)*-1
            else:
                for i in range(len(str_x)):
                    if int(str_x[i])>int(lower_range[i]):
                        return 0
                    elif int(str_x[i])<int(lower_range[i]):
                        return int(str_x)*-1
            return int(str_x)*-1
        else:
            upper_range = "2147483647"
            if len(str_x)>len(upper_range):
                return 0
            elif len(str_x)<len(upper_range):
                return int(str_x)
            else:
                for i in range(len(str_x)):
                    if int(str_x[i])>int(upper_range[i]):
                        return 0
                    elif int(str_x[i])<int(upper_range[i]):
                        return int(str_x)

                return int(str_x)
        return int(str_x)
            
        
