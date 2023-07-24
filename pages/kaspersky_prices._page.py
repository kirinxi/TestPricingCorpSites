import re

x = '\
            Old price $66.99.\
        '
result = re.findall(r'\$\d.*\d', x)
print(result[0])