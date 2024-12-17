import json
import pickle
from abc import ABC, abstractmethod

class FileHandler(ABC):
    """Abstract base class for file handlers."""

    @abstractmethod
    def load(self, filepath):
        """Load data from a file."""
        pass

    @abstractmethod
    def save(self, filepath, data):
        """Save data to a file."""
        pass


class JSONFileHandler(FileHandler):
    """Handles JSON file operations."""

    def load(self, filepath):
        """Loads data from a JSON file."""
        with open(filepath, "r") as file:
            return json.load(file)

    def save(self, filepath, data):
        """Saves data to a JSON file."""
        with open(filepath, "w") as file:
            json.dump(data, file, indent=4)


class BinaryFileHandler(FileHandler):
    """Handles Binary file operations."""

    def load(self, filepath):
        """Loads data from a Binary file."""
        with open(filepath, "rb") as file:
            return pickle.load(file) 
            
    def save(self, filepath, data):
        """Saves data to a Binary file."""
        with open(filepath, "wb") as file:
            pickle.dump(data, file)
