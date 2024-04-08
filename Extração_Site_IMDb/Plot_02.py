import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df =  pd.read_csv('IMDb.csv', delimiter=';')

ano_df = df.groupby('Ano').agg({'Titulo': 'count'})

ano_df.head(20)


ano_df.plot(kind='bar',figsize=(12,6,), color='orangered')
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.title('Número de Filmes por Ano')
plt.xlabel('Ano')
plt.ylabel('Número de Filmes')
plt.xticks(rotation=65)
plt.tight_layout()
plt.show()