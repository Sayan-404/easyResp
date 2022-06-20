import requests
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-u','--url',type=str,help="Returns the status code")
parser.add_argument('-f','--file',type=str,help="Takes a list of input")
parser.add_argument('-o','--output',type=str,help="gives output in a text file please mention .txt at the end")
parser.add_argument('--header',type=str,help="include header type y for yes")
args = parser.parse_args()

def fileparser(filename):
    file=open(filename,"r")
    for line in file:
        line = line.rstrip()
        read = requests.get(line)
        print(line)
        print(read.status_code)
        if args.header=='y':
            print(read.headers)

        if args.output:
            with open(args.output,"a") as f:
                f.write(line+" ")
                f.write(str(read.status_code)+"\n")

                if args.header=='y':
                    f.write(str(read.headers)+"\n")



if args.url:
    read = requests.get(args.url)
    print(read.status_code)

if args.file:
    fileparser(args.file)
