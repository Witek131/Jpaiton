f = open('24102024/26.txt').read().split('\n')
mas = dict()
for i in f:
    s = i.split()
    mas[s[0]] = [sum(int(s[j]) for j in range(1,len(s))), sum(int(s[j]) for j in range(1,len(s)) if int(s[j]) > 0), sum(int(s[j]) for j in range(1,len(s)) if int(s[j]) != 0)]
print(mas)