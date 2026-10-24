"""
CodeAlpha Python Programming Internship - Task 4
Project: Rule-Based Chatbot (Console)
"""

import random
import time
from datetime import datetime

BOT_NAME = "CodeBuddy"

GREETINGS = [
    "Hello {name}! Wonderful to see you today.",
    "Hey {name}! How can I help you?",
    "Hi there, {name}! Hope you are having a great day!"
]

GOODBYES = [
    "Goodbye {name}! Have an amazing day ahead!",
    "Bye {name}! Keep coding and learning!",
    "Catch you later, {name}! Take care!"
]

JOKES = [
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "There are 10 types of people: those who understand binary, and those who don't.",
    "Why was the JavaScript developer sad? Because he didn't know how to 'null' his feelings.",
    "A SQL query walks into a bar, walks up to two tables and asks: 'Can I join you?'",
    "Real programmers count from 0, not 1!"
]

QUOTES = [
    "'The only way to learn a new language is by writing programs in it.' — Dennis Ritchie",
    "'First, solve the problem. Then, write the code.' — John Johnson",
    "'Experience is the name everyone gives to their mistakes.' — Oscar Wilde",
    "'Simplicity is the soul of efficiency.' — Austin Freeman",
    "'Make it work, make it right, make it fast.' — Kent Beck"
]


def clean_input(text):
    """Lowercase text and strip whitespace and common punctuation."""
    cleaned = text.lower().strip()
    for ch in "!?.,;:'\"":
        cleaned = cleaned.replace(ch, "")
    return cleaned


def show_help():
    """Return a clean list of topics the user can ask the bot."""
    topics = [
        "Greetings ('hello', 'hi', 'hey')", "Identity ('who are you', 'your name')",
        "Capabilities ('what can you do')", "Time & Date ('what time is it', 'today date')",
        "Entertainment ('tell me a joke', 'inspire me')", "Internship ('about codealpha')",
        "Small Talk ('i am sad', 'i am happy', 'i am bored')", "Courtesy & Exit ('thank you', 'bye')"
    ]
    return "Here are things you can ask me:\n • " + "\n • ".join(topics)


def get_response(cleaned, user_name):
    """Determine response and exit flag based on keyword matching."""
    words = cleaned.split()

    # 1. Exit
    if any(k in cleaned for k in ["bye", "exit", "quit", "goodbye"]):
        return random.choice(GOODBYES).format(name=user_name), True
    # 2. Greetings
    if any(k in words for k in ["hello", "hi", "hey", "greetings"]):
        return random.choice(GREETINGS).format(name=user_name), False
    # 3. How are you
    if "how are you" in cleaned or "how r u" in cleaned:
        return f"I'm feeling great and ready to chat, {user_name}! How are you doing?", False
    # 4. Identity / Who are you
    if any(k in cleaned for k in ["who are you", "your name"]):
        return f"I am {BOT_NAME}, your friendly assistant for the CodeAlpha internship!", False
    # 5. Capabilities / What can you do
    if "what can you do" in cleaned or "features" in cleaned:
        return f"I can tell jokes, share quotes, give time/date, or just chat! Type 'help' to see all.", False
    # 6. Emotions & Small Talk (checked before date to avoid 'today' conflict)
    if any(k in words for k in ["sad", "unhappy", "depressed", "upset"]):
        return f"I'm sorry you're feeling down, {user_name}. Every bug has a fix! Want a joke?", False
    if any(k in words for k in ["happy", "excited", "joyful"]):
        return f"That's wonderful to hear, {user_name}! Keep spreading the positive energy!", False
    if "bored" in words:
        return f"Bored? Ask me to 'tell me a joke' or share a 'quote' to brighten your day!", False
    # 7. Current Time
    if "time" in words or "clock" in words or "what time" in cleaned:
        return f"The current time is {datetime.now().strftime('%I:%M %p')}.", False
    # 8. Today's Date
    if "date" in words or "what day" in cleaned or "today date" in cleaned or "todays date" in cleaned:
        return f"Today's date is {datetime.now().strftime('%A, %B %d, %Y')}.", False
    # 9. Joke
    if any(k in words for k in ["joke", "jokes", "funny"]):
        return random.choice(JOKES), False
    # 10. Motivational Quote
    if any(k in words for k in ["quote", "quotes", "motivation", "inspire"]):
        return random.choice(QUOTES), False
    # 11. Gratitude / Thanks
    if any(k in words for k in ["thank", "thanks", "thx"]):
        return f"You're very welcome, {user_name}! Always happy to help.", False
    # 12. About CodeAlpha
    if "codealpha" in cleaned or "internship" in cleaned:
        return "CodeAlpha offers fantastic internships empowering students in Python and tech!", False
    # 13. Help
    if "help" in words or "options" in words or "menu" in words:
        return show_help(), False
    # 14. Fallback
    return f"I'm sorry {user_name}, I didn't quite catch that. Type 'help' to see what I can do!", False


def save_chat_log(chat_history):
    """Save user and bot messages with timestamps to chat_log.txt."""
    with open("chat_log.txt", "w", encoding="utf-8") as f:
        f.write(f"CHAT LOG - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n" + "=" * 45 + "\n")
        for sender, msg, ts in chat_history:
            f.write(f"[{ts}] {sender}: {msg}\n")
    print(f"\n[System]: Chat log successfully saved to 'chat_log.txt'.")


def chat():
    """Run interactive chat session with typing delay and log tracking."""
    chat_history = []
    print("\n" + "=" * 42)
    print(f"       WELCOME TO {BOT_NAME.upper()}!       ")
    print("=" * 42)
    name = input("Enter your name to begin: ").strip() or "Friend"
    welcome_msg = f"Nice to meet you, {name}! Type 'help' for options or 'bye' to exit."
    print(f"\n{BOT_NAME}: {welcome_msg}")
    chat_history.append((BOT_NAME, welcome_msg, datetime.now().strftime("%H:%M:%S")))

    while True:
        raw_input = input(f"\n{name}: ").strip()
        if not raw_input:
            print(f"{BOT_NAME}: You didn't enter anything! Type 'help' if you're not sure what to ask.")
            continue
        ts = datetime.now().strftime("%H:%M:%S")
        chat_history.append((name, raw_input, ts))
        cleaned = clean_input(raw_input)
        reply, should_exit = get_response(cleaned, name)

        time.sleep(0.3)
        print(f"{BOT_NAME}: {reply}")
        chat_history.append((BOT_NAME, reply, datetime.now().strftime("%H:%M:%S")))
        if should_exit:
            break

    save_chat_log(chat_history)


def main():
    """Entry point with graceful exit on Ctrl+C."""
    try:
        chat()
    except KeyboardInterrupt:
        print("\n\n[System]: Chat closed gracefully. Goodbye!")


if __name__ == "__main__":
    main()
