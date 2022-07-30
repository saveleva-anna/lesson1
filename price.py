
def get_summ(one, two, delimiter='&'):
    one=str.upper(one)
    two=str.upper(two)
    with_del = one + '&' + two
    return with_del
print(get_summ('learn', 'python'))