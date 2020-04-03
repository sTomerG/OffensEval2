#!/bin/bash
#SBATCH --partition=gpu
#SBATCH --gres=gpu:v100:1
#SBATCH --mem=8000

# . /home/s2545020/.conda/envs/allennlp/bin/
# module load Anaconda3
# module load CUDA/9.1.85
# . /software/software/Anaconda3/2019.07/etc/profile.d/conda.sh
# conda activate allennlp

set -eu -o pipefail

# Train, predict and evaluate AllenNLP models for offenseval shared task
# Always activate allennlp environment first

# Arguments:
# 		 $1: config file (jsonnet)
config=$1

# Set some locations
# This is very hacky, but it gets the dev set location you specified in the config file to here
dev=$(cat $config | sed -e 's/,/\n/g' | grep "validation_data_path" | awk '{$1=$1;print}' | cut -d ' ' -f2 | sed -e 's/"//g')
exps="exps/"
eval_python="src/offenseval_eval.py"

# Save exp information to file in exps/ based on json name
exp_name=$(basename -- "$config")
exp_name="${exp_name%.*}"
exp_folder="$exps$exp_name/"

# First train a model based on the config file
allennlp train $config -s $exp_folder -f

# Then predict the dev set (or any other set)
allennlp predict ${exp_folder}/model.tar.gz $dev --use-dataset-reader --cuda-device 0  --output-file ${exp_folder}pred.txt --predictor text_classifier

# And evaluate using a simple python script
python $eval_python --input_file ${exp_folder}pred.txt --gold_file $dev
