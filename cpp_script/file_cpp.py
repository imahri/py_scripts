
from header import *

def chaa1(name_str):
    ret = "/*   "
    if(len(name_str) >= 43):
        name_str = name_str[0:43]
        ll = 43
    else:
        ll = len(name_str)
    tr = 51 - (ll+4)
    ret += name_str
    ret += ".cpp"
    for i in range(tr):
        ret += " "
    ret += ":+:      :+:    :+:   */\n"
    return ret


def head1(ffile,login,name_str):
    ffile.write("/* ************************************************************************** */\n")
    ffile.write("/*                                                                            */\n")
    ffile.write("/*                                                        :::      ::::::::   */\n")
    ffile.write(chaa1(name_str))
    ffile.write("/*                                                    +:+ +:+         +:+     */\n")
    ffile.write(header_BY(login))
    ffile.write("/*                                                +#+#+#+#+#+   +#+           */\n")
    ffile.write("/*   Created: " + time_now() + " by ")
    ffile.write(created_By(login))
    ffile.write("/*   Updated: " + time_now() + " by ")
    ffile.write(update_By(login))
    ffile.write("/*                                                                            */\n")
    ffile.write("/* ************************************************************************** */\n\n")