from random import*
#Goal is to have:
# 30% is 0
# 50% is 1
# 20% is 2


#attempted broken code with incorrect probabliities


value = -1 
i = 0
num0 = 0
num1 = 0
num2 = 0
numtrails = 10000

while(i < numtrails):
  drandom = randint(1,100) #need to change every roll
  if( drandom < 30):
    value = 0
    num0 = num0 + 1

  elif (drandom < 80):
    value = 1
    num1 = num1 + 1
  else:
    value = 2
    num2 = num2 + 1
  i = i + 1
  #print(value)
print(num0/numtrails)
print(num1/numtrails)
print(num2/numtrails)

# the above probablities are mistakenly:
#30% for 0 
#56% for 1
# 13% for 2