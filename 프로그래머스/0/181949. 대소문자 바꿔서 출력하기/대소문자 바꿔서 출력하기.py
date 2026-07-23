str = input()

answer = []
for char in str:
    if char.isupper():
        answer.append(char.lower())
    else:
        answer.append(char.upper())

print("".join(answer))