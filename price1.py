
def format_price(price):
    price=int(price)
    a = 'цена '
    b = ' рублей'
    return f'{a}{price}{b}'
print(format_price(56.24))