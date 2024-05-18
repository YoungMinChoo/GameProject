# Count the number of names in the list that have the letter M in it (Upper case only)

names = ['Beth', 'Margaret', 'Bob', 'Faye', 'Kristen', 'Luqman', 'Mom', 'Dad', 'Min', 'Johnny']

Mname = 0

for name in names:
    if 'M' in name:
        Mname = Mname + 1
print(Mname)