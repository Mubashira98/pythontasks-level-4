
''' 1. Write a program to find the factorial of a number'''
#
# num = int(input("enter number"))
# factorial = 1
# if num < 0:
#    print("factorial does not exist for negative numbers")
# elif num == 0:
#    print("The factorial of 0 is 1")
# else:
#    for i in range(1,num + 1):
#        factorial = factorial*i
#    print("The factorial of",num,"is",factorial)

'''2. Write a program to generate Fibonacci series of N terms.'''
# n=int(input("enter a limit"))
# f1=0
# f2=1
# print(f1,f2,end=" ")
#
# for i in range(2,n):
#     f3=f1+f2
#     f1=f2
#     f2=f3
#     print(f3,end=" ")


'''
3. Write a program to find the sum of all items in a list.[Using for loop]
'''

# l=[]
# n=int(input("enter limit"))
# for i in range(0,n):
#     l.append(int(input("enter value")))
# sum=0
# for i in l:
#     sum=sum+i
# print(sum)

'''
 4. Generate a list of four digit numbers in a given range with all their digits even and the number is a perfect square
'''
# l=[]
# for i in range(1000,9999):
#     n=str(i)
#     a=int(n[0])
#     b=int(n[1])
#     c=int(n[2])
#     d=int(n[3])
#     m=i**(0.5)
#     if a%2 == 0 and b%2 == 0 and c%2 == 0 and d%2 == 0:
#         if (m//1)==m:
#             l.append(int(n))
# print(l)




'''
5. Write a program using a for loop to print the multiplication table of n, where n is entered by the user.
'''

# n=int(input("enter number"))
# for i in range(1,11):
#     print(i,'*' , n,'=',i*n)


'''
6. Display the given pyramid with the step number accepted from the user. Eg: N=4
1
2 4
3 6 9
4 8 12 16
'''
# n=int(input("enter step number"))
# for i in range(1,n+1):
#
#     for j in range(1,i+1):
#         print(i*j, end=" ")
#     print("")



'''
7. Write a program to generate all factors of a number. [use while loop]
'''
# n=int(input("enter a number"))
# i=n
# while i!=0:
#     if n%i == 0:
#         print(i)
#     i=i-1

'''
8. Write a program to print the reverse of a number. [use while loop]
'''
# n=int(input("enter a number"))
# reverse=0
# while n!=0:
#     digit=n%10
#     reverse = digit+ (reverse*10)
#     n=n//10
#
# print(reverse)

'''
9. Write a program to find whether the given number is an  Armstrong number or not. [use while loop]
'''
# n=int(input("enter number"))
# num=n
# l=len(str(num))
# sum =0
# while num!=0:
#     digit = num%10
#     sum=sum+(digit**l)
#     num=num//10
# if sum == n:
#     print("given number is an armstrong number")
# else:
#     print("not an armstrong number")

'''
10.Construct following pattern using nested loop
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
'''

# for i in range(1,5):
#     for j in range(i):
#         print('*', end=" ")
#     print("")
# for i in range(5,0,-1):
#     for j in range(i):
#         print('*', end=" ")
#     print("")