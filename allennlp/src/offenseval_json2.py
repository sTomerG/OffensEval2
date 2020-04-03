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


def write_to_json(data, idds, output_file):
    '''Write data + labels to JSON file'''
    print("Writing {0} instances to {1}".format(len(data), output_file))
    with open(output_file, 'w', encoding="utf8") as out:
        for tweet, idd in zip(data, idds):
            d = {}
            d["id"] = idd
            d["text"] = tweet
            out.write(json.dumps(d, ensure_ascii=False))
            out.write('\n')


if __name__ == "__main__":
    args = create_arg_parser()
    # Read in data lines
    lines = [x.strip().split('\t') for x in open(args.input_file, 'r', encoding="utf8")]
    data = [l[1] for l in lines][1:]
    ids = [l[0] for l in lines][1:]

    # Write train set to file
    write_to_json(data, ids, args.output_file)
