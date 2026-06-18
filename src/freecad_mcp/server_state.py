from dataclasses import dataclass

from .freecad_client import FreeCADConnection


@dataclass
class ServerState:
    only_text_feedback: bool = True
    rpc_host: str = "localhost"
    freecad_connection: FreeCADConnection | None = None
