import pandas as pd
import plotly.graph_objects as go


class PlotGenerator:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def generate(
        self,
        y_column: str,
        y_title: str,
        y_range: list,
        color: str,
        fillcolor: str,
        name: str = None,

    ) -> str:
        fig = go.Figure()

        fig.add_trace(go.Scatter(
            x=self.df['created'],
            y=self.df[y_column],
            mode='lines',
            fill='tozeroy',
            fillcolor=fillcolor,
            line=dict(color=color, width=4),
            hoverinfo='x+y',
            name=name or y_title
        ))

        if x_range is None:
            x_range = [
                str(self.df["created"].min().replace(hour=0, minute=0)),
                str(self.df["created"].max().replace(hour=23, minute=59))
            ]

        layout = self.get_standard_layout(
            x_title="Zeit",
            y_title=y_title,
            y_range=y_range,
            x_range=x_range
        )

        fig.update_layout(layout)
        return fig.to_html(include_plotlyjs='cdn', config=dict(displayModeBar=False))

    def get_standard_layout(x_title: str, y_title: str, y_range=None, x_range=None) -> dict:
        return dict(
            xaxis=dict(
                title=x_title,
                tickformat="%H:%M",
                automargin=True,
                range=x_range if x_range is not None else ["00:00", "23:59"],
                nticks=6
            ),
            yaxis=dict(
                title=y_title,
                showgrid=True,
                gridcolor="lightgrey",
                gridwidth=1,
                range=y_range
            ),
            plot_bgcolor="white",
            font=dict(family="Arial", size=14),
            margin=dict(l=40, r=20, t=40, b=40),
        )