from PyQt5.QtWidgets import QApplication, QComboBox, QLabel, QVBoxLayout, QHBoxLayout, QWidget, QPushButton, QTextEdit
import sys
import get_rule


class ComboBoxExample(QWidget):
    def __init__(self):
        super().__init__()

        self.select_rule = QComboBox()

        self.select_rule.addItem("Please select a rule")
        self.select_rule.addItems(["50", "51", "52"])
        self.select_rule.setItemData(0, False)

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
        if selected_rule_name == "Please select a rule":
            self.label.setText("Selected: None")
        else:
            self.label.setText(f"Selected: {selected_rule_name}")

    def pressed_button_run_rule(self):
        selected_rule = self.select_rule.currentText()
        if selected_rule == "Please select a rule":
            self.result_display.setText("Please select a valid rule to display results.")
            return
        try:
            results = get_rule.rule_displaying(selected_rule)
            self.result_display.setText("\n".join(results[0]))
        except Exception as e:
            self.result_display.setText("No result found")

    def pressed_button_export_file(self):
        selected_rule_name = self.select_rule.currentText()
        if selected_rule_name == "Please select a rule":
            self.result_display.setText("Please select a valid rule to export.")
            return
        try:
            get_rule.export_file(selected_rule_name)
            self.result_display.setText(f"Rule {selected_rule_name} exported successfully.")
        except Exception as e:
            self.result_display.setText(f"Export failed: {str(e)}")


app = QApplication(sys.argv)
window = ComboBoxExample()
window.show()
sys.exit(app.exec_())
