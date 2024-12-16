A Python-based application for managing MRI device data, developed as part of the staff admission process. The application allows users to:
- Load MRI device data from a file.
- Display the data in a user-friendly table.
- Add, edit, or remove device data.
- Save updated data back to a file.

This project implements the **Model-View-Controller (MVC)** design pattern for better modularity and scalability.

---

## **Features**

1. **Load Data**: 
   - Load MRI device information from a JSON file.
2. **Editable Fields**: 
   - `Vendor` and `Power` fields are dropdowns with fixed options:
     - Vendor: Siemens, GE, Philips.
     - Power: 1.5T, 3.0T.
   - `Version`, `OS`, and `Comments` are editable free-text fields.
3. **Add New Devices**:
   - Add new rows with default values.
4. **Delete Devices**:
   - Remove rows with the click of a button.
5. **Save Data**:
   - Save updated data back into a JSON file for future use.

---

## **Installation**

1. Install Python 3.6 or higher.
2. Install the required dependencies:
   ```bash
   pip install PyQt5

## **Usage**

Run the Application
1. Clone the repository or download the project files.
2. Navigate to the project directory and run the following command
   ```bash
   python main.py

## **Application Workflow**
1. Load Data:

   Click the "Load" button to select a JSON file containing MRI data.
   ### Example JSON Format:
   Here’s a JSON file (`example_data.json`) for testing:
   
   ```json
   [
       {
           "vendor": "GE",
           "power": "1.5T",
           "version": "DV25.0",
           "os": "RedHAT",
           "vnc_supported": true,
           "comments": ""
       },
       {
           "vendor": "Siemens",
           "power": "3.0T",
           "version": "Skyra",
           "os": "Windows10",
           "vnc_supported": false,
           "comments": "New installation"
       }
   ]
   ```

2. Edit Data:
   Modify dropdown fields directly in the table.
   Double-click on free-text fields (e.g., Version, OS, Comments) to edit them.
3. Add Data:
   Click "Add Row" to create a new row with default values.
4. Delete Data:
   Select a row and click "Delete Row" to remove it.
5. Save Data:
   Click "Save" to export the updated data to a JSON file.

## **Project Design**
This project follows the Model-View-Controller (MVC) design pattern and leverages object-oriented programming (OOP) principles:

1. Model (model.py):
    - MRIDevice: Represents individual MRI devices with properties like vendor, power, and version.
    - MRIDeviceManager: Manages a collection of devices and handles data loading and saving.

2. View (view.py):
    - Uses PyQt5 to build the GUI, including a table for displaying devices and controls for user actions.
3. Controller (controller.py):
    - Bridges the Model and View, processing user actions and updating data accordingly.

## **License**

This project is licensed under the MIT License. See the LICENSE file for details.

