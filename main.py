import sys
from PyQt5.QtWidgets import QApplication, QFileDialog, QMessageBox
from model import MRIDeviceManager
from file_handlers import JSONFileHandler, BinaryFileHandler
from view import MRIDeviceView
from controller import MRIDeviceController

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Ask the user to choose a file type
    file_type = input("Choose file type (json/binary): ").strip().lower()
    
    # Initialize the appropriate file handler
    if file_type == "json":
        file_handler = JSONFileHandler()
    elif file_type == "binary":
        file_handler = BinaryFileHandler()
    else:
        print("Invalid file type! Please choose 'json' or 'binary'. Exiting...")
        sys.exit(1)

    # Pass the file_handler to MRIDeviceManager
    model = MRIDeviceManager(file_handler)
    
    # Instantiate view and controller
    view = MRIDeviceView()
    controller = MRIDeviceController(model, view)

    # Show the GUI
    view.show()

    # Start the application loop
    sys.exit(app.exec_())
