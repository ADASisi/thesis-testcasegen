from PyQt5.QtWidgets import QApplication, QComboBox, QLabel, QVBoxLayout, QHBoxLayout, QWidget, QPushButton, QTextEdit, QFileDialog
from PyQt5.QtCore import Qt
import sys
import shutil
import get_rule

class ComboBoxExample(QWidget):
    def __init__(self):
        super().__init__()

        self.select_rule = QComboBox()
        self.select_rule.addItems(["50", "51", "52"])

        self.label = QLabel("Selected: None")
        self.result_display = QTextEdit()
        self.result_display.setReadOnly(True)

        self.display_button = QPushButton("&Display")
        self.create_file_button = QPushButton("&Export rule as a file")

        self.select_rule.currentIndexChanged.connect(self.selection_changed)
        self.display_button.clicked.connect(self.pressed_button_run_rule)
        self.create_file_button.clicked.connect(self.pressed_button_export_file)

        h_layout = QHBoxLayout()
        h_layout.addWidget(self.select_rule)
        h_layout.addWidget(self.display_button)
        h_layout.addWidget(self.create_file_button)

        layout = QVBoxLayout()
        layout.addLayout(h_layout)
        layout.addWidget(self.label)
        layout.addWidget(self.result_display)

        self.setLayout(layout)

    def selection_changed(self):
        selected_rule_name = self.select_rule.currentText()
        self.label.setText(f"Selected: {selected_rule_name}")

    def pressed_button_run_rule(self):
        selected_rule = self.select_rule.currentText()
        results = get_rule.rule_displaying(selected_rule)
        if results:
            self.result_display.setText("\n".join(results[0]))
        else:
            self.result_display.setText("No results found.")

    def pressed_button_export_file(self):
        selected_rule_name = self.select_rule.currentText()
        try:
            get_rule.export_file(selected_rule_name)
            self.result_display.setText(f"Rule {selected_rule_name} exported successfully.")
        except Exception as e:
            self.result_display.setText(f"Export failed: {str(e)}")



app = QApplication(sys.argv)
window = ComboBoxExample()
window.show()
sys.exit(app.exec_())
