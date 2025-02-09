import json

class JSONDataSource:
    def load_instances(self):
        with open('instances.json', 'r') as f:
            return json.load(f)

    def save_instances(self, instances):
        with open('instances.json', 'w') as f:
            json.dump(instances, f)

    def load_analytics(self):
        with open('analytics.json', 'r') as f:
            return json.load(f)

    def save_analytics(self, analytics):
        with open('analytics.json', 'w') as f:
            json.dump(analytics, f)