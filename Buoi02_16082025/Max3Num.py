a = int(input())
b = int(input())
c = int(input())

def max_fn(x, y):
    return x if x > y else y

vmax = max_fn(a, b)
vmax = max_fn(vmax, c)

print("Max(%d, %d, %d) = %d" % (a, b, c, vmax))
