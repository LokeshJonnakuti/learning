
def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return(time_string)
    (mins, secs) = time_string.split(splitter)
    return(mins + '.' + secs)

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

print(sorted(set([sanitize(t) for t in james]))[0:3])
print(sorted(set([sanitize(t) for t in julie]))[0:3])
print(sorted(set([sanitize(t) for t in mikey]))[0:3])
print(sorted(set([sanitize(t) for t in sarah]))[0:3])
