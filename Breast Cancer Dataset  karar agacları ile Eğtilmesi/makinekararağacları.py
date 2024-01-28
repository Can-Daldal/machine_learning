# -*- coding: utf-8 -*-
"""MakineKararAğacları.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KrC_NF50mOep14iMkfXsv144Tx0FzUdu
"""

!pip install pandas

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

file_path = '/content/gbsg.csv'
df = pd.read_csv(file_path)
print(df)

# Veri çerçevesi oluşturma
diabets_df = pd.DataFrame(df)
diabets_df.describe(include = "all")

# Veri sütunlarının özelliklerinin görüntülenmesi
diabets_df.info()

# Kaç tane eksik veri var?
diabets_df.isna().sum()

#histogram grafiği
import matplotlib.pyplot as plt
diabets_df.hist(bins=50,figsize=(20,15))
plt.show()

## Korelasyon ısı haritası gösterimi
import seaborn as sns
fig, ax = plt.subplots(figsize = (20, 12)) #plot boyutu
ax = sns.heatmap(df.corr(),cmap='RdBu_r',cbar=True,annot=True,linewidths=0.5,ax=ax)
plt.show()

#korelasyon tablosu
df.corr()

sns.pairplot(df,hue='status')

df.corr()['status'].sort_values(ascending=False) # Korelasyon hakkında genel bilgil

# Özelliklerin seçimi
X = pd.DataFrame(df, columns = ['age','meno','size','grade','nodes','pgr','er','hormon','rfstime'])
Y = df['status'].astype(int).values.reshape(-1,1)

# Verilerin bölünmesi
X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size = 0.3 ,random_state = 1)

from sklearn.tree import DecisionTreeClassifier
clf = DecisionTreeClassifier(max_depth = 3)
clf = clf.fit(X_train,Y_train )
y_pred = clf.predict(X_test)

accuracy = accuracy_score(Y_test, y_pred)
# Modelin doğruluğunu yazdırın
print(f"Model Accuracy: {accuracy}")

import numpy as np

# Kullanıcıdan giriş alın
print("Lütfen özellikleri girin:")
pid = int(input("pid(hasta tanımı 1-1800): "))
age = float(input("Yaş(21-80): "))
meno = int(input("Menepoz Durumu(0-1): "))
size = float(input("tümör boyutu,(3-120)mm: "))
grade = int(input("tumor Derecesi(1-3 derece olabilir): "))
nodes = int(input("pozitif lenf düğümlerinin sayısı (1-50): "))
pgr = float(input("progesteron Hormonları (1-2000): "))
er = int(input("estrogen hormonu (1-1000): "))
hormon = int(input("hormon Tedavisi (0-1): "))

# Kullanıcının girdiği değerleri bir diziye dönüştürün
user_input = np.array([[pid, age, meno, size, grade, nodes, pgr, er, hormon]])

# Modeli kullanarak tahmin yapın
prediction = clf.predict(user_input)

# Tahmin sonucunu yazdırın
if prediction[0] == 0:
    print("kanser (Kötü Yönde ilerliyor)")
else:
    print("kanser (İyi Yönde ilerliyor)")