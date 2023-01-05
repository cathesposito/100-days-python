# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


name1 = name1.lower()
name2 = name2.lower()

count_t_1 = name1.count('t')
count_r_1 = name1.count('r')
count_u_1 = name1.count('u')
count_e_1 = name1.count('e')

count_t_2 = name2.count('t')
count_r_2 = name2.count('r')
count_u_2 = name2.count('u')
count_e_2 = name2.count('e')

total_true = count_t_1 + count_r_1 + count_u_1 + \
    count_e_1 + count_t_2 + count_r_2 + count_u_2 + count_e_2

count_l_1 = name1.count('l')
count_o_1 = name1.count('o')
count_v_1 = name1.count('v')
count_e_1 = name1.count('e')

count_l_2 = name2.count('l')
count_o_2 = name2.count('o')
count_v_2 = name2.count('v')
count_e_2 = name2.count('e')

total_love = count_l_1 + count_o_1 + count_v_1 + \
    count_e_1 + count_l_2 + count_o_2 + count_v_2 + count_e_2

love_score = str(total_true) + str(total_love)

if int(love_score) < 10 or int(love_score) > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif int(love_score) > 40 and int(love_score) < 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")
