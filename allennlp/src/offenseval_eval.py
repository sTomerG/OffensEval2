#!/usr/bin/env python3
# -*- coding: utf8 -*-

'''
Evaluate predictions
'''

import argparse
import os
import json
from sklearn.metrics import accuracy_score, f1_score


def create_arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--input_file", required=True, type=str, help="Input file with predictions")
    parser.add_argument("-g", "--gold_file", required=True, type=str, help="Gold file with labels")
    args = parser.parse_args()
    return args


def read_predictions(input_file):
    '''Read in JSON predictions and return as list of dicts
       Also returns preds separately for quick eval'''
    dic = []
    with open(input_file, 'r') as f:
        for line in f:
            dic.append(json.loads(line))
    preds = [x["label"] for x in dic]
    return dic, preds


if __name__ == "__main__":
    args = create_arg_parser()
    # Read in pred/gold
    gold_dic, gold = read_predictions(args.gold_file)
    pred_dic, preds = read_predictions(args.input_file)
    acc = accuracy_score(gold, preds)
    f1 = f1_score(gold, preds, pos_label='NOT')
    print("Accuracy: {0}".format(acc))
    print("F1: {0}".format(f1))
