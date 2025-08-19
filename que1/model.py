from pydantic import BaseModel
from typing import Dict


class Student(BaseModel):
    name: str
    subject_scores: Dict[str, float]
    average: float = 0.0
    grade: str = ""

    def calculate_average_and_grade(self):
        total_score = sum(self.subject_scores.values())
        num_subjects = len(self.subject_scores)

        if num_subjects > 0:
            self.average = total_score / num_subjects
        else:
            self.average = 0.0

        if self.average >= 90:
            self.grade = 'A'
        elif self.average >= 80:
            self.grade = 'B'
        elif self.average >= 70:
            self.grade = 'C'
        elif self.average >= 60:
            self.grade = 'D'
        else:
            self.grade = 'F'

    def model_post_init(self, __context):
        self.calculate_average_and_grade()

