
import datetime
import signal
import sys

from file_cpp import *
from file_hpp import *
from canonical import *
from write_makefile import *
from write_main import *
from color import *

def custom_signal_handler(signal, frame):
    sys.exit(1)

def time_now():
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime("%Y/%m/%d %H:%M:%S")
    return formatted_time

def header_BY(login):
    form = login + " <" + login + "@student.42.fr>"
    lentt = len(form)
    tr = 43 - lentt
    str = "/*   By: "
    str += form
    str += " " * tr
    str += "+#+  +:+       +#+        */\n"
    return str

def created_By(login):
    ttr = 18 - len(login)
    spaces = " " * ttr
    form = login + spaces + "#+#    #+#             */\n"
    return form

def update_By(login):
    spaces = " " * (17 - len(login))
    form = login + spaces +"###   ########.fr       */\n"
    return form

def ClassName(str,file):
    file.write("class " + str + "\n")
    file.write("{\n")
    file.write("\tpublic:\n")
    file.write("\t\t" + str + "();\n") # constr
    file.write("\t\t" + str + "(const "+ str +" &"+ str[0].lower() + str[-1].lower() + ");\n") # copy constr
    file.write("\t\t" + str + " &operator=(const " + str + " &" +  str[0].lower() + str[-1].lower() +");\n") # copy assi op
    file.write("\t\t~" + str + "();\n")
    file.write("};\n\n")


def for_head(stt,login):
    if not stt.strip():  # Check if the class name is empty or contains only spaces
        print("Invalid class name. Skipping...")
    else:
        with open((stt + ".hpp"), "w") as file:
            head(file,login,stt)
            file.write("#ifndef " + stt.upper() + "_HPP\n")
            file.write("#define " + stt.upper() + "_HPP\n\n")
            file.write("#include <iostream>\n\n")
            ClassName(stt,file)
            file.write("#endif\n")


def for_head1(stt,login):
    if not stt.strip():  # Check if the class name is empty or contains only spaces
        print("Invalid class name. Skipping...")
    else:
        with open((stt + ".cpp"), "w") as file:
            head1(file,login,stt)
            file.write("#include \"" + stt + ".hpp\"\n\n")
            file.write(cans(stt))

try:
    login = input(Green + "login > ")
    Color_Off
    class_name = input("class Name >> ").split(" ")
    if len(class_name) == 0:
        exit
    if not class_name:
        exit
    includes = ""
    for i in range(len(class_name)):
        includes += "#include \"" + class_name[i] + ".hpp\"\n"
        file_name = class_name[i]
        for_head(file_name,login)
        print(f"File {file_name}.hpp has been created in the current directory.")
        for_head1(file_name,login)
        print(f"File {file_name}.cpp has been created in the current directory.")

    with open(("Makefile"), "w") as file:
        file.write(make_writer())

    with open(("main.cpp"), "w") as file:
        head1(file,login,"main")
        file.write(includes)
        file.write(main_write())

except KeyboardInterrupt:
    pass
    print("\n"+ Red + "\tCtrl + C detected. Exiting..." + Color_Off)
    
except EOFError:
    pass
    print("\n" + Red + "\tCtrl + D detected. Exiting..." + Color_Off)