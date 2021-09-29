def fun():
    d={'John': '01/22/1987', 'Ford': '06/04/1956', 'Bill': '05/02/1949'}
    print('Welcome to the birthday dictionary. We have the birthdays of :')
    for i in d.keys():
        print(i)
    print('Who\'s bithday do you want to lookup?')
    n = input()
    print(d[n])
fun()
