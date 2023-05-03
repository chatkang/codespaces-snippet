# %%
txns = [1.09, 23.56, 57.84, 4.56, 6.78]
TAX_RATE = .08

def get_price_with_tax(txn):
     return txn * (1 + TAX_RATE)

final_prices = map(get_price_with_tax, txns)
list(final_prices)
# %%
TAX_RATE = .08
txns = [1.09, 23.56, 57.84, 4.56, 6.78]

final_prices = map(lambda t: t * (1 + TAX_RATE), txns)
list(final_prices)
# %%
TAX_RATE = .08
txns = [1.09, 23.56, 57.84, 4.56, 6.78]

list(map(lambda t: t * (1 + TAX_RATE), txns))
# %%
[i * i for i in range(10)]
# %%
# new_list = [expression for member in iterable]
'''
expression is the member itself, a call to a method, or any other valid expression that returns a value. In the example above, the expression i * i is the square of the member value.
member is the object or value in the list or iterable. In the example above, the member value is i.
iterable is a list, set, sequence, generator, or any other object that can return its elements one at a time. In the example above, the iterable is range(10).
'''