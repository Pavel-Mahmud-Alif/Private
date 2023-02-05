import os, sys, platform
try:
    import requests
except:
    os.system('pip install requests')
os.system('xdg-open https://www.facebook.com/SH1N50')

bit = platform.architecture()[0]
if bit == '64bit':
    import best
elif bit == '32bit':
    print('w8 for update')
