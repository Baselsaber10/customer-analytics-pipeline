
CSCI461 Assignment 1 - Customer Analytics Pipeline

Project Overview

This project implements a customer analytics pipeline using the Bank Marketing dataset. The pipeline starts by loading the raw dataset, saving a raw copy, then preprocessing the data to make it ready for further analytics, visualization, and clustering tasks.

The project is designed to run inside Docker as required in the assignment.

Dataset

Dataset used: Bank Marketing Dataset

Source: Kaggle / UCI Bank Marketing Dataset

Description:
The dataset contains information collected from direct marketing campaigns of a Portuguese banking institution. The goal is to determine whether a client subscribed to a term deposit.

Main attributes include:

age
job
marital
education
balance
housing
loan
contact
duration
campaign
pdays
previous
poutcome
y
Current Completed Part

The following parts have been completed so far:

Dataset selection
Project structure setup
ingest.py implementation
preprocess.py implementation
Initial pipeline testing
Implemented Files
1. ingest.py

This script:

accepts the dataset path from the command line
loads the raw dataset
saves a raw copy as data_raw.csv
calls preprocess.py and passes the generated raw file
2. preprocess.py

This script performs preprocessing in four main stages:

Data Cleaning
removes duplicate rows
replaces unknown values in selected categorical columns with missing values
replaces pdays = -1 with missing values
fills missing categorical values using the mode
fills missing numeric values using the median
Discretization
bins age into age groups
bins balance into balance groups
bins duration into duration groups
Feature Transformation
converts target variable y from yes/no to 1/0
applies one-hot encoding to categorical features
scales numeric columns using StandardScaler
Dimensionality Reduction
keeps only a selected subset of important features for later analysis

At the end, the script saves the processed data as data_preprocessed.csv.

Generated Outputs

After running the current pipeline, the following files are generated successfully:

data_raw.csv
data_preprocessed.csv
Sample Execution Flow

Run the following command:

python ingest.py dataset/bank-full.csv

The pipeline will:

read the dataset
save data_raw.csv
preprocess the data
save data_preprocessed.csv
Sample Output

Example terminal output after successful execution:

Raw data saved as data_raw.csv
Preprocessing completed successfully.
Preprocessed data saved as data_preprocessed.csv
Project Structure
customer-analytics/
├── dataset/
│   └── bank-full.csv
├── results/
├── Dockerfile
├── ingest.py
├── preprocess.py
├── analytics.py
├── visualize.py
├── cluster.py
├── summary.sh
├── README.md
└── .gitignore
Notes
The Bank Marketing dataset uses ; as the separator, so it is handled correctly in ingest.py.
The preprocessing script was tested successfully and produced the expected output files.
The remaining project files will be completed by other team members.
Next Steps

The remaining parts to be completed are:

analytics.py
visualize.py
cluster.py
Dockerfile
summary.sh
final documentation update

