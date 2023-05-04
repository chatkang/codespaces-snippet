# %%
a = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
a
# %%
a = dict(color='blue', fruit='apple', pet='dog')
a
# %%
dir(dict)
# %%
dir({})
# %%
for k in a:
    print(k)
# %%
for k in a:
    print(k, '->', a[k])
# %%
a.items()
# %%
for i in a.items():
    print(i)
# %%
prices = dict(apple=0.4, orange=0.35, banana=0.25)
for k, v in prices.items():
    prices[k] = round(v * 0.9, 2)
prices
# %%
help(round)
# %%
b = dict(one=1, two=2, three=3, four=4)
n = {}
for key, value, in b.items():
    n[value] = key
n
# %%
b = dict(one=1, two=2, three=3, four=4)
n = {}
for key, value, in b.items():
    if value <= 2 :
        n[value] = key
n

# %%
objects = ['blue', 'apple', 'dog']
categories = ['color', 'fruit', 'pet']
a = {key: value for key, value in zip(categories, objects)}
a
# %%
b = dict(one=1, two=2, three=3, four=4)
n = {value: key for key, value in b.items()}
n
# %%
b = dict(one=1, two=2, three=3, four=4)
n = {value: key for key, value in b.items() if value <= 2}
n

# %%
incomes = {'apple': 5600.00, 'orange': 3500.00, 'banana': 5000.00}
total_income = sum([value for value in incomes.values()])
total_income
# %%
incomes = {'apple': 5600.00, 'orange': 3500.00, 'banana': 5000.00}
total_income = sum(value for value in incomes.values())
total_income

# %%
incomes.values()
# %%
sum(incomes.values())
# %%
incomes = {'apple': 5600.00, 'orange': 3500.00, 'banana': 5000.00}
{k: incomes[k] for k in incomes.keys() - {'orange'}}
# %%
{k: incomes[k] for k in incomes.keys() - {'banana'}}

# %%
incomes = {'apple': 5600.00, 'orange': 3500.00, 'banana': 5000.00}
{k: incomes[k] for k in sorted(incomes)}
# %%
incomes = {'apple': 5600.00, 'orange': 3500.00, 'banana': 5000.00}
def by_value(item):
    return item[1]
for k, v in sorted(incomes.items(), key=by_value):
    print(k, '->', v)
# %%
sorted(incomes.items(), key=by_value)
# %%
for value in sorted(incomes.values()):
    print(value)
# %%
incomes = {'apple': 5600.00, 'orange': 3500.00, 'banana': 5000.00}
for key in sorted(incomes, reverse=True):
   print(key, '->', incomes[key])
# %%
a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}

while True:
    try:
        print(f'Dictionary length: {len(a_dict)}')
        item = a_dict.popitem()
        # Do something with item here...
        print(f'{item} removed')
    except KeyError:
        print('The dictionary has no item now...')
        break
# %%
prices = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25}
def discount(current_price):
    return (current_price[0], round(current_price[1] * 0.95, 2))
dict(map(discount, prices.items()))

# %%
prices = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25}
def has_low_price(price):
    return prices[price] < 0.4

list(filter(has_low_price, prices.keys()))

# %%
list(filter(lambda x: prices[x] < 0.4, prices.keys()))

# %%
vegetable_prices = {'pepper': 0.20, 'onion': 0.55}
fruit_prices = {'apple': 0.40, 'orange': 0.35, 'pepper': .25}
{**vegetable_prices, **fruit_prices}
# %%
# OrderedDict vs dict in Python: The Right Tool for the Job
# %%
from collections import OrderedDict
numbers = OrderedDict()
numbers["one"] = 1
numbers["two"] = 2
numbers["three"] = 3

numbers
# %%
dir(OrderedDict)
# %%
dir(dict)
# %%
help(numbers.move_to_end)
# %%
numbers = OrderedDict([("one", 1), ("two", 2), ("three", 3)])
numbers
# %%
letters = OrderedDict({("a", 1), ("b", 2), ("c", 3)})
letters
# %%
letters = dict((("a", 1), ("b", 2), ("c", 3)))
letters

# %%
type({("a", 1), ("b", 2), ("c", 3)})
# %%
from collections import OrderedDict

keys = ["one", "two", "three"]
OrderedDict.fromkeys(keys, 0)
# %%
dict.fromkeys(keys, 1)
# %%
from collections import OrderedDict
numbers = OrderedDict(one=1, two=2, three=3)
numbers
# %%
OrderedDict([('one', 1), ('two', 2), ('three', 3)])
numbers.move_to_end("one")
numbers
# %%
numbers.move_to_end("one", last=False)
numbers
# %%
from collections import OrderedDict
letters = OrderedDict(b=2, d=4, a=1, c=3)
letters
# %%
sorted(letters)
# %%
for key in sorted(letters):
    letters.move_to_end(key)
letters
# %%
from collections import OrderedDict
letters = OrderedDict(b=2, d=4, a=1, c=3)
letters.sorted_keys = lambda: sorted(letters.keys())
vars(letters)
# %%
letters.sorted_keys()
# %%
letters["e"] = 5
letters.sorted_keys()
# %%
