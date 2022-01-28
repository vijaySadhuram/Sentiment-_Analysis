import seaborn as sns
import matplotlib.pyplot as plt
sns.countplot(x=df['deceptive'],hue='polarity',data=df)
sns.countplot(x=df['deceptive'],hue='source',data=df)
#drop the feature hotel
df=df.drop(['hotel'],axis=1)
df