from PyQt5.QtWidgets import QApplication, QComboBox, QLabel, QVBoxLayout, QHBoxLayout, QWidget, QPushButton
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt
import sys
import get_rule

class ComboBoxExample(QWidget):
    def __init__(self):
        super().__init__()

        self.select_rule = QComboBox()
        self.select_rule.addItems(["50", "51", "52"])

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
        self.display_button.clicked.connect(self.pressed_button_run_rule)
        self.create_file_button.move(100, 50)

    def selection_changed(self):
        selected_rule_name = self.select_rule.currentText()
        self.label.setText(f"Selected: {selected_rule_name}")

    def pressed_button_run_rule(self):
        selected_rule = self.select_rule.currentText()
        get_rule.get_rule_name(selected_rule)


app = QApplication(sys.argv)
window = ComboBoxExample()
window.show()
sys.exit(app.exec_())