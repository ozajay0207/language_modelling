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

file=open("sample_text.txt","r")
word_tokenized_string = word_tokenize(sent_text)


#print("\n\nTrigram")
trigram_list = ngrams(word_tokenized_string, 3)

model = defaultdict(lambda: defaultdict(lambda: 0))
 
for w1, w2, w3 in trigram_list:

	model[(w1, w2)][w3] += 1

for i in model:
	print(i)
	print(model[i].keys())
	print(sum(model[i].values()))
for w1_w2 in model:    
	total_count = float(sum(model[w1_w2].values()))
	for w3 in model[w1_w2]:
		model[w1_w2][w3] /= total_count

for w1_w2 in model:    
	for w3 in model[w1_w2]:
		print(model[w1_w2][w3])


for i in model:
	for j in model[i]:
		print("("+i[0]+","+i[1]+") : "+j+" : "+ str(model[i][j]))


###################################################################################################


word_tokenized_string = word_tokenize(test_text)

#print("\n\nTrigram")
trigram_list = ngrams(word_tokenized_string, 3)

dict1 = {}
N = 0

for w1,w2,w3 in trigram_list:
	N=N+1
	if(model[(w1,w2)][w3]!=0):
		#print(w1+","+w2)
		#print(model[(w1,w2)][w3])
		dict1[(w1,w2,w3)]=model[(w1,w2)][w3]

print(dict1)

prob_final=0.0
for i in dict1.values():
	prob_final = prob_final + (1/i)

print(prob_final+45)
print((prob_final+45)**(1/N))
	
