
# Associate numbers with their combining diacritics (the 8th tone has no diacritic)
diacritics = {
    '1': unichr(0x304), # High tone (macron)
    '2': unichr(0x301), # Rising tone (acute)
    '3': unichr(0x30C), # Falling-rising tone (caron)
    '4': unichr(0x309), # Falling tone (diacritical hook)
    '5': unichr(0x302), # Rising-falling tone (cirxumflex)
    '6': unichr(0x300), # Low tone (grave accent)
    '7': unichr(0x303), # Creaky rising tone (diacritical tilde)
}

# Function to create a single vowel-script (number should be passed as a string)
def create_file(path, vowel, number):
    out_file = open(path + vowel + number + ".py", "w+")  # Create file

    for line in template:                                 # Copy template
        out_file.write(line.rstrip() + '\n') 
        
    out_file.write("paste_character(\'")                  # Copy operational line
    out_file.write(vowel + diacritics[number])            # Character to output
    out_file.write("\')")
    
    out_file.close()                                      # Close file


# Create abbreviation files
for vowel in ['a', 'e', 'i', 'o', 'u']:
    for tone in range(1, 8):
        template = open("/home/evan/.config/autokey/data/toaq/toaq_script_template.py", "r")
        create_file("/home/evan/.config/autokey/data/toaq/", vowel, str(tone)) # Ugly hard-code hack, but okay
        template.close()

