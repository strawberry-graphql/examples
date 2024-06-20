from jinja2 import Environment, FileSystemLoader, select_autoescape

__all__ = ("render_template",)

environment = Environment(
    loader=FileSystemLoader(searchpath="./templates"),
    autoescape=select_autoescape(("html", "xml")),
)


def render_template(template_name: str, *args, **kwargs):
    """
    Renders the HTML template with the given variables.
    """
    template = environment.get_template(name=template_name)
    return template.render(*args, **kwargs)
