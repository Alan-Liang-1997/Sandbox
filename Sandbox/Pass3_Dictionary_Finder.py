with open("english_dictionary.txt", "r") as in_file, open("20As.txt","w") as out_file:
    word_count = 0
    for word in in_file:
        if word[0] == "a" and word_count < 20:
            out_file.write(word)
            word_count +=1

# For assignment, read CSV (comma separated values - a,b,c)