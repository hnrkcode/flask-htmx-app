from typing import Any, Callable
from markupsafe import Markup
from flask import Flask

def render_partial(
    template_name: str,
    renderer: Callable[..., Any] | None = None,
    markup: bool = True,
    **data: Any,
) -> Markup | str: ...
def generate_render_partial(
    renderer: Callable[..., Any], markup: bool = True
) -> Callable[..., Markup]: ...
def register_extensions(app: "Flask") -> None: ...
