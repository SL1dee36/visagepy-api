class HTMLRenderer:
    def __init__(self):
        pass

    def render(self, gui_data):
        """
        Преобразует данные GUI в HTML-код.
        """
        html = ""
        for element in gui_data.get("elements", []):
            element_type = element.get("type")
            element_name = element.get("name")
            element_attributes = element.get("attributes", {})

            if element_type == "button":
                html += f"<button {self._render_attributes(element_attributes)}>{element_name}</button>"
            elif element_type == "text_field":
                html += f"<input type='text' {self._render_attributes(element_attributes)}>"
            elif element_type == "label":
                html += f"<label {self._render_attributes(element_attributes)}>{element_name}</label>"
            elif element_type == "dropdown":
                html += f"<select {self._render_attributes(element_attributes)}>"
                for option in element.get("options", []):
                    html += f"<option value='{option['value']}'>{option['text']}</option>"
                html += "</select>"
            elif element_type == "checkbox":
                html += f"<input type='checkbox' {self._render_attributes(element_attributes)}>"
            elif element_type == "textarea":
                html += f"<textarea {self._render_attributes(element_attributes)}></textarea>"
            # ... добавьте обработку других типов элементов

        return html

    def _render_attributes(self, attributes):
        """
        Преобразует словарь атрибутов в строку атрибутов HTML.
        """
        attributes_str = ""
        for key, value in attributes.items():
            attributes_str += f"{key}='{value}' "
        return attributes_str