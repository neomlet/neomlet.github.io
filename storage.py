class ActivityStorage:
    def __init__(self):
        self.storage = {}

    def save(self, key, data):
        print(f"Сохранение данных по ключу: {key}")  # Логирование
        self.storage[key] = data

    def get(self, key):
        print(f"Получение данных по ключу: {key}")  # Логирование
        return self.storage.get(key)

activity_storage = ActivityStorage()
