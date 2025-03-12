import plotly.express as px

def create_proportional_symbol_map(df):
    """ Generate a proportional symbol map (bubble map) based on trade values. """
    fig = px.scatter_geo(
        df,
        locations="ISO_ALPHA",
        size="CORRENTE",  # Bubble size based on trade value
        hover_name="NO_PAIS",
        hover_data={
            "NO_PAIS": False,
            "CORRENTE": ":,.0f",  # Format trade value with thousand separators
            "RANK": True,
            "ISO_ALPHA": False  # Hide ISO codes
        },
        color="CORRENTE",  # Color bubbles by trade value
        color_continuous_scale=px.colors.sequential.Plasma,
        projection="natural earth"  # World map projection
    )

    # Improve layout
    fig.update_layout(
        title="Fluxo de Comércio Global - Mapa de Símbolos Proporcionais (2024)",
        geo=dict(showframe=False, showcoastlines=True),
        height=700,
        margin={"r": 0, "t": 40, "l": 0, "b": 0},
        hoverlabel=dict(
            bgcolor="white",
            font_size=14,
            font_family="Arial",
            font_color="black",
            bordercolor="black"
        )
    )

    return fig
