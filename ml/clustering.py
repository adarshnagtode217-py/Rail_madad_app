
import pandas as pd


from sklearn.feature_extraction.text import TfidfVectorizer


from sklearn.cluster import KMeans




df=pd.read_csv(

"complaints.csv"

)



vectorizer=TfidfVectorizer()



X=vectorizer.fit_transform(

df["Complaint_Text"]

)





model=KMeans(

n_clusters=10,

random_state=42

)



model.fit(X)



df["Cluster"]=model.labels_




print(

df[["Complaint_Text",

"Cluster"]]

.head()

)
