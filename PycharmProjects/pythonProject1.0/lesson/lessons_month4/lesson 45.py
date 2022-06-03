def num(a):

    a=str(a)
    if len(a)%2==0:
        return f'{a} симметричное'
    else:
        return f'{a} не симметричное'
print(num(5555))