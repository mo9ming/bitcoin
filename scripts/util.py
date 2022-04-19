def str2Hexstr(origin):
	return ''.join(['{:x}'.format(ord(i)) for i in origin])

def hexstr2Str(origin):
	return ''.join([chr(int(origin[i:i + 2], 16)) for i in range(0, len(origin), 2)])

#print(chr(49))
#print(str2Hexstr(chr(49)))
#print(hexstr2Str(str2Hexstr(chr(49))))

#print('hello')
#print(str2Hexstr('hello'))
#print(hexstr2Str(str2Hexstr('hello')))
