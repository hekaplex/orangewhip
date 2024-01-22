# logic
def orange_whip(guess, dudlist):    
# dependencies
    import copy
    import collections
    from english_words import english_words_lower_alpha_set
# figure out which letters to test
    alpha = {a for a in "abcdefghijklmnopqrstuvwxyz"}
    duds = {a for a in dudlist}
    choices = "".join(list(alpha - duds))
    numch = len(list(choices))
    wordslop = []
# figure out how many substitutions of "*"
    repl = collections.Counter(guess)['*']
# generate guess letter combinations
    for blank in range(0,repl):
        for ltr1 in choices:
            if blank == 0:
                wordslop.append(guess.replace("*",ltr1,1))
            else:
                newslop = [w.replace("*",ltr1,1) if "*" in w  else w for w in wordslop]
                wordslop += newslop  
# check guess against known words        
        wordset = list(set(wordslop) & english_words_lower_alpha_set)
    return wordset
# main loop    
g = input("guess:")
d = input("duds:")   
print(orange_whip(g, d))
