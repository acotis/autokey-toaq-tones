#!/usr/bin/env python3

# Associate numbers with their combining diacritics (the 8th tone has no diacritic)
diacritics = {
    '1': chr(0x304), # High tone (macron)
    '2': chr(0x301), # Rising tone (acute)
    '3': chr(0x30C), # Falling-rising tone (caron)
    '4': chr(0x309), # Falling tone (diacritical hook)
    '5': chr(0x302), # Rising-falling tone (cirxumflex)
    '6': chr(0x300), # Low tone (grave accent)
    '7': chr(0x303), # Creaky rising tone (diacritical tilde)
}

# Create the script for a given ending and tone
# (tone number should be passed as a string)
def create_script_file(path, ending, number):
    template = open(path + "script_template.txt", "r")       # Open template    
    out_file = open(path + ending + number + ".py", "w+")    # Create file

    for line in template:                                    # Copy template
        out_file.write(line.rstrip() + '\n') 
        
    out_file.write("paste_character(\'")                     # Copy operational line
    out_file.write(ending[0]+diacritics[number]+ending[1:])  # Character to output
    out_file.write("\')")

    out_file.close()                                         # Close file
    template.close()                                         # Close template

# Create the json abbreviation file for a given ending and tone
# (tone number should be passed as a string)
def create_json_file(path, ending, number):
    template = open(path + "abbreviation_template.txt")      # Open template
    out_file = open(path + "."+ending+number+".json", "w+")  # Create file

    for line in template:                                    # Copy template
        line = line.replace("-", ending + number)            # (Fill in paramaters)
        out_file.write(line)

    out_file.close()                                         # Close file
    template.close()                                         # Close template

# Create abbreviation files from endings list and template files

endings_file = open("./endings.txt", "r")

for ending in endings_file:
    ending = ending.strip()
    for tone in range(1, 8):
        create_script_file("./", ending, str(tone))
        create_json_file("./", ending, str(tone))

endings_file.close()