import random
from typing import List, Tuple


def sample_func(student_name: List,  task_number: List) -> Tuple:
    random.shuffle(student_name)
    random_student = random.choice(student_name)
    random_task = random.choice(task_number)
    print(random_student, random_task)


if __name__ == "__main__":
    student_name = [
        "test",
        "student",
        "hello",
        "world"
    ]
    task_number = [1,
                   2,
                   5,
                   6]

    sample_func(*student_name, task_number)
