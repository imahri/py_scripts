
import datetime

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

