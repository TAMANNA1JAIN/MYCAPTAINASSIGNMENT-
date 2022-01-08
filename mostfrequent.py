str1= "mississippi"
freq = {}  
for i in str1:
    if i in freq: 
        freq[i] += 1
    else:
        freq[i] = 1
  
print(str1)
print(str(freq))