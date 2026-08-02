import string

def check_password_strength(password):
    score = 0
    feedback = []

    # 1. Length Check
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Password is too short (minimum 8 characters).")

    # 2. Character Set Checks
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)

    if has_upper: 
        score += 1
    else: 
        feedback.append("Add uppercase letters.")

    if has_lower: 
        score += 1
    else: 
        feedback.append("Add lowercase letters.")

    if has_digit: 
        score += 1
    else: 
        feedback.append("Add numbers.")

    if has_special: 
        score += 1
    else: 
        feedback.append("Add special characters (!@#$...).")

    return score, feedback

# Main program execution
if __name__ == "__main__":
    user_pass = input("Enter a password to analyze: ")
    score, feedback = check_password_strength(user_pass)

    print(f"\nPassword Score: {score}/6")
    if score < 4:
        print("Status: WEAK ❌")
    elif score < 6:
        print("Status: MODERATE ⚠️")
    else:
        print("Status: STRONG ✅")

    if feedback:
        print("\nRecommendations to improve your password:")
        for tip in feedback:
            print(f" - {tip}")