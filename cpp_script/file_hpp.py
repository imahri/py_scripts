
from header import *

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


def head(ffile,login,str):
    ffile.write("/* ************************************************************************** */\n")
    ffile.write("/*                                                                            */\n")
    ffile.write("/*                                                        :::      ::::::::   */\n")
    ffile.write(chaa(str))
    ffile.write("/*                                                    +:+ +:+         +:+     */\n")
    ffile.write(header_BY(login))
    ffile.write("/*                                                +#+#+#+#+#+   +#+           */\n")
    ffile.write("/*   Created: " + time_now() + " by ")
    ffile.write(created_By(login))
    ffile.write("/*   Updated: " + time_now() + " by ")
    ffile.write(update_By(login))
    ffile.write("/*                                                                            */\n")
    ffile.write("/* ************************************************************************** */\n\n")
