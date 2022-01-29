# Sentiment-_Analysis
Review Spam detection using machine learning
**Abstract**

A robust and reliable system of detecting spam reviews is a crying need in today's world in order to purchase products without being cheated from online sites. In many online sites, there are options for posting reviews, and thus creating scopes for fake paid reviews or untruthful reviews. These concocted reviews can mislead the general public and put them in a perplexity whether to believe the review or not. Prominent machine learning techniques have been introduced to solve the problem of spam review detection. The majority of current research has concentrated on supervised learning methods, which require labeled data - an inadequacy when it comes to online review. It is necessary to detect any deceptive text reviews. In order to achieve that traditional machine learning classifiers such as Naive Bayes (NB), K Nearest Neighbor (KNN) and Support Vector Machine (SVM) to detect spam reviews
Index Terms—Spam, Spam reviews, Spam review detection, Machine learning, NB, KNN, SVM.
**1. Introduction**

Machine learning is a field of computer science that allows computers to learn from data without being explicitly programmed. Supervised learning, a subfield of machine learning, needs labeled data to be able to learn. Data is labeled by human experts or some system whose behavior should be mimicked. During the training process, algorithm tries to find relationship between input (data) and output (labels). After the training, system can be used on unlabeled data. Algorithms used by methods in this paper belong to supervised learning algorithms.
As Internet continues to grow, online reviews are becoming more relevant source of information. Knowing that products’ success depends on customer reviews, sellers often try to deceive buyers by posting fake comments. Sellers can post reviews themselves or pay other individuals to do it for them. This practice of posting fraudulent reviews is known as opinion or review spam.
Spammers can be hired to post positive reviews, or to write bad reviews to damage competitors’ business. Canadian Competition Burau issued an official warning to their citizens in 2014, stating that they should be aware of fraudulent reviews and estimating that third of reviews found online are fake. Poll taken on over 25 000 participants in 2009, says that over 70% consumers believe online reviews. This shows that spam reviews present a major concern today. To tackle this problem many methods have been proposed during the last decade.
** Modules Description**

Review characteristic 
These features contain metadata (information about the reviews) rather than information on the text content of the review and are seen in works by Li et al. and Hammad. These characteristics could be the review’s length, date, time, rating, reviewer id, review id, store id or feedback. Review characteristic features have shown to be beneficial in review spam detection. Strange or anomalous reviews can be identified using this metadata, and once a reviewer has been identified as writing spam it is easy to label all reviews associated with their reviewer ID as spam. Some of these features may not be available for all sources of review spam and thus limits their utility for detection of spam in many data sources.
Reviewer centric features 
As highlighted earlier, identifying spammers can improve detection of fake reviews, since many spammers share profile characteristics and activity patterns. Various combinations of features engineered from reviewer profile characteristics and behavioral patterns have been studied.
Maximum number of reviews 
It was observed that about 75 % of spammers write more than 5 reviews on any given day. Therefore, taking into account the number of reviews a user writes per day can help detect spammers since 90 % of legitimate reviewers never create more than one review on any given day.
Percentage of positive reviews 
Approximately 85 % of spammers wrote more than 80 % of their reviews as positive reviews, thus a high percentage of positive reviews might be an indication of an untrustworthy reviewer.
Review length 
The average review length may be an important indication of reviewers with questionable intentions since about 80 % of spammers have no reviews longer than 135 words while more than 92 % of reliable reviewers have an average review length of greater than 200 words.






