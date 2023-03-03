""" ex_5_3.py
This module contains an entry point that:

- creates a CLi that accepts an input file of data to be processed
- shifts and scales the data to a mean of 0 and a standard deviation 1
- writes the file to the output file argument
"""
import numpy as np
from argparse import ArgumentParser

if __name__ == "__main__":
    # Create your argument parser object here.
    # Collect the filename arguments from the command line
    # Rewrite your 5_3 logic here so that it utilizes the arguments passed from the command line.

    # Tests will run your command using a system call.
    # To test your program with arguments, run it from the command line
    # (see README.md for more details)
    desc = "This program applies a standard scale transform to the data in infile and writes it to outfile."

    parser = argparse.ArgumentParser(description=desc)

    parser.add_argument("infile", type=argparse.FileType('r'))

    parser.add_argument("outfile", type=argparse.FileType('w'))

    args = parser.parse_args()

    raw_data = np.loadtxt(args.infile)

    raw_data -= raw_data.mean()

    std_=raw_data.std()

    processed=raw_data/std_

    np.savetxt(args.outfile, processed, fmt='%.2e')
