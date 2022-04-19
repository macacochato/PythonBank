# F before strings
What **f** does before strings is it let's you insert variables you have already declared into the string. See examples below

```py

variable_1 = 'something else'
variable_2 = 123

print(f'the value is {variable_1}')
# See output to understand what the equal sign does here
print(f'{variable_2 = }')
print(f'{variable_2 % 2 = }')
```
Output:
>the value is something else
variable_2 = 123
variable_2 % 2 = 1

```py
# !a will convert ASCII any information that does not conform to it
# like emoticons
print(f'{variable_1!a}')
# both a and r will print the string with the '' quotes
print(f'{variable_1!r}')
# We should use the above only for troubleshooting
```

Output
>'something else'
'something else'

In this case nothing is printed differently because there are no conversions needed

---
# Extra Formatting Options
```py
import datetime
# get today's date
now = datetime.datetime.utcnow()
# when printing variable now format
# according to the datetime library
print(f'{now:%d-%m-%Y}')
# this will print the number with 2 decimals
print(f'{variable_2:.2f}')
# this will also print the number with 2 decimals
nested_format = ".2f"
print(f'{variable_2:{nested_format}}')
```
Output:
>12-11-2021
123.00
123.00