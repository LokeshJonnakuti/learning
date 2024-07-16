import secrets

guess = ''
ans = ('heads', 'tails')
while guess not in ans:
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()

    toss = ans[secrets.SystemRandom().randint(0, 1)]
    if toss == guess:
        print('You got it!')
    else:
        print('Nope! Guess again! Enter heads or tails:')
        guess = input()
        toss = ans[secrets.SystemRandom().randint(0, 1)]
        if toss == guess:
            print('You got it!')
        else:
            print('Nope. You are really bad at this game.')
