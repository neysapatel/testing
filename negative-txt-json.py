import json

filename = "negative-words.txt"

lstofwords = []
 

with open(filename) as fh:
    for line in fh:
        word = line.strip().split(None)
        
        lstofwords.append(word)

out_file = open("negative-words.json", "w")
json.dump(lstofwords, out_file, sort_keys=False)
out_file.close
