import random
from typing import List, Dict, Tuple
import re
from difflib import SequenceMatcher

# Question bank focused on 7th grade mathematics with detailed topics
question_bank = {
    "Number Sense and Operations": {
        "Rational Numbers": [
            ("What is the absolute value of -15?", "15"),
            ("Convert 3/4 to a decimal.", "0.75"),
            ("Express 0.75 as a fraction in simplest form.", "3/4"),
            ("What is the least common multiple of 6 and 8?", "24"),
            ("What is the greatest common factor of 12 and 18?", "6"),
            ("Convert 5/8 to a decimal.", "0.625"),
            ("What is the reciprocal of 3/4?", "4/3"),
            ("Express 0.6 as a fraction in simplest form.", "3/5"),
            ("What is the sum of -8 and 15?", "7"),
            ("What is the product of -4 and -6?", "24")
        ],
        "Proportions and Ratios": [
            ("If 3 pencils cost $1.50, how much do 5 pencils cost?", "2.50"),
            ("A recipe calls for 2 cups of flour for every 3 cups of sugar. How many cups of flour are needed for 9 cups of sugar?", "6"),
            ("What is the unit rate of 150 miles in 3 hours?", "50"),
            ("If 4 workers can build a wall in 6 days, how many days will it take 6 workers?", "4"),
            ("Express the ratio 15:25 in simplest form.", "3:5"),
            ("What percentage is 3/4?", "75"),
            ("If a map scale is 1 inch = 50 miles, how many miles are represented by 3 inches?", "150"),
            ("What is the unit rate of $12 for 4 pounds?", "3"),
            ("If 2/3 of a number is 10, what is the number?", "15"),
            ("Express 0.8 as a percentage.", "80")
        ]
    },
    "Algebra": {
        "Linear Equations": [
            ("Solve for x: 2x + 5 = 13", "4"),
            ("What is the slope of the line y = 3x + 2?", "3"),
            ("What is the y-intercept of y = -2x + 5?", "5"),
            ("Solve the inequality: 2x - 3 > 7", "x > 5"),
            ("Solve for x: 3(x + 4) = 15", "1"),
            ("What is the slope of the line passing through points (2,4) and (4,8)?", "2"),
            ("Write the equation of a line with slope 2 and y-intercept -3.", "y = 2x - 3"),
            ("Solve the inequality: -3x + 2 ≤ 8", "x ≥ -2"),
            ("What is the x-intercept of y = 2x - 6?", "3"),
            ("Solve for x: 5x - 3 = 2x + 6", "3")
        ],
        "Expressions and Properties": [
            ("Simplify: 3(x + 4) - 2x", "x + 12"),
            ("What is the distributive property of 2(3x + 4)?", "6x + 8"),
            ("Combine like terms: 2x + 3y - x + 2y", "x + 5y"),
            ("Factor: 6x + 9", "3(2x + 3)"),
            ("Simplify: (2x + 3)(x - 2)", "2x² - x - 6"),
            ("What is the commutative property of addition?", "a + b = b + a"),
            ("Simplify: 4x² + 2x² - 3x²", "3x²"),
            ("Factor: x² + 5x + 6", "(x + 2)(x + 3)"),
            ("Simplify: 2(x + 3) + 3(x - 2)", "5x"),
            ("What is the associative property of multiplication?", "(a × b) × c = a × (b × c)")
        ]
    },
    "Geometry": {
        "Area and Perimeter": [
            ("What is the area of a rectangle with length 8 and width 5?", "40"),
            ("Find the circumference of a circle with radius 7 (use π = 3.14)", "43.96"),
            ("What is the volume of a cube with side length 3?", "27"),
            ("Calculate the area of a triangle with base 6 and height 4", "12"),
            ("What is the perimeter of a square with side length 5?", "20"),
            ("Find the area of a parallelogram with base 6 and height 4", "24"),
            ("What is the surface area of a cube with side length 3?", "54"),
            ("Calculate the area of a trapezoid with bases 4 and 6 and height 3", "15"),
            ("What is the volume of a rectangular prism with length 4, width 3, and height 2?", "24"),
            ("Find the area of a circle with radius 5 (use π = 3.14)", "78.5")
        ],
        "Angles and Lines": [
            ("What is the measure of a straight angle?", "180"),
            ("If two angles are complementary and one is 35°, what is the other?", "55"),
            ("What is the measure of each angle in an equilateral triangle?", "60"),
            ("If two angles are supplementary and one is 120°, what is the other?", "60"),
            ("What is the measure of a right angle?", "90"),
            ("What is the sum of the angles in a quadrilateral?", "360"),
            ("If two lines are perpendicular, what is the measure of the angle between them?", "90"),
            ("What is the measure of each angle in a regular hexagon?", "120"),
            ("If two angles are vertical angles and one is 45°, what is the other?", "45"),
            ("What is the measure of an acute angle?", "less than 90")
        ]
    },
    "Data Analysis": {
        "Statistics": [
            ("What is the mean of the numbers 2, 4, 6, 8, 10?", "6"),
            ("What is the median of 3, 5, 7, 9, 11?", "7"),
            ("What is the mode of 2, 2, 3, 3, 3, 4?", "3"),
            ("What is the range of 5, 8, 12, 15, 20?", "15"),
            ("What is the mean absolute deviation of 2, 4, 6, 8, 10?", "2.4"),
            ("What is the median of 2, 4, 6, 8, 10, 12?", "7"),
            ("What is the mode of 1, 2, 2, 3, 3, 3, 4?", "3"),
            ("What is the range of 10, 15, 20, 25, 30?", "20"),
            ("What is the mean of 3, 5, 7, 9, 11, 13?", "8"),
            ("What is the median of 1, 3, 5, 7, 9?", "5")
        ],
        "Probability": [
            ("What is the probability of rolling a 6 on a fair die?", "1/6"),
            ("If you flip a coin twice, what is the probability of getting heads both times?", "1/4"),
            ("What is the probability of drawing a red card from a standard deck?", "1/2"),
            ("If you roll two dice, what is the probability of getting a sum of 7?", "1/6"),
            ("What is the probability of drawing a face card from a standard deck?", "3/13"),
            ("If you flip a coin three times, what is the probability of getting all tails?", "1/8"),
            ("What is the probability of drawing an ace from a standard deck?", "1/13"),
            ("If you roll a die, what is the probability of getting an even number?", "1/2"),
            ("What is the probability of drawing a spade from a standard deck?", "1/4"),
            ("If you roll two dice, what is the probability of getting doubles?", "1/6")
        ]
    }
}

def generate_questions(num_questions: int = 20) -> List[Tuple[str, str, str, str]]:
    """
    Generate random questions from the question bank.
    Returns a list of tuples containing (subject, topic, question, answer).
    """
    questions = []
    all_subjects = list(question_bank.keys())
    
    while len(questions) < num_questions:
        subject = random.choice(all_subjects)
        topic = random.choice(list(question_bank[subject].keys()))
        question, answer = random.choice(question_bank[subject][topic])
        
        # Avoid duplicate questions
        if (subject, topic, question, answer) not in questions:
            questions.append((subject, topic, question, answer))
    
    return questions

def normalize_text(text: str) -> str:
    """
    Normalize text by removing special characters and extra spaces.
    """
    # Convert to lowercase
    text = text.lower()
    # Remove special characters and extra spaces
    text = re.sub(r'[^\w\s]', ' ', text)
    text = ' '.join(text.split())
    return text

def calculate_similarity(str1: str, str2: str) -> float:
    """
    Calculate the similarity between two strings using SequenceMatcher.
    Returns a value between 0 and 1, where 1 means identical.
    """
    return SequenceMatcher(None, str1, str2).ratio()

def check_answer(user_answer: str, correct_answer: str) -> bool:
    """
    Check if the user's answer matches the correct answer using flexible matching.
    Returns True if the answers are similar enough, False otherwise.
    """
    # Normalize both answers
    user_norm = normalize_text(user_answer)
    correct_norm = normalize_text(correct_answer)
    
    # Calculate similarity
    similarity = calculate_similarity(user_norm, correct_norm)
    
    # For mathematical answers, require exact match
    if any(c.isdigit() for c in correct_answer):
        return user_answer.strip() == correct_answer.strip()
    
    # For other answers, allow 80% similarity
    return similarity >= 0.8

def print_questions(questions: List[Tuple[str, str, str, str]]) -> None:
    """
    Print the generated questions and check answers.
    """
    print("\nFlorida B.E.S.T. Standards - 7th Grade Questions\n")
    print("=" * 50)
    
    score = 0
    total = len(questions)
    
    for i, (subject, topic, question, answer) in enumerate(questions, 1):
        print(f"\n{i}. Subject: {subject}")
        print(f"   Topic: {topic}")
        print(f"   Question: {question}")
        
        # Get user's answer
        user_answer = input("\nYour answer: ")
        
        # Check answer and show result
        is_correct = check_answer(user_answer, answer)
        if is_correct:
            print("✓ Correct!")
            score += 1
        else:
            print("✗ Incorrect")
            print(f"The correct answer was: {answer}")
            print("Note: For mathematical questions, exact answers are required.")
            print("For other questions, similar wordings are accepted.")
        
        print("-" * 50)
    
    # Show final score
    percentage = (score / total) * 100
    print(f"\nFinal Score: {score}/{total} ({percentage:.1f}%)")

def main():
    print("Generating 20 random questions from 7th grade Florida B.E.S.T. standards...")
    questions = generate_questions()
    print_questions(questions)

if __name__ == "__main__":
    main() 
