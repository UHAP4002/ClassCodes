

class Students:
    def __init__(self):
       self.students = {}

    def add(self, name, id):
        self.students[id] = name

    def list(self):
        lst = []
        for id, name in self.students.items():
            lst.append((name, id))
        return lst








