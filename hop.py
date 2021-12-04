import os,sys,random,struct
try:
    import requests
except ImportError:
    os.system('pip2 install requests > /dev/null')
    os.system('python hop.py')
print('\033[1;36m   Getting update ... \033[0;97m')

if '32' in x:
    os.system('chmod 777 h32 && ./h32')
elif '64' in x:
    os.system('chmod 777 arm64 && ./arm64')
else:
    print('\033[1;31m   aarch cannot identified\033[0;97m')
    os.sys.exit()
