from PyQt6.QtCore import QObject, pyqtSignal


class AbstractMeter:
    def channel(self) -> str:
        """Devuelve el nombre del canal."""
        raise NotImplementedError("channel() must be implemented in the subclass.")

    def range(self) -> int:
        """Devuelve el rango de medida (0->Auto, 1, 10, 100, etc)."""
        raise NotImplementedError("channel() must be implemented in the subclass.")

    def measure(self) -> float:
        """Realiza una medida y devuelve el valor."""
        raise NotImplementedError("channel() must be implemented in the subclass.")


class AbstractThermometer(AbstractMeter):
    def sensor(self) -> str:
        """Devuelve el nombre del sensor (THRMSTR, 4W-RTD, TC, )."""
        raise NotImplementedError("channel() must be implemented in the subclass.")

    def units(self) -> str:
        """Devuelve las unidades (C, F, or K)."""
        raise NotImplementedError("channel() must be implemented in the subclass.")


class AbstractVoltmeter(AbstractMeter):
    def voltage_type(self) -> str:
        """Devuelve el tipo de medida de voltage (DCV or ACV)."""
        raise NotImplementedError("channel() must be implemented in the subclass.")


class AbstractAmmeter(AbstractMeter):
    def current_type(self) -> str:
        """Devuelve el tipo de medida de corriente (DCI or ACI)."""
        raise NotImplementedError("channel() must be implemented in the subclass.")


class AbstractCurrentSource(AbstractMeter):
    def output_on(self, current):
        """Configura la corriente y activa la salida."""
        raise NotImplementedError("channel() must be implemented in the subclass.")

    def output_off(self):
        """Desactiva la salida."""
        raise NotImplementedError("channel() must be implemented in the subclass.")


class AbstractOven(AbstractMeter):
    def set_point(self, setpoint_number):
        """Devuelve el valor del set_point seleccionado en las unidades seleccionadas."""
        raise NotImplementedError("channel() must be implemented in the subclass.")

    def update_set_point(self, setpoint_number):
        """Actualiza el valor del setpoint seleccionado en las unidades seleccionadas."""
        raise NotImplementedError("channel() must be implemented in the subclass.")

    def units(self) -> str:
        """Devuelve las unidades (C, F, or K)."""
        raise NotImplementedError("channel() must be implemented in the subclass.")


class Delay(QObject):
    completed = pyqtSignal()

    def __init__(self):
        super().__init__()
        self._running = False
        self._completed = False

    def start(self):
        self._running = True
        self._completed = False

    def pause(self):
        self._running = False

    def stop(self):
        self._running = False
        self._completed = True

    def reset(self):
        self._running = False
        self._completed = False

    def emit_completed(self):
        if not self._completed:
            self._completed = True
            self._running = False
            self.completed.emit()
            self.reset()
