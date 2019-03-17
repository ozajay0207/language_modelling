from nltk.tokenize import sent_tokenize,word_tokenize
import nltk
import random

#RANDOMLY SHUFFLE
def shuffle_random(segmented_sentences =[]):
	print(len(segmented_sentences))
	random.shuffle(segmented_sentences)	
	print(len(segmented_sentences))
	random_sentences_filename = "randomly_shuffled_sentences.txt"
	f1 = open(random_sentences_filename, "w")
	print("writing randomly shuffled sentences to file : ",random_sentences_filename)
#	print(segmented_sentences)
	for i in segmented_sentences:
		i=i.strip()
		if i!="" or i!="\n" or i!=" ":
			f1.write(i)
			f1.write("\n")
		
	#counter=0
	#f1.write("\n".join(segmented_sentences))
	#print(counter)

files = ["training_sentences.txt"]
for f in files:
	print("\n\n*********************************************************************************")
	print("Using Corpus:",f)	
	file = open(f, "r")
	segmented_sentences = []

	print("Performing Sentence Segmentation...")
	for i in sent_tokenize(file.read()):
		segmented_sentences.append(i)
	print(len(segmented_sentences))
	
	shuffle_random(segmented_sentences)
	
	

#SPLIT INTO TRAIN AND TEST
file = open("randomly_shuffled_sentences.txt","r")
input_sentences = file.readlines()
#input_sentences =  ' '.join(input_sentences).split()
print(len(input_sentences))
	
train_filename = "training_5.txt"
test_filename = "testing_5.txt"

train_sentences = input_sentences[:(int)(0.9*len(input_sentences))]
test_sentences = input_sentences[(int)(0.9*len(input_sentences)):]
print(len(train_sentences))
print(len(test_sentences))

f1=open(train_filename,"w")
for i in train_sentences:
	i=i.strip()
	f1.write(i)
	f1.write("\n")
	
f1=open(test_filename,"w")
for i in test_sentences:
	i=i.strip()
	f1.write(i)
	f1.write("\n")



