a = r"b'\xff\xff\xff'"
a = str.encode(a[2:-1]).decode('unicode-escape').encode('ISO-8859-1')
print(a)
