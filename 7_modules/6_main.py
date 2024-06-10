#6_main.py

from pythonping import ping

address= input('enter address: ')
ping (address, verbose=True,count=10)
# ping (address, verbose=False,count=10)
