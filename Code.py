

class Code:

    def __init__(self):

        self.cmp_table = {
            "":  "0000000",
            "0": "0101010", "1": "0111111", "-1": "0111010", "D": "0001100",
            "A": "0110000", "!D": "0001101", "!A": "0110001", "-D": "0001111",
            "-A": "0110011", "D+1": "0011111", "A+1": "0110111", "D-1": "0001110",
            "A-1": "0110010", "D+A": "0000010", "D-A": "0010011", "A-D": "0000111",
            "D&A": "0000000", "D|A": "0010101",
            "M": "1110000", "!M": "1110001",
            "-M": "1110011", "M+1": "1110111",
            "M-1": "1110010", "D+M": "1000010", "D-M": "1010011", "M-D": "1000111",
            "D&M": "1000000", "D|M": "1010101"
	    }   

        self.dest_table = {
            "": "000", "M": "001", "D": "010",
		    "MD": "011", "A": "100", "AM": "101", "AD": "110", "AMD": "111"
        }

        self.jmp_table = {
            "": "000", "JGT": "001", "JEQ": "010",
		    "JGE": "011", "JLT": "100", "JNE": "101", "JLE": "110", "JMP": "111"
        }

    def comp(self, value):
        return self.cmp_table[value]
        
    def dest(self, value):
        return self.dest_table[value]

    def jump(self, value):
        return self.jmp_table[value]

    def convert_binary(self, value):
        s = bin(value)[2:]  
        repeat = 15 - len(s)  
        s = "0" * repeat + s  
        return s

    def gen_AC_command(self, addr):
        return "0" + self.convert_binary(addr)
    
    def gen_CC_command(self, dest, comp, jump):
	    return "111" + self.comp(comp) + self.dest(dest) + self.jump(jump)