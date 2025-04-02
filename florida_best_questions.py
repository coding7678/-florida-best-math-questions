import random
import math
from datetime import datetime
import re
from typing import List, Tuple, Dict, Any

# Comprehensive question bank with detailed explanations
question_bank = {
    "Number Sense and Operations": {
        "Rational Numbers": [
            ("What is the sum of -3/4 and 5/6?", "1/12", 
             "To add fractions with different denominators, find a common denominator (12 in this case). "
             "-3/4 becomes -9/12 and 5/6 becomes 10/12. Adding these gives 1/12."),
            ("If you multiply -2/3 by 3/4, what is the result?", "-1/2",
             "Multiply numerators (-2 × 3 = -6) and denominators (3 × 4 = 12). "
             "Simplify -6/12 to -1/2 by dividing both by 6."),
            ("What is the decimal equivalent of 7/8?", "0.875",
             "Divide 7 by 8 using long division or convert to a decimal by dividing 7 by 8."),
            ("Convert 0.6 to a fraction in simplest form.", "3/5",
             "0.6 = 6/10. Simplify by dividing both numerator and denominator by 2 to get 3/5."),
            ("What is -5/6 ÷ 2/3?", "-5/4",
             "To divide fractions, multiply by the reciprocal. -5/6 × 3/2 = -15/12 = -5/4."),
            ("Add 1/3 and 2/5.", "11/15",
             "Find common denominator (15): 1/3 = 5/15, 2/5 = 6/15. Add: 5/15 + 6/15 = 11/15."),
            ("What is 3/4 of 16?", "12",
             "Multiply 3/4 by 16: 3/4 × 16 = 48/4 = 12."),
            ("Convert 0.75 to a fraction.", "3/4",
             "0.75 = 75/100. Simplify by dividing both by 25: 75/100 = 3/4."),
            ("What is 2/3 × 3/4?", "1/2",
             "Multiply numerators (2 × 3 = 6) and denominators (3 × 4 = 12). Simplify 6/12 to 1/2."),
            ("Divide 5/6 by 2/3.", "5/4",
             "Multiply by reciprocal: 5/6 × 3/2 = 15/12 = 5/4.")
        ],
        "Integer Operations": [
            ("What is the product of -8 and 6?", "-48",
             "When multiplying a negative and positive number, the result is negative. 8 × 6 = 48, so -8 × 6 = -48."),
            ("If you subtract -15 from 7, what is the result?", "22",
             "Subtracting a negative is the same as adding a positive. 7 - (-15) = 7 + 15 = 22."),
            ("What is the quotient of -56 and -7?", "8",
             "When dividing two negative numbers, the result is positive. 56 ÷ 7 = 8."),
            ("Find the sum of -12, 8, and -5.", "-9",
             "Add the numbers: -12 + 8 + (-5) = -4 + (-5) = -9."),
            ("What is the result of -3 × (-4) × (-2)?", "-24",
             "Multiply from left to right: -3 × (-4) = 12, then 12 × (-2) = -24."),
            ("What is -20 ÷ 4?", "-5",
             "When dividing a negative by a positive, the result is negative. 20 ÷ 4 = 5, so -20 ÷ 4 = -5."),
            ("Find the sum of -7 and -3.", "-10",
             "When adding two negative numbers, add their absolute values and keep the negative sign."),
            ("What is 5 × (-6)?", "-30",
             "When multiplying a positive and negative number, the result is negative. 5 × 6 = 30, so 5 × (-6) = -30."),
            ("Calculate -9 - (-4).", "-5",
             "Subtracting a negative is like adding a positive. -9 - (-4) = -9 + 4 = -5."),
            ("What is the result of -2 × 3 × (-5)?", "30",
             "Multiply from left to right: -2 × 3 = -6, then -6 × (-5) = 30.")
        ]
    },
    "Algebra": {
        "Linear Equations": [
            ("Solve for x: 3x + 7 = 22", "5",
             "Subtract 7 from both sides: 3x = 15. Then divide both sides by 3: x = 5."),
            ("If 2(x - 4) = 10, what is x?", "9",
             "First divide both sides by 2: x - 4 = 5. Then add 4 to both sides: x = 9."),
            ("What is the solution to 5x - 3 = 2x + 9?", "4",
             "Subtract 2x from both sides: 3x - 3 = 9. Add 3 to both sides: 3x = 12. Divide by 3: x = 4."),
            ("Solve: 4(x + 2) = 3(x - 1)", "-11",
             "Distribute: 4x + 8 = 3x - 3. Subtract 3x: x + 8 = -3. Subtract 8: x = -11."),
            ("If 2/3x = 6, what is x?", "9",
             "Multiply both sides by 3/2: x = 6 × 3/2 = 18/2 = 9."),
            ("Solve: 2x + 5 = 17", "6",
             "Subtract 5 from both sides: 2x = 12. Divide by 2: x = 6."),
            ("What is x if 3(x + 2) = 15?", "3",
             "Divide both sides by 3: x + 2 = 5. Subtract 2: x = 3."),
            ("Solve: 5x - 2 = 3x + 8", "5",
             "Subtract 3x: 2x - 2 = 8. Add 2: 2x = 10. Divide by 2: x = 5."),
            ("If 4x = 20, what is x?", "5",
             "Divide both sides by 4: x = 20 ÷ 4 = 5."),
            ("Solve: 2x + 3 = 7", "2",
             "Subtract 3: 2x = 4. Divide by 2: x = 2.")
        ],
        "Inequalities": [
            ("Solve: 2x + 5 > 13", "x > 4",
             "Subtract 5 from both sides: 2x > 8. Divide by 2: x > 4."),
            ("What values of x satisfy -3x ≤ 12?", "x ≥ -4",
             "Divide both sides by -3 and reverse the inequality: x ≥ -4."),
            ("Solve: 4(x - 2) < 8", "x < 4",
             "Divide both sides by 4: x - 2 < 2. Add 2: x < 4."),
            ("If 2x + 1 ≥ 5, what is x?", "x ≥ 2",
             "Subtract 1: 2x ≥ 4. Divide by 2: x ≥ 2."),
            ("Solve: -2x + 3 > 7", "x < -2",
             "Subtract 3: -2x > 4. Divide by -2 and reverse: x < -2."),
            ("What values of x satisfy x + 3 < 8?", "x < 5",
             "Subtract 3 from both sides: x < 5."),
            ("Solve: 3x - 2 ≥ 10", "x ≥ 4",
             "Add 2: 3x ≥ 12. Divide by 3: x ≥ 4."),
            ("If -4x > 16, what is x?", "x < -4",
             "Divide both sides by -4 and reverse: x < -4."),
            ("Solve: 2(x + 1) ≤ 6", "x ≤ 2",
             "Divide by 2: x + 1 ≤ 3. Subtract 1: x ≤ 2."),
            ("What values of x satisfy 5x + 2 > 12?", "x > 2",
             "Subtract 2: 5x > 10. Divide by 5: x > 2.")
        ]
    },
    "Geometry": {
        "Area and Perimeter": [
            ("Find the area of a rectangle with length 8 units and width 5 units.", "40 square units",
             "Area = length × width = 8 × 5 = 40 square units."),
            ("What is the perimeter of a square with side length 6 units?", "24 units",
             "Perimeter = 4 × side length = 4 × 6 = 24 units."),
            ("Calculate the area of a triangle with base 10 units and height 6 units.", "30 square units",
             "Area = 1/2 × base × height = 1/2 × 10 × 6 = 30 square units."),
            ("Find the circumference of a circle with radius 4 units. (Use π = 3.14)", "25.12 units",
             "Circumference = 2πr = 2 × 3.14 × 4 = 25.12 units."),
            ("What is the area of a circle with diameter 10 units? (Use π = 3.14)", "78.5 square units",
             "Radius = diameter/2 = 5. Area = πr² = 3.14 × 5² = 78.5 square units."),
            ("Find the area of a parallelogram with base 7 units and height 4 units.", "28 square units",
             "Area = base × height = 7 × 4 = 28 square units."),
            ("What is the perimeter of a rectangle with length 9 units and width 3 units?", "24 units",
             "Perimeter = 2(length + width) = 2(9 + 3) = 2(12) = 24 units."),
            ("Calculate the area of a trapezoid with bases 5 and 7 units and height 3 units.", "18 square units",
             "Area = 1/2(b₁ + b₂)h = 1/2(5 + 7)3 = 1/2(12)3 = 18 square units."),
            ("Find the circumference of a circle with diameter 6 units. (Use π = 3.14)", "18.84 units",
             "Radius = diameter/2 = 3. Circumference = 2πr = 2 × 3.14 × 3 = 18.84 units."),
            ("What is the area of a square with side length 4 units?", "16 square units",
             "Area = side length² = 4² = 16 square units.")
        ],
        "Volume": [
            ("Find the volume of a rectangular prism with length 4 units, width 3 units, and height 5 units.", "60 cubic units",
             "Volume = length × width × height = 4 × 3 × 5 = 60 cubic units."),
            ("What is the volume of a cube with edge length 3 units?", "27 cubic units",
             "Volume = edge length³ = 3³ = 27 cubic units."),
            ("Calculate the volume of a cylinder with radius 2 units and height 6 units. (Use π = 3.14)", "75.36 cubic units",
             "Volume = πr²h = 3.14 × 2² × 6 = 75.36 cubic units."),
            ("Find the volume of a cone with radius 3 units and height 4 units. (Use π = 3.14)", "37.68 cubic units",
             "Volume = 1/3πr²h = 1/3 × 3.14 × 3² × 4 = 37.68 cubic units."),
            ("What is the volume of a sphere with radius 2 units? (Use π = 3.14)", "33.49 cubic units",
             "Volume = 4/3πr³ = 4/3 × 3.14 × 2³ = 33.49 cubic units."),
            ("Find the volume of a rectangular prism with length 6 units, width 2 units, and height 3 units.", "36 cubic units",
             "Volume = length × width × height = 6 × 2 × 3 = 36 cubic units."),
            ("What is the volume of a cube with edge length 4 units?", "64 cubic units",
             "Volume = edge length³ = 4³ = 64 cubic units."),
            ("Calculate the volume of a cylinder with radius 3 units and height 5 units. (Use π = 3.14)", "141.3 cubic units",
             "Volume = πr²h = 3.14 × 3² × 5 = 141.3 cubic units."),
            ("Find the volume of a cone with radius 2 units and height 6 units. (Use π = 3.14)", "25.12 cubic units",
             "Volume = 1/3πr²h = 1/3 × 3.14 × 2² × 6 = 25.12 cubic units."),
            ("What is the volume of a sphere with radius 3 units? (Use π = 3.14)", "113.04 cubic units",
             "Volume = 4/3πr³ = 4/3 × 3.14 × 3³ = 113.04 cubic units.")
        ]
    },
    "Data Analysis": {
        "Measures of Central Tendency": [
            ("Find the mean of the numbers: 5, 8, 12, 15, 20", "12",
             "Add all numbers (60) and divide by count (5): 60 ÷ 5 = 12."),
            ("What is the median of: 3, 7, 9, 12, 15, 18?", "10.5",
             "Arrange in order and average middle two numbers: (9 + 12) ÷ 2 = 10.5."),
            ("Find the mode of: 2, 4, 4, 6, 6, 6, 8", "6",
             "6 appears most frequently (3 times)."),
            ("Calculate the range of: 10, 15, 20, 25, 30", "20",
             "Range = maximum - minimum = 30 - 10 = 20."),
            ("What is the mean of: 2, 4, 6, 8, 10, 12?", "7",
             "Add all numbers (42) and divide by count (6): 42 ÷ 6 = 7."),
            ("Find the median of: 1, 3, 5, 7, 9", "5",
             "The middle number in an odd set of ordered numbers is the median."),
            ("What is the mode of: 2, 2, 3, 3, 4, 4, 5?", "No mode",
             "All numbers appear the same number of times (once)."),
            ("Calculate the range of: 5, 8, 12, 15, 20, 25", "20",
             "Range = maximum - minimum = 25 - 5 = 20."),
            ("What is the mean of: 10, 20, 30, 40, 50?", "30",
             "Add all numbers (150) and divide by count (5): 150 ÷ 5 = 30."),
            ("Find the median of: 2, 4, 6, 8, 10, 12, 14", "8",
             "The middle number in an odd set of ordered numbers is the median.")
        ],
        "Probability": [
            ("If you roll a fair six-sided die, what is the probability of getting a 3?", "1/6",
             "There is 1 favorable outcome (3) out of 6 possible outcomes."),
            ("What is the probability of drawing a red card from a standard deck?", "1/2",
             "There are 26 red cards out of 52 total cards: 26/52 = 1/2."),
            ("If you flip a coin twice, what is the probability of getting heads both times?", "1/4",
             "Probability of first heads (1/2) × probability of second heads (1/2) = 1/4."),
            ("What is the probability of rolling an even number on a six-sided die?", "1/2",
             "There are 3 even numbers (2,4,6) out of 6 possible outcomes: 3/6 = 1/2."),
            ("If you draw one card from a deck, what is the probability of getting a face card?", "3/13",
             "There are 12 face cards out of 52 total cards: 12/52 = 3/13."),
            ("What is the probability of rolling a number less than 3 on a six-sided die?", "1/3",
             "There are 2 favorable outcomes (1,2) out of 6 possible outcomes: 2/6 = 1/3."),
            ("If you draw one card, what is the probability of getting a heart?", "1/4",
             "There are 13 hearts out of 52 total cards: 13/52 = 1/4."),
            ("What is the probability of flipping a coin and getting tails?", "1/2",
             "There is 1 favorable outcome (tails) out of 2 possible outcomes."),
            ("If you roll two dice, what is the probability of getting a sum of 7?", "1/6",
             "There are 6 favorable outcomes out of 36 possible outcomes: 6/36 = 1/6."),
            ("What is the probability of drawing a king from a deck?", "1/13",
             "There are 4 kings out of 52 total cards: 4/52 = 1/13.")
        ]
    }
}

class MathWorksheetGenerator:
    def __init__(self):
        self.questions = []
        self.answers = []
        self.explanations = []
        
    def generate_worksheet(self):
        """Generate a complete worksheet with 20 questions from the comprehensive question bank"""
        all_subjects = list(question_bank.keys())
        
        while len(self.questions) < 20:
            subject = random.choice(all_subjects)
            topic = random.choice(list(question_bank[subject].keys()))
            question, answer, explanation = random.choice(question_bank[subject][topic])
            
            # Avoid duplicate questions
            if (subject, topic, question, answer, explanation) not in zip(
                [q[0] for q in self.questions],
                [q[1] for q in self.questions],
                [q[2] for q in self.questions],
                self.answers,
                self.explanations
            ):
                self.questions.append((subject, topic, question))
                self.answers.append(answer)
                self.explanations.append(explanation)
    
    def print_worksheet(self):
        """Print the worksheet with questions and answers"""
        print("\n" + "="*50)
        print("7th Grade Math Worksheet")
        print(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("="*50 + "\n")
        
        print("Questions:")
        print("-"*50)
        for i, (subject, topic, question) in enumerate(self.questions, 1):
            print(f"{i}. Subject: {subject}")
            print(f"   Topic: {topic}")
            print(f"   Question: {question}\n")
            
        print("\n" + "="*50)
        print("Answer Key:")
        print("-"*50)
        for i, (answer, explanation) in enumerate(zip(self.answers, self.explanations), 1):
            print(f"{i}. Answer: {answer}")
            print(f"   Explanation: {explanation}\n")
        print("="*50)

def main():
    generator = MathWorksheetGenerator()
    generator.generate_worksheet()
    generator.print_worksheet()

if __name__ == "__main__":
    main() 
