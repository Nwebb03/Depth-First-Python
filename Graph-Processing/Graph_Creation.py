
empty_dict = {}
key_input = ""
keynum = 1
while key_input != "quit":
    empty_array = []
    key_input = input("Key " + str(keynum) + " ")
    if key_input == "quit":
        break
    value_input = ""
    while value_input != "quit":

        print("Input Values, Type 'quit' to quit")
        value_input = input("Values for 'key' seperatly ")
        if value_input != "quit":
            empty_array.append(value_input)
    keynum = keynum + 1
    empty_dict [key_input] = empty_array


file_title = input("File Name? ")
f = open(file_title, "w")
f.write(str(len(empty_dict)))
for key, value in empty_dict.items():
    f.write("\n")
    f.write(key)
    f.write("\n")
    for i,item in enumerate(value):
        f.write(item)
        if i < len(value)-1:
            f.write(",")
f.close()


