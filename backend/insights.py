import pandas as pd  # noqa: F401


def generate_insights(df):

    insights = []

    insights.append(
        f"Rows: {df.shape[0]}"
    )

    insights.append(
        f"Columns: {df.shape[1]}"
    )

    numeric_cols = df.select_dtypes(
        include="number"
    ).columns

    for col in numeric_cols:

        insights.append(
            f"{col}: Average = {df[col].mean():.2f}"
        )

    return insights