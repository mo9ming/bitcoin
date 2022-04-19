# encoding: utf-8
#
s = '''04:23:a1:cc:5b:ce:87:f0:88:2f:84:8c:36:a6:d9:7c:86:e8:da:0d:8a:a1:e0:76:98:c8:70:a3:3b:1d:78:cf:90:6f:83:e3:64:3c:e3:7b:ff:83:d3:8a:7f:68:46:78:e3:39:aa:d9:c1:4a:7f:e2:e9:82:24:9c:a5:64:d4:ca:b5'''

l = s.split(':')
result = ''

for i in l:
	result += i
	
print(result)
