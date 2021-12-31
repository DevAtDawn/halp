# curl "https://www.codegrepper.com/api/search.php?q=python open file&search_options=search_titles,search_code" 

import json
import requests
import sys
import os
from os import system, name
# from time import sleep

# define our clear function
def clear():

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def make_url(q):
    base = "https://www.codegrepper.com/api/search.php?q={}&search_options=search_titles,search_code" 
    new = base.format(q)
    return new

def get_json(url):
    response = requests.get(url)
    return response.text

def parse_json(data, num=0, inter=False):
    # with open ("response.json", "r") as f:
        # d = json.load(f)
    d = json.loads(data)
    if inter == True:
        out = d["answers"][num]["answer"]
        print('\n\n', out, '\n\n')
        return out

    else:
        try:
            for x in range(num):
            # for x in range(0, num):
                out = d["answers"][x]["answer"]
                print('\n\n', out, '\n\n')
        except:
            pass
    # return out
    # print(d["answers"][num]["answer"])
    # print(d)
    # print(d["answers"])
    # print(d["answers"][0])
        # print(d["answers"][0]["answer"])
global count
count = 0

def interactive():
    global count
    global res
    global data
    # usrin = input('\n### show next answer [y]/[n], previous [p], copy[c], open[o] :\n')
    usrin = input()
    if usrin == 'y':
        # clear()
        count += 1
        data = parse_json(res, count, True)
        interactive()
        # return True
    elif usrin == 'p':
        clear()
        count -= 1
        data = parse_json(res, count, True)
        interactive()
    elif usrin == 'o':
        # os.system('echo "{}"|xclip'.format(data))
        stri = 'echo "{}" | nvim'.format(data)
        # print(stri)
        # os.system(stri)

    else: return False

def main():
    # n = len(sys.argv)
    usr_arg = sys.argv
    length = len(usr_arg)
    if length == 1:
        print('\n### show next answer [y]/[n], previous [p], copy[c] :\n')
        uin = input("Enter Query: ")
    # if length
        # usr_arg0 = 1
        # usr_arg1 = usr_arg[2]
        url = make_url(uin)
        global res
        global data
        res = get_json(url)
        data = parse_json(res, count, True)
        interactive()
    else:
        usr_arg0 = int(usr_arg[1])
    # print(usr_arg0)
        usr_arg1 = usr_arg[2]
        url = make_url(usr_arg1)
        res = get_json(url)
        data = parse_json(res, usr_arg0)
    # print(data)
    # interactive()


if __name__ == "__main__":
    main()
