secret = 9
i = 1;
won = 0;
while (i<=3):
    guess = int(input('Guess one number '))
    if guess == secret:
        print('congratulations')
        won = 1;
        break
    else:
        i = i+1;

if(won==0):
    print('try next time')


