# Input groups number
groups = [100,25,50]

# Input start and end numbers for each group above
starting_numbers = [1,1,1]
ending_numbers = [49,25,49]

# If tens (10, 20, 30, etc.) need to be skipped, set this as True; True is usually the default
skip_tens = True

# If there are any extra numbers to skip, put them here;
# example: if 2 and 4, and 1 and 3 are to be skipped in the first and third groups defined above,
# put [[2,4],[],[1,3]]
numbers_to_skip = []

# Change these to show the correct event and location names as in CIMA
masterclass = "CERN-25Mar2025"
location = "SaoPaoloSprace-25mar25"

# Auxiliary integer to count every 9 groups, just to fill an A4 correctly
# and make it easier to cut the paper
aux_n = 1

# Define header for overleaf document
print("\\documentclass{{article}}".format())
print("\\usepackage{{geometry}}".format())
print("\\geometry{{a4paper, portrait, margin=1in}}".format())
print("\\usepackage{{comment}}".format())
print("\\begin{{document}}\n".format())
print("\n% Use script groups_masterclass.py\n\n")
print("\\begin{{Large}}\n".format())

# Loop over groups
for j, group in enumerate(groups):
    # Loop over start and end numbers
    for i in range(starting_numbers[j],ending_numbers[j]+1):
        # Skip numbers if needed
        if numbers_to_skip != []:
            if i in numbers_to_skip[j]: continue
        # Skip tens (10, 20, 30, ...); this is usually the standard case
        if skip_tens and i % 10 == 0: continue
        # Build the groups string, e.g., 100.1, 100.2, ...
        groupstr = str(group) + "." + str(i)
        # Write the text of the groups in the overleaf document
        print("\\noindent \\textbf{{Masterclass}}: {}\\\\".format(masterclass))
        print("\\textbf{{Location}}: {}\\\\".format(location))
        print("\\textbf{{Group}}: {}\\\\\\\\".format(groupstr))
        # 9 groups are written per page
        if aux_n % 9 == 0 and i != ending_numbers[j]:
            print("\\newpage".format())
            print("\\newpage".format())
        aux_n = aux_n + 1
    # These are here to avoid some issues with line spacing and to write 9 groups per page
    # Remove it in overleaf if needed
    print("\\newpage")
    print("\\newpage")

# Finish the overleaf document
print("\\end{{Large}}\n".format())
print("\\end{{document}}\n".format())