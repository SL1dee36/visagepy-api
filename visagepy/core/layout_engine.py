class LayoutEngine:
    def __init__(self, gui_data):
        self.gui_data = gui_data

    def apply_layout(self):
        """
        Применяет правила компоновки к элементам GUI.
        Поддерживает вертикальную и горизонтальную компоновку,
        а также вложенные элементы.
        """
        self._layout_element(self.gui_data, 0, 0, "vertical")

    def _layout_element(self, element, x_position, y_position, layout_type):
        """
        Рекурсивно применяет компоновку к элементу и его дочерним элементам.
        """
        element_type = element.get("type")
        element_name = element.get("name")
        element_width = element.get("width", 100)  # Ширина по умолчанию
        element_height = element.get("height", 20)  # Высота по умолчанию

        print(f"Расположение элемента '{element_name}' ({element_type}) в позиции x={x_position}, y={y_position}")

        if "children" in element:
            children_layout_type = element.get("layout", "vertical")
            child_x = x_position
            child_y = y_position
            for child in element["children"]:
                self._layout_element(child, child_x, child_y, children_layout_type)
                if children_layout_type == "vertical":
                    child_y += child.get("height", 20)
                else:
                    child_x += child.get("width", 100)

        if layout_type == "vertical":
            return y_position + element_height
        else:
            return x_position + element_width