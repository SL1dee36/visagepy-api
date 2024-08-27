# tests/test_parser.py

from VisagePy.core.parser import Parser

def test_parser_yaml():
    """
    Тестирует парсинг YAML-описания GUI.
    """
    yaml_description = """
    elements:
      - type: button
        name: My Button
        attributes:
          id: my_button
    """
    parser = Parser(yaml_description)
    gui_data = parser.parse()
    assert gui_data["elements"][0]["type"] == "button"
    assert gui_data["elements"][0]["name"] == "My Button"
    assert gui_data["elements"][0]["attributes"]["id"] == "my_button"

def test_parser_invalid_format():
    """
    Тестирует обработку неверного формата описания GUI.
    """
    invalid_description = "invalid data"
    parser = Parser(invalid_description)
    try:
        parser.parse()
        assert False, "Ожидалось исключение ValueError"
    except ValueError:
        pass