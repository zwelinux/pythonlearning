import random
coin_result = random.randint(1,2) # random အဖြစ် ထုတ်ပေးတဲ့ function ဖြစ်ပါတယ်။

choice = int(input("Enter your choice (head for 1/tail for 2) : "))

if choice == 1 and coin_result == 1:
    print("It's Head. You Won")
elif choice == 1 and coin_result == 2:
    print("It's Tail. You Loose")
elif choice == 2 and coin_result == 2:
    print("It's Tail. You Won")
elif choice == 2 and coin_result == 1:
    print("It's Head. You Loose")