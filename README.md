# CodeAlpha_BasicChatbot - Task 4

A clean, beginner-friendly, console-based **Rule-Based Chatbot** developed in Python for **Task 4** of the **CodeAlpha Python Programming Internship**.

---

## 📌 Project Overview
**CodeBuddy** is a rule-based conversational assistant built purely in standard Python (console-only) without any third-party NLP or AI/ML libraries. The chatbot identifies user intent through keyword matching and returns context-aware, personalized predefined responses.

This project demonstrates core programming fundamentals, string normalization, flow control, randomized responses, modular function design, and file persistence.

---

## 🚀 Key Features
- **100% Pure Standard Python**: Zero external dependencies, web APIs, or machine learning libraries required.
- **Personalized Experience**: Asks for the user's name at the start and addresses them naturally throughout the conversation.
- **Smart Input Normalization**:
  - Automatically lowercases text and strips leading/trailing whitespaces.
  - Removes common punctuation (`!`, `?`, `.`, `,`, `;`, quotes) so that `"Hello!!"`, `"HELLO"`, and `"hello"` trigger the same intent.
- **12+ Distinct Conversational Intents**:
  1. **Greetings**: Random variations for friendly welcomes.
  2. **Well-being**: Responses to "how are you".
  3. **Identity**: Introduces itself as CodeBuddy.
  4. **Capabilities**: Explains what it can do.
  5. **Live Time**: Formatted current time using Python's `datetime` module.
  6. **Live Date**: Today's formatted calendar date and day.
  7. **Jokes**: Random selection from a bank of 5 programmer jokes.
  8. **Quotes**: Random selection from 5 famous software engineering quotes.
  9. **Gratitude**: Warm responses to "thank you".
  10. **About CodeAlpha**: Information regarding the CodeAlpha internship.
  11. **Emotions & Small Talk**: Empathetic replies to feelings of sadness, happiness, or boredom.
  12. **Help Menu**: Overview of available questions and keywords.
  13. **Exit / Goodbye**: Friendly sign-off variations.
- **Graceful Fallback**: Suggests typing `'help'` when an intent is unrecognized.
- **Simulated Typing Delay**: Uses a short `time.sleep` delay to emulate real-time human interaction.
- **Chat History Logging**: Automatically saves the full conversation with timestamps to `chat_log.txt` on exit.
- **Error Handling**: Gracefully handles empty inputs and `Ctrl+C` (`KeyboardInterrupt`) termination.

---

## 🛠️ Concepts & Technologies Used
- **Standard Library Modules**: `random` (for response variation), `datetime` (for real-time date/time and logging), `time` (for typing effect).
- **Control Flow**: `if-elif-else` conditional branching and `while` loop for conversation lifecycle.
- **String Manipulation**: `.lower()`, `.strip()`, `.replace()`, `.split()`, and formatted f-strings.
- **Data Structures**: Lists for jokes, quotes, greetings, and tuple lists for chat history tracking.
- **File Handling**: Writing timestamped conversation logs to disk using `with open(...)`.
- **Software Design**: PEP 8 compliance, single-responsibility functions, and `if __name__ == "__main__":` entry point.

---

## 💻 How to Run the Project

### Prerequisites
- Python 3.x installed on your computer.

### Execution
1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/CodeAlpha_BasicChatbot.git
   cd CodeAlpha_BasicChatbot
   ```
2. Run the chatbot in terminal or command prompt:
   ```bash
   python chatbot.py
   ```

---

## 🎮 Sample Conversation

```text
==========================================
       WELCOME TO CODEBUDDY!       
==========================================
Enter your name to begin: Aarav

CodeBuddy: Nice to meet you, Aarav! Type 'help' for options or 'bye' to exit.

Aarav: Hello!!
CodeBuddy: Hello Aarav! Wonderful to see you today.

Aarav: How are you doing today?
CodeBuddy: I'm feeling great and ready to chat, Aarav! How are you doing?

Aarav: Tell me a funny joke
CodeBuddy: Why do programmers prefer dark mode? Because light attracts bugs!

Aarav: What time is it now?
CodeBuddy: The current time is 11:12 PM.

Aarav: Thank you so much CodeBuddy!
CodeBuddy: You're very welcome, Aarav! Always happy to help.

Aarav: bye
CodeBuddy: Goodbye Aarav! Have an amazing day ahead!

[System]: Chat log successfully saved to 'chat_log.txt'.
```

---

## 📄 Exported Chat Log (`chat_log.txt`)

```text
CHAT LOG - 2026-10-24 23:12:12
=============================================
[23:12:08] CodeBuddy: Nice to meet you, Aarav! Type 'help' for options or 'bye' to exit.
[23:12:08] Aarav: Hello!!
[23:12:08] CodeBuddy: Hello Aarav! Wonderful to see you today.
[23:12:08] Aarav: How are you doing today?
[23:12:09] CodeBuddy: I'm feeling great and ready to chat, Aarav! How are you doing?
[23:12:10] Aarav: Tell me a funny joke
[23:12:10] CodeBuddy: Why do programmers prefer dark mode? Because light attracts bugs!
[23:12:12] Aarav: bye
[23:12:12] CodeBuddy: Goodbye Aarav! Have an amazing day ahead!
```

---

## 🔮 Future Improvements
- Integrate fuzzy string matching (`thefuzz` / Levenshtein distance) to handle spelling mistakes.
- Load jokes, quotes, and intents dynamically from an external JSON file.
- Connect a graphical user interface (GUI) using Tkinter or CustomTkinter.

---

## 👤 Author
- **Intern Name**: Beginner Intern
- **Internship**: Python Programming Intern at [CodeAlpha](https://www.linkedin.com/company/codealpha/)
