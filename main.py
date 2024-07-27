import sys
import random
from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QTextEdit, QPushButton, \
    QVBoxLayout, QLineEdit, QLabel


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUI()
        self.setWindowTitle("Typing Speed Checker")

    def random_text_genrator(self):
        word_file = []
        random_word = random.randint(0, 6)
        with open("para.txt") as file:
            for item in file:
                word_file.append(item)
        return word_file[random_word]

    def setupUI(self):
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.show_words = QLabel(self.random_text_genrator())
        layout.addWidget(self.show_words)

        self.input = QTextEdit()
        self.input.setMinimumSize(500, 200)
        self.input.setStyleSheet("padding: 5px; margin: 0px;")
        layout.addWidget(self.input)

        button_layout = QHBoxLayout()
        layout.addLayout(button_layout)

        self.next_button = QPushButton("Next")
        self.next_button.clicked.connect(self.generate_text)
        button_layout.addWidget(self.next_button)

        self.check_button = QPushButton("check")
        self.check_button.clicked.connect(self.error_checker)
        button_layout.addWidget(self.check_button)


    def generate_text(self):
        new_text = self.random_text_genrator()
        self.show_words.setText(new_text)

    def error_checker(self):
        typed_data = self.input.toPlainText()
        show = self.show_words.text()
        word1 = typed_data.split()
        word2 = show.split()

        correct = []
        wrong = []
        for item, (word1, word2) in enumerate(zip(word1, word2)):
            if word1 == word2:
                correct.append(word1)
            else:
                wrong.append(word2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
