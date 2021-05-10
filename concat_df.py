from pandas import read_csv, concat

# Retorna a base de dados original, a partir dos arquivos csvs disponiveis no repositorio do github
def concat_df():
    dfs = []
    csvs = ['data/'+ str(x) + '.csv' for x in range(2009, 2018)] # List comprehension dos csvs
    for csv in csvs:
        df = read_csv(csv)
        dfs.append(df)
        
    return concat(dfs)
