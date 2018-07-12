#!/usr/bin/python3

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

# Create the script for a given vowel and tone
# (tone number should be passed as a string)
def create_script_file(path, vowel, number):
    template = open(path + "toaq_script_template.txt", "r")  # Open template    
    out_file = open(path + vowel + number + ".py", "w+")     # Create file

    for line in template:                                    # Copy template
        out_file.write(line.rstrip() + '\n') 
        
    out_file.write("paste_character(\'")                     # Copy operational line
    out_file.write(vowel + diacritics[number])               # Character to output
    out_file.write("\')")

    out_file.close()                                         # Close file
    template.close()                                         # Close template

# Create the json abbreviation file for a given vowel and tone
# (tone number should be passed as a string)
def create_json_file(path, vowel, number):
    template = open(path + "toaq_hotkey_template.txt")       # Open template
    out_file = open(path + "."+vowel+number+".json", "w+")   # Create file

    for line in template:                                    # Copy template
        line = line.replace("-", vowel + number)             # (Fill in paramaters)
        out_file.write(line)

    out_file.close()                                         # Close file
    template.close()                                         # Close template
    
# Create abbreviation files
for vowel in ['a', 'e', 'i', 'o', 'u']:
    for tone in range(1, 8):
        create_script_file("./", vowel, str(tone))
        create_json_file("./", vowel, str(tone))