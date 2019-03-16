from nltk.tokenize import sent_tokenize,word_tokenize
import nltk

files = ["xad"]
for f in files:
	print("\n\n*********************************************************************************")
	print("Using Corpus:",f)	
	file = open(f, "r")
	
	file_name = "sentence_segmentation_nltk_main"
#	file_name = file_name + f
	file_name = file_name + ".txt"
	print("Writing to file...")
	f1 = open(file_name, "a")

	print("Performing Sentence Segmentation...")
	for i in sent_tokenize(file.read()):
		f1.write(i)
		f1.write('\n')
