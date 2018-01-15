#!/usr/bin/env python
import distsim
import numpy as np
from collections import defaultdict
import time

start_time=time.time()

#word_to_vec_dict = distsim.load_word2vec("nyt_word2vec.4k")
word_to_vec_dict = distsim.load_word2vec("glove.6B.50d.txt")

relations=open("word-test.v3.txt","r")

relation_dict=defaultdict(list)
relation_count={}

for relation in relations:
	if relation.startswith("//"):
		continue
	elif relation.startswith(":"):
		temp=relation.split(" ")
		#print temp
		key=temp[1].strip()
		relation_dict[key]=[]
		# if count!=0:
		# 	relation_count[key]=count
	else:
		relation_dict[key].append(relation)

# for val in relation_dict:
# 	#print val
# 	if val=="currency":
# 		print val,relation_dict[val]
# 		break
result_dict=defaultdict(list)
nonmatch_list=defaultdict(list)
for val in relation_dict:
	temp=relation_dict[val]
	best_1=0
	best_5=0
	best_10=0
	#print "val",val
	num_snt=0 #counting number of sentences
	for i in temp:
		num_snt+=1
		#print "i",i
		words=i.split(" ")
		word1 = word_to_vec_dict[words[0].strip()]
		word2 = word_to_vec_dict[words[1].strip()]
		word3 = words[2].strip()
		word4 = word_to_vec_dict[words[3].strip()]
		new_word=word1-word2+word4
		# print "words[0]",words[0]
		# print "words[0]",words[1]
		# print "words[0]",words[3]
		#for i, (word, score) in enumerate(distsim.show_nearest(word_to_vec_dict,new_word,set([words[0].strip(),words[1].strip(),words[3].strip()]),distsim.cossim_dense), start=1):
		ret = distsim.show_nearest(word_to_vec_dict,new_word,set([words[0].strip(),words[1].strip(),words[3].strip()]),distsim.cossim_dense)
		counter=0
		#print ret[counter][0]
		while counter<=9:
			if counter==0 and ret[counter][0]==word3:
				#print "ji",ret[counter][0]
				best_1+=1
				best_5+=1
				best_10+=1
				break
			elif counter>0 and counter<=4 and ret[counter][0]==word3:
				best_5+=1
				best_10+=1
				break
			elif counter>4 and counter<=9 and ret[counter][0]==word3:
				best_10+=1
				break
			else:
				if val not in nonmatch_list:
					nonmatch_list[val].append(ret[counter][0])
					nonmatch_list[val].append(word3)
					nonmatch_list[val].append(words[0].strip())
					nonmatch_list[val].append(words[1].strip())
					nonmatch_list[val].append(words[3].strip())

			counter+=1
	# print "best_1",best_1	
	# print "best_5",best_5	
	# print "best_10",best_10	
	best_1=float(best_1)/float(num_snt)
	best_5=float(best_5)/float(num_snt)
	best_10=float(best_10)/float(num_snt)
	result_dict[val].append([round(best_1,2),round(best_5,2),round(best_10,2)])

print "CATEGORY\t1-BEST\t5-BEST\t10-BEST"
for key in result_dict:
	best=result_dict[key]
	for item in best:
		print key+"\t"+str(item[0])+"\t"+str(item[1])+"\t"+str(item[2])

# for key in nonmatch_list:
# 	print key,nonmatch_list[key]

print "CATEGORY\t\tIncorrectly predicted\t\tCorrect Answer"
for key in nonmatch_list:
		print key+"\t\t"+str(nonmatch_list[key][0])+"\t\t"+str(nonmatch_list[key][1])


new_time=time.time()-start_time
print "new_time",new_time
#print result_dict