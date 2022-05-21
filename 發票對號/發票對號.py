win = open('中獎號碼.txt').read().split()
mine = open('我的號碼.txt').read().split()

for i, num in enumerate(mine):
    if num in win:
        print('第', i+1, '張發票對中號碼', num, '!')