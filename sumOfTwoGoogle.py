def sumOfTwo(a, b, v):
    b_ = set(b)
    for num1 in a:
        if (v-num1) in b_:
            return True
    return False
