import argparse
import urllib.request
import logging
import datetime

def downloadData(url='https://s3.amazonaws.com/cuny-is211-spring2015/birthdays100.csv'):
    g = urllib.request.urlopen(url)    
    name = g.url[url.rfind('/') + 1:]
    with open(name, 'wb') as f:
        return f.write(g.read())

def processData(file_content):
    pass


def displayPerson(id, personData):
    pass

def main(url):
    print(f"Running main with URL = {url}...")


if __name__ == "__main__":
    """Main entry point"""
    getFile = downloadData()
    processFile = processData(getFile)
    #parser = argparse.ArgumentParser()
    #parser.add_argument("--url", help="URL to the datafile", type=str, required=True)
    #args = parser.parse_args()
    #main(args.url)
