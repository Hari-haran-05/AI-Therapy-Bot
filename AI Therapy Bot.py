def get_emotion_response(user_input):
    user_input = user_input.lower()
    
    happy_words = ["happy", "good", "great", "excited", "thankful", "joy"]
    sad_words = ["sad", "upset", "depressed", "lonely", "bad", "cry"]
    anxious_words = ["anxious", "worried", "nervous", "panic", "scared"]
    angry_words = ["angry", "mad", "furious", "irritated", "annoyed"]

    if any(word in user_input for word in happy_words):
        return "😊 I'm glad you're feeling good! Keep focusing on the positives in your life."
    elif any(word in user_input for word in sad_words):
        return "😔 I'm here for you. It's okay to feel sad sometimes. Want to talk more about it?"
    elif any(word in user_input for word in anxious_words):
        return "🧘 Take a deep breath. Try to breathe in for 4 seconds, hold for 4, and breathe out for 4. You’re not alone."
    elif any(word in user_input for word in angry_words):
        return "😡 I hear that you're angry. Do you want to talk about what's bothering you?"
    else:
        return "🤔 Thank you for sharing. Do you want to tell me more about how you're feeling?"

def main():
    print("🌿 Welcome to your AI Therapy Companion 🌿")
    print("I'm here to listen. How are you feeling today?\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("AI Bot: Thank you for talking with me today. Take care of yourself. 💙")
            break
        response = get_emotion_response(user_input)
        print("AI Bot:", response)

if __name__ == "__main__":
    main()

