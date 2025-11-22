import sqlite3

# -----------------------------
# Database Setup
# -----------------------------
def create_table():
    conn = sqlite3.connect("loan.db")
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS loan_applications (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT,
                        age INTEGER,
                        salary INTEGER,
                        credit_score INTEGER,
                        loan_amount INTEGER,
                        status TEXT
                    )''')
    conn.commit()
    conn.close()


# -----------------------------
# Eligibility Check Logic
# -----------------------------
def check_eligibility(age, salary, credit_score):
    if age < 21:
        return "Rejected: Age Criteria"
    if salary < 25000:
        return "Rejected: Low Salary"
    if credit_score < 650:
        return "Pending: Manual Review"
    return "Approved"


# -----------------------------
# Insert Record into Database
# -----------------------------
def save_to_db(name, age, salary, credit_score, loan_amount, status):
    conn = sqlite3.connect("loan.db")
    cursor = conn.cursor()

    cursor.execute("""INSERT INTO loan_applications 
                      (name, age, salary, credit_score, loan_amount, status)
                      VALUES (?, ?, ?, ?, ?, ?)""",
                   (name, age, salary, credit_score, loan_amount, status))

    conn.commit()
    conn.close()


# -----------------------------
# MAIN PROGRAM WITH USER INPUT
# -----------------------------
def main():
    create_table()

    print("\n----- LOAN APPROVAL SYSTEM -----\n")

    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    salary = int(input("Enter your monthly salary (in ₹): "))
    credit_score = int(input("Enter your credit score (300-900): "))
    loan_amount = int(input("Enter desired loan amount (in ₹): "))

    # Eligibility Check
    status = check_eligibility(age, salary, credit_score)

    # Save to Database
    save_to_db(name, age, salary, credit_score, loan_amount, status)

    print("\n------------------------------------")
    print(" Loan Application Status:", status)
    print("------------------------------------")

    print("\nYour data has been saved successfully!")


# Run the project
if __name__ == "__main__":
    main()