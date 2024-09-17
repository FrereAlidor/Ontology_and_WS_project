from nltk.stem.porter import *
from nltk.corpus import stopwords
from os import listdir
from os import path
from os import remove
from os import makedirs
from tinydb import TinyDB,Query
from collections import Counter
from collections import defaultdict


Words = defaultdict(list)
word_rating = defaultdict(list)
word_Count = defaultdict(list)
words_documents = defaultdict(list)
def getAllFiles(top_directory):
    files = []
    for directory in listdir(top_directory):
        if path.isfile(str(top_directory + directory)):
            files.append(str(top_directory + directory))
        else:
            files = files + (getAllFiles(str(top_directory + directory + "/")))
    return files

def removePunc(text):
    from string import punctuation
    new_body = ""
    punc = set(punctuation)
    punc.remove('/')

    for i in range(len(text)):
        if (text[i] in punc ):
            continue
        else:
            new_body += text[i]
    return new_body


def stemWords(words):

    stemed_words = []
    stemmer = PorterStemmer()
    for word in words:
        stemed_words.append(stemmer.stem(word))
    return stemed_words


def removeStopWords(text):
    words=[]
    new_words = []
    stopwrds = stopwords.words('english')
    for line in text.split('\n'):
        for word in line.split():
            words.append(word)
    for word in words:
        if word.lower() not in stopwrds:
            new_words.append(word.lower())
    return new_words

def Clean(text):
    text = removePunc(text)
    words = removeStopWords(text)
    words = stemWords(words)
    return words

def InvertedIndex(source_top_directory, dest_top_directory):
    files = getAllFiles(source_top_directory)


    try:
        makedirs(dest_top_directory)
        print("Output top directory check: Created")
    except:
        print("Output top directory check: Exists")
    i=0
    for file in files:
        counter = Counter()
        word_rate={}
        words=[]
        with open(file) as f:
            title = text=f.readline()
            text=f.read()

        Clean_Words = Clean(text)

        for word in Clean_Words:
            rating = Clean_Words.index(word)
            if word in title:
                rating-=10
            counter.update({word})
            if word not in word_rate:
                word_rate[word]=rating

        for word in counter:
            Words[word].append((file,counter[word],word_rate[word]))

        output_file_path = dest_top_directory + str(i)
        print("Parsing Complete")
        print(file, "parsed to output file: ", output_file_path, "\n\n")
        of = open(output_file_path, 'w')
        for word in words:
            try:
                of.write(str(word) + " ")
            except:
                continue
        of.close()
        i+=1

def CreateDatabase():
    InvertedIndex('./Documents/','./Preprocessed/')
    db = TinyDB('db.json')
    db.purge()
    qr = Query()
    for word in Words:
        documents=[]
        count=[]
        rating=[]
        for list in Words[word]:
            documents.append(list[0])
            count.append(list[1])
            rating.append(list[2])
        print("Inserting Word:"+word+" For Documents: "+ str(documents)+" Count: "+str(count)+" Place: "+str(rating))
        db.insert({'Word': word, 'Documents': documents,'Count':count,'Place':rating})

