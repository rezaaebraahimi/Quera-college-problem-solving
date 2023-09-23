ls = []
chr_inpt = []

q = int(input())

for n in range(q):
    chr_inpt = list(input().split())
    
    if chr_inpt[0] == '+': 
        ls.insert(int(chr_inpt[1])-1,int(chr_inpt[2]))
        print(*ls, sep=' ')

    elif chr_inpt[0] == '-':
        ls.pop(int(chr_inpt[1])-1)
        print(*ls, sep=' ')
        if ls == []:
            print('EMPTY')
            pass
        
        