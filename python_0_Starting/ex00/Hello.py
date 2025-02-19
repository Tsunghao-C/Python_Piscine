ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

# your code here

ft_list[1] = 'World!'
ft_tuple = ("Hello", "France!")
ft_set.remove("tutu!")
ft_set.add("Paris!")
ft_dict["Hello"] = "42Paris!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)

# Lists stores mutable data that needs to be changed frequently

# Tuples are immutable. Usually store data that cannot be changed.

# Sets are used to store unique elements. Often used as index storage

# Dict is a key-value pair that key needs to be unique. Easy to look up
