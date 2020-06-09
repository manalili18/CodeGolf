#!/usr/bin/python3

import argparse, bs4, urllib.request, os, subprocess

def main():
    init()
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

    # TODO add htmlpreview.github.io/?<url> link to prompt
    prompt = url
    prompt += '\n\n'
    prompt += soup.find("a",{"class":"question-hyperlink"}).parent.prettify()
    prompt += '\n\n'
    prompt += soup.find("div",{"class":"post-text"}).prettify()

def create_working_dir():
    # Description: File i/o help
    # Source: https://www.tutorialspoint.com/python/python_files_io.htm
    # Source: https://www.pythonforbeginners.com/files/with-statement-in-python
    # Date Accessed: 2020-06-09

    os.mkdir(name)
    with open(name+'/prompt.html','w') as prompt_file:
        prompt_file.write(prompt)

    with open(name+'/main.py','w') as prototype:
        prototype.write('# Code goes here')


def git_track_prompt():
    prompt_path = name+'/prompt.html'
    prototype_path = name+'/main.py'

    # Description: shell commands in python
    # Source: https://janakiev.com/blog/python-shell-commands/
    # Date Accessed: 2020-06-09
    # TODO try this with subprocess instead
    #os.system('git add ' + prompt_path + ' ' + prototype_path 
            #+ '; git commit -m "added prompt for ' + name + '; git push')
    
if __name__ == "__main__":
    main()
