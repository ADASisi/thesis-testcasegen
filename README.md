# Software Development for Creating Test Structures for Physical Design Rules

## 🌟 Overview
Welcome to the **Test Structure Generator**—an innovative tool designed for the efficient creation, visualization, and verification of test structures based on physical design rules. This software streamlines the workflow for engineers and researchers in the semiconductor industry and academia, simplifying complex processes with a touch of modern technology.

## 🎯 Features
- **Rule Selection**: Input and choose from a list of physical design rules.
- **Test Structure Generation**: Create comprehensive test structures that adhere to various physical rules, including:
  - **Area constraints**
  - **Width specifications**
  - **Spacing requirements**
  - **Enclosure checks**
  - **Overlap evaluations**
- **File Export**: Save generated test structures into standard file formats for further use.
- **Visualization**: Interactive preview of generated test structures with the ability to adjust and fine-tune.
- **Verification**: Built-in verification processes to ensure the compliance of structures with specified design rules.

## 🛠 Tech Stack
- **Python Libraries**:
  - `Gdspy`: Core library for creating and manipulating GDSII files.
  - `PyQt5`: Utilized for building an intuitive and interactive graphical user interface.
- **Industry Tools**:
  - **Caliber**: Tool used for verification and rule checks.
  - **KLayout**: Open-source viewer and editor for GDSII files.

## 💻 Installation Guide
### Prerequisites
Ensure Python is installed on your system. Python 3.6 or later is recommended.

### Steps:
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/yourproject.git
   cd yourproject
   ```
2. Install the required libraries:
   ```bash
    pip install -r requirements.txt
   ```
3. (Optional) Install `KLayout` for better visualization and handling of GDSII files:
   - [Download KLayout](https://www.klayout.de/downloads.html)

## 📂 `requirements.txt`
Ensure your repository contains a requirements.txt file with the following content:
```bash
   PyQt5~=5.15.11
   gdspy~=1.6.12
   ```


## 🚀 Quick Start
1. **Run the application**:
   ```bash
   python qui.py
   ```
2. **Choose design rules** from the list or input your own custom parameters.
3. **Generate and preview** test structures directly in the GUI.
4. **Export** the structure in GDSII format.
5. **Verify** the design using integrated verification routines or with third-party tools for thorough compliance checks.

## 🔍 Example Workflow
1. **Input Rules**: Choose rules for area, spacing, and overlap.
2. **Generate**: Click “Generate Structure” to create a visual representation.
3. **Export & Verify**: Save the structure and verify it using `Caliber`.

## 📸 Screenshots
![Screenshot 2025-01-27 004353](https://github.com/user-attachments/assets/6fbbb80c-4d87-4126-b1a6-ba02277a84b9)
![Screenshot 2025-01-27 005218](https://github.com/user-attachments/assets/4c821e39-fff9-4231-9127-1186f55a75d2)
![Screenshot 2025-01-27 013106](https://github.com/user-attachments/assets/9b471168-7f04-4f1e-8ae9-9643ded83fdf)
![image](https://github.com/user-attachments/assets/00966ade-660f-4844-a38a-214170b887f5)
![MIN_T3_OVERLAP_OF_NW_TEST_no_markers](https://github.com/user-attachments/assets/f2993923-85c9-424d-8fd4-6bd42aa94659)
<img width="482" alt="PC_MIN_AREA_TEST_with_markers" src="https://github.com/user-attachments/assets/2afa617e-4aa8-4ab3-98b1-a078f14f2bca" />

## 🤝 Acknowledgments
This project was made possible through the guidance and support of my thesis advisor Petar Ivanov from GlobalFoundries.

## 📝 Author
Developed by Silvia Antova.

---

