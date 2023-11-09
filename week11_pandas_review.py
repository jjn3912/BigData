import pandas as pd


df = pd.DataFrame(
    [
        [99, 89, 100],
        [91, 98, 90],
        [100, 97, 85],
        [83, 97, 94]
    ], index=[1, 2, 3, 4],
    columns=["KOR","ENG","MAT"]

)
print(df)
df_copy = df.loc[df['KOR']>=95,['KOR','MAT']]
print(df_copy)
print(df.at[1,'MAT'])
print(df.iat[0,2])