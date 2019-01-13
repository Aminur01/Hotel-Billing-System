def menu():
    print('Items :')
    print('1.chai-         rs 15\n2.coffee-       rs 25\n3.chingara-     rs 20\n4.paratha-      rs 39\n5.veg roll-     rs 59\n6.chick roll-   rs 79\n7.veg chaw-     rs 69\n8.chick chaw-   rs 99\n9.veg biryani-  rs 199\n10.chick biryani-rs 299')
def bill():
    q1=q2=q3=q4=q5=q6=q7=q8=q9=q10=0
    print('do you want to place order ?')
    print('press y to yes no n exit\n')
    b=input()  
    while b=='y':
           c=int(input("choose please"))
           if c==1:
              q1=int(input('quantity?'))
              b=input('y to more\n')
           if c==2:
              q2=int(input('quantity?'))
              b=input('y to more\n')
           if c==3:
              q3=int(input('quantity?'))
              b=input('y to more\n')
           if c==4:
              q4=int(input('quantity?'))
              b=input('y to more\n')
           if c==5:
              q5=int(input('quantity?'))
              b=input('y to more\n')
           if c==6:
              q6=int(input('quantity?'))
              b=input('y to more\n')
           if c==7:
              q7=int(input('quantity?'))
              b=input('y to more\n')
           if c==8:
              q8=int(input('quantity?'))
              b=input('y to more\n')
           if c==9:
              q9=int(input('quantity?'))
              b=input('y to more\n')
           if c==10:
              q10=int(input('quantity?'))
              b=input('y to more\n')
           lst=[q1,q2,q3,q4,q5,q6,q7,q8,q9,q10]
           sum=q1+q2+q3+q4+q5+q6+q7+q8+q9+q10
           print('total quantity is %d'%(sum))
           total=15*lst[0]+25*lst[1]+20*lst[2]+39*lst[3]+59*lst[4]+79*lst[5]+69*lst[6]+99*lst[7]+199*lst[8]+299*lst[9]
           print('your total bill is %d'%(total))
    print('do you want to place order enter y to yes else n\n')
    m=input()
    if m=='y':
       print('thank you!!!! your order has been placed [avrg wait time 15 mnt]')
    else:
       print('thank you visit again :)')
print('welcome to Hotel Flamingo !!!')
print('what would you like to have sir')
print('press e to menu')
a=input()
if a=='e':
    menu()
    bill()
