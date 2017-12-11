 
## Scrambler for Terrachron ##

### Files ###

- scrambler - DIRECTORY
    * `__init__.py` - FILE that contains the scrable functions.
- scramble-these-files.py - FILE that imports the scrambler module
  and uses the functions contained therein.
- hackers.txt - FILE testing material

### Functions of the scrambler module ###

Before you can use the functions, you'll need to import the module.

    import scrambler

It might be worth executing the test function.

    scrambler.test()

This will throw errors if the functions are broken.

The following functions are available.

- std_chr_scramble() 
- min_chr_scramble() 
- adv_chr_scramble() 
- lel_chr_scramble()
- main() - prints some sample text
- test() - will run tests

## Example ##

```shell
[robbe@teslacoil scram4terra]$ python scramble-these-files.py 
# Standard Scrambling
BACH => DICR
AAAA => EIOU
Hi, my name is Sir-Ragnarok. How are you? => Li, vw yuhe os Fiy-Heqnuvej. Hem uve yua?
--------------------------------------------------------------------------------
# Minimal Scrambling
BACH => DEFL
AAAA => EEEE
Hi, my name is Sir-Ragnarok. How are you? => Lo, nz reni oc Cov-Vejrevup. Lux evi zua?
--------------------------------------------------------------------------------
# Advanced Scrambling
BACH => DOSX
AAAA => IOUA
Hi, my name is Sir-Ragnarok. How are you? => Ro, yz lani uf Col-Niqwayij. Niv ayi lae?
--------------------------------------------------------------------------------
# LEL Scrambling
BACH => QUFR
AAAA => OOOO
[seed = 1]       Hi, my name is Sir-Ragnarok. How are you? => Le, ll lele ef Fel-Ledleled. Lel ele lee?
[seed = 2]       Hi, my name is Sir-Ragnarok. How are you? => Mi, mm mimi is Sim-Migmimig. Mim imi mii?
[seed = 3]       Hi, my name is Sir-Ragnarok. How are you? => No, nn nono oc Con-Nojnonoj. Non ono noo?
[seed = 4]       Hi, my name is Sir-Ragnarok. How are you? => Ru, rr ruru uf Fur-Rukruruk. Rur uru ruu?
[seed is random] Hi, my name is Sir-Ragnarok. How are you? => Ha, hh haha af Fah-Habhahab. Hah aha haa?
[seed is random] Hi, my name is Sir-Ragnarok. How are you? => Mi, mm mimi if Fim-Mikmimik. Mim imi mii?
```
