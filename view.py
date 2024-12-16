from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QTableWidget, QPushButton, QTableWidgetItem, QComboBox

class MRIDeviceView(QMainWindow):
    """Handles the GUI (View in MVC)."""
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MRI Manager")

        # Layout for the main window
        self.layout = QVBoxLayout()
        self.table = QTableWidget()
        self.table.setColumnCount(6)  # Number of columns for device data
        self.table.setHorizontalHeaderLabels(
            ["Vendor", "Power", "Version", "OS", "VNC Supported", "Comments"]
        )
        self.layout.addWidget(self.table)

        # Buttons for user actions
        self.load_button = QPushButton("Load")
        self.save_button = QPushButton("Save")
        self.add_button = QPushButton("Add Row")
        self.delete_button = QPushButton("Delete Row")

        # Adding buttons to the layout
        self.layout.addWidget(self.load_button)
        self.layout.addWidget(self.save_button)
        self.layout.addWidget(self.add_button)
        self.layout.addWidget(self.delete_button)

        # Setting the central widget
        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)

    def populate_table(self, devices):
        """Populates the table with data from the model."""
        self.table.setRowCount(len(devices))  # Set the number of rows
        for row, device in enumerate(devices):
            self.populate_row(row, device)

    def populate_row(self, row, device):
        """Populates a single row in the table with device data."""
        # Vendor as a dropdown
        vendor_combo = QComboBox()
        vendor_combo.addItems(["Siemens", "GE", "Philips"])
        vendor_combo.setCurrentText(device.vendor)
        self.table.setCellWidget(row, 0, vendor_combo)

        # Power as a dropdown
        power_combo = QComboBox()
        power_combo.addItems(["1.5T", "3.0T"])
        power_combo.setCurrentText(device.power)
        self.table.setCellWidget(row, 1, power_combo)

        # Free-text fields for other attributes
        self.table.setItem(row, 2, QTableWidgetItem(device.version))
        self.table.setItem(row, 3, QTableWidgetItem(device.os))

        # VNC Supported as a dropdown
        vnc_combo = QComboBox()
        vnc_combo.addItems(["True", "False"])
        vnc_combo.setCurrentText("True" if device.vnc_supported else "False")
        self.table.setCellWidget(row, 4, vnc_combo)

        # Free-text for comments
        self.table.setItem(row, 5, QTableWidgetItem(device.comments))
