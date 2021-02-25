user_namber= input('введите число от 0 до 20: ')
if user_namber.isdigit() != True:
    print('вы ввели другое значение.')
elif int(user_namber) >20 and int(user_namber)<0:
    print('Вы ввели число вне диапазона.')
else:
    if int(user_namber)>0 and int(user_namber)<2:
        print (f'{user_namber} процент')
    elif int(user_namber)>2 and int(user_namber)<5:
        print (f'{user_namber} процента')
    else:
        print(f'{user_namber} процентов')

