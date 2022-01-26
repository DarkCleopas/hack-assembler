from os import path, listdir
import sys

from Parser import Parser 
from SymbolTable import SymbolTable
from Code import Code



def write_line(file_path, line):

    with open(file_path, "a") as f:
        f.write(line + "\n")


def first_step(p: Parser, st: SymbolTable):

    current_address = 0

    while p.has_more_commands():

        command = p.next_command()

        if command[0] == "Label" or command[0] == "At":

            current_address += 1
        
        elif len(command) == 3:

            st.add_entry(command[1], current_address)


def second_step(p: Parser, st: SymbolTable, file_path):

    with open(file_path, "w") as f:
        f.write("")

    code = Code()

    var_address = 16

    print(f"Assembling to {file_path}\n")

    while p.has_more_commands():

        command = p.next_command()

        if len(command) == 3: # CC command

            # print(command)

            write_line(file_path, code.gen_CC_command(command[0], command[1], command[2]))

        if command[0] == "At": # AC command

            address, has_addres = st.get_address(command[1])

            if has_addres:

                write_line(file_path, code.gen_AC_command(address))
            
            else:

                try:

                    address = int(command[1])

                    write_line(file_path, code.gen_AC_command(address))

                except ValueError:

                    st.add_entry(command[1], var_address)
                    write_line(file_path, code.gen_AC_command(var_address))
                    var_address += 1
                
                    

def main():

    try:
        if path.isdir(sys.argv[1]):
            files = listdir(sys.argv[1])
            real_path = path.realpath(sys.argv[1])
            for file in files:
                if file.endswith('.asm'):

                    file_path = real_path + "/" + file

                    p = Parser(file_path)
                    st = SymbolTable()

                    first_step(p, st)

                    p.reset()

                    second_step(p, st, file_path.replace(".asm", ".hack"))

        elif path.isfile(sys.argv[1]):

            p = Parser(sys.argv[1])
            st = SymbolTable()

            first_step(p, st)

            p.reset()

            second_step(p, st, sys.argv[1].replace(".asm", ".hack"))

        else:
            raise FileNotFoundError
            
        
    except FileNotFoundError:

        print("File not found.")

if __name__ == "__main__":

    main()