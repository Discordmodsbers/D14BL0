#Run this if you want to run 'diablo -h' and not 'python3 diablo.py -h'

USRDIR = '/usr/bin/'
USRDIR2 = '/usr/bin/D14BL0'
import os

os.system(f'git clone https://github.com/Discordmodsbers/D14BL0 {USRDIR}')
os.system('chmod +x diablo.py')
os.system(f'mv diablo.py {USRDIR2}')

with open('/etc/bash.bashrc', 'a') as f:
  f.write("alias diablo='python3 /usr/bin/D14BL0 diablo.py'")
  f.close()
 
print("Install finished please run 'diablo -h'")
