a = 19
b = 16
print(bin(a))
print(len(bin(a)))
flag_list = ['URG', 'ACK', 'PSH', 'RST', 'SYN', 'FIN']
res = []
a = bin(a)
for i in range(len(a) - 2):
    if a[i + 2] == '1':
        res.append(flag_list[i + (8 - len(a))])
print(','.join(res))
