from PySide6.QtCore import QObject, Signal, Slot, QThread
from model.instrument_model import InstrumentModel

class MeasurementWorker(QObject):
    finished = Signal(float)
    started = Signal()

    def __init__(self, model, current):
        super().__init__()
        self.model = model
        self.current = current

    def run(self):
        self.started.emit()
        self.model.apply_current(self.current)
        voltage = self.model.get_voltage()
        self.finished.emit(voltage)

class InstrumentViewModel(QObject):
    voltageChanged = Signal(float)
    measurementStarted = Signal()

    def __init__(self):
        super().__init__()
        self.model = InstrumentModel()

    @Slot(float)
    def set_current(self, current):
        self.thread = QThread()
        self.worker = MeasurementWorker(self.model, current)
        self.worker.moveToThread(self.thread)

        self.thread.started.connect(self.worker.run)
        self.worker.started.connect(self.measurementStarted)
        self.worker.finished.connect(self.voltageChanged.emit)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)

        self.thread.start()