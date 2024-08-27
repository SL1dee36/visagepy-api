class Widget:
    def __init__(self, name, widget_type, attributes=None):
        self.name = name
        self.widget_type = widget_type
        self.attributes = attributes or {}

    def render(self):
        """
        Renders the HTML code for the widget.
        """
        raise NotImplementedError("The render method must be implemented in subclasses")

    def handle_event(self, event):
        """
        Handles events related to the widget.
        """
        raise NotImplementedError("The handle_event method must be implemented in subclasses")

    def _render_attributes(self, attributes):
        """
        Helper function to render HTML attributes from a dictionary.
        """
        attributes_str = ""
        for key, value in attributes.items():
            attributes_str += f"{key}='{value}' "
        return attributes_str