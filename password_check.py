name = input("Write your name here")
lastname = input("Write your lastname here")
year = input("Write your year of birth here")
weak_patterns = ["1234", "12345", "123456", "qwerty", "password", "1111"]

password = input("Write your password to check")

# Alphabet, Numbers, Special Characters
alpha = "abcdefghijklmnopqrstuvwxyz"
nums = "0123456789"
signs = "!@#$%^&*()-_+=<>?/"

# Counters of what a password consists of
countalpha = 0
countnum = 0
countsign = 0
countupper = 0

# Comparison with regular passwords
checkname = ""
checklastname = ""
checkyear = ""

# Variables
result = 0
alphasize = 0

for ch in password:
    if ch in alpha:
        countalpha += 1

    if ch in nums:
        countnum += 1

    if ch in signs:
        countsign += 1

    if ch.isupper():
        countupper += 1

# Points for password length
if len(password) < 8:
    result = 0
elif 8 <= len(password) <= 14:
    result += 3
elif 14 < len(password) <= 26:
    result += 5
elif len(password) > 26:
    result += 10
    print("WHO ARE YOU ???")

# Points for numbers
numprocent = (countnum / len(password)) * 100  # Percentage of digits in password
if numprocent >= 20 and numprocent <= 40:
    result += 5
elif numprocent > 40 and numprocent <= 70:
    result += 2
elif numprocent < 20 or numprocent > 70:
    result = 0

# Points for letters
alphaprocent = (countalpha / len(password)) * 100  # Percentage of letters in a password
if (countupper / len(password)) * 100 >= 10 and (
    countupper / len(password)
) * 100 < 30:  # Процент больших букв в пароле
    result += 5
if alphaprocent > 30 and alphaprocent < 60:
    result += 5
elif alphaprocent < 30 or alphaprocent > 60:
    result += 0

# Points for special signs
signprocent = (countsign / len(password)) * 100  # Percentage of special characters in a password
if signprocent >= 15 and signprocent <= 30:
    result += 5
elif signprocent > 30 and signprocent < 80:
    result += 2
elif signprocent < 15 or signprocent >= 80:
    result += 0

# The presence of a common combination in the password
for paterns in weak_patterns:
    if paterns in password.lower():
        result -= 5

# Ability to attack using a custom wordlist
if (
    name.lower() in password.lower()
    or lastname.lower() in password.lower()
    or year in password
):
    result -= 5

if countalpha > 0:
    alphasize += 26
if countupper > 0:
    alphasize += 26
if countnum > 0:
    alphasize += 10
if countsign > 0:
    alphasize += 32

bruteforce = (
    f"There are {alphasize**len(password)} possible variations of your password."
)

if 0 <= result <= 10:
    print(
        f"Password security percentage {(result/25)*100}% | Scored points {result} out of 25"
    )
    print(
        "Your password is too weak. High risk of a successful brute-force attack.",
        "\n",
        bruteforce,
    )
elif 10 < result <= 17:
    print(
        f"Password security percentage {(result/25)*100}% | Scored points {result} out of 25"
    )
    print(
        "Fair protection, but entropy is low. Consider adding more symbols or length.",
        "\n",
        bruteforce,
    )
elif 17 < result:
    print(
        f"Password security percentage {(result/25)*100}% | Scored points {result} out of 25 "
    )
    print(
        "Excellent entropy. This password is practically uncrackable with current technology.",
        "\n",
        bruteforce,
    )
