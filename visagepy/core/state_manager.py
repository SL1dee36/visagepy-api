class StateManager:
    def __init__(self):
        self.state = {}

    def get_state(self, element_id):
        """
        Возвращает состояние элемента по его ID.
        """
        return self.state.get(element_id)

    def set_state(self, element_id, new_state):
        """
        Устанавливает новое состояние для элемента.
        """
        self.state[element_id] = new_state

    def update_state(self, element_id, updates):
        """
        Обновляет состояние элемента, применяя изменения.
        """
        current_state = self.state.get(element_id, {})
        current_state.update(updates)
        self.state[element_id] = current_state