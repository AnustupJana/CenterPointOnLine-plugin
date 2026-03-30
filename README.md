# Center Point on Line QGIS Plugin

![Diagram of the System](https://github.com/AnustupJana/CenterPointOnLine-plugin/blob/main/icon.png?raw=true)

## Overview
The **Center Point on Line** plugin for QGIS allows users to generate a center point along a line feature using a simple and efficient workflow. The plugin calculates the midpoint of each line feature and creates a corresponding point layer.

This tool is useful for:
- Road center analysis
- Utility network mapping
- Linear infrastructure planning
- GIS data preprocessing

---

## Features

### ✔ Automatic Geometry Handling
- Fixes invalid geometries before processing

### ✔ CRS Support
- Reprojects data to a selected CRS before calculation

### ✔ Accurate Center Point Calculation
- Uses geometry expression to calculate midpoint of line

### ✔ Processing Toolbox Integration
- Available inside QGIS Processing Toolbox

### ✔ One-Click Execution
- Run directly from plugin toolbar icon

---

## Installation

### 🔹 From ZIP File
1. Download the plugin ZIP file
2. Open QGIS
3. Go to: Plugins → Manage and Install Plugins → Install from ZIP
4. Select ZIP file → Click **Install Plugin**

---

### 🔹 Manual Installation
1. Download or clone repository
2. Copy plugin folder: CenterPointOnLine
3. Paste into:

**Windows**

C:\Users<YourUsername>\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins\


4. Restart QGIS

---

## Usage

### Step 1: Load Data
- Add a **Line layer** to QGIS

---

### Step 2: Run Plugin
- Click plugin icon in toolbar  
OR  
- Go to: Plugins → Center Point on Line

---

### Step 3: Tool Opens
- Processing dialog will open

---

### Step 4: Input Parameters
- Select Line layer
- Choose CRS (optional)
- Select output location

---

### Step 5: Run
- Click **Run**
- Output point layer will be created

---

## Output

- A **Point layer**
- Each point represents **center point of line**

---

## Requirements

- QGIS Version: **3.0 or higher**
- Input: Line vector layer

---

## Troubleshooting

### ❌ Tool not opening
- Restart QGIS
- Reinstall plugin

### ❌ No output
- Ensure input layer is Line type
- Check CRS compatibility

### ❌ Plugin not visible
- Verify plugin folder structure
- Ensure all files exist:
- `center_point_on_line.py`
- `metadata.txt`
- `__init__.py`
- `icon.png`

---

## Contributing

- Fork repository
- Submit pull requests
- Report issues via GitHub

---

## License

This plugin is licensed under the **GNU General Public License v2.0 or later**

---

## Author

**Name:** Anustup Jana  
**Email:** anustupjana21@gmail.com  

© 2026 Anustup Jana
