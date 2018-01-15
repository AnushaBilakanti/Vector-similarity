#!/usr/bin/env python
import distsim
word_to_vec_dict = distsim.load_word2vec("nyt_word2vec.4k")
###Provide your answer below

###Answer examples
#distsim.show_nearest(word_to_vec_dict, word_to_vec_dict['jack'],set(['jack']),distsim.cossim_dense)


words=["jack","london","fantastic","explained","introduced","bus"]
for word1 in words:
	print "word",word1
	for i, (word, score) in enumerate(distsim.show_nearest(word_to_vec_dict, word_to_vec_dict[word1], set([word1]), distsim.cossim_dense), start=1):
	    print("{}: {} ({})".format(i, word, score))


