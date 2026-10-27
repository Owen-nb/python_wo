f_p={'wzj':['1','2','3'],'fjw':['4','5','6'],'csy':['7','8','9']}
for n,ps in f_p.items():
    print(n,end=',')
    print('like',end=' ')
    for p in ps:
        print(f'{p}',end=' ')
    print("\n")

