# for i in range(100):
#     print("I want to be a great programmer")

result =0 
# for i in range(50):
#    result= result+1


# range(start,n,increment)
for _ in range(2,50,2):
    result= result+1

print(result)

numbers =[1,4,5,3,8,54,4]
maxNumber =numbers[0]

for i in numbers:
    if i>maxNumber:
        maxNumber=i
        
print(maxNumber)