import math
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.collocations import *
from nltk import bigrams
from nltk import ngrams
import nltk

from nltk.corpus import reuters
from nltk import bigrams, trigrams
from collections import Counter, defaultdict
		
sent_text = "Zipf's law is an empirical law formulated using mathematical statistics. The law is named after the linguist George Kingsley Zipf, who first proposed it.Zipf's law states that given a large sample of words used, the frequency of any word is inversely proportional to its rank in the frequency table. So word number n has a frequency proportional to 1/n.Thus the most frequent word will occur about twice as often as the second most frequent word, three times as often as the third most frequent word, etc. For example, in one sample of words in the English language, the most frequently occurring word, the, accounts for nearly 7% of all the words (69,971 out of slightly over 1 million). True to Zipf's Law, the second-place word of accounts for slightly over 3.5% of words (36,411 occurrences), followed by and (28,852). Only about 135 words are needed to account for half the sample of words in a large sample.[3] The same relationship occurs in many other rankings, unrelated to language, such as the population ranks of cities in various countries, corporation sizes, income rankings, etc. The appearance of the distribution in rankings of cities by population was first noticed by Felix Auerbach in 1913.[4]. It is not known why Zipf's law holds for most languages."

test_text = "This might be related to Zipf's law. But it is not formulated using mathematical statistics.It is something else.This is me. So word here used are mine and proportional to my brain logic used to mess around with the corpus which is running since 1997 with a 3.5% hit rate."

'''
test_text="Greece and India. The word 'atom' was coined by ancient Greek philosophers. However, these ideas were founded in philosophical and theological reasoning rather than evidence and experimentation. As a result, their views on what atoms look like and how they behave were incorrect. They also could not convince everybody, so atomism was but one of a number of competing theories on the nature of matter. It was not until the 19th century that the idea was embraced and refined by scientists, when the blossoming science of chemistry produced discoveries that only the concept of atoms could explain.In the early 1800s, John Dalton used the concept of atoms to explain why elements always react in ratios of small whole numbers (the law of multiple proportions). For instance, there are two types of tin oxide: one is 88.1% tin and 11.9% oxygen and the other is 78.7% tin and 21.3% oxygen (tin(II) oxide and tin dioxide respectively). This means that 100g of tin will combine either with 13.5g or 27g of oxygen. 13.5 and 27 form a ratio of 1:2, a ratio of small whole numbers. This common pattern in chemistry suggested to Dalton that elements react in whole number multiples of discrete units—in other words, atoms. In the case of tin oxides, one tin atom will combine with either one or two oxygen atoms.Dalton also believed atomic theory could explain why water absorbs different gases in different proportions. For example, he found that water absorbs carbon dioxide far better than it absorbs nitrogen. Dalton hypothesized this was due to the differences in mass and complexity of the gases' respective particles. Indeed, carbon dioxide molecules (CO) are heavier and larger than nitrogen molecules (N).In 1827, botanist Robert Brown used a microscope to look at dust grains floating in water and discovered that they moved about erratically, a phenomenon that became known as 'Brownian motion'. This was thought to be caused by water molecules knocking the grains about. In 1905 Albert Einstein proved the reality of these molecules and their motions by producing the first Statistical physics analysis of Brownian motion. French physicist Jean Perrin used Einstein's work to experimentally determine the mass and dimensions of atoms, thereby conclusively verifying Dalton's atomic theory.The physicist J. J. Thomson measured the mass of cathode rays, showing they were made of particles, but were around 1800 times lighter than the lightest atom, hydrogen. Therefore, they were not atoms, but a new particle, the first 'subatomic' particle to be discovered, which he originally called 'corpuscle' but was later named 'electron', after particles postulated by George Johnstone Stoney in 1874. He also showed they were identical to particles given off by photoelectric and radioactive materials. It was quickly recognized that they are the particles that carry electric currents in metal wires, and carry the negative electric charge within atoms. Thomson was given the 1906 Nobel Prize in Physics for this work. Thus he overturned the belief that atoms are the indivisible, ultimate particles of matter. Thomson also incorrectly postulated that the low mass, negatively charged electrons were distributed throughout the atom in a uniform sea of positive charge. This became known as the plum pudding model."
'''

test="Zipf's law is an empirical law formulated using mathematical statistics."



###################################################################################################

file=open("training_1.txt","r")
print("\n\n#################### TRAINING ######################")
print("\nTokenizing ...")
word_tokenized_string = word_tokenize(file.read())

print("\nCalculating Bigrams...")
bigram_list = ngrams(word_tokenized_string, 2)
model1 = defaultdict(lambda: defaultdict(lambda: 0))
total_count=0 

print("\nModelling Bigrams..")
for w1, w2 in bigram_list:
	model1[w1][w2] += 1



print("\nCalculating Unigrams...")
unigram_list=ngrams(word_tokenized_string,1)
total_count=0
model2=defaultdict(lambda: 0)
	
print("\nModelling Unigrams...")

least_prob=0
k=0	
for w1 in unigram_list:
	model2[w1]+=1

for w1 in model2:
	total_count+=model2[w1]
	
for w1 in model2:
	model2[w1]/=total_count
	if(k==0 and model2[w1]!=0):
		least_prob=model2[w1]
		k=1
	elif(least_prob>model2[w1] and model2[w1]!=0):
		least_prob=model2[w1]

	
print("\nCalculating Trigrams...")
trigram_list = ngrams(word_tokenized_string, 3)

model = defaultdict(lambda: defaultdict(lambda: 0))
 
print("\nModelling Trigrams...")
for w1, w2, w3 in trigram_list:
	model[(w1, w2)][w3] += 1

for w1_w2 in model:    
	total_count = float(sum(model[w1_w2].values()))
	for w3 in model[w1_w2]:
		model[w1_w2][w3] /= total_count



###################################################################################################




model_interpolation = defaultdict(lambda: defaultdict(lambda: 0))
lambda_1 = 1/3
lambda_2 = 1/3
lambda_3 = 1/3

f1 = open("inteprolation_model.txt","w")

for w1_w2 in model:    
	for w3 in model[w1_w2]:
		model_interpolation[w1_w2][w3] = (lambda_1 * model[w1_w2][w3]) + (lambda_2 * model1[w2][w3]) + (lambda_3 * model2[w3])	
		if(model_interpolation[w1_w2][w3] == 0):
			counter = counter+1
		
#		print(model_interpolation[w1_w2][w3])
#		print(model[w1_w2][w3])
#		print(model1[w2][w3])
#		print(model2[w3])



###################################################################################################

print("\n\n#################### TESTING ######################")

print("\nLeast Probability:"+str(least_prob))

file1=open("testing_1.txt","r")
print("\nTokenizing ...")
word_tokenized_string = word_tokenize(file1.read())

print("\nCalculating Trigrams...")
trigram_list = ngrams(word_tokenized_string, 3)

dict1 = {}
N = 0

count_UNK=0
count_bigram=0
count_unigram=0
count_trigram=0
print("\nModelling Trigrams...")
for w1,w2,w3 in trigram_list:
	N=N+1
	if(model[(w1,w2)][w3]!=0):
		count_trigram=count_trigram+1
		dict1[(w1,w2,w3)]=model_interpolation[(w1,w2)][w3]
	else:
		count_UNK = count_UNK + 1
		dict1[(w1,w2,w3)]=least_prob


print(count_UNK)


