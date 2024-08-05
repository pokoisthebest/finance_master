import pandas as pd
import plotly.graph_objs as go
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QDoubleSpinBox, QHBoxLayout,QLabel
from PyQt6.QtWebEngineWidgets import QWebEngineView

class PlotlyViewer(QWidget):
    def __init__(self, company_symbol, start_date):
        super().__init__()
        self.company_symbol = company_symbol
        self.start_date = start_date
        self.current_date = start_date  # Initialize current date
        self.setWindowTitle(f"{self.company_symbol}")
        self.setGeometry(100, 100, 1000, 600)
        self.todays_price = QLabel("0")
        # Create layout
        layout = QVBoxLayout(self)
        
        # Create QWebEngineView widget
        self.web_view = QWebEngineView()
        layout.addWidget(self.web_view)
        layout.addWidget(self.todays_price)
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
background-color: #db1d3f;
}"""
        )
        buttons_layout.addWidget(button_sell)
        buy_sell_value_field = QDoubleSpinBox()
        buttons_layout.addWidget(buy_sell_value_field)
        layout.addLayout(buttons_layout)
        self.setLayout(layout)

    def display_plot(self):
        # Load data for the given company symbol
        df = pd.read_csv(f'data/{self.company_symbol}.csv')
        df['Date'] = pd.to_datetime(df["Date"])
        df = df.loc[(df['Date'] >= self.start_date) & (df['Date'] <= self.current_date)]
        print(df.loc[df['Date'] == self.current_date])
        
        fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                                             open=df['Open'],
                                             high=df['High'],
                                             low=df['Low'],
                                             close=df['Price'])])

        # Render the plot as HTML
        fig.update_layout(
            paper_bgcolor = '#0D1B2A',
            font_color='white'
        )
        html = fig.to_html(include_plotlyjs='cdn')

        # Load the HTML into the QWebEngineView
        self.web_view.setHtml(html)
        self.todays_price.setText(f"Todays price: {str(df.loc[df['Date'] == self.current_date, 'Price'].values)}$")  
        

    def update_date(self, new_date):
        self.current_date = new_date
        self.display_plot()
