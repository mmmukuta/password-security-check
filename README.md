# Secure Password Checker (Terminal-based)

A Python application that performs a deep analysis of password strength. Unlike simple length-checkers, this tool evaluates complexity using statistical distribution of characters and cross-references with personal user data.

## Features
- **Personal Data Analysis:** Checks if the password contains your name, last name, or birth year to prevent social engineering risks.
- **Pattern Matching:** Detects common weak patterns like `123456`, `qwerty`, etc.
- **Character Distribution:** Calculates the percentage of numbers, uppercase letters, and special symbols.
- **Brute-Force Estimation:** Calculates the total number of possible combinations based on the character sets used.
- **Scoring System:** Provides a final security score out of 25 and a percentage-based rating.

## How It Works
1. The script asks for basic information (Name, Lastname, Birth Year).
2. It prompts for the password to analyze.
3. The algorithm runs through several checks:
   - **Length:** Points scaled from 0 to 10.
   - **Complexity:** Checks if characters are balanced (e.g., not too many numbers, enough symbols).
   - **Entropy:** Estimates how many variations an attacker would need to brute-force.

## Tech Stack
- **Language:** Python 3.x
- **Logic:** Conditional branching (if-else), String manipulation, Statistical math.

## Scoring Logic
- **0-10 pts:** Weak (High risk)
- **11-17 pts:** Fair (Low entropy)
- **18+ pts:** Excellent (Uncrackable with current tech)


## IS THIS FOR PRACTICE ? 
This project was created not only for technical practice but as a free tool to help people improve their digital safety. I believe that security should be accessible to everyone. I’ve shared this tool with my friends and community to help them protect their personal data, and I am committed to developing more useful, society-focused security tools in the future. There are also plans to develop an interface to make password verification more convenient and accessible to the entire community.
