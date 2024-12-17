## **MRI Device Data Management Application**

A Python-based application for managing MRI device data, developed as part of the staff admission process. The application allows users to:
- Load MRI device data from a JSON or Binary file.
- Display the data in a user-friendly table.
- Add, edit, or remove device data.
- Save updated data back to a file.

This project implements the **Model-View-Controller (MVC)** design pattern for better modularity and scalability.

---

## **Features**

1. **Load Data**: 
   - Load MRI device information from a JSON or Binary file.
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
   - Save updated data back into a JSON or Binary file for future use.

---

## **Installation**

1. Install Python 3.6 or higher.
2. Install the required dependencies:
   ```bash
   pip install PyQt5

## **Usage**

## *Run the Application*
1. Clone the repository or download the project files.
   ```bash
   git clone https://github.com/your-username/MRI_Manager.git
   cd MRI_Manager
2. Navigate to the project directory and run the following command
   ```bash
   python main.py

## **Application Workflow**
1. Load Data:

   - Click the "Load" button to select a JSON or Binary file containing MRI data.
   - File Options: Choose between .json or .bin format.
   ### Example JSON Format:
   Here’s a JSON file (`data.json`):
   
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
   - Modify dropdown fields directly in the table.
   - Free-text fields: Double-click on Version, OS, and Comments to edit them.
3. Add Data:
   - Click the "Add Row" button to create a new row with default values.
4. Delete Data:
   - Select a row and click the "Delete Row" button to remove it.
5. Save Data:
   - Click "Save" to export the updated data:
      - JSON format: Creates a .json file.
      - Binary format: Creates a .bin file (using pickle for serialization)

## **Project Design**
This project follows the Model-View-Controller (MVC) design pattern and leverages object-oriented programming (OOP) principles:

1. Model (model.py):
      - MRIDevice: Represents individual MRI devices with properties like vendor, power, and version.
      - MRIDeviceManager: Manages a collection of devices and handles file operations (loading/saving) dynamically via 
        file_handler.

2. File Handlers (file_handler.py):
      - JSONFileHandler: Handles saving/loading data in JSON format.
      - BinaryFileHandler: Handles saving/loading data in binary format (using pickle).

3. View (view.py):
    Uses PyQt5 to build the GUI:
      - Displays data in a table.
      - Includes buttons for user actions like Load, Save, Add, and Delete.
        
4. Controller (controller.py):
    - Processes user actions (e.g., Load, Save, Add, Delete) and updates the Model and View accordingly.

## ** Example File Support **

    - JSON File: Standard JSON format for readability and text-based editing.
    - Binary File: Optimized storage using pickle for faster read/write operations.

## **License**

This project is licensed under the MIT License. See the LICENSE file for details.

