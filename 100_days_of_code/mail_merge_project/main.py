#Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

with open("./Input/Name/invited_names.txt", 'r') as names_file:
    names = names_file.readlines()

with open("./Input/Letters/starting_letter.txt", 'r') as starting_letter:
    template_letter = starting_letter.read()
    for name in names:
        stripped_name = name.strip()
        personalized_letter = template_letter.replace("[name]", stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", "w") as new_letter:
            new_letter.write(personalized_letter)


