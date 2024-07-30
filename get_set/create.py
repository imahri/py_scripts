
from color import *
import re

def arr_empty(stt):
    opening_bracket_index = stt.find("[")
    closing_bracket_index = stt.find("]")
    res = stt[opening_bracket_index+1:closing_bracket_index]
    if len(res) >= 1:
        return 0
    else:
        return 1

def checked(stt):
    opening_bracket_index = stt.find("[")
    closing_bracket_index = stt.find("]")
    flag = 0
    if opening_bracket_index != -1 and closing_bracket_index != -1 and opening_bracket_index < closing_bracket_index:
        if len(stt[:opening_bracket_index]) != 0:
            print("Pattern is matched")
        else:
            print("Pattern is not matched")
            flag = 1
    else:
        print("Pattern is not matched")
        flag = 1
    return flag

# std::string
def for_str(str, class_name):
    nam = ""
    if checked(str) == 0 and arr_empty(str) == 0:
        opening_bracket_index = str.find("[")
        str = str[:opening_bracket_index]
        nam = "\nstd::string " + class_name + "::get" + str.capitalize() + "(int index)\n{\n\treturn " + str + "[index];\n}\n\n"
        nam += "void " + class_name + "::set" + str.capitalize() + "(std::string " + str + ")\n{\n\tthis->" + str + "[index] = " + str + ";\n}\n\n"
    else :
        nam = "\nstd::string " + class_name + "::get" + str.capitalize() + "()\n{\n\treturn " + str + ";\n}\n\n"
        nam += "void " + class_name + "::set" + str.capitalize() + "(std::string " + str + ")\n{\n\tthis->" + str + " = " + str + ";\n}\n\n"
    return nam

# int
def for_int(str, class_name):
    if checked(str) == 0 and arr_empty(str) == 0:
        opening_bracket_index = str.find("[")
        str = str[:opening_bracket_index]
        nam = "\nint " + class_name + "::get" + str.capitalize() +  "(int index)\n{\n\treturn " + str + "[index];\n}\n\n"
        nam += "void " + class_name + "::set" + str.capitalize() + "(int " + str + ")\n{\n\tthis->" + str + "[index] = " + str + "[index];\n}\n\n"
    else:
        nam = "\nint " + class_name + "::get" + str.capitalize() +  "()\n{\n\treturn " + str + ";\n}\n\n"
        nam += "void " + class_name + "::set" + str.capitalize() + "(int " + str + ")\n{\n\tthis->" + str + " = " + str + ";\n}\n\n"
    return nam

# double
def for_double(str, class_name):
    if checked(str) == 0 and arr_empty(str) == 0:
        opening_bracket_index = str.find("[")
        str = str[:opening_bracket_index]
        nam = "\ndouble " + class_name + "::get" + str.capitalize() +  "(int index)\n{\n\treturn " + str + "[index];\n}\n\n"
        nam += "void " + class_name + "::set" + str.capitalize() + "(double " + str + ")\n{\n\tthis->" + str + "[index] = " + str + ";\n}\n\n"
    else:
        nam = "\ndouble " + class_name + "::get" + str.capitalize() +  "()\n{\n\treturn " + str + ";\n}\n\n"
        nam += "void " + class_name + "::set" + str.capitalize() + "(double " + str + ")\n{\n\tthis->" + str + " = " + str + ";\n}\n\n"
    return nam

# float
def for_float(str, class_name):
    if checked(str) == 0 and arr_empty(str) == 0:
        opening_bracket_index = str.find("[")
        str = str[:opening_bracket_index]
        nam = "\nfloat " + class_name + "::get" + str.capitalize() +  "(int index)\n{\n\treturn " + str + "[index];\n}\n\n"
        nam += "void " + class_name + "::set" + str.capitalize() + "(float " + str + ")\n{\n\tthis->" + str + "[index] = " + str + ";\n}\n\n"
    else:
        nam = "\nfloat " + class_name + "::get" + str.capitalize() +  "()\n{\n\treturn " + str + ";\n}\n\n"
        nam += "void " + class_name + "::set" + str.capitalize() + "(float " + str + ")\n{\n\tthis->" + str + " = " + str + ";\n}\n\n"
    return nam

# bool
def for_boolean(str, class_name):
    if checked(str) == 0 and arr_empty(str) == 0:
        opening_bracket_index = str.find("[")
        str = str[:opening_bracket_index]
        nam = "\nboolean " + class_name + "::get" + str.capitalize() +  "(int index)\n{\n\treturn " + str + "[index];\n}\n\n"
        nam += "void " + class_name + "::set" + str.capitalize() + "(boolean " + str + ")\n{\n\tthis->" + str + "[index] = " + str + ";\n}\n\n"
    else:
        nam = "\nboolean " + class_name + "::get" + str.capitalize() +  "()\n{\n\treturn " + str + ";\n}\n\n"
        nam += "void " + class_name + "::set" + str.capitalize() + "(boolean " + str + ")\n{\n\tthis->" + str + " = " + str + ";\n}\n\n"
    return nam

# char
def for_char(str, class_name):
    if checked(str) == 0 and arr_empty(str) == 0:
        opening_bracket_index = str.find("[")
        str = str[:opening_bracket_index]
        nam = "\nchar " + class_name + "::get" + str.capitalize() +  "(int index)\n{\n\treturn " + str + "[index];\n}\n\n"
        nam += "void " + class_name + "::set" + str.capitalize() + "(char " + str + ")\n{\n\tthis->" + str + "[index] = " + str + ";\n}\n\n"
    else:
        nam = "\nchar " + class_name + "::get" + str.capitalize() +  "()\n{\n\treturn " + str + ";\n}\n\n"
        nam += "void " + class_name + "::set" + str.capitalize() + "(char " + str + ")\n{\n\tthis->" + str + " = " + str + ";\n}\n\n"
    return nam

# char*
def for_char_p(str, class_name):
    nam = "\nchar " + class_name + "::get" + str.capitalize() +  "()\n{\n\treturn *" + str + ";\n}\n\n"
    nam += "void " + class_name + "::set" + str.capitalize() + "(char &" + str + ")\n{\n\tthis->" + str + " = &" + str + ";\n}\n\n"
    return nam

def tesstter(var_type, str, typo):
    nam = ""
    if typo == 1:
        nam = "\n" + var_type + class_name + "::get" + str.capitalize() + "()\n{\n\treturn *" + str + ";\n}\n\n"
        nam += "void " + class_name + "::set" + str.capitalize() + "(char &" + str + ")\n{\n\tthis->" + str + " = &" + str + ";\n}\n\n"
    elif typo == 2:
        nam = "\n" + var_type + " " + class_name + "::get" + str.capitalize() + "()\n{\n\treturn " + str + ";\n}\n\n"
        nam += "void " + class_name + "::set" + str.capitalize() + "(" + var_type + " " + str + ")\n{\n\tthis->" + str + " = " + str + ";\n}\n\n"
    elif typo == 3:
        nam = "\n" + var_type[:-1] + " " + class_name + "::get" + str.capitalize() + "()\n{\n\treturn *" + str + ";\n}\n\n"
        nam += "void " + class_name + "::set" + str.capitalize() + "(char &" + str + ")\n{\n\tthis->" + str + " = &" + str + ";\n}\n\n"
    elif typo == 4:
        nam = "\n" + var_type + class_name + "::get" + str.capitalize() + "(int index)\n{\n\treturn *" + str + "[index];\n}\n\n"
        nam += "void " + class_name + "::set" + str.capitalize() + "(" + var_type + " " + str + ", int i)\n{\n\tthis->" + str + "[index] = " + str + ";\n}\n\n"
    return nam


def for_other(varr,var_type,yt):
    quss = "\n" + BIPurple + "\tfor the " + str(yt) + " attribute:\n" + Color_Off
    quss += BICyan + "type : " + Color_Off + BGreen +var_type + Color_Off + ";\n"
    quss += BICyan + "name of attribute : " + Color_Off + BGreen  + varr + Color_Off + ";\n"
    choise = BIRed + "this is a special type :\n" + Color_Off + Purple +  "\t1 - pointer\n\t2 - other data type\n\t3 - pointer of other data type\n\t4 - array of object" + Color_Off
    print(quss)
    print(choise)
    choises = int(input(">> "))
    return tesstter(var_type,varr,choises)


def check_var_type(varr,var_type,file,class_name,yt):
    if var_type == "std::string":
        file.write(for_str(varr,class_name))
    elif var_type == "int":
        file.write(for_int(varr,class_name))
    elif var_type == "double":
        file.write(for_double(varr,class_name))
    elif var_type == "float":
        file.write(for_float(varr,class_name))
    elif var_type == "boolean":
        file.write(for_boolean(varr,class_name))
    elif var_type == "char":
        file.write(for_char(varr,class_name))
    elif var_type == "char*":
        file.write(for_char_p(varr,class_name))
    else:
        file.write(for_other(varr,var_type,yt))


def cccheck(my_map,i,yt,file_name,class_name):
    with open(file_name, "a+") as file:
        arr = my_map[i].split(" ")
        if len(arr) != 2:
            file.write("//param "+ str(yt) + " not registred\n")
        else:
            check_var_type(arr[0],arr[1],file,class_name,yt)

while True:
    file_name = input(BGreen + "file name" + Color_Off + BGreen +" : " + Color_Off)
    file_name = file_name.strip()
    file_name = ' '.join(file_name.split())
    if len(file_name.split()) == 1:
        print(Green + "ok" + Color_Off)
        break
    else :
        print(BRed + "Retry " + Color_Off)
        continue

while True:
    class_name = input(BGreen + "class name" + Color_Off + BGreen +" : " + Color_Off)
    class_name = class_name.strip()
    class_name = ' '.join(class_name.split())
    if len(class_name.split()) == 1:
        print(Green + "ok" + Color_Off)
        break
    else :
        print(BRed + "Retry " + Color_Off)
        continue


my_map = {}
count = 0
i = 0
yt = 0
param = ""
print(Color_Off + BBlue +"  Enter the : " + Color_Off + Cyan + "attribute  ->  type" + Color_Off)
print(BYellow + "    Example:" + Color_Off)
print(Purple + "\tname\t" + Cyan + "std::string\n" + Purple + "\tage"+ Cyan +"\tint\n"+ Purple +"\tprice " + Cyan +"\tfloat\n"+ Color_Off)
while True:
    try:
        param = input(BGreen + "nbr of attribute : " + Color_Off)
        param = param.strip()
        param = ' '.join(param.split())
        if len(param.split()) == 1:
            param = int(param)
            print(f"You entered a valid integer: {param}")
            print(Green + "ok" + Color_Off)
            break
        else :
            print(BRed + "Retry " + Color_Off)
            continue
    except ValueError:
        print("Invalid input. Please enter a valid integer.")


while True:
    get_them = input(BYellow + "Give me the attribute and its type (separated by a space): " + Color_Off)
    get_them = get_them.strip()
    output_string = ' '.join(get_them.split())
    if len(output_string.split()) == 2:
        my_map[i] = output_string
        cccheck(my_map,i,yt,file_name,class_name)
        i += 1
        count += 1
        yt += 1
        print(BGreen + "Done" + Color_Off)
        if count == param:
            break
    else:
        print(BRed + "retry" + Color_Off)
        continue
            
        
# ------------------------------------- Start


# ooption(file_name,class_name)