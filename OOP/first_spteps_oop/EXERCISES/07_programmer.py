class Programmer:
    def __init__(self, name: str, language: str, skills: int):
        self.skills = skills
        self.language = language
        self.name = name

    def watch_course(self, course_name: str, language, skill_earned: int) -> str:
        if self.language == language:
            self.skills += skill_earned
            return f"{self.name} watched {course_name}"
        return f"{self.name} does not know {language}"

    def change_language(self, new_language: str, skills_needed: int):
        if self.skills >= skills_needed:
            if self.language != new_language:
                last_language = self.language
                self.language = new_language
                return f"{self.name} switched from {last_language} to {new_language}"
            return f"{self.name} already knows {self.language}"
        return f"{self.name} needs {skills_needed - self.skills} more skills"


programmer = Programmer("John", "Java", 50)
print(programmer.watch_course("Python Masterclass", "Python", 84))
print(programmer.change_language("Java", 30))
print(programmer.change_language("Python", 100))
print(programmer.watch_course("Java: zero to hero", "Java", 50))
print(programmer.change_language("Python", 100))
print(programmer.watch_course("Python Masterclass", "Python", 84))
