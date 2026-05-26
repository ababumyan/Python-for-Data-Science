import datetime
import time
import locale


locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
time = time.time()
tousand_separator = locale.format_string("%.4f", time, grouping=True)
today = datetime.datetime.now()

print(tousand_separator)
print(f"Seconds since January 1, 1970: {tousand_separator} or {time:2e} in \
scientific notation.")
print(today.strftime("%B %d %Y"))
