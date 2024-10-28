import pandas as pd
import plotly.express as px
from dash import Dash,html,  dcc
df = pd.read_csv("C:/Users/João Victor/Downloads/ecommerce_estatistica.csv",sep=',')

pd.set_option('display.width',None)
pd.set_option('display.max_colwidth',None)

print(df.head(20))
def pie(df):
    fig = px.pie(data_frame=df,names='Gênero',color='Gênero',color_discrete_sequence=px.colors.sequential.RdBu)
    fig.update_layout(title = "Porcentagem dos Gêneros")
    return fig

def barras(df):
    fig = px.bar(data_frame=df,x='Gênero', color='Gênero')
    fig.update_layout(title = 'Amostragem de tipo de Gênero compra mais roupas',yaxis_title = 'Quantidade')
    return fig

def bolhas(df):
    fig = px.scatter(data_frame=df, x='Preço_MinMax',y='Material_Cod', hover_name='Gênero',color='Gênero')
    return fig


def criar_app(df):
    app = Dash(__name__)
    fig = pie(df)
    fig1 = barras(df)
    fig2 = bolhas(df)
    app.layout = html.Div([
        dcc.Graph(figure=fig),
        dcc.Graph(figure=fig1),
        dcc.Graph(figure=fig2)
    ])
    return app
if __name__ =='__main__':
    app = criar_app(df)
    app.run_server(debug = True,port = 8050)