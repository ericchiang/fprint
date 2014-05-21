import sys
import json
from datetime import datetime

default_format = "%y:%m:%d %H:%M:%S"

ansi_colors = {
    "red":'\033[91m',
    "r":'\033[91m',
    "blue":'\033[94m',
    "green":'\033[92m',
    "g":'\033[92m',
    "purple":'\033[95m',
    "yellow":'\033[93m',
    "y":'\033[93m'
}
ansi_ending = '\033[0m'

def _get_time(fmt=default_format):
    return datetime.now().strftime(default_format)

def fancy_print(msg,time=True,header=None,color=None,end='\n',file=sys.stdout):
    if isinstance(file,str):
        file = open(file,"a")
    msg = "%s%s" % (msg,end)
    if header:
        msg = "%s: %s" % (header,msg)
    if time is True:
        msg = "[%s] %s" % (_get_time(),msg)
    if color:
        if color.lower() in ansi_colors:
            msg = ansi_colors[color.lower()] + msg + ansi_ending
        else:
            raise Exception("%s is not an available color" % color)
    file.write(msg)

def print_color(msg,color,end='\n',file=sys.stdout):
    fancy_print(msg,time=False,color=color,end=end,file=file)

def print_info(msg,end='\n',file=sys.stdout):
    fancy_print(msg,header="INFO",end=end,file=file)

def print_success(msg,end='\n',file=sys.stdout):
    fancy_print(msg,header="SUCCESS",color="green",end=end,file=file)

def print_error(msg,end='\n',file=sys.stdout):
    fancy_print(msg,header="ERROR",color="red",end=end,file=file)

def print_warning(msg="",end='\n',file=sys.stdout):
    fancy_print(msg,header="WARNING",color="yellow",end=end,file=file)


def print_time(msg="",end='\n',file=sys.stdout):
    fancy_print(msg,end=end,file=file)

def print_json(json_obj,indent=2,end='\n',file=sys.stdout):
    file.write(json.dumps(json_obj,indent=indent))

