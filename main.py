import sys
from PyQt5.QtWidgets import QApplication
from model import MRIDeviceManager
from view import MRIDeviceView
from controller import MRIDeviceController

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Instantiate MVC components
    model = MRIDeviceManager()
    view = MRIDeviceView()
    controller = MRIDeviceController(model, view)

    # Show the GUI
    view.show()

    # Start the application loop
    sys.exit(app.exec_())
