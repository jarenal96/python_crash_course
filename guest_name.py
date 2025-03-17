from pathlib import Path

file_name = '.venv/guest.txt'
path = Path(file_name)

quit = False
name = ''
directory = []
exit = "quit".title()


while quit == False:
    name = input("What is your full name?").title()
    if name != exit:
        directory.append(name)

    elif name == exit:
        quit = True

for name in directory:
    path.write_text(directory.pop())

print(directory)
