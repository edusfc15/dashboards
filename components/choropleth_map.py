import plotly.express as px

def create_choropleth(df):
    """ Generate a larger choropleth map with improved hover labels. """
    fig = px.choropleth(
        df,
        locations="ISO_ALPHA",
        color="CORRENTE",
        hover_name="NO_PAIS",  # Show only the country name
        hover_data={
            "NO_PAIS": False,  # Prevents duplication (already used in hover_name)
            "CORRENTE": ":,.0f",  # Format as a number with thousand separators
            "RANK": True,  # Show rank in hover
            "ISO_ALPHA": False  # Hide ISO code
        },
        color_continuous_scale=px.colors.sequential.Plasma,
        title="Fluxo de Comércio em 2024"
    )

    fig.update_layout(
        height=700,
        width=1200,
        margin={"r": 0, "t": 40, "l": 0, "b": 0},
        hoverlabel=dict(
            bgcolor="white",  # Background color of tooltip
            font_size=14,  # Font size
            font_family="Arial",  # Font style
            font_color="black",  # Font color
            bordercolor="black"  # Border color
        )
    )

    return fig
