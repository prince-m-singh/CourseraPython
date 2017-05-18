def stringcount(word,letter):
    count = 0
    for ch in word:
        if ch == letter:
            count = count + 1
    print count
stringcount("banana","a")
