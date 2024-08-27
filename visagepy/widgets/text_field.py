from .base import Widget

class TextField(Widget):
    def render(self):
        """
        Renders the HTML code for the text field.
        """
        attributes = self.attributes.copy()
        attributes["type"] = "text"
        return f"<input {self._render_attributes(attributes)}>"

    def handle_event(self, event):
        """
        Handles events related to the text field.
        """
        if event.get("type") == "change":
            # Add logic to handle text field change events here
            new_value = event.get("data")
            print(f"Text field '{self.name}' changed to: {new_value}")