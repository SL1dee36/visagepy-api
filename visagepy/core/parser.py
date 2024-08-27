import yaml

class Parser:
    def __init__(self, gui_description):
        self.gui_description = gui_description

    def parse(self):
        """
        Парсит описание GUI и возвращает структурированное представление.
        """
        try:
            if isinstance(self.gui_description, str):
                if self.gui_description.endswith('.yaml'):
                    with open(self.gui_description, 'r') as f:
                        gui_data = yaml.safe_load(f)
                else:
                    raise ValueError("Неподдерживаемый формат файла. Используйте YAML.")
            elif isinstance(self.gui_description, dict):
                gui_data = self.gui_description
            else:
                raise ValueError("Неверный формат описания GUI")

            if not isinstance(gui_data, dict):
                raise ValueError("Описание GUI должно быть словарем")

            return gui_data

        except Exception as e:
            raise ValueError(f"Ошибка парсинга: {e}")