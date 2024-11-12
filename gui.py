from PyQt5.QtWidgets import QApplication, QComboBox, QLabel, QVBoxLayout, QHBoxLayout, QWidget, QPushButton
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt
import sys

class ComboBoxExample(QWidget):
    def __init__(self):
        super().__init__()

        self.select_rule = QComboBox()
        self.select_rule.addItems(["Option 1", "Option 2", "Option 3"])

        self.label = QLabel("Selected: None")

        self.display_button = QPushButton("&Display")
        self.create_file_button = QPushButton("&Export rule as a file")

        self.select_rule.currentIndexChanged.connect(self.selection_changed)

        self.layout = QVBoxLayout()

        h_layout = QHBoxLayout()
        h_layout.addWidget(self.select_rule)
        h_layout.addWidget(self.display_button)
        h_layout.addWidget(self.create_file_button)

        layout = QVBoxLayout()
        layout.addLayout(h_layout)
        layout.addWidget(self.label)
        self.setLayout(layout)
        self.create_file_button.move(100, 50)

    def selection_changed(self):
        selected_text = self.select_rule.currentText()
        self.label.setText(f"Selected: {selected_text}")



app = QApplication(sys.argv)
window = ComboBoxExample()
window.show()
sys.exit(app.exec_())