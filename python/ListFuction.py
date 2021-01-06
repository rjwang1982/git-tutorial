lucky_numbers = [4,8,15,16,23,42]
friends = ["Kevin","Kare","Jim","Oscar","Tod"]
friends.append("Greed")
print(friends)
friends.extend(lucky_numbers)
print(friends)
friends.insert(1,"Kelly")
print(friends)
friends.remove("Jim")
print(friends)
friends.pop()
print(friends)
print(friends.index("Tod"))
print(friends.count("Kelly"))

lucky_numbers.sort()
lucky_numbers.reverse()
print(lucky_numbers)

#friends2 = friends.copy()
#print(friends2)
