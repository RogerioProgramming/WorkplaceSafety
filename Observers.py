class Observer:
    def update(self, event_type, data):
        pass

class LoggerObserver(Observer):
    def update(self, event_type, data):
        print(f"[LOG] Evento '{event_type}' ocorreu com dados: {data}")

class ReportGeneratorObserver(Observer):
    def update(self, event_type, data):
        if event_type == "save_instances":
            print("[REPORT] Gerando relatório para novas instâncias...")
        elif event_type == "save_analytics":
            print("[REPORT] Gerando relatório para novos dados analíticos...")