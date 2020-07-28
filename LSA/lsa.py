import pandas as pd
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.utils.extmath import randomized_svd
import umap
from sklearn.cluster import KMeans

datafile = 'lsa.csv'
document = pd.read_csv(datafile, header=None)

news_df = pd.DataFrame(document)
del news_df[0]

# removing everything except alphabets`
news_df['clean_doc'] = news_df[1].str.replace("[^a-zA-Z#]", " ")
# removing null fields
news_df = news_df[news_df['clean_doc'].notnull()]
# removing short words
news_df['clean_doc'] = news_df['clean_doc'].apply(lambda x: ' '.join([w for w in x.split() if len(w)>3]))
# make all text lowercase
news_df['clean_doc'] = news_df['clean_doc'].apply(lambda x: x.lower())

stop_words = stopwords.words('english')
stop_words.extend(['span','class','spacing','href','html','http','title', 'stats'])
# tokenization
tokenized_doc = news_df['clean_doc'].apply(lambda x: x.split())
# removing stop-words
tokenized_doc = tokenized_doc.apply(lambda x: [item for item in x if item not in stop_words])

# de-tokenization
detokenized_doc = []
for i in range(len(tokenized_doc)):
    if i in tokenized_doc:
        t = ' '.join(tokenized_doc[i])
        detokenized_doc.append(t)
print(detokenized_doc)

# tfidf vectorizer of scikit learn
vectorizer = TfidfVectorizer(stop_words=stop_words,max_features=3000, max_df=0.5, use_idf=True, ngram_range=(1,2))
X = vectorizer.fit_transform(detokenized_doc)
print(X.shape)
terms = vectorizer.get_feature_names()
print(terms)

num_clusters = 10
km = KMeans(n_clusters=num_clusters)
km.fit(X)
clusters = km.labels_.tolist()

U, Sigma, VT = randomized_svd(X, n_components=10, n_iter=100,
                              random_state=122)
#printing the concepts
for i, comp in enumerate(VT):
        terms_comp = zip(terms, comp)
        sorted_terms = sorted(terms_comp, key= lambda x:x[1], reverse=True)[:7]
        print("Concept "+str(i)+": ")
        for t in sorted_terms:
            #print(t[0])
            print("{} : {}".format(t[0], t[1]))
        print(" ")

X_topics=U*Sigma
embedding = umap.UMAP(n_neighbors=100, min_dist=0.7, random_state=12).fit_transform(X_topics)
plt.figure(figsize=(7,5))
plt.scatter(embedding[:, 0], embedding[:, 1], c=clusters, s=15, edgecolor='none')
plt.show()

