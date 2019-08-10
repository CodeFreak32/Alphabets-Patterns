for row in range(7):
    for col in range(5):
        if (col==0 or col==4) or (row==4 and col==2) or (row==5 and col==1) or (row==5 and col==3): 
            print("*",end=" ")
        else:
            print(end="  ")
    print()