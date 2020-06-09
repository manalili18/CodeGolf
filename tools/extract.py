#!/usr/bin/python3

import argparse, bs4, urllib.request

def main():
    init()
    print(prompt)
    # TODO make files/folders, extract the prompt
    create_working_dir()

def init():
    init_argparse()
    init_beautiful_soup()

# TODO take in just a title name and search through the page for the closest one
def init_argparse():
    global name, url

    # Description: How to setup/use argparse
    # Source: https://docs.python.org/3/library/argparse.html
    # Date Accessed: 2020-06-08
    parser = argparse.ArgumentParser(description='Setup new codegolfing env')
    parser.add_argument('name', help='Challenge title')
    parser.add_argument('url', help='URL of challenge')
    args = parser.parse_args()

    name = args.name
    url = args.url

def init_beautiful_soup():
    global prompt

    # Description: How to readout html from a URL
    # Source: https://stackoverflow.com/questions/24153519/how-to-read-html-from-a-url-in-python-3
    # Date Accessed: 2020-06-08
    fp = urllib.request.urlopen(url)
    mybytes = fp.read()

    soup = bs4.BeautifulSoup(mybytes,features="html.parser")

    #print(soup.findAll("div",{"class":"post-text"}).prettify())
    prompt = soup.find("a",{"class":"question-hyperlink"}).parent.prettify()
    prompt += '\n\n\n'
    prompt += soup.find("div",{"class":"post-text"}).prettify()

def create_working_dir():

    # Description: File i/o help
    # Source: https://www.tutorialspoint.com/python/python_files_io.htm
    # Date Accessed: 2020-06-09

    return

if __name__ == "__main__":
    main()
