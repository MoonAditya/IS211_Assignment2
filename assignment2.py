import argparse
import urllib.request
import logging
import datetime
import csv
import re


def downloadData(url='https://s3.amazonaws.com/cuny-is211-spring2015/birthdays100.csv'):
    g = urllib.request.urlopen(url)
    name = g.url[url.rfind('/') + 1:]
    with open(name, 'wb') as f:
        return f.write(g.read())


def processData(file_content='birthdays100.csv'):
    with open(file_content, 'r') as fromFile:
        reader = csv.reader(fromFile, delimiter= ",")
        header = next(reader)
        dict_list = {}
        for eachRow in reader:
            person_id = int(eachRow[0])
            person_Name = eachRow[1]
            person_Dob = eachRow[2]
            try:
                person_Dob = re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\\3-\\2-\\1', eachRow[2])
            except ValueError:
                logging.getLogger("Assignment2")
                logging.error("Error processing line #{} for ID #{}\n".format(eachRow[0], eachRow[0]))

            dict_list[person_id] = (person_Name, person_Dob)
            return dict_list


def displayPerson(id, personData):
    pass

def main(url):
    print(f"Running main with URL = {url}...")


if __name__ == "__main__":
    """Main entry point"""

