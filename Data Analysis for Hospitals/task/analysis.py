import pandas as pd

pd.set_option('display.max_columns', 8)

# Imports
df_general = pd.read_csv('test/general.csv')
df_prenatal = pd.read_csv('test/prenatal.csv')
df_sports = pd.read_csv('test/sports.csv')

datasets = [df_general, df_prenatal, df_sports]


# # Unifying columns names
def unifying_col_names(data):
    """
    Unifying column names.
    :param data: pandas DataFrame
    :return: pandas DataFrame
    """
    cols = data.columns[1:3]
    return data.rename({cols[0]: 'hospital', cols[1]: 'gender'}, axis=1)


for i, dataset in enumerate(datasets):
    datasets[i] = unifying_col_names(dataset)

# Merging datasets, getting rid of irrelevant column 'Unnamed: 0'
df = pd.concat(datasets, ignore_index=True).drop('Unnamed: 0', axis=1)

# Getting rid of empty rows
df = df.dropna(how='all')

# Unifying gender column
df.gender = df.gender.map({'male': 'm', 'man': 'm', 'female': 'f', 'woman': 'f'})
df.loc[df['hospital'] == 'prenatal', 'gender'] = 'f'

# Dealing with NaNs in other columns
selected_cols = ['bmi', 'diagnosis', 'blood_test', 'ecg', 'ultrasound', 'mri', 'xray', 'children', 'months']
df[selected_cols] = df[selected_cols].fillna(0)

print(f'Data shape: {df.shape}')
print(df.sample(n=20, random_state=30))
