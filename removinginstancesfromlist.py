responses = {}

# Set a flag to indicate that polling is active

polling_active = True

while polling_active:
    # Prompt for the person's name and response.
    name = input("\n What is your name?")
    response = input("Which mountain would you like to climb someday?")

    # Store response in the dictionary
    responses[name] = response

    # Find out if anyone else is going to take the poll.

    repeat = input("Is anybody else going to respond the poll? (yes/no)")
    if repeat == 'no':
        polling_active = False

# Polling is complete, show the results
print("\n --- Poll Results ---")
for name,response in responses.items():
    print(f"{name.title()} would like to climb {response.title()}.")

print(responses)