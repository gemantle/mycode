#!/usr/bin/envi python3
"""using cvs data"""
import csv

def main():
    # open the cvs data
    with open ("vendor.csv", "r") as venfile:
        vendata = csv.reader(venfile, delimiter=",")
        #coments here
        for row in vendata:
            print("the ip address " + row[2] + " reqires the driver " + row[3])

main()
