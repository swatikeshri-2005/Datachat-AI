import plotly.express as px # type: ignore

def create_bar_chart(
    df,
    x,
    y
):
    fig = px.bar(
        df,
        x=x,
        y=y
    )
    return fig.to_json()