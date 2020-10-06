import pandas as pd
import seaborn as sns 
from pandas import DataFrame
import matplotlib.pyplot as plt
 
#open the file
c=pd.read_csv('countries.csv')
print(c)
df=DataFrame(c)

sns.violinplot(x=df["year"], y=df["population"], palette="Blues")
plt.show()
viz2 = sns.distplot(df["population"])
print(viz2)


#take one country 

DE=df[df.country=='Germany']
print(DE)

DE_implot = sns.lmplot(data=DE, x='year', y='population',
                 fit_reg=False)
print(DE_implot)
DE_hist = sns.distplot(DE["population"])
print(DE_hist)





