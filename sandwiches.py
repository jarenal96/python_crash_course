ingridients = []
active = True

def make_sandwich(ingridients):
    while active == True:
        current_ingridient = input("What ingredient do you want? ")
        if current_ingridient == 'q':
           break

        ingridients.append(current_ingridient)
    print("Making a sandwich with: ")
    for ingridient in ingridients:
        print(f" - {ingridient}")
print(ingridients)

print("To exit enter 'q'.")
make_sandwich(ingridients[:])
make_sandwich(ingridients[:])
make_sandwich(ingridients[:])

