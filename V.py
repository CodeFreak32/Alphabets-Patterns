for row in range(7):
    for col in range(5):
        if ((col==0 or col==4) and row!=5 and row!=6) or (row==5 and col==1) or (row==5 and col==3) or (row==6 and col==2):
            print("*",end=" ")
        else:
            print(end="  ")
    print()
