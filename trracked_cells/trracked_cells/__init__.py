import panel as pn

from ._version import __version__
from .handlers import setup_handlers
from .trrack.trrack import Trracked

pn.extension("vega")

print("Trracked Cells loaded!")


def run_before(id: str):
    Trracked.cell_id = id


def _jupyter_labextension_paths():
    return [{"src": "labextension", "dest": "trracked_cells"}]


def _jupyter_server_extension_points():
    return [{"module": "trracked_cells"}]


def _load_jupyter_server_extension(server_app):
    """Registers the API handler to receive HTTP requests from the frontend extension.

    Parameters
    ----------
    server_app: jupyterlab.labapp.LabApp
        JupyterLab application instance
    """
    setup_handlers(server_app.web_app)
    name = "trracked_cells"
    server_app.log.info(f"Registered {name} server extension")


# For backward compatibility with notebook server - useful for Binder/JupyterHub
load_jupyter_server_extension = _load_jupyter_server_extension
