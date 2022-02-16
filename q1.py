userName = ''
while len(userName) < 3:
    userName = input("Enter your name ")
output = "Hello <<UserName>>, How are you?"
output = output.replace("<<UserName>>", userName)
print(output)