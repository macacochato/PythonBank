# Calculate characters permutations
Gigantic calculation of all the possible characters permutations with a max of 10 characters in this specific case.

>**NOTE**: Initially I tried creating a ==list== with the results from the ==product== function, this is a big NO NO as it will atempt to store the whole list into RAM and no matter how much memory you have it will crash your computer with Memory Error, trust me on this one `far:SmileBeam`

```py

from itertools import product

# List of characters
Crazy = "0123456789abcçdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

# "0123456789abcçdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&'()*+,-./:;<=>?@[\]^_`{|}~ "

# This product function will iterate through all the possibilities
Full_list = product(Crazy, repeat=10)

for item in Full_list:
	outfile = open('C:\\Tiago\\Super_Calculation.txt','a')
	outfile.write(str(item[0]+item[1]+item[2]+item[3]+item[4]+item[5]+item[6]+item[7]+item[8]+item[9]) + "\n")
	print(item)
outfile.close()
```

Found the solution to my ==Memory Error== issue here: [Link](https://coderedirect.com/questions/163869/prevent-memory-error-in-itertools-permutation)