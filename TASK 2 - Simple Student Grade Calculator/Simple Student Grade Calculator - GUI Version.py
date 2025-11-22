import csv
import os
import sys
from datetime import datetime
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIntValidator, QFont
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QSpinBox,
    QPushButton,
    QGridLayout,
    QMessageBox,
    QFileDialog,
    QHBoxLayout,
    QVBoxLayout,
    QTableWidget,
    QTableWidgetItem,
    QCheckBox,
)


# ------------------ Calculation functions ------------------

def calculate_total(m1, m2, m3):
    return m1 + m2 + m3


def calculate_average(total, subjects=3):
    if subjects <= 0:
        return 0
    return total / subjects


def calculate_grade(avg):
    """Return grade A/B/C/D/F based on average."""
    if avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 50:
        return "D"
    else:
        return "F"


# ------------------ Main Window ------------------

class GradeCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student Grade Calculator — PyQt5")
        self.setMinimumSize(700, 460)
        self._init_ui()
        self.csv_headers_written = False

    def _init_ui(self):
        # Fonts
        label_font = QFont("Segoe UI", 10)
        big_font = QFont("Segoe UI", 11, QFont.Weight.Bold)

        # Inputs
        self.name_label = QLabel("Student Name:")
        self.name_label.setFont(label_font)
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Enter full name")
        self.name_input.setFont(label_font)

        self.m1_label = QLabel("Subject 1 (0-100):")
        self.m1_label.setFont(label_font)
        self.m1_input = QSpinBox()
        self.m1_input.setRange(0, 100)

        self.m2_label = QLabel("Subject 2 (0-100):")
        self.m2_label.setFont(label_font)
        self.m2_input = QSpinBox()
        self.m2_input.setRange(0, 100)

        self.m3_label = QLabel("Subject 3 (0-100):")
        self.m3_label.setFont(label_font)
        self.m3_input = QSpinBox()
        self.m3_input.setRange(0, 100)

        # Buttons
        self.calc_button = QPushButton("Calculate")
        self.calc_button.clicked.connect(self.on_calculate)
        self.calc_button.setFont(big_font)

        self.reset_button = QPushButton("Reset")
        self.reset_button.clicked.connect(self.on_reset)

        self.save_button = QPushButton("Save Result")
        self.save_button.clicked.connect(self.on_save)

        # Dark mode toggle
        self.dark_checkbox = QCheckBox("Dark mode")
        self.dark_checkbox.setChecked(True)
        self.dark_checkbox.stateChanged.connect(self.toggle_theme)

        # Output labels
        self.total_label = QLabel("Total: —")
        self.average_label = QLabel("Average: —")
        self.grade_label = QLabel("Grade: —")
        for lbl in (self.total_label, self.average_label, self.grade_label):
            lbl.setFont(big_font)

        # Results layout
        result_layout = QVBoxLayout()
        result_layout.addWidget(self.total_label)
        result_layout.addWidget(self.average_label)
        result_layout.addWidget(self.grade_label)
        result_layout.addStretch(1)

        # Table to show saved results in current session
        self.table = QTableWidget(0, 6)
        self.table.setHorizontalHeaderLabels([
            "Timestamp",
            "Name",
            "S1",
            "S2",
            "S3",
            "Grade",
        ])
        self.table.horizontalHeader().setStretchLastSection(True)

        # Layout arrangement
        grid = QGridLayout()
        grid.addWidget(self.name_label, 0, 0)
        grid.addWidget(self.name_input, 0, 1, 1, 3)

        grid.addWidget(self.m1_label, 1, 0)
        grid.addWidget(self.m1_input, 1, 1)
        grid.addWidget(self.m2_label, 1, 2)
        grid.addWidget(self.m2_input, 1, 3)

        grid.addWidget(self.m3_label, 2, 0)
        grid.addWidget(self.m3_input, 2, 1)

        # Buttons row
        buttons_h = QHBoxLayout()
        buttons_h.addWidget(self.calc_button)
        buttons_h.addWidget(self.reset_button)
        buttons_h.addWidget(self.save_button)
        buttons_h.addStretch(1)
        buttons_h.addWidget(self.dark_checkbox)

        left_v = QVBoxLayout()
        left_v.addLayout(grid)
        left_v.addLayout(buttons_h)
        left_v.addLayout(result_layout)

        main_h = QHBoxLayout()
        main_h.addLayout(left_v, 2)
        main_h.addWidget(self.table, 3)

        self.setLayout(main_h)

        # Start with dark theme
        self.apply_dark_theme()

    # ------------------ UI Interaction ------------------

    def on_calculate(self):
        name = self.name_input.text().strip()
        if not name:
            QMessageBox.warning(self, "Input Error", "Please enter the student's name.")
            return

        m1 = int(self.m1_input.value())
        m2 = int(self.m2_input.value())
        m3 = int(self.m3_input.value())

        total = calculate_total(m1, m2, m3)
        average = calculate_average(total, 3)
        grade = calculate_grade(average)

        self.display_results(total, average, grade)

    def display_results(self, total, average, grade):
        self.total_label.setText(f"Total: {total}")
        self.average_label.setText(f"Average: {average:.2f}")
        self.grade_label.setText(f"Grade: {grade}")
        # Color coding
        color = self.grade_color(grade)
        self.grade_label.setStyleSheet(f"color: {color}; font-weight: bold;")

    def grade_color(self, grade):
        return {
            "A": "#00c853",  # green
            "B": "#4caf50",
            "C": "#ffb300",
            "D": "#ff6d00",
            "F": "#d50000",
        }.get(grade, "#ffffff")

    def on_reset(self):
        self.name_input.clear()
        self.m1_input.setValue(0)
        self.m2_input.setValue(0)
        self.m3_input.setValue(0)
        self.total_label.setText("Total: —")
        self.average_label.setText("Average: —")
        self.grade_label.setText("Grade: —")
        self.grade_label.setStyleSheet("")

    def on_save(self):
        # Ensure we have calculated at least once
        if self.total_label.text().endswith("—"):
            QMessageBox.information(self, "Nothing to save", "Please calculate the grade before saving.")
            return

        # Gather data
        name = self.name_input.text().strip()
        m1 = int(self.m1_input.value())
        m2 = int(self.m2_input.value())
        m3 = int(self.m3_input.value())
        total_text = self.total_label.text().replace("Total:", "").strip()
        avg_text = self.average_label.text().replace("Average:", "").strip()
        grade_text = self.grade_label.text().replace("Grade:", "").strip()

        # Let user choose where to save (CSV)
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "Save result as CSV",
            f"student_result_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
            "CSV Files (*.csv);;All Files (*)",
            options=options,
        )
        if not file_path:
            return

        # Write CSV (append if file exists)
        write_header = not os.path.exists(file_path)
        try:
            with open(file_path, "a", newline="", encoding="utf-8") as csvfile:
                writer = csv.writer(csvfile)
                if write_header:
                    writer.writerow([
                        "timestamp",
                        "name",
                        "subject1",
                        "subject2",
                        "subject3",
                        "total",
                        "average",
                        "grade",
                    ])
                writer.writerow([
                    datetime.now().isoformat(),
                    name,
                    m1,
                    m2,
                    m3,
                    total_text,
                    avg_text,
                    grade_text,
                ])
        except Exception as e:
            QMessageBox.critical(self, "Save Error", f"Failed to save file.\n{e}")
            return

        # Add to session table
        row = self.table.rowCount()
        self.table.insertRow(row)
        self.table.setItem(row, 0, QTableWidgetItem(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        self.table.setItem(row, 1, QTableWidgetItem(name))
        self.table.setItem(row, 2, QTableWidgetItem(str(m1)))
        self.table.setItem(row, 3, QTableWidgetItem(str(m2)))
        self.table.setItem(row, 4, QTableWidgetItem(str(m3)))
        self.table.setItem(row, 5, QTableWidgetItem(grade_text))

        QMessageBox.information(self, "Saved", "Result saved to CSV successfully.")

    # ------------------ Theme ------------------

    def apply_dark_theme(self):
        dark = """
        QWidget { background-color: #121212; color: #e0e0e0; }
        QLineEdit, QSpinBox, QTableWidget { background-color: #1e1e1e; color: #e0e0e0; }
        QPushButton { background-color: #2b2b2b; border: 1px solid #333; padding: 6px; }
        QPushButton:hover { border: 1px solid #555; }
        QHeaderView::section { background-color: #2b2b2b; }
        QTableWidget { gridline-color: #333; }
        QToolTip { color: #000; background: #e0e0e0; }
        """
        self.setStyleSheet(dark)

    def apply_light_theme(self):
        self.setStyleSheet("")

    def toggle_theme(self, state):
        if state == Qt.Checked:
            self.apply_dark_theme()
        else:
            self.apply_light_theme()


# ------------------ Run ------------------

def main():
    app = QApplication(sys.argv)
    window = GradeCalculator()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
