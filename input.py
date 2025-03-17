prompt = "If you share your name, we can personalize the messages you see."
prompt += "\n What is your first name?"

name= input(prompt)
print(f"\nHello {name}!")

age = int(input(f"\nHow old are you {name}?"))
print(age>=18)