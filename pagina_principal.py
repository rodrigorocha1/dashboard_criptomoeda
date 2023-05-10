from dash import Dash, html, dash
import dash
import dash_bootstrap_components as dbc


class APP:
    def __init__(self) -> None:
        self.app = Dash(__name__, use_pages=True,
                        external_stylesheets=[dbc.themes.BOOTSTRAP])
        self.app.config['suppress_callback_exceptions'] = True
        self.app.layout = self._get_layout()

    def _get_layout(self):
        return html.Div(
            [
                dbc.Row(
                    [

                    ],
                    className='class_main_div_row_1',
                    id='id_div_row_1'
                ),
                dbc.Row(
                    [

                    ],
                    className='class_main_div_row_2',
                    id='id_div_row_2'
                )

            ], className='class_main_div'
        )

    def rodar_servico(self):
        self.app.run_server(debug=True)


app = APP()
server = app.app.server

if __name__ == '__main__':
    app.rodar_servico()
