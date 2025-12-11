class person:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def get_gender(self):
        return self.gender


class Collage:
    def __init__(self, name):
        self.name = name
        self.student1 = person("alice", "female")
        self.student2 = person("bob", "male")
    
    def print_student_genders(self):
        print(f"collage: {self.name}")
        print(f"student1: {self.student1.name} ({self.student1.get_gender()})")
        print(f"student2: {self.student2.name} ({self.student2.get_gender()})")


def main():
    c = Collage("xyz")
    c.print_student_genders()


main()
