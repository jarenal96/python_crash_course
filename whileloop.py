#prompt = "\nTell me something, and I will repeat it back to you."
#prompt += "\nEnter 'quit' to end the program."

#active = True
#while active:
    #message = input(prompt)

    #if message == 'quit':
        #active = False
    #else:
        #print(message)

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)