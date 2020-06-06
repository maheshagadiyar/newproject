#finding vowels in a sequence
def fun(v):
    letters = ['a', 'e', 'i', 'o''u']
    if (v in letters):
        return True
    else:
        return False


sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r']
result = list(filter(fun, sequence))
print(result)
