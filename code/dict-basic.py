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
