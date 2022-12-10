from data import question_data
from question_model import Question
from quiz_brain import QestionBrain

# dans le tableau, on va stocke les differentes questions
Question_bank =[]
for question in question_data:
    # question texte va recuperer les questions stocke dans le fichier data
    # question answer va recuper les reponses des questions
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    # question bank vas recupere les question et les reponces entre pas les utilisateurs
    Question_bank.append(new_question)

quiz = QestionBrain(Question_bank)
while quiz.shill_has_question():
    quiz.next_question()

print("vous aver terminer le Quizz")
print(f"votre score finial est : {quiz.score}/{quiz.question_number}")
