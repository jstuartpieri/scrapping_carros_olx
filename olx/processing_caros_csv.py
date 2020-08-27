import pandas as pd

base = pd.read_csv('carros.csv')
base.preço = base.preço.str.slice(3)
base.preço = base.preço.fillna(0)
base['preço'] = base['preço'].astype(float)

base = base[(base.preço <= 20) & (base.preço > 0)]

base.Ano = base.Ano.fillna(0)
base['Ano'] = base['Ano'].astype(int)

base = base[base.Ano >= 2012]

base.to_excel('teste.xlsx', index = False)