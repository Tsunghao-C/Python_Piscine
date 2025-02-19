import time
import locale


# Set locale to use comma as a thousand separator
locale.setlocale(locale.LC_ALL, '')

current_time = time.time()
formatted_time = locale.format_string("%.4f", current_time, grouping=True)
scientific_not_time = "{:.2e}".format(current_time)

print(f"Seconds since January 1, 1970: \
{formatted_time} or {current_time:.2e} in scientific notation")
print(time.strftime("%b %d %Y"))
