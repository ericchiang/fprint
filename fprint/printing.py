import sys
import json
from datetime import datetime

default_format = "%y:%m:%d %H:%M:%S"

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

def _get_time(fmt=default_format):
    return datetime.now().strftime(default_format)

def print_info(msg,end='\n',file=sys.stdout):
    msg = "[%s] INFO: %s%s" % (_get_time(),msg,end)
    file.write(msg)

def print_error(msg,end='\n',file=sys.stdout):
    msg = bcolors.FAIL + "[%s] ERROR: %s%s" % (_get_time(),msg,end) + bcolors.ENDC
    file.write(msg)

def print_time(msg="",end='\n',file=sys.stdout):
    file.write("[%s] %s%s" % (_get_time(),msg,end))

def print_json(json_obj,indent=2,end='\n',file=sys.stdout):
    file.write(json.dumps(json_obj,indent=indent))
