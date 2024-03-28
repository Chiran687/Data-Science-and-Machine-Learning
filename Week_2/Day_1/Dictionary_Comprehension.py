# write your program here

# Sample list of questions
questions = [
    "What is the capital of France?",
    "Who wrote the play 'Romeo and Juliet'?",
    "What is the symbol for the chemical element oxygen?",
    "In which year did World War II end?",
    "What is the tallest mammal on Earth?",
]

# Sample list of corresponding answers
answers = [
    "Paris",
    "William Shakespeare",
    "O",
    "1945",
    "Giraffe",
]
Updated_Dictionary= {q : a for q, a in zip(questions, answers)}
Updated_Dictionary