
import sys

import requests as requests





def print_fn():
    print("Hi")

def url(urlString,time):
    print(urlString)
    r =requests.get(urlString)
    print(r.status_code)
    print(time)


if __name__ == "__main__":
    args = sys.argv
    # args[0] = current file
    # args[1] = function name
    # args[2:] = function args : (*unpacked)
    globals()[args[1]](*args[2:])