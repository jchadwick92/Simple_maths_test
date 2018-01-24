import random, time, csv, datetime

class Multiplication():

    def __init__(self, num_of_questions=100):
        self.num_of_questions = num_of_questions
        self.score = 0
        self.wrong_answers = []
        self.date = str(datetime.date.today()).replace('-', '.')
        
    def run(self):
        input('Type in your name and press enter to begin: ')
        time.sleep(0.3)
        self.start_time = time.time()
        for i in range(self.num_of_questions):
            self.gen_que()
        self.end_time = time.time()
        self.time_taken()
        self.final_score = str((self.score / self.num_of_questions)*100) + '%'
        print('Score: ' + self.final_score)
        if self.wrong_answers != []:
            print('Questions that you answered wrong: ')
            for i in self.wrong_answers:
                print(i)
        self.save_results()

    def time_taken(self):
        self.total_secs = self.end_time - self.start_time
        self.secs = self.total_secs % 60
        self.mins = int((self.total_secs - self.secs) / 60)
        self.time_taken = str(self.mins) + ' minutes, ' + str(round(self.secs)) + ' seconds'
        print('Time taken: ' + self.time_taken)
        
    def gen_que(self):
        self.a = random.randint(2,12)
        self.b = random.randint(2,12)
        self.question = str(self.a) + ' x ' + str(self.b)
        self.ans = str(self.a * self.b)
        self.answer = input(self.question + ' = ')
        if self.answer == self.ans:
            self.score += 1
        if self.answer != self.ans:
            self.wrong_answers.append(self.question)

    def save_results(self):
        csvFile = open('Multiplication_results.csv', 'a', newline='')
        writer = csv.writer(csvFile)
        writer.writerow([self.date] + [self.final_score] + [self.time_taken])
        csvFile.close()
        
                    
M = Multiplication()
M.run()

