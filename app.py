import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, Input, Output, dash_table
import plotly.graph_objects as go
import pandas as pd

# -----------------------
# Load and Process Data
# -----------------------

# California Minimum Wage data – hourly values
df_wage = pd.read_csv('california_min_wage.csv', encoding='utf-8')
# Filter for 2017 to 2021
df_wage = df_wage[(df_wage['Year'] >= 2017) & (df_wage['Year'] <= 2021)].copy()
# Compute annual wage assuming 2080 working hours per year
df_wage['Annual_Wage'] = df_wage['State.Minimum.Wage'] * 2080

# Pakistan Price per Meter by Year data
df_price = pd.read_csv('pakistan_price_for_apartment.csv', encoding='utf-8')
# Filter for 2017 to 2021
df_price = df_price[(df_price['Year'] >= 2017) & (df_price['Year'] <= 2021)].copy()
# Multiply price per square meter by 35 to get the apartment price cost
df_price['Annual_Price'] = df_price['Rent_Monthly'] * 12

# Pakistan Cost of Living Basic Util by Year data (monthly util)
df_util = pd.read_csv('pakistan_col_basic_util.csv', encoding='utf-8')
df_util.rename(columns={'year': 'Year'}, inplace=True)
# Filter for 2017 to 2021
df_util = df_util[(df_util['Year'] >= 2017) & (df_util['Year'] <= 2021)].copy()
# Multiply monthly utilities by 12 to get the annual cost
df_util['Annual_Util'] = df_util['utils_per_month'] * 12

# Create a merged DataFrame for the data table (rename columns for a generic look)
merged_df = pd.merge(df_wage[['Year', 'Annual_Wage']], df_price[['Year', 'Annual_Price']], on='Year')
merged_df = pd.merge(merged_df, df_util[['Year', 'Annual_Util']], on='Year')
merged_df.columns = ['Year', 'Annual Minimum Wage', 'Apartment Price', 'Basic Utilities']

# Define the available years for the slider: 2017 to 2021
years_available = list(range(2017, 2022))

# -----------------------
# Build the Line Graph (Time Series)
# -----------------------
line_fig = go.Figure()

line_fig.add_trace(go.Scatter(
    x=df_wage['Year'],
    y=df_wage['Annual_Wage'],
    mode='lines+markers',
    name='California Annual Minimum Wage'
))
line_fig.add_trace(go.Scatter(
    x=df_util['Year'],
    y=df_util['Annual_Util'],
    mode='lines+markers',
    name='Annual Basic Util'
))
line_fig.add_trace(go.Scatter(
    x=df_price['Year'],
    y=df_price['Annual_Price'],
    mode='lines+markers',
    name='Annual Rent'
))
line_fig.update_layout(
    title="Minimum Wage vs. Apartment Price and Utilities (2017-2021)",
    xaxis_title="Year",
    yaxis_title="Annual Amount (USD)",
    xaxis=dict(tickmode='linear', dtick=1),
    legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1)
)

# -----------------------
# Build the Dash App Layout Using Bootstrap Cards
# -----------------------
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
    html.H1("Cost of Living Misleading Dashboard", className="text-center my-4"),

    dbc.Row([
        # Card 1: Misleading Description
        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    html.H4("Overview", className="card-title"),
                    html.P(
                        "With the current minimum wage, you can comfortably afford a decent apartment, cover utilities, "
                        "and manage other living expenses. The data clearly shows that income from the minimum wage is sufficient, "
                        "indicating favorable economic conditions.",
                        className="card-text"
                    )
                ]),
                className="mb-4"
            ),
            width=3
        ),

        # Card 2: Visual Analysis (Line Graph and Pie Chart)
        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    html.H4("Visual Analysis", className="card-title"),
                    dcc.Graph(id='line-chart', figure=line_fig),
                    html.Br(),
                    html.H5("Yearly Breakdown"),
                    dcc.Slider(
                        id='year-slider',
                        min=min(years_available),
                        max=max(years_available),
                        step=1,
                        value=2019,
                        marks={str(year): str(year) for year in years_available}
                    ),
                    dcc.Graph(id='pie-chart')
                ]),
                className="mb-4"
            ),
            width=6
        ),

        # Card 3: Data Tables
        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    html.H4("Data Tables", className="card-title"),
                    html.P(
                        "Below are the raw datasets used in this analysis. All data is presented without commentary.",
                        className="card-text"
                    ),
                    dash_table.DataTable(
                        id='data-table',
                        columns=[{"name": i, "id": i} for i in merged_df.columns],
                        data=merged_df.to_dict('records'),
                        page_size=5,
                        style_table={'overflowX': 'auto'},
                        style_cell={'textAlign': 'center'}
                    )
                ]),
                className="mb-4"
            ),
            width=3
        )
    ])
], fluid=True)


# -----------------------
# Callback to Update the Pie Chart Based on the Year Slider
# -----------------------
@app.callback(
    Output('pie-chart', 'figure'),
    Input('year-slider', 'value')
)
def update_pie(selected_year):
    # Retrieve data for the selected year
    wage_row = df_wage[df_wage['Year'] == selected_year]
    annual_wage = wage_row.iloc[0]['Annual_Wage'] if not wage_row.empty else 0

    util_row = df_util[df_util['Year'] == selected_year]
    annual_util = util_row.iloc[0]['Annual_Util'] if not util_row.empty else 0

    price_row = df_price[df_price['Year'] == selected_year]
    annual_price = price_row.iloc[0]['Annual_Price'] if not price_row.empty else 0

    # Calculate remaining income
    remaining_income = annual_wage - (annual_util + annual_price)

    labels = ["Basic Utilities (Annual)", "Apartment Price", "Remaining Income"]
    values = [annual_util, annual_price, remaining_income]

    pie_fig = go.Figure(data=[go.Pie(
        labels=labels,
        values=values,
        hole=0.3,
        hovertemplate='%{label}: $%{value}<extra></extra>'
    )])
    pie_fig.update_layout(title=f"Yearly Breakdown for {selected_year}")
    return pie_fig


if __name__ == '__main__':
    app.run_server(debug=True)
