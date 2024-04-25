
"""
Star pattern like this :
    
*
**
***
****
*****
...

"""

num = int(input("please enter number:"))

for i in range(0,num):
  #  for j in range(0,num-i-1): //agar bekhahim mesl heram chap shavad
   #     print(end = " ") 
    for j in range(0,i+1):
        print("*",end = " ")
    print()
