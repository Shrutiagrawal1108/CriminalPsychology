# CriminalPsychology
A Python application that simulates a simple "Criminal Psychology" analysis tool using PyQt5 for the GUI (Graphical User Interface), NLTK's VADER for sentiment analysis, and MySQL for data storage.

1] QuestionAnswersWindow Class:
      This class represents the window where users answer a set of predefined questions related to criminal behavior.
      It uses PyQt5 for creating the interface elements such as labels, text inputs, buttons, and layouts.
      Upon answering all questions, it calculates the sentiment score based on the user's responses and stores the average sentiment score for the user in a MySQL database.

2] AnalysisWindow Class:
      This class displays the analysis result to the user. It shows each question along with the user's answers and calculates the average sentiment score based on the responses provided.

3] LoginRegisterApp Class:
      This class is responsible for the login and registration functionalities.
      It uses PyQt5 to create a login/register form where users can input their username and password to either log in or register.
      Upon successful login, it opens the QuestionAnswersWindow for the user to answer the predefined questions.
      It also provides an option to view statistics, which fetches data from the MySQL database and visualizes the average sentiment scores of users using Matplotlib's bar chart.

4] MySQL Database:
      The application uses a MySQL database named "criminalPsychology" to store user credentials, sentiment scores, and related data.

5] perform_sentiment_analysis: 
      Performs sentiment analysis using NLTK's VADER on the provided answers.
      store_sentiment_score: Stores the calculated average sentiment score for the user in the database.
      connect_to_db and close_connection: Functions for establishing and closing connections to the MySQL database.
      login, register, and view_stats: Functions handling the login, registration, and statistics display functionalities respectively. 

6] Execution:
      The run_app() function initializes the PyQt5 application, creates an instance of LoginRegisterApp, and starts the GUI application loop.


The application flow is as follows:
a] User logs in or registers.
b] Upon successful login, the user answers a set of predefined questions in the QuestionAnswersWindow.
c] After answering all questions, the application calculates the sentiment score and displays the analysis result in the AnalysisWindow.
d] Users can also view statistics (average sentiment scores) through the "View Stats" button.
