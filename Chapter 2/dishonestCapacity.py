# this is dishonest Capacity
# Chapter 2: AtBS
# author: diablo010

print("Enter TB or GB for the advertised unit: ")
unit = input(">").upper()

if unit == "TB":
    discrepancy = 1000000000000 / 1099511627776
elif unit == "GB":
    discrepancy = 1000000000 / 1073741824

print("Enter the advertised capacity:")
advertised_capacity = input(">")
advertised_capacity = float(advertised_capacity)     

real_capacity = round(advertised_capacity * discrepancy, 2)

print(f"The actual capacity is {real_capacity} unit")