# mood_responses.py
def mood_response(mood):
    mood = mood.lower()  # Normalize input to lower case
    if mood == "happy":
        return "That's great to hear! Keep smiling!"
    elif mood == "sad":
        return "I'm sorry to hear that. It's okay to feel sad sometimes."
    elif mood == "excited":
        return "Awesome! Excitement is contagious!"
    elif mood == "angry":
        return "Take a deep breath. It's important to calm down."
    elif mood == "anxious":
        return "It's normal to feel anxious. Try to take it one step at a time."
    else:
        return "That's an interesting mood! Care to share more?"