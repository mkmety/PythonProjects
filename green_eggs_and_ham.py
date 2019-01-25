import re

file = "green_eggs_and_ham.txt"

with open(file) as f:
    data = f.read()
    replace = re.sub(r'(i )', r'I ', data)
#    replace = re.sub(r'(?<= )(i)(?= )', r'I', data)
#    replace = re.sub(r'(?<=-)(i)(?=-)', r'I', data)
    print(replace)

    for line in f:
        #print(line)
        #data = f.read()
#        replace = re.sub(r'^i', r'I', line)
#        replace = re.sub(r'(?<= )(i)(?= )', r'I', line)
#        replace = re.sub(r'(?<=-)(i)(?=-)', r'I', line)
        print(replace)
