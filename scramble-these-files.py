import scrambler
import re

# Available functions
# - std_chr_scramble() 
# - min_chr_scramble() 
# - adv_chr_scramble() 
# - lel_chr_scramble()
# - main() - prints some sample text
# - test() - will run tests


scrambler.test() # will throw errors if something changes.
scrambler.main() # print a few test cases.

def scramble_file(file_name, scram_fn):   
    output_s = ""
    with open(file_name) as fh:
        lines = fh.readlines()
        output_s = ""
        for line in lines:
            out_line = ""
            tokens = re.findall("[\w]+|[\W]+", line)
            for token in tokens:
                out_line += scram_fn(token)
            output_s += out_line
            
    return output_s

output_s = scramble_file("hackers.txt", scrambler.std_chr_scramble)

with open("hackers_std_scram.txt", 'w') as fh:
    fh.write(output_s)
    
    
