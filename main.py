# import sys
# import mysql.connector
# from mysql.connector import Error
# from database_config import DB_CONFIG
# from PyQt5.QtWidgets import (
#     QApplication,
#     QWidget,
#     QLabel,
#     QLineEdit,
#     QPushButton,
#     QVBoxLayout,
#     QMessageBox,
#     QTextEdit,
# )
# from PyQt5.QtCore import Qt, QPropertyAnimation, QRect
# import pandas as pd
# import nltk
# from nltk.sentiment.vader import SentimentIntensityAnalyzer
#
# nltk.data.path.append("vader.py")
#
# class QuestionAnswersWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Criminal Psychology")
#         self.setGeometry(100, 100, 600, 400)
#
#         self.setStyleSheet(
#             "background-color: #f0f0f0; font-size: 16px; color: #333;"
#         )
#
#
#         self.question_number = 0
#         self.questions = [
#             "Question 1: Have you ever deliberately hurt someone physically?",
#             "Question 2: Have you ever stolen something?",
#             "Question 3: Have you ever lied to gain an advantage?",
#             "Question 4: Have you ever felt no remorse after hurting someone?",
#             "Question 5: Have you ever enjoyed seeing someone suffer?",
#         ]
#         self.answers = []
#
#         layout = QVBoxLayout()
#
#         self.question_label = QLabel(self.questions[self.question_number])
#         self.question_label.setStyleSheet(
#             "font-size: 20px; color: #222;"
#         )
#         layout.addWidget(self.question_label)
#
#         self.answer_input = QTextEdit()  # For text input answers
#         self.answer_input.setStyleSheet(
#             "background-color: #fff; font-size: 16px; color: #222;"
#         )
#         layout.addWidget(self.answer_input)
#
#         next_button = QPushButton("Next")
#         next_button.setStyleSheet(
#             "background-color: #4caf50; color: white; font-size: 18px; border-radius: 8px;"
#         )
#         layout.addWidget(next_button)
#         next_button.clicked.connect(self.next_question)
#
#         self.setLayout(layout)
#
#     def next_question(self):
#         answer = self.answer_input.toPlainText().strip()
#         if self.question_number == 2:
#             answer = "Yes" if answer.lower() == "yes" else "No"
#         self.answers.append(answer)
#
#         self.question_number += 1
#         if self.question_number < len(self.questions):
#             self.animate_question_change()
#         else:
#             self.open_analysis()
#
#     def animate_question_change(self):
#         animation = QPropertyAnimation(self.question_label, b"geometry")
#         animation.setDuration(800)
#         current_rect = self.question_label.geometry()
#         end_rect = QRect(
#             current_rect.x(),
#             current_rect.y() - 70,
#             current_rect.width(),
#             current_rect.height(),
#         )
#         animation.setEndValue(end_rect)
#         animation.start()
#
#         self.question_label.setText(self.questions[self.question_number])
#         self.answer_input.clear()
#
#         animation_reverse = QPropertyAnimation(self.question_label, b"geometry")
#         animation_reverse.setDuration(800)
#         animation_reverse.setStartValue(end_rect)
#         animation_reverse.setEndValue(current_rect)
#         animation_reverse.start()
#
#     def open_analysis(self):
#         analyzer = SentimentIntensityAnalyzer()
#         result = self.perform_sentiment_analysis(analyzer, self.answers)
#
#         self.analysis_window = AnalysisWindow(result, self.questions, self.answers)
#         self.analysis_window.show()
#         self.hide()
#
#     def perform_sentiment_analysis(self, analyzer, answers):
#         sentiment_scores = []
#         for answer in answers:
#             sentiment_score = analyzer.polarity_scores(answer)
#             sentiment_scores.append(sentiment_score["compound"])
#         return sentiment_scores
#
#
# class AnalysisWindow(QWidget):
#     def __init__(self, analysis_result, questions, answers):
#         super().__init__()
#         self.setWindowTitle("Criminal Psychology")
#         self.setGeometry(100, 100, 600, 400)
#
#         self.setStyleSheet(
#             "background-color: #f0f0f0; font-size: 16px; color: #333;"
#         )
#
#         self.analysis_result = analysis_result
#         self.questions = questions
#         self.answers = answers
#
#         layout = QVBoxLayout()
#
#         result_label = QLabel("Sentiment Analysis Result:")
#         result_label.setStyleSheet(
#             "font-size: 20px; font-weight: bold; color: #222;"
#         )
#         layout.addWidget(result_label)
#
#         for i, (question, answer) in enumerate(zip(self.questions, self.answers)):
#             answer_text = "Yes" if answer.lower() == "yes" else answer
#             label = QLabel(f"{question}\nYour Answer: {answer_text}")
#             label.setStyleSheet("font-size: 18px; color: #222;")
#             layout.addWidget(label)
#
#         avg_score = sum(self.analysis_result) / len(self.analysis_result)
#         avg_label = QLabel(f"Average Sentiment Score: {avg_score}")
#         avg_label.setStyleSheet(
#             "font-size: 20px; font-weight: bold; color: #222;"
#         )
#         layout.addWidget(avg_label)
#
#         self.setLayout(layout)
#
#
# class LoginRegisterApp(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Criminal Psychology")
#         self.setGeometry(100, 100, 500, 350)
#
#         self.setStyleSheet(
#             "background-color: #f0f0f0; font-size: 16px; color: #333;"
#         )
#
#         self.username_label = QLabel("Username:")
#         self.username_label.setStyleSheet(
#             "font-size: 20px; color: #222;"
#         )
#         self.username_entry = QLineEdit()
#         self.username_entry.setStyleSheet(
#             "background-color: #fff; font-size: 16px; color: #222;"
#         )
#         self.username_entry.setFixedWidth(350)
#         self.password_label = QLabel("Password:")
#         self.password_label.setStyleSheet(
#             "font-size: 20px; color: #222;"
#         )
#         self.password_entry = QLineEdit()
#         self.password_entry.setEchoMode(QLineEdit.Password)
#         self.password_entry.setStyleSheet(
#             "background-color: #fff; font-size: 16px; color: #222;"
#         )
#         self.password_entry.setFixedWidth(350)
#         self.login_button = QPushButton("Login")
#         self.login_button.setStyleSheet(
#             "background-color: #4caf50; color: white; font-size: 18px; border-radius: 8px;"
#         )
#         self.register_button = QPushButton("Register")
#         self.register_button.setStyleSheet(
#             "background-color: #2196f3; color: white; font-size: 18px; border-radius: 8px;"
#         )
#
#         layout = QVBoxLayout()
#         layout.addWidget(self.username_label)
#         layout.addWidget(self.username_entry)
#         layout.addWidget(self.password_label)
#         layout.addWidget(self.password_entry)
#         layout.addWidget(self.login_button)
#         layout.addWidget(self.register_button)
#         layout.setAlignment(Qt.AlignCenter)
#
#         self.setLayout(layout)
#
#         self.login_button.clicked.connect(self.login)
#         self.register_button.clicked.connect(self.register)
#
#     def connect_to_db(self):
#         try:
#             connection = mysql.connector.connect(**DB_CONFIG)
#             if connection.is_connected():
#                 return connection
#         except Error as e:
#             print("Error connecting to database:", e)
#             return None
#
#     def close_connection(self, connection):
#         if connection.is_connected():
#             connection.close()
#
#     def login(self):
#         username = self.username_entry.text()
#         password = self.password_entry.text()
#
#         connection = self.connect_to_db()
#         if connection:
#             try:
#                 cursor = connection.cursor()
#                 select_query = "SELECT * FROM users WHERE username = %s AND password = %s"
#                 cursor.execute(select_query, (username, password))
#                 user = cursor.fetchone()
#                 cursor.close()
#
#                 if user:
#                     QMessageBox.information(
#                         self, "Login", "Login successful!"
#                     )
#                     self.open_question_answers()
#                 else:
#                     QMessageBox.warning(
#                         self, "Login", "Invalid username or password."
#                     )
#             except Error as e:
#                 print("Error logging in:", e)
#             finally:
#                 self.close_connection(connection)
#
#     def open_question_answers(self):
#         self.question_answers_window = QuestionAnswersWindow()
#         self.question_answers_window.show()
#         self.hide()
#
#     def register(self):
#         username = self.username_entry.text()
#         password = self.password_entry.text()
#
#         connection = self.connect_to_db()
#         if connection:
#             try:
#                 cursor = connection.cursor()
#                 insert_query = "INSERT INTO users (username, password) VALUES (%s, %s)"
#                 cursor.execute(insert_query, (username, password))
#                 connection.commit()
#                 cursor.close()
#                 QMessageBox.information(
#                     self, "Registration", "Registration successful!"
#                 )
#             except Error as e:
#                 print("Error registering user:", e)
#             finally:
#                 self.close_connection(connection)
#
#
# def run_app():
#     app = QApplication(sys.argv)
#     window = LoginRegisterApp()
#     window.show()
#     sys.exit(app.exec_())
#
#
# if __name__ == "__main__":
#     run_app()
#
#
#
# import sys
# import mysql.connector
# from mysql.connector import Error
# from PyQt5.QtWidgets import (
#     QApplication,
#     QWidget,
#     QLabel,
#     QLineEdit,
#     QPushButton,
#     QVBoxLayout,
#     QMessageBox,
#     QTextEdit,
# )
# from PyQt5.QtCore import Qt, QPropertyAnimation, QRect
# from nltk.sentiment.vader import SentimentIntensityAnalyzer
#
# class QuestionAnswersWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Criminal Psychology")
#         self.setGeometry(100, 100, 600, 400)
#         self.setStyleSheet(
#             "background-color: #f0f0f0; font-size: 16px; color: #333;"
#         )
#
#         self.question_number = 0
#         self.questions = [
#             "Question 1: Have you ever deliberately hurt someone physically?",
#             "Question 2: Have you ever stolen something?",
#             "Question 3: Have you ever lied to gain an advantage?",
#             "Question 4: Have you ever felt no remorse after hurting someone?",
#             "Question 5: Have you ever enjoyed seeing someone suffer?",
#         ]
#         self.answers = []
#
#         layout = QVBoxLayout()
#
#         self.question_label = QLabel(self.questions[self.question_number])
#         self.question_label.setStyleSheet(
#             "font-size: 20px; color: #222;"
#         )
#         layout.addWidget(self.question_label)
#
#         self.answer_input = QTextEdit()  # For text input answers
#         self.answer_input.setStyleSheet(
#             "background-color: #fff; font-size: 16px; color: #222;"
#         )
#         layout.addWidget(self.answer_input)
#
#         next_button = QPushButton("Next")
#         next_button.setStyleSheet(
#             "background-color: #4caf50; color: white; font-size: 18px; border-radius: 8px;"
#         )
#         layout.addWidget(next_button)
#         next_button.clicked.connect(self.next_question)
#
#         self.setLayout(layout)
#
#     def next_question(self):
#         answer = self.answer_input.toPlainText().strip()
#         if self.question_number == 2:
#             answer = "Yes" if answer.lower() == "yes" else "No"
#         self.answers.append(answer)
#
#         self.question_number += 1
#         if self.question_number < len(self.questions):
#             self.animate_question_change()
#         else:
#             self.open_analysis()
#
#     def animate_question_change(self):
#         animation = QPropertyAnimation(self.question_label, b"geometry")
#         animation.setDuration(800)
#         current_rect = self.question_label.geometry()
#         end_rect = QRect(
#             current_rect.x(),
#             current_rect.y() - 70,
#             current_rect.width(),
#             current_rect.height(),
#         )
#         animation.setEndValue(end_rect)
#         animation.start()
#
#         self.question_label.setText(self.questions[self.question_number])
#         self.answer_input.clear()
#
#         animation_reverse = QPropertyAnimation(self.question_label, b"geometry")
#         animation_reverse.setDuration(800)
#         animation_reverse.setStartValue(end_rect)
#         animation_reverse.setEndValue(current_rect)
#         animation_reverse.start()
#
#     def open_analysis(self):
#         analyzer = SentimentIntensityAnalyzer()
#         result = self.perform_sentiment_analysis(analyzer, self.answers)
#
#         avg_score = sum(result) / len(result)
#         self.store_sentiment_score('username', avg_score)  # Replace 'username' with the actual username
#
#         self.analysis_window = AnalysisWindow(result, self.questions, self.answers)
#         self.analysis_window.show()
#         self.hide()
#
#     def perform_sentiment_analysis(self, analyzer, answers):
#         sentiment_scores = []
#         for answer in answers:
#             sentiment_score = analyzer.polarity_scores(answer)
#             sentiment_scores.append(sentiment_score["compound"])
#         return sentiment_scores
#
#     def store_sentiment_score(self, username, avg_score):
#         try:
#             connection = mysql.connector.connect(
#                 host='localhost',
#                 user='root',
#                 password='',  # Replace with your password
#                 database='criminalPsychology'
#             )
#             if connection.is_connected():
#                 cursor = connection.cursor()
#                 insert_query = "INSERT INTO sentiment_scores (name, average_score) VALUES (%s, %s)"
#                 cursor.execute(insert_query, (username, avg_score))
#                 connection.commit()
#                 cursor.close()
#                 connection.close()
#         except Error as e:
#             print("Error storing sentiment score:", e)
#
# class AnalysisWindow(QWidget):
#     def __init__(self, analysis_result, questions, answers):
#         super().__init__()
#         self.setWindowTitle("Criminal Psychology")
#         self.setGeometry(100, 100, 600, 400)
#         self.setStyleSheet(
#             "background-color: #f0f0f0; font-size: 16px; color: #333;"
#         )
#
#         self.analysis_result = analysis_result
#         self.questions = questions
#         self.answers = answers
#
#         layout = QVBoxLayout()
#
#         result_label = QLabel("Sentiment Analysis Result:")
#         result_label.setStyleSheet(
#             "font-size: 20px; font-weight: bold; color: #222;"
#         )
#         layout.addWidget(result_label)
#
#         for i, (question, answer) in enumerate(zip(self.questions, self.answers)):
#             answer_text = "Yes" if answer.lower() == "yes" else answer
#             label = QLabel(f"{question}\nYour Answer: {answer_text}")
#             label.setStyleSheet("font-size: 18px; color: #222;")
#             layout.addWidget(label)
#
#         avg_score = sum(self.analysis_result) / len(self.analysis_result)
#         avg_label = QLabel(f"Average Sentiment Score: {avg_score}")
#         avg_label.setStyleSheet(
#             "font-size: 20px; font-weight: bold; color: #222;"
#         )
#         layout.addWidget(avg_label)
#
#         self.setLayout(layout)
#
# class LoginRegisterApp(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Criminal Psychology")
#         self.setGeometry(100, 100, 500, 350)
#         self.setStyleSheet(
#             "background-color: #f0f0f0; font-size: 16px; color: #333;"
#         )
#
#         self.username_label = QLabel("Username:")
#         self.username_label.setStyleSheet(
#             "font-size: 20px; color: #222;"
#         )
#         self.username_entry = QLineEdit()
#         self.username_entry.setStyleSheet(
#             "background-color: #fff; font-size: 16px; color: #222;"
#         )
#         self.username_entry.setFixedWidth(350)
#         self.password_label = QLabel("Password:")
#         self.password_label.setStyleSheet(
#             "font-size: 20px; color: #222;"
#         )
#         self.password_entry = QLineEdit()
#         self.password_entry.setEchoMode(QLineEdit.Password)
#         self.password_entry.setStyleSheet(
#             "background-color: #fff; font-size: 16px; color: #222;"
#         )
#         self.password_entry.setFixedWidth(350)
#         self.login_button = QPushButton("Login")
#         self.login_button.setStyleSheet(
#             "background-color: #4caf50; color: white; font-size: 18px; border-radius: 8px;"
#         )
#         self.register_button = QPushButton("Register")
#         self.register_button.setStyleSheet(
#             "background-color: #2196f3; color: white; font-size: 18px; border-radius: 8px;"
#         )
#
#         layout = QVBoxLayout()
#         layout.addWidget(self.username_label)
#         layout.addWidget(self.username_entry)
#         layout.addWidget(self.password_label)
#         layout.addWidget(self.password_entry)
#         layout.addWidget(self.login_button)
#         layout.addWidget(self.register_button)
#         layout.setAlignment(Qt.AlignCenter)
#
#         self.setLayout(layout)
#
#         self.login_button.clicked.connect(self.login)
#         self.register_button.clicked.connect(self.register)
#
#     def connect_to_db(self):
#         try:
#             connection = mysql.connector.connect(
#                 host='localhost',
#                 user='root',
#                 password='',  # Replace with your password
#                 database='criminalPsychology'
#             )
#             if connection.is_connected():
#                 return connection
#         except Error as e:
#             print("Error connecting to database:", e)
#             return None
#
#     def close_connection(self, connection):
#         if connection.is_connected():
#             connection.close()
#
#     def login(self):
#         username = self.username_entry.text()
#         password = self.password_entry.text()
#
#         connection = self.connect_to_db()
#         if connection:
#             try:
#                 cursor = connection.cursor()
#                 select_query = "SELECT * FROM users WHERE username = %s AND password = %s"
#                 cursor.execute(select_query, (username, password))
#                 user = cursor.fetchone()
#                 cursor.close()
#
#                 if user:
#                     QMessageBox.information(
#                         self, "Login", "Login successful!"
#                     )
#                     self.open_question_answers()
#                 else:
#                     QMessageBox.warning(
#                         self, "Login", "Invalid username or password."
#                     )
#             except Error as e:
#                 print("Error logging in:", e)
#             finally:
#                 self.close_connection(connection)
#
#     def open_question_answers(self):
#         self.question_answers_window = QuestionAnswersWindow()
#         self.question_answers_window.show()
#         self.hide()
#
#     def register(self):
#         username = self.username_entry.text()
#         password = self.password_entry.text()
#
#         connection = self.connect_to_db()
#         if connection:
#             try:
#                 cursor = connection.cursor()
#                 insert_query = "INSERT INTO users (username, password) VALUES (%s, %s)"
#                 cursor.execute(insert_query, (username, password))
#                 connection.commit()
#                 cursor.close()
#                 QMessageBox.information(
#                     self, "Registration", "Registration successful!"
#                 )
#             except Error as e:
#                 print("Error registering user:", e)
#             finally:
#                 self.close_connection(connection)
#
#
# def run_app():
#     app = QApplication(sys.argv)
#     window = LoginRegisterApp()
#     window.show()
#     sys.exit(app.exec_())
#
#
# if __name__ == "__main__":
#     run_app()


#
# import sys
# import mysql.connector
# from mysql.connector import Error
# from PyQt5.QtWidgets import (
#     QApplication,
#     QWidget,
#     QLabel,
#     QLineEdit,
#     QPushButton,
#     QVBoxLayout,
#     QMessageBox,
#     QTextEdit,
# )
# from PyQt5.QtCore import Qt, QPropertyAnimation, QRect
# from nltk.sentiment.vader import SentimentIntensityAnalyzer
#
# class QuestionAnswersWindow(QWidget):
#     def __init__(self, username):
#         super().__init__()
#         self.setWindowTitle("Criminal Psychology")
#         self.setGeometry(100, 100, 600, 400)
#         self.setStyleSheet(
#             "background-color: #f0f0f0; font-size: 16px; color: #333;"
#         )
#
#         self.username = username
#
#         self.question_number = 0
#         self.questions = [
#             "Question 1: Have you ever deliberately hurt someone physically?",
#             "Question 2: Have you ever stolen something?",
#             "Question 3: Have you ever lied to gain an advantage?",
#             "Question 4: Have you ever felt no remorse after hurting someone?",
#             "Question 5: Have you ever enjoyed seeing someone suffer?",
#         ]
#         self.answers = []
#
#         layout = QVBoxLayout()
#
#         self.question_label = QLabel(self.questions[self.question_number])
#         self.question_label.setStyleSheet(
#             "font-size: 20px; color: #222;"
#         )
#         layout.addWidget(self.question_label)
#
#         self.answer_input = QTextEdit()  # For text input answers
#         self.answer_input.setStyleSheet(
#             "background-color: #fff; font-size: 16px; color: #222;"
#         )
#         layout.addWidget(self.answer_input)
#
#         next_button = QPushButton("Next")
#         next_button.setStyleSheet(
#             "background-color: #4caf50; color: white; font-size: 18px; border-radius: 8px;"
#         )
#         layout.addWidget(next_button)
#         next_button.clicked.connect(self.next_question)
#
#         self.setLayout(layout)
#
#     def next_question(self):
#         answer = self.answer_input.toPlainText().strip()
#         if self.question_number == 2:
#             answer = "Yes" if answer.lower() == "yes" else "No"
#         self.answers.append(answer)
#
#         self.question_number += 1
#         if self.question_number < len(self.questions):
#             self.animate_question_change()
#         else:
#             self.open_analysis()
#
#     def animate_question_change(self):
#         animation = QPropertyAnimation(self.question_label, b"geometry")
#         animation.setDuration(800)
#         current_rect = self.question_label.geometry()
#         end_rect = QRect(
#             current_rect.x(),
#             current_rect.y() - 70,
#             current_rect.width(),
#             current_rect.height(),
#         )
#         animation.setEndValue(end_rect)
#         animation.start()
#
#         self.question_label.setText(self.questions[self.question_number])
#         self.answer_input.clear()
#
#         animation_reverse = QPropertyAnimation(self.question_label, b"geometry")
#         animation_reverse.setDuration(800)
#         animation_reverse.setStartValue(end_rect)
#         animation_reverse.setEndValue(current_rect)
#         animation_reverse.start()
#
#     def open_analysis(self):
#         analyzer = SentimentIntensityAnalyzer()
#         result = self.perform_sentiment_analysis(analyzer, self.answers)
#
#         avg_score = sum(result) / len(result)
#         self.store_sentiment_score(self.username, avg_score)  # Store the actual username
#
#         self.analysis_window = AnalysisWindow(result, self.questions, self.answers)
#         self.analysis_window.show()
#         self.hide()
#
#     def perform_sentiment_analysis(self, analyzer, answers):
#         sentiment_scores = []
#         for answer in answers:
#             sentiment_score = analyzer.polarity_scores(answer)
#             sentiment_scores.append(sentiment_score["compound"])
#         return sentiment_scores
#
#     def store_sentiment_score(self, username, avg_score):
#         try:
#             connection = mysql.connector.connect(
#                 host='localhost',
#                 user='root',
#                 password='',  # Replace with your password
#                 database='criminalPsychology'
#             )
#             if connection.is_connected():
#                 cursor = connection.cursor()
#                 insert_query = "INSERT INTO sentiment_scores (name, average_score) VALUES (%s, %s)"
#                 cursor.execute(insert_query, (username, avg_score))
#                 connection.commit()
#                 cursor.close()
#                 connection.close()
#         except Error as e:
#             print("Error storing sentiment score:", e)
#
# class AnalysisWindow(QWidget):
#     def __init__(self, analysis_result, questions, answers):
#         super().__init__()
#         self.setWindowTitle("Criminal Psychology")
#         self.setGeometry(100, 100, 600, 400)
#         self.setStyleSheet(
#             "background-color: #f0f0f0; font-size: 16px; color: #333;"
#         )
#
#         self.analysis_result = analysis_result
#         self.questions = questions
#         self.answers = answers
#
#         layout = QVBoxLayout()
#
#         result_label = QLabel("Sentiment Analysis Result:")
#         result_label.setStyleSheet(
#             "font-size: 20px; font-weight: bold; color: #222;"
#         )
#         layout.addWidget(result_label)
#
#         for i, (question, answer) in enumerate(zip(self.questions, self.answers)):
#             answer_text = "Yes" if answer.lower() == "yes" else answer
#             label = QLabel(f"{question}\nYour Answer: {answer_text}")
#             label.setStyleSheet("font-size: 18px; color: #222;")
#             layout.addWidget(label)
#
#         avg_score = sum(self.analysis_result) / len(self.analysis_result)
#         avg_label = QLabel(f"Average Sentiment Score: {avg_score}")
#         avg_label.setStyleSheet(
#             "font-size: 20px; font-weight: bold; color: #222;"
#         )
#         layout.addWidget(avg_label)
#
#         self.setLayout(layout)
#
# class LoginRegisterApp(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Criminal Psychology")
#         self.setGeometry(100, 100, 500, 350)
#         self.setStyleSheet(
#             "background-color: #f0f0f0; font-size: 16px; color: #333;"
#         )
#
#         self.username_label = QLabel("Username:")
#         self.username_label.setStyleSheet(
#             "font-size: 20px; color: #222;"
#         )
#         self.username_entry = QLineEdit()
#         self.username_entry.setStyleSheet(
#             "background-color: #fff; font-size: 16px; color: #222;"
#         )
#         self.username_entry.setFixedWidth(350)
#         self.password_label = QLabel("Password:")
#         self.password_label.setStyleSheet(
#             "font-size: 20px; color: #222;"
#         )
#         self.password_entry = QLineEdit()
#         self.password_entry.setEchoMode(QLineEdit.Password)
#         self.password_entry.setStyleSheet(
#             "background-color: #fff; font-size: 16px; color: #222;"
#         )
#         self.password_entry.setFixedWidth(350)
#         self.login_button = QPushButton("Login")
#         self.login_button.setStyleSheet(
#             "background-color: #4caf50; color: white; font-size: 18px; border-radius: 8px;"
#         )
#         self.register_button = QPushButton("Register")
#         self.register_button.setStyleSheet(
#             "background-color: #2196f3; color: white; font-size: 18px; border-radius: 8px;"
#         )
#
#         layout = QVBoxLayout()
#         layout.addWidget(self.username_label)
#         layout.addWidget(self.username_entry)
#         layout.addWidget(self.password_label)
#         layout.addWidget(self.password_entry)
#         layout.addWidget(self.login_button)
#         layout.addWidget(self.register_button)
#         layout.setAlignment(Qt.AlignCenter)
#
#         self.setLayout(layout)
#
#         self.login_button.clicked.connect(self.login)
#         self.register_button.clicked.connect(self.register)
#
#     def connect_to_db(self):
#         try:
#             connection = mysql.connector.connect(
#                 host='localhost',
#                 user='root',
#                 password='',  # Replace with your password
#                 database='criminalPsychology'
#             )
#             if connection.is_connected():
#                 return connection
#         except Error as e:
#             print("Error connecting to database:", e)
#             return None
#
#     def close_connection(self, connection):
#         if connection.is_connected():
#             connection.close()
#
#     def login(self):
#         username = self.username_entry.text()
#         password = self.password_entry.text()
#
#         connection = self.connect_to_db()
#         if connection:
#             try:
#                 cursor = connection.cursor()
#                 select_query = "SELECT * FROM users WHERE username = %s AND password = %s"
#                 cursor.execute(select_query, (username, password))
#                 user = cursor.fetchone()
#                 cursor.close()
#
#                 if user:
#                     QMessageBox.information(
#                         self, "Login", "Login successful!"
#                     )
#                     self.open_question_answers(username)
#                 else:
#                     QMessageBox.warning(
#                         self, "Login", "Invalid username or password."
#                     )
#             except Error as e:
#                 print("Error logging in:", e)
#             finally:
#                 self.close_connection(connection)
#
#     def open_question_answers(self, username):
#         self.question_answers_window = QuestionAnswersWindow(username)
#         self.question_answers_window.show()
#         self.hide()
#
#     def register(self):
#         username = self.username_entry.text()
#         password = self.password_entry.text()
#
#         connection = self.connect_to_db()
#         if connection:
#             try:
#                 cursor = connection.cursor()
#                 insert_query = "INSERT INTO users (username, password) VALUES (%s, %s)"
#                 cursor.execute(insert_query, (username, password))
#                 connection.commit()
#                 cursor.close()
#                 QMessageBox.information(
#                     self, "Registration", "Registration successful!"
#                 )
#             except Error as e:
#                 print("Error registering user:", e)
#             finally:
#                 self.close_connection(connection)
#
#
# def run_app():
#     app = QApplication(sys.argv)
#     window = LoginRegisterApp()
#     window.show()
#     sys.exit(app.exec_())
#
#
# if __name__ == "__main__":
#     run_app()
#

import sys
import mysql.connector
from mysql.connector import Error
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QMessageBox,
    QTextEdit,
)
from PyQt5.QtCore import Qt, QPropertyAnimation, QRect
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt


class QuestionAnswersWindow(QWidget):
    def __init__(self, username):
        super().__init__()
        self.setWindowTitle("Criminal Psychology")
        self.setGeometry(100, 100, 600, 400)
        self.setStyleSheet(
            "background-color: #f0f0f0; font-size: 16px; color: #333;"
        )

        self.username = username

        self.question_number = 0
        self.questions = [
            "Question 1: Have you ever deliberately hurt someone physically?",
            "Question 2: Have you ever stolen something?",
            "Question 3: Have you ever lied to gain an advantage?",
            "Question 4: Have you ever felt no remorse after hurting someone?",
            "Question 5: Have you ever enjoyed seeing someone suffer?",
        ]
        self.answers = []

        layout = QVBoxLayout()

        self.question_label = QLabel(self.questions[self.question_number])
        self.question_label.setStyleSheet(
            "font-size: 20px; color: #222;"
        )
        layout.addWidget(self.question_label)

        self.answer_input = QTextEdit()  # For text input answers
        self.answer_input.setStyleSheet(
            "background-color: #fff; font-size: 16px; color: #222;"
        )
        layout.addWidget(self.answer_input)

        next_button = QPushButton("Next")
        next_button.setStyleSheet(
            "background-color: #4caf50; color: white; font-size: 18px; border-radius: 8px;"
        )
        layout.addWidget(next_button)
        next_button.clicked.connect(self.next_question)

        self.setLayout(layout)

    def next_question(self):
        answer = self.answer_input.toPlainText().strip()
        if self.question_number == 2:
            answer = "Yes" if answer.lower() == "yes" else "No"
        self.answers.append(answer)

        self.question_number += 1
        if self.question_number < len(self.questions):
            self.animate_question_change()
        else:
            self.open_analysis()

    def animate_question_change(self):
        animation = QPropertyAnimation(self.question_label, b"geometry")
        animation.setDuration(800)
        current_rect = self.question_label.geometry()
        end_rect = QRect(
            current_rect.x(),
            current_rect.y() - 70,
            current_rect.width(),
            current_rect.height(),
        )
        animation.setEndValue(end_rect)
        animation.start()

        self.question_label.setText(self.questions[self.question_number])
        self.answer_input.clear()

        animation_reverse = QPropertyAnimation(self.question_label, b"geometry")
        animation_reverse.setDuration(800)
        animation_reverse.setStartValue(end_rect)
        animation_reverse.setEndValue(current_rect)
        animation_reverse.start()

    def open_analysis(self):
        analyzer = SentimentIntensityAnalyzer()
        result = self.perform_sentiment_analysis(analyzer, self.answers)

        avg_score = sum(result) / len(result)
        self.store_sentiment_score(self.username, avg_score)  # Store the actual username

        self.analysis_window = AnalysisWindow(result, self.questions, self.answers)
        self.analysis_window.show()
        self.hide()

    def perform_sentiment_analysis(self, analyzer, answers):
        sentiment_scores = []
        for answer in answers:
            sentiment_score = analyzer.polarity_scores(answer)
            sentiment_scores.append(sentiment_score["compound"])
        return sentiment_scores

    def store_sentiment_score(self, username, avg_score):
        try:
            connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='',  # Replace with your password
                database='criminalPsychology'
            )
            if connection.is_connected():
                cursor = connection.cursor()
                insert_query = "INSERT INTO sentiment_scores (name, average_score) VALUES (%s, %s)"
                cursor.execute(insert_query, (username, avg_score))
                connection.commit()
                cursor.close()
                connection.close()
        except Error as e:
            print("Error storing sentiment score:", e)


class AnalysisWindow(QWidget):
    def __init__(self, analysis_result, questions, answers):
        super().__init__()
        self.setWindowTitle("Criminal Psychology")
        self.setGeometry(100, 100, 600, 400)
        self.setStyleSheet(
            "background-color: #f0f0f0; font-size: 16px; color: #333;"
        )

        self.analysis_result = analysis_result
        self.questions = questions
        self.answers = answers

        layout = QVBoxLayout()

        result_label = QLabel("Sentiment Analysis Result:")
        result_label.setStyleSheet(
            "font-size: 20px; font-weight: bold; color: #222;"
        )
        layout.addWidget(result_label)

        for i, (question, answer) in enumerate(zip(self.questions, self.answers)):
            answer_text = "Yes" if answer.lower() == "yes" else answer
            label = QLabel(f"{question}\nYour Answer: {answer_text}")
            label.setStyleSheet("font-size: 18px; color: #222;")
            layout.addWidget(label)

        avg_score = sum(self.analysis_result) / len(self.analysis_result)
        avg_label = QLabel(f"Average Sentiment Score: {avg_score}")
        avg_label.setStyleSheet(
            "font-size: 20px; font-weight: bold; color: #222;"
        )
        layout.addWidget(avg_label)

        self.setLayout(layout)


class LoginRegisterApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Criminal Psychology")
        self.setGeometry(100, 100, 500, 350)
        self.setStyleSheet(
            "background-color: #f0f0f0; font-size: 16px; color: #333;"
        )

        self.username_label = QLabel("Username:")
        self.username_label.setStyleSheet(
            "font-size: 20px; color: #222;"
        )
        self.username_entry = QLineEdit()
        self.username_entry.setStyleSheet(
            "background-color: #fff; font-size: 16px; color: #222;"
        )
        self.username_entry.setFixedWidth(350)
        self.password_label = QLabel("Password:")
        self.password_label.setStyleSheet(
            "font-size: 20px; color: #222;"
        )
        self.password_entry = QLineEdit()
        self.password_entry.setEchoMode(QLineEdit.Password)
        self.password_entry.setStyleSheet(
            "background-color: #fff; font-size: 16px; color: #222;"
        )
        self.password_entry.setFixedWidth(350)
        self.login_button = QPushButton("Login")
        self.login_button.setStyleSheet(
            "background-color: #4caf50; color: white; font-size: 18px; border-radius: 8px;"
        )
        self.register_button = QPushButton("Register")
        self.register_button.setStyleSheet(
            "background-color: #2196f3; color: white; font-size: 18px; border-radius: 8px;"
        )
        self.view_stats_button = QPushButton("View Stats")
        self.view_stats_button.setStyleSheet(
            "background-color: #ff9800; color: white; font-size: 18px; border-radius: 8px;"
        )

        layout = QVBoxLayout()
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_entry)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_entry)
        layout.addWidget(self.login_button)
        layout.addWidget(self.register_button)
        layout.addWidget(self.view_stats_button)
        layout.setAlignment(Qt.AlignCenter)

        self.setLayout(layout)

        self.login_button.clicked.connect(self.login)
        self.register_button.clicked.connect(self.register)
        self.view_stats_button.clicked.connect(self.view_stats)

    def connect_to_db(self):
        try:
            connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='',  # Replace with your password
                database='criminalPsychology'
            )
            if connection.is_connected():
                return connection
        except Error as e:
            print("Error connecting to database:", e)
            return None

    def close_connection(self, connection):
        if connection.is_connected():
            connection.close()

    def login(self):
        username = self.username_entry.text()
        password = self.password_entry.text()

        connection = self.connect_to_db()
        if connection:
            try:
                cursor = connection.cursor()
                select_query = "SELECT * FROM users WHERE username = %s AND password = %s"
                cursor.execute(select_query, (username, password))
                user = cursor.fetchone()
                cursor.close()

                if user:
                    QMessageBox.information(
                        self, "Login", "Login successful!"
                    )
                    self.open_question_answers(username)
                else:
                    QMessageBox.warning(
                        self, "Login", "Invalid username or password."
                    )
            except Error as e:
                print("Error logging in:", e)
            finally:
                self.close_connection(connection)

    def open_question_answers(self, username):
        self.question_answers_window = QuestionAnswersWindow(username)
        self.question_answers_window.show()
        self.hide()

    def register(self):
        username = self.username_entry.text()
        password = self.password_entry.text()

        connection = self.connect_to_db()
        if connection:
            try:
                cursor = connection.cursor()
                insert_query = "INSERT INTO users (username, password) VALUES (%s, %s)"
                cursor.execute(insert_query, (username, password))
                connection.commit()
                cursor.close()
                QMessageBox.information(
                    self, "Registration", "Registration successful!"
                )
            except Error as e:
                print("Error registering user:", e)
            finally:
                self.close_connection(connection)

    def view_stats(self):
        try:
            connection = self.connect_to_db()
            if connection:
                cursor = connection.cursor()
                select_query = "SELECT name, AVG(average_score) AS avg_score FROM sentiment_scores GROUP BY name"
                cursor.execute(select_query)
                rows = cursor.fetchall()
                cursor.close()
                self.close_connection(connection)

                if rows:
                    usernames = [row[0] for row in rows]
                    avg_scores = [row[1] for row in rows]

                    plt.figure(figsize=(8, 6))
                    plt.bar(usernames, avg_scores, color='skyblue')
                    plt.xlabel('Usernames')
                    plt.ylabel('Average Sentiment Score')
                    plt.title('Average Sentiment Scores by User')
                    plt.xticks(rotation=45)
                    plt.tight_layout()

                    plt.show()
                else:
                    QMessageBox.information(
                        self, "View Stats", "No data available."
                    )
        except Error as e:
            print("Error viewing stats:", e)


def run_app():
    app = QApplication(sys.argv)
    window = LoginRegisterApp()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    run_app()
