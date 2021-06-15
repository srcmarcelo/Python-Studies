def scr(*n, sit=False):
    """
    ->Student's scores and situation analyzer.
    :param n: Student's scores.
    :param sit: (optional) Class's situation.
    :return: Dictionary with all the information.
    """
    d = {}
    b = s = su = q = 0
    for c, v in enumerate(n):
        q += 1
        su += v
        if c == 0:
            b = s = v
        else:
            if v > b:
                b = v
            if v < s:
                s = v
    d['Amount of scores'] = q
    d['Higher Score'] = b
    # d['Higher Score'] = max(n)
    d['Lower Score'] = s
    d['Media'] = su / q
    if sit:
        if su / q >= 7:
            d['Situation'] = 'Good'
        if 6 <= su / q < 7:
            d['Situation'] = 'Satisfactory'
        if su / q < 6:
            d['Situation'] = 'Bad'
    return d


asn = scr(5.5, 5, 3, 6.5, sit=True)
print(asn)
