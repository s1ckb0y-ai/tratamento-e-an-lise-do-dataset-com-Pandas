import pandas as pd
import numpy as np

# 1. Leitura do CSV
df = pd.read_csv("dados.csv", sep=";")

# 2. Informações gerais
print("\nINFORMAÇÕES GERAIS")
df.info()

# 3. Primeiras 5 linhas
print("\nPRIMEIRAS 5 LINHAS")
print(df.head())

# 4. Últimas 5 linhas
print("\nÚLTIMAS 5 LINHAS")
print(df.tail())

# 5. Criando uma cópia do DataFrame
df_tratado = df.copy()

# 6. Substituindo valores nulos de Calories por 0
df_tratado["Calories"] = df_tratado["Calories"].fillna(0)

print("\nAPÓS PREENCHIMENTO DE CALORIES")
print(df_tratado)

# 7. Substituindo valor nulo de Date por 1900/01/01
df_tratado["Date"] = df_tratado["Date"].fillna("1900/01/01")

print("\nAPÓS PREENCHIMENTO DE DATE")
print(df_tratado)

# 8. Retirando as aspas das datas
df_tratado["Date"] = df_tratado["Date"].str.replace(
    "'",
    "",
    regex=False
)

# 9. Substituindo 1900/01/01 novamente por valor nulo
df_tratado["Date"] = df_tratado["Date"].replace(
    "1900/01/01",
    np.nan
)

# 10. Corrigindo a data que está no formato 20201226
df_tratado["Date"] = df_tratado["Date"].replace(
    "20201226",
    "2020/12/26"
)

# 11. Convertendo a coluna Date para datetime
df_tratado["Date"] = pd.to_datetime(
    df_tratado["Date"],
    format="%Y/%m/%d"
)

print("\nAPÓS CONVERSÃO DE DATE")
print(df_tratado)

# 12. Removendo registros que possuem valores nulos em Date
df_tratado = df_tratado.dropna(subset=["Date"])

# 13. Exibindo o DataFrame final
print("\nDATAFRAME FINAL")
print(df_tratado)