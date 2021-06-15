def double(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


v = [2, 4, 8, 9, 3, 10]
double(v)
print(v)
