# 🔐 Password Tool

**- A Python command-line utility designed to generate secure random passwords and evaluate the strength of existing ones**.

## ✨ Features

**🔑 Password Generation**
* Generates a random password that includes uppercase letters, lowercase letters, digits, and special characters.
* Enforces a minimum length of 4 to ensure all character types are included.
* Generates passwords with a default length of 8 characters via the interactive menu.

**💪 Password Strength Checker**
* Evaluates password strength based on length and character variety.
* Checks for the presence of a length greater than or equal to 8, lowercase letters, uppercase letters, digits, and punctuation.
* Categorizes the evaluated password as "Weak", "Moderate", or "Strong" based on a calculated score.

**🖥️ Interactive Menu**
* Provides a simple text-based menu to easily choose between generating a password, checking a password's strength, or exiting the tool.

---

## 🛠️ Technologies Used

* 🐍 **Python 3**
* Built-in `random` and `string` modules (No external dependencies required).

---

## 🚀 How to Run

1. Ensure you have Python installed on your system.
2. Save the code to a file (e.g., `password_tool.py`).
3. Run the program using your terminal or command prompt:

```bash
python password_tool.py
```
## 📋 Menu Options
​When you run the tool, you are presented with the following interface:
```bash
=== Password Tool Menu ===
1. Generate password
2. Check password strength
3. Exit
```
**Option 1: Generate password**
​*Selecting 1 automatically creates and displays an 8-character password containing a random mix of letters, numbers, and symbols.*
​**Option 2: Check password strength**
​*Selecting 2 prompts you to input a password, which is then scored and categorized as Weak, Moderate, or Strong.*  
​**Option 3: Exit**
​*Selecting 3 prints a goodbye message and ends the program loop. Invalid selections will prompt you to choose 1, 2, or 3 again.*

## 💡 Usage Examples
​Below is a demonstration of how the tool interacts in the terminal.
​***Generating a Password:***
```bash
=== Password Tool Menu ===
1. Generate password
2. Check password strength
3. Exit
Choose an option (1-3): 2

Enter password to evaluate: monkey123
Password strength: Weak
```
```
Enter password to evaluate: P@ssw0rd2024!
Password strength: Strong
```
## 🔮 Future Improvements
​[ ] Allow the user to specify custom password lengths directly from the CLI menu.
​[ ] Add the ability to copy the generated password directly to the clipboard.
​[ ] Implement secrets module instead of random for even stronger cryptographic security.
​[ ] Add a bulk generation feature (e.g., generate 10 passwords at once).
## 👨‍💻 Author
​***Developed by Yash Kumar Singh.***

