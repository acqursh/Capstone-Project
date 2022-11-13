import numpy as np
import pandas as pd

df1 = pd.read_csv(
    r"C:\Users\arkop\OneDrive\Desktop\Capstone\CapstoneProject\Data Fetch\Datasets\df.csv")

df2 = pd.read_csv(
    r"C:\Users\arkop\OneDrive\Desktop\Capstone\CapstoneProject\Data Fetch\Datasets\heart.csv")

df1 = df1.drop(['ca', 'thal'], axis=1)

df1_cols, df2_cols = list(df1.columns), list(df2.columns)
new_columns = dict(zip(df2_cols, df1_cols))

df2.rename(columns=new_columns, inplace=True)


def convert_sex(text):
    if text == 'M':
        return 1
    return 0


def convert_cp(text):
    if text == 'ATA':
        return 1
    elif text == 'NAP':
        return 2
    elif text == 'ASY':
        return 3
    return 0


def convert_restecg(text):
    if text == 'ST':
        return 1
    elif text == 'LVH':
        return 2
    return 0


def convert_exang(text):
    if text == 'Y':
        return 1
    return 0


def convert_slope(text):
    if text == 'Flat':
        return 1
    elif text == 'Down':
        return 2
    return 0


df2['sex'] = df2['sex'].apply(convert_sex)
df2['cp'] = df2['cp'].apply(convert_cp)
df2['restecg'] = df2['restecg'].apply(convert_restecg)
df2['exang'] = df2['exang'].apply(convert_exang)
df2['slope'] = df2['slope'].apply(convert_slope)

frames = [df1, df2]

merged_df = pd.concat(frames)

merged_df.loc[merged_df['chol'] == 0, 'chol'] = np.nan
merged_df["chol"] = merged_df["chol"].fillna(int(merged_df["chol"].median()))

print(merged_df['chol'])

merged_df.to_csv(
    r"C:\Users\arkop\OneDrive\Desktop\Capstone\CapstoneProject\Data Fetch\Datasets\combined.csv",
    index=False)
