# Split Operations

###### Syntax
_string_.split(_separator, maxsplit_)

---

###### Example 1:
```py
txt = "hello, my name is Peter, I am 26 years old"    
x = txt.split(", ")
print(x)
```
output:
```py
["hello", "my name is Peter", "I am 26 years old"]   
```
>**Conclusion:** it split the string where it found a comma together with a space and packed the split strings into 1 list.

---

###### Example 2:
```py
txt = "apple#banana#cherry#orange"  
x = txt.split("#")  
print(x)
```
output:
```py
["apple", "banana", "cherry", "orange"]   
```
>**Conclusion:** it split the string where it found a # and packed the split strings into 1 list.

---

###### Example 3:
```py
txt = "apple#banana#cherry#orange"  
# setting the maxsplit parameter to 1, will return a list with 2 elements!  
x = txt.split("#", 1)
print(x)
```
output:
```py
["apple", "banana"]   
```
>**Conclusion:** it split the string where it found the 1st # only and packed the split strings (2 in this case) into 1 list.

---

#### Why is this handy?
Because we can then get only the part of the string(s) we need.

So if a username is something like Steve#1230928 we can extract only the name
by x = txt.split(#) and then get the name x[0]

```py
txt = "Steve#1230928"  
x = txt.split("#")
print(x[0])
print(x[1])
```
output:
```py
["Steve"]
["1230928"]
```

---

##### Example 4:
Note that you can use a variable in a slice:
```py
l = ['a','b','c','d',' e']
c_index = l.index("c")
l2 = l[:c_index]
l3 = l[c_index:]
print(l2)
print(l3)
```

This would put the first two entries of l in l2
("c" is used as the splitter)
output:
```py
['a','b']
['c','d','e']
```