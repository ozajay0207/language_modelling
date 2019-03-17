from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.collocations import *
from nltk import bigrams
from nltk import ngrams
import nltk
import matplotlib.pyplot as plt


#word_text = "hello there how are you doing how are you"
sent_text = "Hello Mr. Arun today we are gonna do some heavy lifting. Are you up for it?"
#word_text = "Zipf's law is an empirical law formulated using mathematical statistics. The law is named after the linguist George Kingsley Zipf, who first proposed it.Zipf's law states that given a large sample of words used, the frequency of any word is inversely proportional to its rank in the frequency table. So word number n has a frequency proportional to 1/n.Thus the most frequent word will occur about twice as often as the second most frequent word, three times as often as the third most frequent word, etc. For example, in one sample of words in the English language, the most frequently occurring word, the, accounts for nearly 7% of all the words (69,971 out of slightly over 1 million). True to Zipf's Law, the second-place word of accounts for slightly over 3.5% of words (36,411 occurrences), followed by and (28,852). Only about 135 words are needed to account for half the sample of words in a large sample.[3] The same relationship occurs in many other rankings, unrelated to language, such as the population ranks of cities in various countries, corporation sizes, income rankings, etc. The appearance of the distribution in rankings of cities by population was first noticed by Felix Auerbach in 1913.[4]. It is not known why Zipf's law holds for most languages"


file = open("xaa", "r")

#word_tokenized_string = word_tokenize(word_text)
word_tokenized_string = word_tokenize(file.read())


########################################################################################
#Printing uni Grams in corpus
unigram_string = ngrams(word_tokenized_string, 1)

print("Unigram_string:\n")

freq_distribution = nltk.FreqDist(unigram_string)


#print(freq_distribution.values())
#freq_distribution = nltk.FreqDist(freq_distribution.most_common(5))



#for k,v in sorted(freq_distribution.items(),key=freq_distribution.values() ):
#    print(k,v)

#freq_distribution.plot();
x = []
y = []

count=1
for k in freq_distribution.most_common(500):
    #x.append(count)
    #y.append(k[1])
    #count=count+1
    x.append(k[0][0])
    y.append(k[1])


plt.plot(x, y)
plt.title("Unigram distribution")
plt.show()
print("\n")




'''
#########################################################################################
#Printing Bigrams in corpus

bigram_string = ngrams(word_tokenized_string, 2)

print("Bigram_string:\n")


fdist = nltk.FreqDist(bigram_string)
x = []
y = []

#print(fdist.most_common(3))
for k in fdist.most_common(10):
#    x.append(k[0])
#    y.append(k[1])
    x.append(k[0][0] + " " +k[0][1])
    y.append(k[1])

plt.plot(x, y)
plt.show()
#for k,v in fdist.items():
#    print (k,v)

##########################################################################################
'''

'''
#Priting Trigrams in corpus
trigram_string = ngrams(word_tokenized_string, 3)

print("Trigram_string:\n")

freq_distribution = nltk.FreqDist(trigram_string)
for k,v in freq_distribution.items():
    print (k, v)


##########################################################################################
#plt.show()




# Code to open corpus file, read it, tokenize it on basis of word and dump it in other file

#file = open("xaa", "r")
#file_1 = open("word_tokenized.txt", "w")

for i in word_tokenize(file.read()):
    print(file_1.write("'"))
    print(file_1.write(i))
    print(file_1.write("' "))

'''
