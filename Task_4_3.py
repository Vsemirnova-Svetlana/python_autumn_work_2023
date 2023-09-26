import string
line1 = input("-->").lower()
line2 = input("-->").lower()

line1_new=line1.translate(str.maketrans('','',string.punctuation))
line2_new=line2.translate(str.maketrans('','',string.punctuation))

dct1 = {}
dct2 = {}

for k in line1_new:
    dct1[k] = dct1.get(k,'') + k


for h in line2_new:
    dct2[h] = dct2.get(h,'') + h

print(dct1==dct2)