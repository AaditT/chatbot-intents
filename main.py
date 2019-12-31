import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
stop_words = set(stopwords.words('english'))

from nltk.corpus import wordnet

def gen_syn(wd):
    synonyms = []
    antonyms = []
    for syn in wordnet.synsets(wd):
        for l in syn.lemmas():
            synonyms.append(l.name())
            if l.antonyms():
                antonyms.append(l.antonyms()[0].name())
    return (set(synonyms))


def gen_phrases(txt):
    tokenized = sent_tokenize(txt)
    for i in tokenized:
        wordsList = nltk.word_tokenize(i)
        wordsList = [w for w in wordsList if not w in stop_words]
        tagged = nltk.pos_tag(wordsList)
        print(tagged)
        for word in tagged:
            if word[1] == "NN":
                for syn in gen_syn(word[0]):
                    print(txt.replace(str(word[0]),str(syn)))
