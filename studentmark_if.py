rno=int(input("roll no :"))
sname=input("Student name : ")
s1=int(input("Enter marks Of sub 1 : "))
s2=int(input("Enter marks Of sub 2 : "))
s3=int(input("Enter marks Of sub 3 : "))

total=s1+s2+s3
per=total/3

print("Roll Number : ",rno)
print("Student Name : ",sname)
print("Roll Total : ",total)
print("Roll Persantage : ",per)

if per>=70:
    print("Gread A")
elif per>=60:
    print("Gread B")
elif per>=50:
    print("Gread C")
elif per>=40:
    print("Gread D")
else:
    print("Fail")

