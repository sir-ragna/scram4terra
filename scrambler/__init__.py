
import sys
import random

# TODO: Keep case for characters
# TODO: Don't work on a sentence but word basis.

# Debug var + function
# Quickly toggle all debug output on/off
DEBUG = False

def debug(msg):
    global DEBUG
    if DEBUG:
        print(msg)

# global cramble arrays
arr1 = "b,d,g,j,k,p,q,t".split(',')
arr2 = "a,e,i,o,u".split(',')
arr3 = "c,f,s".split(',')
arr4 = "h,l,m,n,r,v,w,x,y,z".split(',')


# standard character scrambling
# Index + 1 in array
# BACH => DICR
def std_chr_scramble(input_s):
    global arr1
    global arr2
    global arr3
    global arr4

    output_s = ""
    
    for index, char in enumerate(list(input_s.lower())):
        debug("char: %s, index: %d" % (char, index))
        debug("(index + 1) %% len(arr1) => %d" % ((index + 1) % len(arr1)))
        debug("=> %s" % arr1[(index + 1) % len(arr1)])
        if char in arr1:
            
            output_s += arr1[(index + 1) % len(arr1)]
        elif char in arr2:
            output_s += arr2[(index + 1) % len(arr2)]
        elif char in arr3:
            output_s += arr3[(index + 1) % len(arr3)]
        elif char in arr4:
            output_s += arr4[(index + 1) % len(arr4)]
        else:
            # Are you working with a non-ascii char set?
            # sys.stderr.write("Error character not found.\n")    
            output_s += char
    
    debug(output_s)
    return output_s

# Minimal character scrambling
# Next char in the array
# BACH => DEFL
def min_chr_scramble(input_s):
    # Scramble arrays
    global arr1
    global arr2
    global arr3
    global arr4
    output_s = ""
    
    for index, char in enumerate(list(input_s.lower())):
        if char in arr1:
            output_s += arr1[(arr1.index(char) + 1) % len(arr1)]
        elif char in arr2:
            output_s += arr2[(arr2.index(char) + 1) % len(arr2)]
        elif char in arr3:
            output_s += arr3[(arr3.index(char) + 1) % len(arr3)]
        elif char in arr4:
            output_s += arr4[(arr4.index(char) + 1) % len(arr4)]
        else:
            # Are you working with a non-ascii char set?
            # sys.stderr.write("Error character not found.\n")    
            output_s += char
    
    debug(output_s)
    return output_s

# Advanced character scrambling
# BACH => DOSX
def adv_chr_scramble(input_s):
    global arr1
    global arr2
    global arr3
    global arr4

    output_s = ""
    
    for index, char in enumerate(list(input_s.lower())):
        if char in arr1:
            
            output_s += arr1[(index + 1) % len(arr1)]
        elif char in arr2:
            output_s += arr2[(index + 2) % len(arr2)]
        elif char in arr3:
            output_s += arr3[(index + 3) % len(arr3)]
        elif char in arr4:
            output_s += arr4[(index + 4) % len(arr4)]
        else:
            # Are you working with a non-ascii char set?
            # sys.stderr.write("Error character not found.\n")    
            output_s += char
    
    debug(output_s)
    return output_s

# LEL SCRAMBLER
# random letter of each array
def lel_chr_scramble(input_s, seed=-1):
    global arr1
    global arr2
    global arr3
    global arr4
    output_s = ""
    
    # if seed is zero or negative.
    # we'll choose a random seed.
    if seed <= 0:   
        seed = random.randint(0,1000)
        
    for index, char in enumerate(list(input_s.lower())):
        if char in arr1:            
            output_s += arr1[seed % len(arr1)]
        elif char in arr2:
            output_s += arr2[seed % len(arr2)]
        elif char in arr3:
            output_s += arr3[seed % len(arr3)]
        elif char in arr4:
            output_s += arr4[seed % len(arr4)]
        else:
            # Are you working with a non-ascii char set?
            # sys.stderr.write("Error character not found.\n")    
            output_s += char
    
    debug(output_s)
    return output_s

def test():
    # These are test statements.
    # They'll throw errors if behaviour changes are detected.
    assert(std_chr_scramble("BACH") == "dicr")
    assert(std_chr_scramble("AAAA") == "eiou")    
    assert(adv_chr_scramble("BACH") == "dosx")
    assert(adv_chr_scramble("AAAA") == "ioua")
    
def main():
    print("# Standard Scrambling")
    print("BACH => %s" % (std_chr_scramble("BACH")))
    print("AAAA => %s" % (std_chr_scramble("AAAA")))
    print("Hi, my name is Sir-Ragnarok. How are you? => %s" \
        % (std_chr_scramble("Hi, my name is Sir-Ragnarok. How are you?")))

    print("-" * 80)
    print("# Minimal Scrambling")
    print("BACH => %s" % (min_chr_scramble("BACH")))
    print("AAAA => %s" % (min_chr_scramble("AAAA")))
    print("Hi, my name is Sir-Ragnarok. How are you? => %s" \
        % (min_chr_scramble("Hi, my name is Sir-Ragnarok. How are you?")))

    print("-" * 80)
    print("# Advanced Scrambling")
    print("BACH => %s" % (adv_chr_scramble("BACH")))
    print("AAAA => %s" % (adv_chr_scramble("AAAA")))
    print("Hi, my name is Sir-Ragnarok. How are you? => %s" \
        % (adv_chr_scramble("Hi, my name is Sir-Ragnarok. How are you?")))

    print("-" * 80)
    print("# LEL Scrambling")
    print("BACH => %s" % (lel_chr_scramble("BACH")))
    print("AAAA => %s" % (lel_chr_scramble("AAAA")))
    print("[seed = 1]       Hi, my name is Sir-Ragnarok. How are you? => %s" \
        % (lel_chr_scramble("Hi, my name is Sir-Ragnarok. How are you?", 1)))
    print("[seed = 2]       Hi, my name is Sir-Ragnarok. How are you? => %s" \
        % (lel_chr_scramble("Hi, my name is Sir-Ragnarok. How are you?", 2)))
    print("[seed = 3]       Hi, my name is Sir-Ragnarok. How are you? => %s" \
        % (lel_chr_scramble("Hi, my name is Sir-Ragnarok. How are you?", 3)))
    print("[seed = 4]       Hi, my name is Sir-Ragnarok. How are you? => %s" \
        % (lel_chr_scramble("Hi, my name is Sir-Ragnarok. How are you?", 4)))
    print("[seed is random] Hi, my name is Sir-Ragnarok. How are you? => %s" \
        % (lel_chr_scramble("Hi, my name is Sir-Ragnarok. How are you?")))
    print("[seed is random] Hi, my name is Sir-Ragnarok. How are you? => %s" \
        % (lel_chr_scramble("Hi, my name is Sir-Ragnarok. How are you?")))
    
if __name__== "__main__":
    # We are getting executed directly
    # (=> this is not a module being imported.)
    main()
