num1=[1,2,3]
num2=[4,5,6]
num3=[7,8,9]
print("original list:")
print(num1)
print(num2)
print(num3)
result=map(lambda x,y,z: x+y+z, num1,num2,num3)
print("\n new list:")
print(list(result))

