# 자연수 number를 입력 받아, 각 자릿수의 합을 계산하여 출력하시오.
# sum_of_digit(1234) #=> 10
# sum_of_digit(4321) #=> 10
def sum_of_digit(number):
    lst_numbers = list(str(number))
    add_num = 0
    for lst_number in lst_numbers:
        add_num += int(lst_number)
    return add_num
print(sum_of_digit(1234))
print(sum_of_digit(4321))
