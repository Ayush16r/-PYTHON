class staff:
    def display(self):
        print(self.name, self.sid)
class faculty(staff):
    def __init__(self,name,desigination):
        super().__init__(name,sid)
        self.desigination=degination