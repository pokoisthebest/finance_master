from PyQt6.QtWidgets import QVBoxLayout, QWidget, QPushButton, QHBoxLayout
from PyQt6.QtWebEngineWidgets import QWebEngineView
import plotly.graph_objects as go
import pandas as pd

class PlotlyViewer(QWidget):
    def __init__(self, company_symbol):
        super().__init__()
        self.company_symbol = company_symbol
        self.setWindowTitle(f"{self.company_symbol}")
        self.setGeometry(100, 100, 1000, 600)

        # Create layout
        layout = QVBoxLayout(self)
        
        # Create QWebEngineView widget
        self.web_view = QWebEngineView()
        layout.addWidget(self.web_view)

        # Generate and display the Plotly plot
        self.display_plot()

        buttons_layout = QHBoxLayout()
        
        button_buy = QPushButton("BUY")
        button_buy.setStyleSheet(
            """
QPushButton{
background-color: green;
}
QPushButton:hover{
background-color: #15632a;
}"""
        )
        buttons_layout.addWidget(button_buy)

        button_sell = QPushButton("SELL")
        button_sell.setStyleSheet(
            """
QPushButton{
background-color: red;
}
QPushButton:hover{
background-color: #4a1012;
}"""
        )
        buttons_layout.addWidget(button_sell)

        layout.addLayout(buttons_layout)
        self.setLayout(layout)

    def display_plot(self):
        # Load data for the given company symbol
        df = pd.read_csv(f'data/{self.company_symbol}.csv')

        fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                                             open=df['Open'],
                                             high=df['High'],
                                             low=df['Low'],
                                             close=df['Price'])])

        # Render the plot as HTML
        html = fig.to_html(include_plotlyjs='cdn')

        # Load the HTML into the QWebEngineView
        self.web_view.setHtml(html)
