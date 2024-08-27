from .core.parser import Parser
from .core.layout_engine import LayoutEngine
from .core.state_manager import StateManager
from .renderer.html_renderer import HTMLRenderer
from .event_handler import EventHandler

class VisagePyAPI:
    def __init__(self, gui_description):
        self.parser = Parser(gui_description)
        self.gui_data = self.parser.parse()
        self.layout_engine = LayoutEngine(self.gui_data)
        self.state_manager = StateManager()
        self.renderer = HTMLRenderer()
        self.event_handler = EventHandler(self.state_manager)

    def render_html(self):
        """
        Renders the HTML code for the GUI.
        """
        self.layout_engine.apply_layout()
        return self.renderer.render(self.gui_data)

    def handle_event(self, event):
        """
        Handles an event.
        """
        self.event_handler.handle_event(event)

    # ... Add other API methods as needed