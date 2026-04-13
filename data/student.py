class Student : 
    def __init__(self,sid,name):
        self.sid = sid
        self.name = name
        self.marks = {}

    def add_marks(self,subject,mark):
        self.marks[subject] = mark

    def get_total(self):
        return sum(self.marks.values())    

    def get_avg(self):
        if len(self.marks) == 0 :
            return 0
        return self.get_total() / len(self.marks)
    
    def get_grade(self):
        avg = self.get_avg()

        if avg >= 80 :
            return "A"
        
        elif avg >= 60 :
            return "B"
        
        elif avg >= 40 :
            return "C"
        
        else :
            return "F"
        

    def display(self):
        print(f"Id : {self.sid} \n")
        print(f"Name : {self.name} \n")
        print(f"Marks : ")

        for sub , mark in self.marks.items():
            print(f" {sub} : {mark} \n")

        print(f"Total : {self.get_total} \n")
        print(f"Average : {self.get_avg} \n")
        print(f"Grade : {self.get_grade} \n")
