#!/usr/bin/env python
#
# This script calculates the average of a list of numbers from a file.

import argparse
import numpy as np

def find_max_region(numbers, n):
    """
    Finds the largest mean of sub-sequences of length n in numbers
    """
    means = []
    for i in range(len(numbers)-n):
        mean = np.mean(numbers[i:i+n])
        means.append((i,mean))
    x = max(means)
    return x[1]

def load_numbers_from_file(filepath):
    """
    Loads numbers from a file, one number per line.
    """
    numbers = []
    try:
        with open(filepath, 'r') as f:
            for line in f:
               numbers.append(float(line.strip()))
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        exit(1)
    except ValueError:
        print(f"Error: Could not convert line to a number in {filepath}. Please ensure all lines contain valid numbers.")
        exit(1)
    return numbers

def main():
    parser = argparse.ArgumentParser(description="Calculate the average of numbers from a file.")
    parser.add_argument("filepath", help="Path to the file containing numbers (one per line).")
    parser.add_argument("seqlen", help="Size of subsequence to use")
    args = parser.parse_args()

    numbers = load_numbers_from_file(args.filepath)
    max_mean = find_max_region(np.array(numbers), int(args.seqlen))

    #print(f"Numbers loaded: {numbers}")
    #print(f"Largest Mean: {max_mean}")
    print(max_mean)



if __name__ == "__main__":
    main()
