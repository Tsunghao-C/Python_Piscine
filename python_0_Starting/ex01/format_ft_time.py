import time

current_time = time.time()
scientific_not_time = "{:.2e}".format(current_time)

print(f"Seconds since January 1, 1970: {current_time} or {scientific_not_time} in scientific notation")
print(time.strftime("%b %d %Y"))