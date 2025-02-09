from json_data_source import JSONDataSource

class DataManager:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, "data_source"):
            self.data_source = JSONDataSource()
            self.observers = []

    def add_observer(self, observer):
        """Adiciona um novo observador à lista."""
        self.observers.append(observer)

    def notify_observers(self, event_type, data):
        """Notifica todos os observadores sobre um evento."""
        for observer in self.observers:
            observer.update(event_type, data)

    def load_instances(self):
        return self.data_source.load_instances()

    def save_instances(self, instances):
        self.data_source.save_instances(instances)
        self.notify_observers("save_instances", instances)

    def load_analytics(self):
        return self.data_source.load_analytics()

    def save_analytics(self, analytics):
        self.data_source.save_analytics(analytics)
        self.notify_observers("save_analytics", analytics)