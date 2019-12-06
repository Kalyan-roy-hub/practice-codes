n=int(input('enter a num:'))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=' ')
    print()

       
for num in range(10):
    
    for i in range(num):
        print (num, end=" ")   
    print('\n')   
    
    
    
    
t=input('enter a num:')
if t == t[::-1]:
    print(True)
else:
    print(False)