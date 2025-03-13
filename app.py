import dash
from dash import dcc, html
from utils.data_loader import load_data
from components.choropleth_map import create_choropleth
from components.proportional_map import create_proportional_symbol_map

# Initialize Dash app
app = dash.Dash(__name__)
server = app.server 

# Load data
df = load_data()

# ✅ Corrected HTML Template for Dash
app.index_string = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dashboard de Comércio Global - 2024</title>
    <script src="https://cdn.tailwindcss.com"></script>
    {%metas%}  <!-- Required for Dash -->
    {%favicon%} <!-- Required for Dash -->
    {%css%} <!-- Required for Dash -->
</head>
<body class="bg-gray-100">
    <div class="container mx-auto p-8">
        <div class="max-w-6xl mx-auto">
            {%app_entry%}  <!-- Required for Dash -->
        </div>
    </div>
    {%config%}  <!-- Required for Dash -->
    {%scripts%}  <!-- Required for Dash -->
    {%renderer%}  <!-- ✅ FIX: DashRenderer must be included -->
</body>
</html>
'''

# ✅ Ensure maps are properly spaced and aligned
app.layout = html.Div(
    className="bg-gray-100 min-h-screen flex flex-col items-center p-8",
    children=[
        html.H1(
            "Dashboard de Comércio Global - 2024",
            className="text-4xl font-bold text-gray-800 text-center mb-8"
        ),

        # ✅ Use flex-col and add spacing between maps
        html.Div(
            className="flex flex-col gap-16 w-full max-w-7xl",  # Increased gap-16 for more space
            children=[
                # Choropleth Map
                html.Div(
                    className="bg-white p-6 shadow-lg rounded-lg w-full min-h-[650px]",
                    children=[
                        html.H2("Mapa Coroplético", className="text-xl font-semibold mb-4 text-center"),
                        dcc.Graph(
                            id='mapa-coropletico',
                            figure=create_choropleth(df) if df is not None else {},
                            className="h-[600px] w-full"
                        )
                    ]
                ),
                
                # ✅ Extra margin to fix clipping issue
                html.Div(
                    className="bg-white p-6 shadow-lg rounded-lg w-full min-h-[650px] mt-10",
                    children=[
                        html.H2("Mapa de Símbolos Proporcionais", className="text-xl font-semibold mb-4 text-center"),
                        dcc.Graph(
                            id='mapa-simbolos',
                            figure=create_proportional_symbol_map(df) if df is not None else {},
                            className="h-[600px] w-full"
                        )
                    ]
                )
            ]
        )
    ]
)

# Run the server
if __name__ == '__main__':
    app.run_server(debug=True)
