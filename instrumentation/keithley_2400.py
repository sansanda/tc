class Keithley2400:
    def __init__(self, resource):
        self.resource = resource  # Simulado o conectado vía PyVISA

    def set_current(self, value):
        print(f"[Keithley2400] Setting current to {value} A")

    def measure_voltage(self):
        print("[Keithley2400] Measuring voltage")
        return 3.1415