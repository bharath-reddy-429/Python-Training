def fun():
    p1=input('player 1 enter your choice :')
    p2=input('player 2 enter your choice :')
    c=[p1,p2]
    c1=['Rock','Scissors']
    c2=['Scissors','Paper']
    c3=['Paper','Rock']
    if c==c1:
        print('Congratulations player 1')
    elif c==c2:
        print('Congratulations player 1')
    elif c==c3:
        print('Congratulations player 1')
    else:
        print('Congratulations Player 2')
    print('Do you want to play again')
    print('Type Yes if you want else No')
    e=input()
    return e
e='Yes'
while(e=='Yes'):
    e=fun()


