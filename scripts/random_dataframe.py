from envtest import random_dataframe

lines = input("No. of lines: ")
columns = input("No. of columns: ")
size = (int(lines), int(columns))

df = random_dataframe(size)
print(df)

