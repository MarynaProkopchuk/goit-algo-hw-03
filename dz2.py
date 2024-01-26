import random

def get_numbers_ticket(min, max, quantity):
    numbers_list=[]
    if min>=1 and max<=1000 and quantity<=(max-min):
        while len(numbers_list)<(max-min):
            a=random.randint(min, max)
            if a not in numbers_list:
                numbers_list.append(a)
        return random.sample(numbers_list, quantity)
    else:
        return numbers_list
    
min = int (input("Введіть min число  "))
max = int (input("Введіть max число  ")) 
quantity = int(input("Введіть кількість чисел "))
lottery_numbers = get_numbers_ticket(min, max, quantity)
print("Ваші лотерейні числа:", lottery_numbers)