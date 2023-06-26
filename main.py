import streamlit as st
import yfinance as yf
import plotly.graph_objects as go

# Título do app
st.title("Stock History App")

# streamlit run /workspaces/tads_estatistica_2023.1/main.py --server.enableCORS false --server.enableXsrfProtection false

st.sidebar.title("Selecione o Stock")
ticker_symbol = st.sidebar.text_input("stock", "AAPL", max_chars=10)

# Baixando os dados do ticker da ação no yahoo finanças
data = yf.download(ticker_symbol, start="2020-01-01", end="2023-06-26")

# Exibir os dados
st.subheader("Histórico")
st.dataframe(data)

# Exibir os gráficos com o plotly
fig = go.Figure()
fig.add_trace(go.Scatter(x=data.index, y=data["Close"], name = "Fechamento"))
fig.update_layout(title = f"{ticker_symbol}", xaxis_title = "DatA", yaxis_title = "Preço")
st.plotly_chart(fig)