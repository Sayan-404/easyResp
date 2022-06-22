import requests
import sys
import argparse
from simple_colors import *
import time

parser = argparse.ArgumentParser()
parser.add_argument('-u','--url',type=str,help="Returns the status code")
parser.add_argument('-f','--file',type=str,help="Takes a list of input")
parser.add_argument('-o','--output',type=str,help="gives output in a text file please mention .txt at the end")
parser.add_argument('--header',type=str,help="include header type y for yes")
#parser.add_argument('-d','--delay',type=float,help="Time delay between two successful requests in seconds")
args = parser.parse_args()

def fileparser(filename):

    file=open(filename,"r")
    for line in file:
        try:
            line = line.rstrip()
            read = requests.get(line)
            print(line,timeout=5)
            print(green(read.status_code,['bold']))
            if args.header=='y':
                print(read.headers)

            if args.output:
                with open(args.output,"a") as f:
                    f.write(line+" ")
                    f.write(str(green(read.status_code,['bold']))+"\n")

                    if args.header=='y':
                        f.write(str(read.headers)+"\n")
        except:
            print(line+": 500 maybe")



if args.url:
    read = requests.get(args.url)
    print(args.url,end=" ")
    print(green(read.status_code,['bold']))

if args.file:
    fileparser(args.file)
