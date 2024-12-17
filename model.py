import json

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
        data = self.file_handler.load(filepath)  # Use dynamic file handler

        # Check if data is already a list of MRIDevice objects (Binary)
        if isinstance(data, list) and all(isinstance(item, MRIDevice) for item in data):
            self.devices = data  # Directly assign for Binary files
        else:
            # Convert dictionaries to MRIDevice objects (JSON)
            self.devices = [MRIDevice.from_dict(item) for item in data]

    def save_to_file(self, filepath):
        """Saves devices using the specified file handler."""
        data = [device.to_dict() for device in self.devices]
        self.file_handler.save(filepath, data)
