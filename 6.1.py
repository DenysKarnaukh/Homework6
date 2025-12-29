

import string
data = input()

start_letter, end_letter = data.split("-")
letters = string.ascii_letters

start_index = letters.index(start_letter)
end_index = letters.index(end_letter)

print(letters[start_index:end_index + 1])