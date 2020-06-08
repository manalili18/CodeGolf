#!/usr/bin/python3

import argparse, bs4

args = ''

def main():
    init()
    print(args)
    print(args.name,args.url)

def init():
    global args
    parser = argparse.ArgumentParser(description='Setup new codegolfing env')
    parser.add_argument('name', help='Challenge title')
    parser.add_argument('url', help='URL of challenge')
    args = parser.parse_args()

if __name__ == "__main__":
    main()
