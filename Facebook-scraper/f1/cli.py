from InputReader import *
import argparse


def main():
    # create argument parser object
    parser = argparse.ArgumentParser(description = "Weather Reporter")

    parser.add_argument( "--cookies", type = str,nargs='*',metavar = "location", default = None, help = "cookies")

    parser.add_argument( "--posts", type = str,nargs='*',metavar = "location", default = None, help = "users' posts")

    parser.add_argument( "--profile", type =str,nargs='*',metavar = "days", default = None, help = "users' profile")

    parser.add_argument( "--Users", type =str,nargs='*',metavar = "days", default = None, help = "Path of the file containing users,splitter")

    parser.add_argument( "--profilePath", type =str,nargs='*',metavar = "days", default = None, help = "Path of the file containing features of profiles")

    parser.add_argument( "--postPath", type =str,nargs='*',metavar = "days", default = None, help = "Path of the file containing features of posts")

    parser.add_argument( "--outputPath", type =str,nargs='*',metavar = "days", default = None, help = "Path of the output")

    args = parser.parse_args()

    i=InputReader()
    i.readData(args)



if __name__ == "__main__":
    main()