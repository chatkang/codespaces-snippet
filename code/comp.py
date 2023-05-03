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


# %%
txns = [1.09, 23.56, 57.84, 4.56, 6.78]
TAX_RATE = .08

final_prices = [(lambda t: t * (1 + TAX_RATE))(i) for i in txns]
final_prices

# %%
sentence = 'the rocket came back from mars'
vowels = [i for i in sentence if i in 'aeiou']
vowels
# %%
sentence = 'The rocket, who was named Ted, came back \
from Mars because he missed his friends.'
def is_consonant(letter):
    vowels = 'aeiou'
    return letter.isalpha() and letter.lower() not in vowels

consonants = [i for i in sentence if is_consonant(i)]
consonants

# %%
sentence = 'The rocket, who was named Ted, came back \
from Mars because he missed his friends.'
vowels = 'aeiou'

is_consonant = lambda c: c.isalpha() and c.lower() not in vowels
consonants = [i for i in sentence if is_consonant(i)]
consonants

# %%
original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
prices = [i if i > 0 else 0 for i in original_prices]
prices

# %%
original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
prices = ['양수' if i > 0 else '음수' for i in original_prices]
prices

# %%
quote = "life, uh, finds a way"
unique_vowels = {i for i in quote if i in 'aeiou'}
unique_vowels

# %%
squares = {i: i * i for i in range(10)}
squares

# %%
import random
def get_weather_data():
    return random.randrange(90, 110)

# 100도 이상인 자료만 출력
hot_temps = [temp for _ in range(20) if (temp := get_weather_data()) >= 100]
hot_temps
# %%
import random
def get_weather_data():
    return random.randrange(90, 110)

# 100도 이상인 자료만 출력
hot_temps = [for _ in range(20) if get_weather_data() >= 100]
hot_temps

# %%
## 1번 코드 -> 일반 코드
s='walrus eat kimchi' ## s에 문자열을 할당
result = 'walrus' in s ## 'walrus' in s를 result에 할당
if result: ## result가 True라면
    print(s) ## s 출력
    print(result) ## result 출력
 
 
## 2번 코드 -> := 사용
## s에 문자열을 할당하고, 'walrus' in s를 result에 할당하고, result가 True 라면
if result := 'walrus' in (s := 'walrus eat kimchi'):
    print(s)  ## s 출력
    print(result) ## result 출력
# %%
