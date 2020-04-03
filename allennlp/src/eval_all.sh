#!/bin/bash

set -eu -o pipefail

exps="exps/"
eval_python="src/offenseval_eval.py"

for file in 'configs/ar_bert.json'  'configs/dk_bert.json'  'configs/en_bert.json'  'configs/gr_bert.json'  'configs/tu_bert.json'
do
    dev=$(cat $file | sed -e 's/,/\n/g' | grep "validation_data_path" | awk '{$1=$1;print}' | cut -d ' ' -f2 | sed -e 's/"//g')

    # Save exp information to file in exps/ based on json name
    exp_name=$(basename -- "$file")
    exp_name="${exp_name%.*}"
    exp_folder="$exps$exp_name/"

    # And evaluate using a simple python script
    echo "File: " . $file
    python $eval_python --input_file ${exp_folder}pred.txt --gold_file $dev
done