#!/usr/bin/python3

import argparse, bs4, urllib.request

def main():
    init()
    # TODO make files/folders, extract the prompt

def init():
    init_argparse()
    init_beautiful_soup()

def init_argparse():
    global name, url

    # Description: How to setup/use argparse
    # Source: https://docs.python.org/3/library/argparse.html
    # Date: 08-06-2020
    parser = argparse.ArgumentParser(description='Setup new codegolfing env')
    parser.add_argument('name', help='Challenge title')
    parser.add_argument('url', help='URL of challenge')
    args = parser.parse_args()

    name = args.name
    url = args.url

def init_beautiful_soup():
    # Description: How to readout html from a URL
    # Source: https://stackoverflow.com/questions/24153519/how-to-read-html-from-a-url-in-python-3
    # Date Accessed: 08-06-2020
    fp = urllib.request.urlopen("http://www.python.org")
    mybytes = fp.read()

    # TODO setup the soup

if __name__ == "__main__":
    main()
