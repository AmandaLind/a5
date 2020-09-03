n = int(input("Enter the length of the sequence: ")) # Do not change this line

number_1=1
number_2=2
number_3=3

print(number_1,', ', number_2,', ',number_3,', ',end=' ')

for counter in range(1,n-2):
    sum_int=0
    sum_int=sum_int+number_1+number_2+number_3
    
    number_1=number_2
    number_2=number_3
    number_3=sum_int
    print(number_3,', ',end=' ')
