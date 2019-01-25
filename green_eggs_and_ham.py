file = "green_eggs_and_ham.txt"

with open(file) as f:
    data = f.read()
    replace = data.replace('i ', 'I ').replace('-i-', '-I-')
    print(replace)
