class Solution:
    
    def process_line(self, current_line, maxWidth, is_last_line):
        diff = maxWidth-sum([len(w) for w in current_line])
        space_vector = [1 for _ in range(len(current_line)-1)]
        diff -= len(space_vector)
        if not is_last_line:
            j = 0
            while len(space_vector) and diff>0:
                print(j, len(space_vector))
                space_vector[j] += 1
                diff -= 1
                j = (j+1)%len(space_vector)        
        current_line_str = ""
        for j in range(len(current_line)-1):
            current_line_str += current_line[j]+" "*space_vector[j]
        current_line_str += current_line[-1]
        if diff>0:
            current_line_str+= " "*diff
        return current_line_str
    
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        lines = []
        i = 0
        current_line = []
        current_size = 0
        while i<len(words):
            print(i)
            if current_size+len(words[i])<=maxWidth:
                current_line.append(words[i])
                current_size += len(words[i])+1
                i += 1
            else:
                lines.append(self.process_line(current_line, maxWidth, False))
                current_size = 0
                current_line = []
        if current_line:
            lines.append(self.process_line(current_line, maxWidth, True))
        return lines          
                
            