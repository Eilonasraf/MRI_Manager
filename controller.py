from PyQt5.QtWidgets import QFileDialog, QMessageBox
from model import MRIDevice
from file_handlers import JSONFileHandler, BinaryFileHandler  # Import file handlers

class MRIDeviceController:
    """Connects the View and Model (Controller in MVC)."""
    def __init__(self, model, view):
        self.model = model # MRIDeviceManager
        self.view = view  # MRIDeviceView

        # Connect View buttons to their respective functions
        self.view.load_button.clicked.connect(self.load_data)
        self.view.save_button.clicked.connect(self.save_data)
        self.view.add_button.clicked.connect(self.add_device)
        self.view.delete_button.clicked.connect(self.delete_device)

    def load_data(self):
        """Loads data from a file into the model and updates the view."""
        filepath, _ = QFileDialog.getOpenFileName(self.view, "Load File", "", "All Files (*.*)")
        if filepath:
            try:
                self.model.load_from_file(filepath)  # Dynamically loads using the file handler
                self.view.populate_table(self.model.devices)  # Update the view with the loaded data
            except Exception as e:
                QMessageBox.critical(self.view, "Error", f"Failed to load file: {str(e)}")

    def save_data(self):
        """Saves data from the model into a file."""
        # Ask the user to choose JSON or Binary
        file_type, ok = QFileDialog.getSaveFileName(
            self.view,
            "Save File As",
            "data", 
            "JSON Files (*.json);;Binary Files (*.bin)"
        )

        if file_type and ok:
            try:
                # Automatically set the handler based on file extension
                if file_type.endswith(".json"):
                    handler = JSONFileHandler()
                    filepath = file_type
                elif file_type.endswith(".bin"):
                    handler = BinaryFileHandler()
                    filepath = file_type
                else:
                    QMessageBox.warning(self.view, "Invalid", "Unsupported file type!")
                    return

                # Assign the new handler temporarily
                self.model.file_handler = handler
                
                # Extract devices from the table and save
                self.model.devices = self.get_devices_from_table()
                self.model.save_to_file(filepath)
                QMessageBox.information(self.view, "Success", f"File saved successfully as {filepath}!")
            except Exception as e:
                QMessageBox.critical(self.view, "Error", f"Failed to save file: {str(e)}")

    def get_devices_from_table(self):
        """Extracts device data from the table into a list of MRIDevice objects."""
        devices = []
        for row in range(self.view.table.rowCount()):
            vendor = self.view.table.cellWidget(row, 0).currentText()
            power = self.view.table.cellWidget(row, 1).currentText()
            version = self.view.table.item(row, 2).text()
            os = self.view.table.item(row, 3).text()
            vnc_supported = self.view.table.cellWidget(row, 4).currentText() == "True"
            comments = self.view.table.item(row, 5).text()
            devices.append(MRIDevice(vendor, power, version, os, vnc_supported, comments))
        return devices

    def add_device(self):
        """Adds a new default device to the model and updates the view."""
        new_device = MRIDevice("Siemens", "1.5T", "Default Version", "Default OS", False, "")
        self.model.add_device(new_device)
        self.view.populate_table(self.model.devices)

    def delete_device(self):
        """Deletes the selected device from the model and updates the view."""
        selected_row = self.view.table.currentRow()
        if selected_row >= 0:
            self.model.remove_device(selected_row)
            self.view.populate_table(self.model.devices)
        else:
            QMessageBox.warning(self.view, "No Selection", "Please select a row to delete.")
