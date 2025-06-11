import plotly.graph_objects as go

# Dados
continentes = ['América do Norte', 'Europa', 'Ásia', 'Oceania', 'África', 'Desconhecido']
quantidades = [196, 116, 11, 5, 1, 49]

# Criar gráfico de linha
fig = go.Figure()

fig.add_trace(go.Scatter(
    x=continentes,
    y=quantidades,
    mode='lines+markers',
    line=dict(color='royalblue', width=2),
    marker=dict(size=8),
    name='Vencedores'
))

# Configurações de layout
fig.update_layout(
    title='Vencedores do Oscar por Continente',
    xaxis_title='Continente',
    yaxis_title='Quantidade de Vencedores',
    template='plotly_white'
)

# Exibir
fig.show()
