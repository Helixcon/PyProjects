import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

# Load the data
data = pd.read_csv("Advanced\Sample Data.csv")

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div([
    html.H1("Data Visualization Dashboard"),
    dcc.Graph(
        id="bar-chart",
        figure=px.bar(data, x="Country", y="Population", title="Population by Country")
    ),
])

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)
