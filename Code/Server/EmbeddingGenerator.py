from gensim.parsing.preprocessing import remove_stopwords
from nltk.stem import WordNetLemmatizer
from gensim.models import KeyedVectors
import numpy as np
import string

# Use word embeddings by Google, directly from the file
embeddings = KeyedVectors.load_word2vec_format('../Data/GoogleNews-vectors-negative300.bin', binary=True)

# To Get Processed data tokens from the text file
def preprocessFile(filename):
    f = open(filename,'r')
    wordlist = []
    wnl = WordNetLemmatizer()
    for line in f:
        #Step 1: Removing Punctuations
        line="".join([i for i in line if i not in string.punctuation])
        #Step 2: Converting to lower case
        line = line.lower()
        #Step 3: Removing stopwords from the text
        line = remove_stopwords(line)
        #Step 4: Tokenization
        line = line.split()
        #Step 5: Lemmetization (Preffered over Stemming)
        for word in line:
            wordlist.append(wnl.lemmatize(word))
    return wordlist

# To get a single Video embeddings from the transcript            
def getEmbedding(filename,embeddings):
    wordlist = preprocessFile(filename)
    embedding = np.zeros((300,))
    count = 0
    for word in wordlist:
        try:
            embedding += embeddings[word]
        except:
            count += 1
    embedding /= (len(wordlist)-count)
    return embedding

file = "../Data/sampledata.txt"
vec = getEmbedding(filename=file,embeddings=embeddings)
most_similar = embeddings.most_similar(positive=[vec],topn=3)
print(most_similar)


