

def number(input):
    return int_comma(input)

def int_comma(x):
    x = int(x)
    result = ''
    while x >= 1000:
        x, r = divmod(x, 1000)
        result = ",%03d%s" % (r, result)
    return "%d%s" % (x, result)

