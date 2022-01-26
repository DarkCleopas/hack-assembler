

from turtle import position


class Parser:

    # def __init__(self, tokens, position, current_token):

    def __init__(self, file_name):

        self.file_name = file_name
        
        self.tokens = self.load_tokens()

        self.position = 0

        self.current_token = ""



    def load_tokens(self):

        with open(self.file_name) as f:
            
            lines = map(lambda line: self.remove_comments(line).replace(" ", "").replace("\n", ""), f.readlines())
            
            tokens = [line for line in lines if line != ""]

            print(tokens)

            return tokens
    

    def remove_comments(self, line):

        j = 0
        for i in range(1, len(line)):
            if line[j] == line[i] == "/":
                return line[:j]
            j += 1

        return line

    
    def reset(self):
        
        self.position = 0

    
    def advance(self):

        self.current_token = self.tokens[self.position]

        self.position += 1


    def has_more_commands(self):
        
        return self.position < len(self.tokens)
    

    def next_command(self):

        self.advance()

        command = self.current_token

        if command[0] == "(": # LC command

            return ["Label", command[1:len(command)]]

        elif command[0] == "@": # AC command

            return ["At", command[1:len(command)]]
        
        else: # CC command

            dest, cmp, jmp = "", "", ""

            if "=" in command:

                dest = command.split("=")[0]
                rest = command.split("=")[1]

                if ";" in rest:
                    cmp = command.split(";")[0]
                    jmp = command.split(";")[1]
                else:
                    cmp = rest

            else:

                if ";" in command:
                    cmp = command.split(";")[0]
                    jmp = command.split(";")[1]
                else:
                    cmp = command
            
            return [dest, cmp, jmp]

                