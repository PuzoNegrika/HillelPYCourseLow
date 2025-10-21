import string

x = input("Введіть через дефіс дві літери: ")

start = x[0]
end = x[2]
x_letters = string.ascii_letters

start_i = x_letters.index(start) # знайде 1 входження і кінець
end_i = x_letters.index(end)

x_letters = x_letters[start_i:end_i+1] # видасть усі символи між (+1, щоб включно до останнього)
print(x_letters)