import csv
import os
import pathlib
import shutil


def read_data(filename):
    with open(filename) as f:
        data = [line for line in csv.reader(f)]
    return data


def classify(data):
    del data[0]
    for row in range(len(data)):
        filename = data[row][0]
        if int(data[row][1]) < 256 or int(data[row][2]) < 256:
            destination = "unused_test256/"+filename
            shutil.move("test/"+filename,destination)


def main():
    elem = "unused_test256"
    if elem not in os.listdir():
        print(f"mkdir {elem}")
        os.mkdir(elem)
    data = read_data("test.csv")
    classify(data)
main()
