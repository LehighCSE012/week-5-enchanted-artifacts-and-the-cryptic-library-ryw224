with open("my_input.txt", "r") as file:
    f = file.readlines()
    print(f)
with open("my_input.txt", "r") as file:
    f = file.readlines()
    for linenumber, line in enumerate(f):
        print(f"{linenumber + 1}. {line.strip()}")
with open("my_input.txt", "r") as file:
    word = "Python"
    for line in f:
        if word.strip() in line:
            print(line)
