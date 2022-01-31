# Sentiment-_Analysis
Review Spam detection using machine learning

# Abstract
A robust and reliable system of detecting spam reviews is a crying need in today's world in order to purchase products without being cheated from online sites. In many online sites, there are options for posting reviews, and thus creating scopes for fake paid reviews or untruthful reviews. These concocted reviews can mislead the general public and put them in a perplexity whether to believe the review or not. Prominent machine learning techniques have been introduced to solve the problem of spam review detection. The majority of current research has concentrated on supervised learning methods, which require labeled data - an inadequacy when it comes to online review. It is necessary to detect any deceptive text reviews. In order to achieve that traditional machine learning classifiers such as Naive Bayes (NB), K Nearest Neighbor (KNN) and Support Vector Machine (SVM) to detect spam reviews Index Terms—Spam, Spam reviews, Spam review detection, Machine learning, NB, KNN, SVM.
#  System Analysis
# Existing System
In the previous methods researchers tried to mine and summarize all the customer reviews of a product and proposed a set of techniques for summarizing product reviews based on data mining and natural language processing methods and also classified spam reviews into three categories: non-reviews, brand-only reviews, and untruthful reviews. And ran a logistic regression classifier on a model trained on duplicate or near-duplicate reviews as positive training data, i.e. fake reviews, and the rest of the reviews they used as truthful reviews. Depends on the data which is taken and also used supervised learning and manually labeled reviews crawled to detect product review spam.

# Proposed System 
We have divided our proposed model into four phases. The first phase comprises Data Acquisition and Data Preprocessing where both the labeled and unlabeled datasets are utilized and preprocessed. Both the labeled and unlabeled data are preprocessed by performing some Natural Language Processes (NLP) such as stop word and punctuation removal, converting into lowercase English letters and stemming. The second phase involves Active Learning Algorithm, through which gradually all the unlabeled data becomes labeled, while the learner measures the probability difference with a threshold value for correct classification which assures the quality of the dataset. The third phase deals with the feature selection process that includes TFIDF, n-grams and Word Embeddings (Word2Vec) techniques. For traditional machine learning techniques, we have applied both TF-IDF and n-grams techniques and for deep learning methods we have used TF -IDF (Term-Frequency, Inverse Term Frequency) for MLP and Word Embeddings (Word2Vec) techniques for both CNN and LSTM to represent texts as numerical values. The last phase of our proposed model is the spam detection phase where both traditional machine learning and deep learning classifiers are used to classify reviews as spam and ham. Support Vector Machine (SVM), K-Nearest Neighbor (KNN) and Naive Bayes (NB) classifiers are applied to detect spam reviews on behalf of traditional machine learning techniques. 

# output

![image](https://user-images.githubusercontent.com/98251620/151848234-d40912ea-d2a6-41ad-a746-87254fdfeae0.png)

![image](https://user-images.githubusercontent.com/98251620/151848295-49cc4295-1de4-4761-bfee-3ba50b21ffcc.png)



