def product(x, y):
    if x < 10 or y < 10:
        return x * y
    if y > x:
        return product(y, x)
    
    n = len(str(x))
    half = n // 2
    a = x // (10 ** half)
    b = x % (10 ** half)
    c = y // (10 ** half)
    d = y % (10 ** half)

    ac = product(a, c)
    bd = product(b, d)
    temp = product(a+b, c+d)
    ad_plus_bc = temp - ac - bd

    ret = (10 ** (2*half)) * ac + bd + (10 ** half) * (ad_plus_bc)
    return int(ret)

a = 2718281828459045235360287471352662497757247093699959574966967627
b = 31415926535897932384626433832795028841971693993751058209749445923141592653589793238462643383279502884197169399375105820974944592

print(product(a, b) == a * b)