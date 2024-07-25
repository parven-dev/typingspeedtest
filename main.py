import sys
from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QTextEdit, QPushButton, \
    QVBoxLayout, QLineEdit, QLabel





class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUI()
        self.setWindowTitle("Typing Speed Checker")

    def setupUI(self):
        layout = QVBoxLayout()
        self.setLayout(layout)

        words = "The way to get started is to quit talking and begin doing."
        self.show_words = QLabel(words)
        layout.addWidget(self.show_words)

        self.input = QTextEdit()
        self.input.setMinimumSize(500, 200)

        self.input.setStyleSheet("padding: 5px; margin: 0px;")
        layout.addWidget(self.input)

        button_layout = QHBoxLayout()
        layout.addLayout(button_layout)

        self.start_button = QPushButton("Start")
        button_layout.addWidget(self.start_button)

        self.stop_button = QPushButton("Stop")
        button_layout.addWidget(self.stop_button)

        self.new_text_button = QPushButton("New Text")
        button_layout.addWidget(self.new_text_button)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
