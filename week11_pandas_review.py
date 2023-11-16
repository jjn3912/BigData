import pandas as pd

df = pd.DataFrame(
    [[99, 89, 81],
scores = [[99, 89, 81],
        [91, 98, 90],
        [95, 97, 85],
        [83, 96, 94]],
    index=[1, 2, 3, 4],
    columns=['KOR', 'ENG', 'MAT']
)
        [83, 96, 94]]

index = [1, 2, 3, 4]
columns = ['KOR', 'ENG', 'MAT']

for c in columns:
    print(f'{c}', end=' ')
print()
for row in range(4):
    print(index[row], end=' ')
    for col in range(3):
        print(scores[row][col], end=' ')
        scores[row][col] = scores[row][col]+1  # update
    print()

# def scale_score(n):
#     return n + 1
#
#
# print(df)
# df = df.apply(scale_score)
# print(df)
print()

print(df)
df = df.apply(lambda n: n + 1)
print(df)
for c in columns:
    print(f'{c}', end=' ')
print()
for row in range(4):
    print(index[row], end=' ')
    for col in range(3):
        print(scores[row][col], end=' ')
    print()