for i in range(1, 1000):
    s = '1'*8
    while '111' in s:
        s = s.replace('111', '2', 1)
        s = s.replace('222', '11',1)
        s = s.replace('1', '2', 1)
    if s.count('1') > 0:
        print(i, s)