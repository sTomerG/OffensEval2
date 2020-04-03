#!/bin/bash
#SBATCH --partition=gpu
#SBATCH --gres=gpu:v100:1
#SBATCH --mem=8000

set -eu -o pipefail

exps="exps/"

for file in 'configs/ar_bert.json' 'configs/dk_bert.json'  'configs/en_bert.json' 'configs/gr_bert.json' 'configs/tu_bert.json'
do
    dev=$(cat $file | sed -e 's/,/\n/g' | grep "validation_data_path" | awk '{$1=$1;print}' | cut -d ' ' -f2 | sed -e 's/"//g')
    T="$(cut -d'/' -f2 <<<"$dev")"
    test="data/$T/test_data.json"

    # Save exp information to file in exps/ based on json name
    exp_name=$(basename -- "$file")
    exp_name="${exp_name%.*}"
    exp_folder="$exps$exp_name/"

    model=${exp_folder}model.tar.gz
    output=${exp_folder}pred_test.txt

    # And evaluate using a simple python script
    echo "File: " . $file . $model . $test. $output
    # Then predict the dev set (or any other set)
    allennlp predict $model $test --use-dataset-reader --cuda-device 0  --output-file $output --predictor text_classifier
done
