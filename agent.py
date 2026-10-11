def ai_agent():
    print("Basic Rule-Based AI Agent")
    problem = input("Enter your problem: ").lower()

    if "study" in problem:
        print("AI Suggestion: Make a study timetable.")
    elif "tired" in problem:
        print("AI Suggestion: Take some rest.")
    elif "python" in problem:
        print("AI Suggestion: Practice Python programs.")
    else:
        print("AI Suggestion: Please explain your problem clearly.")

ai_agent()
