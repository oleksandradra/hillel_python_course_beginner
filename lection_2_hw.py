print('Hello user!')
user_name = input('Fill up your name, please \n')  # пишем Sasha
print('Cool!')

user_age = input('Fill up your age, please \n')
user_age_int = int(user_age)


if user_age_int == 16:
    print('Dear Sasha needs to wait one year ;( ')

elif 70 < user_age_int < 90:
    print('You are lucky Sasha and welcome!')

elif user_age_int > 121:
    print('You are not real Sasha.')
elif user_age_int > 16:
    print('Welcome Sasha on our website!')
else:
    print("I'm sorry Sasha you are too young.")
