
import sys
import random

# TODO: Keep case for characters

# global cramble arrays
arr1 = "b,d,g,j,k,p,q,t".split(',')
arr2 = "a,e,i,o,u".split(',')
arr3 = "c,f,s".split(',')
arr4 = "h,l,m,n,r,v,w,x,y,z".split(',')


def case_correcter(original_char):
    def set_case(c):
        if original_char.isupper():
            return c.upper()
        else:
            return c.lower()
    return set_case

# standard character scrambling
# Index + 1 in array
# BACH => DICR
def std_chr_scramble(input_s):
    global arr1
    global arr2
    global arr3
    global arr4

    output_s = ""
    
    for index, char_c in enumerate(list(input_s)):
        set_case = case_correcter(char_c)
        char = char_c.lower()
        if char in arr1:            
            output_s += set_case(arr1[(index + 1) % len(arr1)])
        elif char in arr2:
            output_s += set_case(arr2[(index + 1) % len(arr2)])
        elif char in arr3:
            output_s += set_case(arr3[(index + 1) % len(arr3)])
        elif char in arr4:
            output_s += set_case(arr4[(index + 1) % len(arr4)])
        else: 
            output_s += char
    
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
    
    for index, char_c in enumerate(list(input_s)):
        set_case = case_correcter(char_c)
        char = char_c.lower()
        if char in arr1:
            output_s += set_case(arr1[(arr1.index(char) + 1) % len(arr1)])
        elif char in arr2:
            output_s += set_case(arr2[(arr2.index(char) + 1) % len(arr2)])
        elif char in arr3:
            output_s += set_case(arr3[(arr3.index(char) + 1) % len(arr3)])
        elif char in arr4:
            output_s += set_case(arr4[(arr4.index(char) + 1) % len(arr4)])
        else: 
            output_s += char
    
    return output_s

# Advanced character scrambling
# BACH => DOSX
def adv_chr_scramble(input_s):
    global arr1
    global arr2
    global arr3
    global arr4

    output_s = ""
    
    for index, char_c in enumerate(list(input_s)):
        set_case = case_correcter(char_c)
        char = char_c.lower()
        if char in arr1:            
            output_s += set_case(arr1[(index + 1) % len(arr1)])
        elif char in arr2:
            output_s += set_case(arr2[(index + 2) % len(arr2)])
        elif char in arr3:
            output_s += set_case(arr3[(index + 3) % len(arr3)])
        elif char in arr4:
            output_s += set_case(arr4[(index + 4) % len(arr4)])
        else: 
            output_s += char
    
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
        
    for index, char_c in enumerate(list(input_s)):
        set_case = case_correcter(char_c)
        char = char_c.lower()
        if char in arr1:            
            output_s += set_case(arr1[seed % len(arr1)])
        elif char in arr2:
            output_s += set_case(arr2[seed % len(arr2)])
        elif char in arr3:
            output_s += set_case(arr3[seed % len(arr3)])
        elif char in arr4:
            output_s += set_case(arr4[seed % len(arr4)])
        else:    
            output_s += char
    
    return output_s

def test():
    # These are test statements.
    # They'll throw errors if behaviour changes are detected.
    assert(std_chr_scramble("BACH") == "DICR")
    assert(std_chr_scramble("bach") == "dicr")
    assert(std_chr_scramble("BaCh") == "DiCr")
    assert(std_chr_scramble("aaaa") == "eiou")
    assert(std_chr_scramble("AAAA") == "EIOU") 
    assert(min_chr_scramble("BACH") == "DEFL")
    assert(min_chr_scramble("bach") == "defl")
    assert(min_chr_scramble("bAcH") == "dEfL") 
    assert(adv_chr_scramble("bach") == "dosx")
    assert(adv_chr_scramble("BACH") == "DOSX")
    assert(adv_chr_scramble("aaaa") == "ioua")
    assert(adv_chr_scramble("AAAA") == "IOUA")
    assert(lel_chr_scramble("Hi, my name is Sir-Ragnarok. How are you?", 1) == "Le, ll lele ef Fel-Ledleled. Lel ele lee?",
           "LEL Scrambler seed 1 failed.")
    assert(lel_chr_scramble("Hi, my name is Sir-Ragnarok. How are you?", 2) == "Mi, mm mimi is Sim-Migmimig. Mim imi mii?",
           "LEL Scrambler seed 2 failed.")
    
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
