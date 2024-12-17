import json
from file_handlers import JSONFileHandler, BinaryFileHandler  # Import file handlers

class MRIDevice:
    """Represents a single MRI device (Model in MVC)."""
    def __init__(self, vendor, power, version, os, vnc_supported, comments):
        self.vendor = vendor
        self.power = power
        self.version = version
        self.os = os
        self.vnc_supported = vnc_supported
        self.comments = comments

    def to_dict(self):
        """Converts the device to a dictionary for JSON serialization."""
        return {
            "vendor": self.vendor,
            "power": self.power,
            "version": self.version,
            "os": self.os,
            "vnc_supported": self.vnc_supported,
            "comments": self.comments,
        }

    @staticmethod
    def from_dict(data):
        """Creates an MRIDevice object from a dictionary."""
        return MRIDevice(
            data["vendor"],
            data["power"],
            data["version"],
            data["os"],
            data["vnc_supported"],
            data["comments"]
        )

class MRIDeviceManager:
    """Manages a list of MRI devices."""
    def __init__(self, file_handler):
        self.devices = []  # Internal storage for devices
        self.file_handler = file_handler  # File handler (JSON/Binary)

    def add_device(self, device):
        """Adds a new device to the list."""
        self.devices.append(device)

    def remove_device(self, index):
        """Removes a device by index."""
        if 0 <= index < len(self.devices):
            self.devices.pop(index)

    def update_device(self, index, updated_device):
        """Updates an existing device at a given index."""
        if 0 <= index < len(self.devices):
            self.devices[index] = updated_device

    def load_from_file(self, filepath):
        """Loads devices using the specified file handler."""
        try:
            data = self.file_handler.load(filepath)

            if isinstance(data, list):
                # Check if data is already MRIDevice objects (Binary) or dictionaries (JSON)
                if all(isinstance(item, MRIDevice) for item in data):
                    self.devices = data  # Already MRIDevice objects (Binary file)
                else:
                    # Convert JSON dictionaries to MRIDevice objects
                    self.devices = [MRIDevice.from_dict(item) for item in data]
            else:
                raise ValueError("Invalid file format.")
        except Exception as e:
            raise ValueError(f"Failed to load data: {e}")

    def save_to_file(self, filepath):
        """Saves devices using the specified file handler."""
        if isinstance(self.file_handler, BinaryFileHandler):
            # Save the list of MRIDevice objects directly for Binary files
            self.file_handler.save(filepath, self.devices)
            
        elif isinstance(self.file_handler, JSONFileHandler):
            # Convert MRIDevice objects to dictionaries for JSON files
            json_data = [device.to_dict() for device in self.devices]
            self.file_handler.save(filepath, json_data)
            
        else:
            raise ValueError("Unsupported file handler.")




