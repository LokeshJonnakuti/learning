with open('james.txt') as jaf:
    data = jaf.readline(5_000_000)
james = data.strip().split(',')

with open('julie.txt') as juf:
    data = juf.readline(5_000_000)
julie = data.strip().split(',')

with open('mikey.txt') as mif:
    data = mif.readline(5_000_000)
mikey = data.strip().split(',')

with open('sarah.txt') as saf:
    data = saf.readline(5_000_000)
sarah = data.strip().split(',')

print(james)
print(julie)
print(mikey)
print(sarah)
