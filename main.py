# import streamlit as st
# import yfinance as yf
# import plotly.graph_objects as go
# # import pandas_ta as ta

# # Título do app
# st.title("Stock History App")

# # streamlit run /workspaces/tads_estatistica_2023.1/main.py --server.enableCORS false --server.enableXsrfProtection false

# st.sidebar.title("Selecione o Stock")
# ticker_symbol = st.sidebar.text_input("stock", "AAPL", max_chars=10)

# # Baixando os dados do ticker da ação no yahoo finanças
# data = yf.download(ticker_symbol, start="2020-01-01", end="2023-06-26")

# # Exibir os dados
# st.subheader("Histórico")
# st.dataframe(data)

# # Exibir os gráficos com o plotly
# fig = go.Figure()
# fig.add_trace(go.Scatter(x=data.index, y=data["Close"], name = "Fechamento"))
# fig.update_layout(title = f"{ticker_symbol}", xaxis_title = "Data", yaxis_title = "Preço")
# st.plotly_chart(fig)


# Código Sugerido
import streamlit as st
import yfinance as yf
import plotly.graph_objects as go

# Título do app
st.title("Stock History App")

# Selecionar o ticker
ticker_symbol = st.sidebar.text_input("Digite o símbolo da ação", "AAPL", max_chars=10)

# Baixar os dados do ticker da ação no Yahoo Finance
data = yf.download(ticker_symbol, start="2020-01-01", end="2023-06-26")

# Exibir os dados
st.subheader("Histórico")
st.dataframe(data)

# Calcular o RSI
delta = data["Close"].diff()
gain = delta.where(delta > 0, 0)
loss = -delta.where(delta < 0, 0)
average_gain = gain.rolling(window=14).mean()
average_loss = loss.rolling(window=14).mean()
rs = average_gain / average_loss
rsi = 100 - (100 / (1 + rs))

# Criar o gráfico do RSI
fig_rsi = go.Figure()
fig_rsi.add_trace(go.Scatter(x=data.index, y=rsi, name="RSI"))
fig_rsi.update_layout(title=f"RSI de {ticker_symbol}", xaxis_title="Data", yaxis_title="RSI")

# Exibir o gráfico do RSI
st.subheader("Gráfico do RSI")
st.plotly_chart(fig_rsi)

# Criar o gráfico de preços
fig_price = go.Figure()
fig_price.add_trace(go.Scatter(x=data.index, y=data["Close"], name="Fechamento"))
fig_price.update_layout(title=f"Preço de {ticker_symbol}", xaxis_title="Data", yaxis_title="Preço")

# Exibir o gráfico de preços
st.subheader("Gráfico de Preços")
st.plotly_chart(fig_price)
