# this is Opposite Day
# Chapter 2: AtBS
# author: diablo010

today_opposite_day = bool(input("Enter (T/F)"))
print(today_opposite_day)
# Set say based on today
if today_opposite_day == True:
    say_opposite_day = True
else:
    say_opposite_day = False

# If today is true, negate say
if today_opposite_day == True:
    say_opposite_day = not say_opposite_day

# Answer
if say_opposite_day == True:
    print("Today is Opposite Day!")
else:
    print("Today is not Opposite Day!")
