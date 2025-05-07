import math
from model.interfaces import Delay
from PyQt6.QtCore import QTimer

class StdDevDelay(Delay):
    def __init__(self, window_size, threshold):
        super().__init__()
        self.window_size = window_size
        self.threshold = threshold
        self.values = []

    def add_value(self, value):
        if not self._running:
            return
        self.values.append(value)
        if len(self.values) > self.window_size:
            self.values.pop(0)
        self._check_completion()

    def _calculate_stddev(self):
        n = len(self.values)
        if n == 0:
            return float('inf')
        mean = sum(self.values) / n
        variance = sum((x - mean) ** 2 for x in self.values) / n
        return math.sqrt(variance)

    def _check_completion(self):
        if len(self.values) < self.window_size:
            return
        stddev = self._calculate_stddev()
        if stddev <= self.threshold:
            self.emit_completed()

    def reset(self):
        super().reset()
        self.values = []


class MinDelay(Delay):
    def __init__(self, min_value, window_size):
        super().__init__()
        self.min_value = min_value
        self.window_size = window_size
        self.values = []

    def add_value(self, value):
        if not self._running:
            return
        self.values.append(value)
        if len(self.values) > self.window_size:
            self.values.pop(0)
        self._check_completion()

    def _check_completion(self):
        if len(self.values) < self.window_size:
            return
        if all(v >= self.min_value for v in self.values):
            self.emit_completed()

    def reset(self):
        super().reset()
        self.values = []


class TimeDelay(Delay):
    def __init__(self, duration_ms, callback=None):
        """
        :param duration_ms: Tiempo en milisegundos
        :param callback: Función Python que se llamará al completar el delay
        """
        super().__init__()
        self.duration_ms = duration_ms
        self.callback = callback
        self._timer = QTimer()
        self._timer.setSingleShot(True)
        self._timer.timeout.connect(self._on_timeout)

    def start(self):
        if not self._running:
            super().start()
            self._timer.start(self.duration_ms)

    def pause(self):
        if self._running:
            self._timer.stop()
            self._running = False

    def stop(self):
        self._timer.stop()
        super().stop()

    def reset(self):
        self._timer.stop()
        super().reset()

    def _on_timeout(self):
        if self._running:
            if self.callback:
                self.callback()
            self.emit_completed()