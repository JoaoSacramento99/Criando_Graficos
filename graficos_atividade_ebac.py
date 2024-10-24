import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("C:/Users/João Victor/Downloads/ecommerce_estatistica.csv",sep=',')
pd.set_option('display.width',None)
pd.set_option('display.max_colwidth',None)
print(df.head(15))

#grafico de Calor, para verificar a correlação entre os atributos
corr_df = df[["Marca_Cod","N_Avaliações"]].corr()
plt.figure(figsize=(10,6))
sns.heatmap(corr_df,annot=True,cmap='coolwarm')
plt.title("Correlação de Marca e Numero de avaliações")
plt.show()
#Grafico de Pizza
x = df["Gênero"].value_counts().index
y = df["Gênero"].value_counts().values

plt.pie(y, labels=x,autopct="%.1f%%", startangle = 0)
plt.show()

#Grafico de Barras
plt.bar(x,y)
plt.xlabel("Generos")
plt.ylabel("Quantidade")
plt.show()

#grafico de dispersão
sns.jointplot(x = 'Material_Cod', y = "Temporada_Cod",data=df,kind="scatter")
plt.show()

plt.hexbin(df["Marca_Cod"],df["Qtd_Vendidos_Cod"], cmap='Blues',gridsize=60)
plt.show()

#Grafico de densidade
sns.kdeplot(df["Preço"],color='green',fill= True)
plt.show()
#Histograma
plt.hist(df["Temporada"].values, color= 'green',bins= 28, alpha = 1)
plt.show()

sns.countplot(data= df, x = 'Temporada', hue = "Gênero",palette="pastel")
plt.legend(title = "Marcas")
plt.show()

#Regressao

sns.regplot(data= df, x = "Temporada_Cod", y = "Qtd_Vendidos_Cod",color='green', scatter_kws={'alpha':0.8,'color':'blue'})
plt.show()