import pandas as pd
import sys

input1 = sys.argv[1]
input2 = sys.argv[2]
output = sys.argv[3]

data1 = pd.read_csv(input1)
data2 = pd.read_csv(input2)

data_m = data1.merge(data2, left_on='respondent_id', right_on='id')
data_m.drop(columns=['id'], inplace=True)
data_m.dropna(inplace=True)
data_m = data_m[~data_m['job'].str.contains('insurance|Insurance')]

data_clean = data_m[['respondent_id', 'name', 'address', 'phone', 'job', 'company', 'birthdate']]
data_clean.to_csv(output, index=False)