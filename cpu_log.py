from datetime import datetime
from subprocess import call, check_output

"""
First you need to install lm-sensors

"""

#result = call('sensors', shell=True)
result = check_output(['sensors'])
result = result.decode().split()[10:]

print(datetime.now())
line = '' 
for text in result:
    if text[-1] == ')':
        print(line + ' ' + text)
        line = ''
    else:
        line += ' ' + text

