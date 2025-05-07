from PySide6.QtWidgets import QMainWindow, QPushButton, QDoubleSpinBox, QLabel, QProgressBar
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODeviceBase
from viewmodel.instrument_viewmodel import InstrumentViewModel

class MainWindow(QMainWindow):


    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        ui_file = QFile("view/main_window.ui")
        r = ui_file.open(QIODeviceBase.OpenModeFlag.ReadOnly)
        self.ui = loader.load(ui_file, self)
        ui_file.close()

        self.setCentralWidget(self.ui)

        self.viewmodel = InstrumentViewModel()
        self.viewmodel.voltageChanged.connect(self.update_voltage_display)
        self.viewmodel.measurementStarted.connect(self.on_measurement_started)

        self.ui.pushButton.clicked.connect(self.send_current)

        self.ui.show()

    def send_current(self):
        value = self.ui.doubleSpinBox.value()
        self.viewmodel.set_current(value)

    def update_voltage_display(self, voltage):
        self.ui.label.setText(f"Voltage: {voltage:.3f} V")
        self.ui.progressBar.setVisible(False)

    def on_measurement_started(self):
        self.ui.progressBar.setVisible(True)
        self.ui.progressBar.setRange(0, 0)  # modo indeterminado