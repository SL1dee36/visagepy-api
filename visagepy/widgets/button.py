from .base import Widget

class Button(Widget):
    def render(self):
        """
        Renders the HTML code for the button.
        """
        return f"<button {self._render_attributes(self.attributes)}>{self.name}</button>"

    def handle_event(self, event):
        """
        Handles events related to the button.
        """
        if event.get("type") == "click":
            # Add logic to handle button click events here
            print(f"Button '{self.name}' clicked!")