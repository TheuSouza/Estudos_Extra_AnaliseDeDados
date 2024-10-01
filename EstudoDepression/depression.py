import pandas as pd

depression_df = pd.read_csv('./EstudoDepression/Anxiety-Depression.csv', sep=',')

print(depression_df.head(15))