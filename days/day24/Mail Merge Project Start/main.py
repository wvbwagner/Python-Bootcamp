#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open('Mail Merge Project Start/Input/Names/invited_names.txt') as names:
    list_of_names = names.readlines()


for names in list_of_names:
    with open('Mail Merge Project Start/Input/Letters/starting_letter.txt') as letter:
        names_for_letter = letter.read().replace('[name]', names.strip())
    with open(f'Mail Merge Project Start/Output/ReadyToSend/letter_for_{names}.txt' , mode='x') as file:
        file.write(names_for_letter)

    
