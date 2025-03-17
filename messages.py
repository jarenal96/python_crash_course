messages = ['Good morning', 'Good afternoon', 'Good eveninig', 'Good night']
sent_messages = []

def show_messages(messages):
    for message in messages:
        print(message)


show_messages(messages)

def send_messages(messages):
    while messages:
        current_message = messages.pop()
        print(f"Sending: {current_message}")
        sent_messages.append(current_message)
        print("Message Sent.")
send_messages(messages[:])

print(messages)
print(sent_messages)