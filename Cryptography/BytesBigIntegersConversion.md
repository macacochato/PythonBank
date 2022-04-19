# Bytes and Big Integers Conversion


```py
import Crypto.Util.number as crypt

Crack = '11515195063862318899931685488813747395775516287289682636499965282714637259206269'
CrackBytes = crypt.long_to_bytes(int(Crack))
print(CrackBytes)
print(crypt.bytes_to_long(CrackBytes))
```

>b'crypto{3nc0d1n6_4ll_7h3_w4y_d0wn}'
>11515195063862318899931685488813747395775516287289682636499965282714637259206269