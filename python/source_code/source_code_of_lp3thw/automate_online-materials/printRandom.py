import secrets

for i in range(5):
    print(secrets.SystemRandom().randint(1, 10))
