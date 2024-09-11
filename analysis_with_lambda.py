import pandas as pd
import json

athos_vs_cadres = {
  "players": [
    {
      "name": "Athos",
      "builds": [
        {
          "name": "Castle",
          "nota": 95
        },
        {
          "name": "Farm",
          "nota": 88
        },
        {
          "name": "Bridge",
          "nota": 60
        }
      ]
    },
    {
      "name": "Cadres",
      "builds": [
        {
          "name": "Castle",
          "nota": 40
        },
        {
          "name": "Farm",
          "nota": 85
        },
        {
          "name": "Bridge",
          "nota": 50
        }
      ]
    }
  ]
}






# JSON original
data = '''
[
  {
    "player": "Athos",
    "build": "Castle",
    "nota": 95
  },
  {
    "player": "Athos",
    "build": "Farm",
    "nota": 88
  },
  {
    "player": "Athos",
    "build": "Bridge",
    "nota": 60
  },
  {
    "player": "Cadres",
    "build": "Castle",
    "nota": 40
  },
  {
    "player": "Cadres",
    "build": "Farm",
    "nota": 85
  },
  {
    "player": "Cadres",
    "build": "Bridge",
    "nota": 50
  }
]
'''

# Carregar o JSON
json_data = json.loads(data)

# Criar DataFrame do pandas
df = pd.DataFrame(json_data)

# Exibir DataFrame
print(df)
#exibir as colunas no df 
print(df.columns)
#filtra notas maior que 60
lista_notas = df['nota'].tolist() 
maior_sessenta = list(filter(lambda nota: nota >=60, lista_notas))
print(maior_sessenta)
#dar o dobro de xp para essas notas maiores que 60
xp =0
dobro_xp = list(map(lambda nota: nota*2,maior_sessenta))
print(dobro_xp)

#adicionar o xp com os nomes que tem os maiores scores


# Use 'zip' with an index for correct mapping
for i, (xp, nota) in enumerate(zip(dobro_xp, maior_sessenta)):
  df.loc[i, 'xp'] = xp 
  df.loc[i, 'nota_updated'] = nota
print(df)
df = df.dropna()
print(df)
