k=0

def test_func(x):
    global k
    k = x+k
    return k

test_func(2)

