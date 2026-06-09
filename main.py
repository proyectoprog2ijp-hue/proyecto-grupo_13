import codecs;
import csv

def read():
    archivo = open("establecimientos-educativos-12K.csv", newline='')
    for i in archivo:
            print("".join(i))



def main():
    read()

main()
