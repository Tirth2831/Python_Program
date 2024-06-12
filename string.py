#capital,small,space,alphabet,numirical count.

s=input('Enter String : ')

up=0
lo=0
sp=0
al=0
num=0

for i in s:
    if i.isupper():
        up=up+1
    elif i.islower():
        lo=lo+1
    elif i.isspace():
        sp=sp+1
    elif i.isalpha():
        al=al+1
    elif i.isnumeric():
        num=num+1

print("Upper case : ",up)
print("Lower case : ",lo)
print("Space : ",sp)
print("Alphabet : ",al)
print("Numeric : ",num)
