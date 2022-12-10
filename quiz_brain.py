class QestionBrain:

    def __init__(self, q_list):
        # on crée un attribut question_number qui vas compte le nombre de question au quel on a repondu
        self.question_number = 0
        # une variable qui compte le score des jouer
        self.score = 0
        # une variable question list qui retourner
        self.question_liste = q_list
    # une fonction qui compte le nombre de question au quel pn a repondu
    def shill_has_question(self):
        return self.question_number < len(self.question_liste)

    # une fonction prochaine question
    def next_question(self):
        current_question = self.question_liste[self.question_number]
        # on incrementer questuion number
        self.question_number += 1
        # reponce du jour
        user_answer = input(f"Q.{self.question_number}: {current_question.question}: True/False")
        self.question_answer(user_answer, current_question.question)
    def question_answer(self):
        if user_answer.lower() == correct_answer.lower():
            self.score +=1
            print("question suivante")
        else:
            print("game over")
        print(f"la bonne reponce est: {correct_answer}")
        print(f'ton score est {self.score}/{self.question_number}')
        print("\n")