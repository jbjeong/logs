from datetime import datetime
from subprocess import call, check_output

"""
First you need to install lm-sensors

Add to crontab
*/5 * * * * python cpu_log.py >> cpu.log

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

