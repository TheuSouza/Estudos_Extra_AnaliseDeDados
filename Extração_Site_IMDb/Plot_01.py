import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('./IMDb.csv', delimiter=';')


classificacao_livre = df[df['Classificação'] == 'Livre']
classificacao_10 = df[df['Classificação'] == '10']
classificacao_12 = df[df['Classificação'] == '12']
classificacao_14 = df[df['Classificação'] == '14']
classificacao_16 = df[df['Classificação'] == '16']
classificacao_18 = df[df['Classificação'] == '18']
classificacao_passed = df[df['Classificação'] == 'Passed']
classificacao_approved = df[df['Classificação'] == 'Approved']
classificacao_banned = df[df['Classificação'] == '(Banned)']
classificacao_Not_Rated = df[df['Classificação'] == 'Not Rated']

'''filme_ano = df.groupby('Ano')
for filme in filme_ano:
    print('==' * 50)
    print(filme)'''

filmes_por_ano = df['Ano'].value_counts().sort_index().rename('Quantidade')
print(filmes_por_ano)

plt.figure(figsize=(19, 10))
filmes_por_ano.plot(kind='bar', color='skyblue')
plt.title('Número de Filmes por Ano')
plt.xlabel('Ano')
plt.ylabel('Número de Filmes')
plt.xticks(rotation=90)
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()


plt.figure(figsize=(19, 10))
sns.countplot(data=df, x='Ano', hue='Ano', palette='viridis', legend=False)
plt.xticks(rotation=90)
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.title('Número de Filmes por Ano')
plt.xlabel('Ano')
plt.ylabel('Número de Filmes')
plt.tight_layout()
plt.show()


plt.figure(figsize=(19, 10))
sns.lineplot(data=filmes_por_ano, marker='o', color='black')
plt.xticks(rotation=90)
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.title('Número de Filmes por Ano')
plt.xlabel('Ano')
plt.ylabel('Número de Filmes')
plt.tight_layout()
plt.show()

