
import datetime

def time_now():
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime("%Y/%m/%d %H:%M:%S")
    return formatted_time

def chaa(str):
    ret = "/*   "
    if(len(str) >= 43):
        str = str[0:43]
        ll = 43
    else:
        ll = len(str)
    tr = 51 - (ll+4)
    ret += str
    ret += ".hpp"
    for i in range(tr):
        ret += " "
    ret += ":+:      :+:    :+:   */\n"
    return ret

def chaa1(str):
    ret = "/*   "
    if(len(str) >= 43):
        str = str[0:43]
        ll = 43
    else:
        ll = len(str)
    tr = 51 - (ll+4)
    ret += str
    ret += ".cpp"
    for i in range(tr):
        ret += " "
    ret += ":+:      :+:    :+:   */\n"
    return ret


def head(ffile):
    ffile.write("/* ************************************************************************** */\n")
    ffile.write("/*                                                                            */\n")
    ffile.write("/*                                                        :::      ::::::::   */\n")
    ffile.write(chaa(str))
    ffile.write("/*                                                    +:+ +:+         +:+     */\n")
    ffile.write("/*   By: imahri <imahri@student.42.fr>              +#+  +:+       +#+        */\n")
    ffile.write("/*                                                +#+#+#+#+#+   +#+           */\n")
    ffile.write("/*   Created: " + time_now() + " by imahri            #+#    #+#             */\n")
    ffile.write("/*   Updated: " + time_now() + " by imahri           ###   ########.fr       */\n")
    ffile.write("/*                                                                            */\n")
    ffile.write("/* ************************************************************************** */\n\n")

def head1(ffile):
    ffile.write("/* ************************************************************************** */\n")
    ffile.write("/*                                                                            */\n")
    ffile.write("/*                                                        :::      ::::::::   */\n")
    ffile.write(chaa1(str))
    ffile.write("/*                                                    +:+ +:+         +:+     */\n")
    ffile.write("/*   By: imahri <imahri@student.42.fr>              +#+  +:+       +#+        */\n")
    ffile.write("/*                                                +#+#+#+#+#+   +#+           */\n")
    ffile.write("/*   Created: " + time_now() + " by imahri            #+#    #+#             */\n")
    ffile.write("/*   Updated: " + time_now() + " by imahri           ###   ########.fr       */\n")
    ffile.write("/*                                                                            */\n")
    ffile.write("/* ************************************************************************** */\n\n")

def ClassName(str,file):
    file.write("class " + str + "\n")
    file.write("{\n")
    file.write("\tpublic:\n")
    file.write("\t\t" + str + "();\n") # constr
    file.write("\t\t" + str + "(const "+ str +" &"+ str[0].lower() + str[-1].lower() + ");\n") # copy constr
    file.write("\t\t" + str + " &operator=(const " + str + " &" +  str[0].lower() + str[-1].lower() +");\n") # copy assi op
    file.write("\t\t~" + str + "();\n")
    file.write("};\n\n")


def for_head(stt):
    with open((stt + ".hpp"), "w") as file:
        head(file)
        file.write("#ifndef " + stt.upper() + "_HPP\n")
        file.write("#define " + stt.upper() + "_HPP\n\n")
        file.write("#include <iostream>\n\n")
        ClassName(stt,file)
        file.write("#endif\n")


def for_head1(stt):
    with open((stt + ".cpp"), "w") as file:
        head(file)
        file.write("#include \"" + stt + ".hpp\"\n\n")



str = input("class Name > ")
file_name = str
for_head(file_name)
print(f"File {file_name}.hpp has been created in the current directory.")
for_head1(file_name)
print(f"File {file_name}.cpp has been created in the current directory.")
