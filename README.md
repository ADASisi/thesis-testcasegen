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
  - **KLayout**: Open-source viewer and editor for GDSII files.
  - **Virtuoso**: Industry-standard platform for IC design.
  - **Caliber**: Tool used for verification and rule checks.

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
   pip install gdspy PyQt5
   ```
3. (Optional) Install `KLayout` for better visualization and handling of GDSII files:
   - [Download KLayout](https://www.klayout.de/downloads.html)

## 🚀 Quick Start
1. **Run the application**:
   ```bash
   python main.py
   ```
2. **Choose design rules** from the list or input your own custom parameters.
3. **Generate and preview** test structures directly in the GUI.
4. **Export** the structure for use in tools like KLayout, Virtuoso, or Caliber.
5. **Verify** the design using integrated verification routines or with third-party tools for thorough compliance checks.

## 🔍 Example Workflow
1. **Input Rules**: Choose rules for area, spacing, and overlap.
2. **Generate**: Click “Generate Structure” to create a visual representation.
3. **Export & Verify**: Save the structure and verify it using `Caliber`.

## 📸 Screenshots
_Showcase interactive previews, rule selection screens, and structure verification displays here._

## 🤝 Acknowledgments
This project was made possible through the guidance and support of my thesis advisor Petar Ivanov from GlobalFoundries.

## 📝 Author
Developed by Silvia Antova, combining passion for software and semiconductor design. For queries or collaboration opportunities, reach out at [your.email@example.com].

---

