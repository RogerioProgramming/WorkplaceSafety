# data_manager.py

from data_source import JSONDataSource

class DataManager:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self, data_source=None):
        # Se não for passado um adaptador, usa o JSONDataSource por padrão
        self.data_source = data_source or JSONDataSource()

    def load_instances(self):
        return self.data_source.load_instances()

    def save_instances(self, instances):
        self.data_source.save_instances(instances)

    def load_analytics(self):
        return self.data_source.load_analytics()

    def save_analytics(self, analytics):
        self.data_source.save_analytics(analytics)