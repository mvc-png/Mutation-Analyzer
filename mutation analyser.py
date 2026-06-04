

import matplotlib.pyplot as plt
import numpy as np

wild_type = "MGHFTEEDKATITSLWGKVNVEDAGGETLGRLLVVYPWTQRFFDSFGNLSSASAIMGNPKVKAHGKKVLTSLGDAIKHLDDLKGTFAQLSELHCDKLHVDPENFKLLGNVLVTVLAIHFGKEFTPEVQASWQKMVTGVASALSSRYH"
mutant = "MGHFTEEDKATITSLWGKVNVEDAGGETLGRLLVVYPWTQRFFDSFGNLSSASAIMGNPKVKAHGKKVLTSLGDATKHLDDLKGTFAQLSELHCDKLHVDPENFKLLGNVLVTVLAIHFGKEFTPEVQASWQKMVTAVASALSSRYH"

hydrophobic = ["A", "V", "I", "L", "M", "F", "W", "Y"]
polar = ["S", "T", "N", "Q"]
positive = ["K", "R", "H"]
negative = ["D", "E"] 

total_mutations = 0
conservative_count = 0
non_conservative_count = 0
severe_count = 0


mutation_data = []  
print("Mutations observed at positions:")
def classify_mutation(original, mutant):

    if original in hydrophobic and mutant in hydrophobic:
        return "Conservative", 1

    elif original in polar and mutant in polar:
        return "Conservative", 1

    elif original in positive and mutant in positive:
        return "Conservative", 1

    elif original in negative and mutant in negative:
        return "Conservative", 1
    
    elif original in negative and mutant in positive:
        return "Charge Reversal", 2
    
    elif original in positive and mutant in negative:
        return "Charge Reversal", 2

    elif mutant == "P":
        return "Possible helix disruption", 3
    

    else:
        return "Non-conservative", 2


for i in range(len(wild_type)):

    if wild_type[i] != mutant[i]:

        total_mutations += 1

        original = wild_type[i]
        changed = mutant[i]

        mutation_type, score = classify_mutation(original, changed)

        if mutation_type == "Conservative":
            conservative_count += 1

        elif mutation_type == "Non-conservative":
            non_conservative_count += 1

        elif mutation_type == "Possible helix disruption":
            severe_count += 1
        print("Position", i + 1, ":", original, "->", changed, "|", mutation_type, "| Severity Score:", score)
print("total mutations" , total_mutations)


labels = ["Helix", "Sheet", "Turn"]
wild = [57.5, 35.8, 6.7]
mutant = [45.2, 42.1, 12.7]

x = np.arange(len(labels))
width = 0.25

plt.bar(x - width/2, wild, width, label = "Wild Type" ,  color = "darkred")
plt.bar(x + width/2, mutant, width, label = "Mutant", color = "darkblue")
plt.xticks(x, labels, fontsize = 12 )
plt.ylabel("Percentage", fontsize = 12)
plt.title("Protein 2° Structure Comparison")
plt.legend()
plt.show()