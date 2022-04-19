# How to Decode XOR

### If we get 2 strings similar to this:
```py
s1 = "44585d6b2368737c65252166234f20626d"
s2 = "1010101010101010101010101010101010"
```
### Open a Python script with the below:
```py
s1 = "44585d6b2368737c65252166234f20626d"
s2 = "1010101010101010101010101010101010"
h = hex(int(s1, 16) ^ int(s2, 16))[2:]
final = bytes.fromhex(h).decode('utf-8')
print(final)
```

>THM{3xclu51v3_0r}