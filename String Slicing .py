name = "Bro Code"
first_name = name[0:3]
last_name = name[4:8]
funcky_name = name[::3]
reversed_name = name[::-1]

print(first_name)
print(last_name)
print(funcky_name)
print(reversed_name)

#------------------------------------------------------------------------------------

website1 = "http://google.com"
website2 = "http://wiki.com"

slice = slice(7,-4)

print(website1[slice])
print(website2[slice])