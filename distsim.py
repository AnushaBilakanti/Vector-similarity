from __future__ import division
import sys,json,math
import os
import numpy as np
import math

def load_word2vec(filename):
    # Returns a dict containing a {word: numpy array for a dense word vector} mapping.
    # It loads everything into memory.
    
    w2vec={}
    with open(filename,"r") as f_in:
        for line in f_in:
            line_split=line.replace("\n","").split()
            w=line_split[0]
            vec=np.array([float(x) for x in line_split[1:]])
            w2vec[w]=vec
    return w2vec

def load_contexts(filename):
    # Returns a dict containing a {word: contextcount} mapping.
    # It loads everything into memory.

    data = {}
    for word,ccdict in stream_contexts(filename):
        data[word] = ccdict
        # print "ccdict",ccdict
    print "file %s has contexts for %s words" % (filename, len(data))
    return data

def stream_contexts(filename):
    # Streams through (word, countextcount) pairs.
    # Does NOT load everything at once.
    # This is a Python generator, not a normal function.
    for line in open(filename):
        word, n, ccdict = line.split("\t")
        n = int(n)
        ccdict = json.loads(ccdict)
        yield word, ccdict

def cossim_sparse(v1,v2):
    # Take two context-count dictionaries as input
    # and return the cosine similarity between the two vectors.
    # Should return a number beween 0 and 1
    dot_product=0
    for k1 in v1:
        if k1 in v2:
            dot_product=dot_product+v1[k1]*v2[k1]

    n_v1=0
    for k1 in v1:
        if k1 in v1:
            n_v1=n_v1+math.pow(v1[k1],2)

    n_v1=math.sqrt(n_v1)

    n_v2=0
    for k1 in v2:
        if k1 in v2:
                n_v2=n_v2+math.pow(v2[k1],2)
    n_v2=math.sqrt(n_v2)

    res=0
    res=dot_product/(n_v1*n_v2)
    return res


    ## TODO: delete this line and implement me

    pass

def cossim_dense(v1,v2):
    # v1 and v2 are numpy arrays
    # Compute the cosine simlarity between them.
    # Should return a number between -1 and 1
    dot_product=0
    for val1,val2 in zip(v1,v2):
        dot_product=dot_product+val1*val2

    n_v1=0
    for val1 in v1:
        n_v1=n_v1+math.pow(val1,2)
    n_v1=math.sqrt(n_v1)
    
    n_v2=0
    for val2 in v2:
        n_v2=n_v2+math.pow(val2,2)
    n_v2=math.sqrt(n_v2)

    res=0
    res=dot_product/(n_v1*n_v2)
    return res
    pass

def show_nearest(word_2_vec, w_vec, exclude_w, sim_metric):
    #word_2_vec: a dictionary of word-context vectors. The vector could be a sparse (dictionary) or dense (numpy array).
    #w_vec: the context vector of a particular query word `w`. It could be a sparse vector (dictionary) or dense vector (numpy array).
    #exclude_w: the words you want to exclude in the responses. It is a set in python.
    #sim_metric: the similarity metric you want to use. It is a python function
    # which takes two word vectors as arguments.

    # return: an iterable (e.g. a list) of up to 10 tuples of the form (word, score) where the nth tuple indicates the nth most similar word to the input word and the similarity score of that word and the input word
    # if fewer than 10 words are available the function should return a shorter iterable
    #
    # example:
    #[(cat, 0.827517295965), (university, -0.190753135501)]
    
    ## TODO: delete this line and implement me
    result=[]
    templist=[]

    # "hello"
    #print word_2_vec
    for k1 in word_2_vec:
        if k1 not in exclude_w:
            similarity=sim_metric(word_2_vec[k1],w_vec)  
            #print "similarity",k1,similarity 
            templist.append((k1,similarity))

    
    count=0
    
    #return the sorted list in descending order
    #return sorted(templist,key=lambda x: -x[1])
    result=sorted(templist,key=lambda x: -x[1])
    return result[0:10]
    
    pass
