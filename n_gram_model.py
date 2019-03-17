from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.collocations import *
from nltk import bigrams
from nltk import ngrams
import nltk
#import matplotlib.pyplot as plt

sent_text = "Zipf's law is an empirical law formulated using mathematical statistics. The law is named after the linguist George Kingsley Zipf, who first proposed it.Zipf's law states that given a large sample of words used, the frequency of any word is inversely proportional to its rank in the frequency table. So word number n has a frequency proportional to 1/n.Thus the most frequent word will occur about twice as often as the second most frequent word, three times as often as the third most frequent word, etc. For example, in one sample of words in the English language, the most frequently occurring word, the, accounts for nearly 7% of all the words (69,971 out of slightly over 1 million). True to Zipf's Law, the second-place word of accounts for slightly over 3.5% of words (36,411 occurrences), followed by and (28,852). Only about 135 words are needed to account for half the sample of words in a large sample.[3] The same relationship occurs in many other rankings, unrelated to language, such as the population ranks of cities in various countries, corporation sizes, income rankings, etc. The appearance of the distribution in rankings of cities by population was first noticed by Felix Auerbach in 1913.[4]. It is not known why Zipf's law holds for most languages."
word_tokenized_string = word_tokenize(sent_text)

print("\n\nUnigram")
unigram_list = ngrams(word_tokenized_string,1)
fdist_unigram = nltk.FreqDist(unigram_list)
#for k,v in fdist_unigram.items():
#    print (k,v)


print("\n\nBigram")
bigram_list =nltk.bigrams(word_tokenized_string)
#print(list(bigram_list))
fdist_bigram = nltk.FreqDist(bigram_list)
#for k,v in fdist.items():
#    print (k,v)

print("\n\nTrigram")
trigram_list = ngrams(word_tokenized_string, 3)
fdist_trigram = nltk.FreqDist(trigram_list)
#for k,v in fdist.items():
#    print (k,v)

