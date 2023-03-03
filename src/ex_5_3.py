""" ex_5_3.py
This module contains an entry point that:

- creates a CLi that accepts an input file of data to be processed
- shifts and scales the data to a mean of 0 and a standard deviation 1
- writes the file to the output file argument
"""
import numpy as np
from argparse import ArgumentParser
import os

if __name__ == "__main__":
    # Create your argument parser object here.
    # Collect the filename arguments from the command line
    # Rewrite your 5_3 logic here so that it utilizes the arguments passed from the command line.

    # Tests will run your command using a system call.
    # To test your program with arguments, run it from the command line
    # (see README.md for more details)
    par = ArgumentParser(description='This program applies a standard scale transform to the data in infile and writes it to outfile.')
    par.add_argument('infile',help='input file path',nargs='?')
    par.add_argument('outfile',help='output file path',nargs='?')
    arg_parse = par.parse_args()
    input_data = np.loadtxt(arg_parse.infile)
    mean_data = (input_data - input_data.mean(axis=0)) 
    std_data = input_data.std(axis=0)
    processed = mean_data/std_data
    root_dir = get_repository_root()
    os.makedirs(root_dir / "outputs", exist_ok=True)
    np.savetxt(arg_parse.outfile, processed, fmt='%.2e')
