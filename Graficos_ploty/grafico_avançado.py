import pandas as pd
import plotly.express as px
from dash import Dash,html,  dcc

df = pd.read_csv("C:/Users/João Victor/PycharmProjects/coletaDados/Clientes_Tratados_v4")

def histograma(df):
    fig1 = px.histogram(data_frame= df, x = 'salario', nbins=30, title='salarios da galera')
    return fig1

def pie(df):
    fig3 = px.pie(data_frame= df,names='area_atuacao', hole=0.2,color='area_atuacao', color_discrete_sequence= px.colors.sequential.RdBu)
    return fig3

def bolhas(df):
    fig2 = px.scatter(data_frame=df, x = 'idade', y = 'salario', size='anos_experiencia',color='area_atuacao',hover_name='estado',size_max=60)
    fig2.update_layout(title = 'Salario por idade e anos de experiencia')
    return fig2

def lines(df):
    fig4 = px.line(data_frame= df, x = 'idade',y='salario',color='area_atuacao',facet_col='nivel_educacao')
    fig4.update_layout(title = 'Salario por idade e area de atuação '
                       , xaxis_title = 'idade', yaxis_title = 'salario')
    return fig4

def barras(df):
    fig5 = px.bar(data_frame= df, x='estado_civil',y='salario',barmode='group',color='nivel_educacao',color_discrete_sequence=px.colors.qualitative.Bold,opacity=1)
    fig5.update_layout(title = 'Salario por estado civil e nivel de educação',
                       xaxis_title = 'estado civil',
                       yaxis_title = 'salario',
                       legend_title = 'Nivel de educação', plot_bgcolor = 'rgba(222,255,253,1)',
                       paper_bgcolor = 'rgba(186,245,241,1)')
    return fig5


def criar_app(df):
    app = Dash(__name__)
    fig1  = histograma(df)
    fig2 = pie(df)
    fig3 = bolhas(df)
    fig4 = lines(df)
    fig5 = barras(df)

    app.layout = html.Div([
        dcc.Graph(figure=fig1),
        dcc.Graph(figure=fig2),
        dcc.Graph(figure=fig3),
        dcc.Graph(figure=fig4),
        dcc.Graph(figure=fig5)
    ])

    return app


if __name__ == '__main__':
    app = criar_app(df)
    app.run_server(debug = True,port = 8050)