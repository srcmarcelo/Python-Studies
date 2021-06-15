def vote(y):
    from datetime import datetime
    a = datetime.today().year - y
    print(f'When {a} years old: ', end='')
    if 0 <= a < 16:
        return "Cannot vote."
    if 16 <= a < 18 or a > 65:
        return "Optional vote."
    if 18 <= a <= 65:
        return "Required vote."


print(vote(int(input('Enter here a person`s year of birth: '))))
