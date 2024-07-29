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

    def error_checker(self):
        typed_data = self.input.toPlainText()
        show = self.show_words.text()
        word1 = typed_data.split()
        word2 = show.split()
        correct = 0
        wrong = 0

        for item, (word1, word2) in enumerate(zip(word1, word2)):
            if word1 == word2:
                correct += len(word1)
            else:
                wrong += len(word2)

        total = correct + wrong
        accuracy = (correct / total) * 100 if total > 0 else 0
        words = len(word1)
        gross_wpm = words / 2

        return f"Accuracy: {accuracy}%, Words: {words}, Gross WPM: {gross_wpm}"

    def setupUI(self):
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.show_words = QLabel(self.random_text_genrator().lower())
        layout.addWidget(self.show_words)

        self.input = QTextEdit()
        self.input.setMinimumSize(400, 400)
        self.input.setStyleSheet("padding: 5px; margin: 0px;")
        layout.addWidget(self.input)

        button_layout = QHBoxLayout()
        layout.addLayout(button_layout)

        self.next_button = QPushButton("Next")
        self.next_button.clicked.connect(self.generate_text)
        button_layout.addWidget(self.next_button)

        self.check_button = QPushButton("check")
        self.check_button.clicked.connect(self.update_accuracy)
        button_layout.addWidget(self.check_button)

        self.accuracy = QLabel()
        layout.addWidget(self.accuracy)

    def generate_text(self):
        new_text = self.random_text_genrator()
        self.show_words.setText(new_text)
        self.input.clear()
        self.accuracy.clear()


    def update_accuracy(self):
        result = self.error_checker()
        self.accuracy.setText(result)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
