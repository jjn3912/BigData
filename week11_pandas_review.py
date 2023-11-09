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

print(df.query('KOR>=95 and ENG>=95'))