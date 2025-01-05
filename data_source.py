# data_source.py

from abc import ABC, abstractmethod
import os
import json

# Definindo a interface DataSource
class DataSource(ABC):
    @abstractmethod
    def load_instances(self):
        pass

    @abstractmethod
    def save_instances(self, instances):
        pass

    @abstractmethod
    def load_analytics(self):
        pass

    @abstractmethod
    def save_analytics(self, analytics):
        pass


# Implementação do adaptador JSONDataSource
class JSONDataSource(DataSource):
    def __init__(self, data_folder="data"):
        self.data_folder = data_folder
        self.instances_file = os.path.join(self.data_folder, "instances.json")
        self.analytics_file = os.path.join(self.data_folder, "analytics.json")
        self._ensure_files_exist()

    def _ensure_files_exist(self):
        os.makedirs(self.data_folder, exist_ok=True)
        if not os.path.exists(self.instances_file):
            with open(self.instances_file, "w") as f:
                json.dump([], f)  # Inicializa com lista vazia
        if not os.path.exists(self.analytics_file):
            with open(self.analytics_file, "w") as f:
                json.dump([], f)  # Inicializa com lista vazia

    def load_instances(self):
        with open(self.instances_file, "r") as f:
            return json.load(f)

    def save_instances(self, instances):
        with open(self.instances_file, "w") as f:
            json.dump(instances, f, indent=4)

    def load_analytics(self):
        with open(self.analytics_file, "r") as f:
            return json.load(f)

    def save_analytics(self, analytics):
        with open(self.analytics_file, "w") as f:
            json.dump(analytics, f, indent=4)