n = int(input("enter the number :"))    # Kitni rows ka pattern banana hai



for row in range(1, n+1):  # 1 se n tak rows loop
    for col in range(1, 4):  # 1 se row number tak columns loop
        if (col==1) or (row==1 and col<3) or (row==3 and col<3) or (row==5 and col<3) or (row==2 and col==3) or (row==4 and col==3):
            print("*", end=' ')
        else:
            print(" ", end=' ')

    print()  # Har row ke baad next lin
    
print("\n")

for row in range(1, n+1):
    for col in range(1, 4):  # 3 columns ka R banayenge
        if (col == 1) or \
           (row == 1 and col < 3) or \
           (row == 3 and col < 3) or \
           (row == 2 and col == 3) or \
           (row == 4 and col == 2) or \
           (row == 5 and col == 3):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


print("\n")

for row in range(1, n+1):
    for col in range(1, 6):
        if col==1 or row==5 or col==5 :
            print("*",end='')
        else:
            print(" ",end='')
    print()        

print("\n")

for i in range(1,n+1):
    for j in range(1,n+1):
        if j==1 or j==i or j==5:
            print("*",end='')
        else:
            print(" ",end='')
    print()    
    
print("\n")
# (j == 1 and i != 1 and i!= n) or (j == n and i!= 1 and i!= n) or(i==1 and j!= 1 and j!= n) or(i== n and j!= 1 and j!= n)
for i in range(1,n+1):
    for j in range(1,n+1):
        if(j == n and i!= 1 and i!= n) or (j==1 and i!=1 and i!=n) or (i==1 and j!=1 and j!=n) or (i==n and j!=5 and j!=1):
            print("*",end='')
        else:
            print(" ",end='')
            
    print()  