import re

new_string = 'gate 37;\n'
new_result = re.findall('[0-9]+', new_string)
print(new_result[0])
