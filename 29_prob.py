def code():
    ls = []
    for a in range(2,101):
        for b in range(2,101):
            i = a**b
            if not(i in ls):
                ls.append(i)
    return len(ls)