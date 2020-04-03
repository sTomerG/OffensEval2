#!/usr/bin/env python3
# -*- coding: utf8 -*-

'''
Put offenseval input data in JSON format for training with AllenNLP
'''

import argparse
import os
import json
from random import shuffle


def create_arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--input_file", required=True, type=str, help="Input file")
    parser.add_argument("-o", "--output_file", required=True, type=str, help="Folder for JSON output (dict per line)")
    parser.add_argument("-d", "--dev_amount", default=0, type=int,
                        help="Amount of instances we we write to dev set (default 0 means only train)")
    args = parser.parse_args()
    return args


def write_to_json(data, labels, output_file):
    '''Write data + labels to JSON file'''
    print("Writing {0} instances to {1}".format(len(data), output_file))
    with open(output_file, 'w') as out:
        for tweet, label in zip(data, labels):
            d = {}
            d["text"] = tweet
            d["label"] = label
            out.write(json.dumps(d, ensure_ascii=False))
            out.write('\n')


def shuffle_dependent_lists(lst1, lst2):
    '''Shuffle lists but keep dependency between the two'''
    assert (len(lst1) == len(lst2))

    num_list = [i for i in range(len(lst1))]
    shuffle(num_list)  # random list of numbers
    new_lst1 = []
    new_lst2 = []

    for idx in num_list:
        new_lst1.append(lst1[idx])
        new_lst2.append(lst2[idx])

    return new_lst1, new_lst2


if __name__ == "__main__":
    args = create_arg_parser()
    # Read in data lines
    lines = [x.strip().split('\t') for x in open(args.input_file, 'r')]
    data = [l[1] for l in lines][1:]
    labels = [l[2] for l in lines][1:]

    data, labels = shuffle_dependent_lists(data, labels)
    # Write train set to file
    write_to_json(data, labels, args.output_file)
