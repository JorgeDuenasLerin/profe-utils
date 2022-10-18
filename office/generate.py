#!/bin/python3
import pandas as pd
import sys

import argparse

text = 'Program to train a model with groups data. It uses a Dense as an embedding.'
parser = argparse.ArgumentParser(description=text)
parser.add_argument('--outdir', type=str, required=True, help="Output directory")
parser.add_argument('--modelFile', type=str, required=True, help="Model file")
parser.add_argument('--seed', type=str, required=True, help="Seed")
parser.add_argument('--k', type=int, required=True, help="Number of factor in each embedding")
parser.add_argument('--dataset', type=str, required=True, help="Dataset")

args = parser.parse_args()