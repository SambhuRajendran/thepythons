def rev_a_str(revr):
    rev = ''
    for char in revr:
        rev = char + rev
    return rev


stringtorev = str(input('enter the string: '))
print('reversed str is:', rev_a_str(stringtorev))
