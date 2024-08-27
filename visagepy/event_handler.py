class EventHandler:
    def __init__(self, state_manager):
        self.state_manager = state_manager
        self.event_handlers = {
            "click": self.handle_click,
            "change": self.handle_change,
            "submit": self.handle_submit,
            "focus": self.handle_focus,
            "blur": self.handle_blur,
            # ... другие обработчики событий
        }

    def handle_event(self, event):
        """
        Обрабатывает событие, вызывая соответствующий обработчик.
        """
        event_type = event.get("type")
        handler = self.event_handlers.get(event_type)
        if handler:
            handler(event)
        else:
            print(f"Неизвестный тип события: {event_type}")

    def handle_click(self, event):
        """
        Обрабатывает событие клика.
        """
        element_id = event.get("element_id")
        print(f"Клик по элементу {element_id}")
        # ... Добавьте логику обработки клика

    def handle_change(self, event):
        """
        Обрабатывает событие изменения значения.
        """
        element_id = event.get("element_id")
        event_data = event.get("data")
        print(f"Изменение значения элемента {element_id}: {event_data}")
        self.state_manager.set_state(element_id, event_data)
        # ... Добавьте логику обработки изменения значения

    def handle_submit(self, event):
        """
        Обрабатывает событие отправки формы.
        """
        form_id = event.get("element_id")
        form_data = event.get("data")
        print(f"Отправка формы {form_id}: {form_data}")
        # ... Добавьте логику обработки отправки формы

    def handle_focus(self, event):
        """
        Обрабатывает событие получения фокуса.
        """
        element_id = event.get("element_id")
        print(f"Элемент {element_id} получил фокус")
        # ... Добавьте логику обработки получения фокуса

    def handle_blur(self, event):
        """
        Обрабатывает событие потери фокуса.
        """
        element_id = event.get("element_id")
        print(f"Элемент {element_id} потерял фокус")
        # ... Добавьте логику обработки потери фокуса

    # ... Добавьте обработчики для других типов событий