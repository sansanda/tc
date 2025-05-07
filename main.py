from PySide6.QtWidgets import QApplication

from model.Delays import TimeDelay
from view.main_window import MainWindow
import sys

# Only needed for access to command line arguments
import sys

# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.
# If you know you won't use command line arguments QApplication([]) works too.
app = QApplication(sys.argv)


# Create a Main window, which will be our window.
# window = MainWindow()
# window.show()  # IMPORTANT!!!!! Windows are hidden by default.

def on_time_done():
    print("Callback ejecutado.")


def on_time_signal():
    print("Señal Qt emitida.")
    app.quit()


time_delay = TimeDelay(duration_ms=10000, callback=on_time_done)
time_delay.completed.connect(on_time_signal)
time_delay.start()

# Start the event loop.
sys.exit(app.exec())

# Your application won't reach here until you exit and the event
# loop has stopped.
