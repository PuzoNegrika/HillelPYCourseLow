x = int(input("Введіть кількість секунд, яке більше або дорівнює 0, і менше ніж 8640000: "))

days, rest = divmod(x, 86400)  # кількість днів і залишок секунд
hours, rest = divmod(rest, 3600)  # години і залишок секунд
minutes, seconds = divmod(rest, 60)  # хвилини і секунди

if days == 1:
    day_word = "день"
elif days >= 1:
    day_word = "дня"
else:
    day_word = "днів"
if hours < 10:
    hours = "0" + str(hours)
if minutes < 10:
    minutes = "0" + str(minutes)
if seconds < 10:
    seconds = "0" + str(seconds)

print(str(days) + " " + day_word + ", " + str(hours) + ":" + str(minutes) + ":" + str(seconds))