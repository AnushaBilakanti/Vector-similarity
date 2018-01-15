#!/usr/bin/env python
import distsim

# you may have to replace this line if it is too slow 
word_to_ccdict = distsim.load_contexts("nytcounts.4k")


### provide your answer below

###Answer examples

words=["jack","london","fantastic","explained","introduced","bus"]
for word1 in words:
	print "word:",word1
	for i, (word, score) in enumerate(distsim.show_nearest(word_to_ccdict, word_to_ccdict[word1], set([word1]), distsim.cossim_sparse), start=1):
	    # if i<=10:
	    	print("{}: {} ({})".format(i, word, score))

