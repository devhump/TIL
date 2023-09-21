
full_letters = input()

result = ""
result += full_letters[0]

for i in range(len(full_letters)):
    if full_letters[i] == '-':
        result += full_letters[i+1]

print(result)