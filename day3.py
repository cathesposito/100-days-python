# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

love_score = name1 + name2

love_score = love_score.lower()

count_t = love_score.count('t')
count_r = love_score.count('r')
count_u = love_score.count('u')
count_e = love_score.count('e')

count_l = love_score.count('l')
count_o = love_score.count('o')
count_v = love_score.count('v')
count_e = love_score.count('e')

total_true = count_t + count_r + count_u + \
    count_e
    
total_love = count_l + count_o + count_v + \
    count_e

love_score = int(str(total_true) + str(total_love))

if love_score < 10 or love_score > 90:

    print(f"Your score is {love_score}, you go together like coke and mentos.")

elif love_score >= 40 and love_score <= 50:

    print(f"Your score is {love_score}, you are alright together.")

else:

    print(f"Your score is {love_score}.")
