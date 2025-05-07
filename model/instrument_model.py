from instrumentation.keithley_2400 import Keithley2400

class InstrumentModel:
    def __init__(self):
        self.instrument = Keithley2400("GPIB0::24::INSTR")

    def apply_current(self, current):
        self.instrument.set_current(current)

    def get_voltage(self):
        return self.instrument.measure_voltage()