def ask_question(question, options):
    print(question)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    choice = input("Enter the number of your choice: ")
    return int(choice) - 1  # Convert to zero-based index

# Questions and their corresponding options
questions = [
    {
        "text": "How does your skin feel when you wake up in the morning?",
        "options": ["Tight and uncomfortable", "Shiny or greasy", "Oily in some areas, dry in others", "No discomfort or shine", "Red or irritated"],
        "response_mapping": [0, 1, 2, 3, 4]  # Dry, Oily, Combination, Normal, Sensitive
    },
    {
        "text": "How often do you experience breakouts (pimples, blackheads)?",
        "options": ["Rarely", "Often, especially in the T-zone", "Occasionally", "Often accompanied by redness or irritation"],
        "response_mapping": [3, 1, 2, 4]  # Normal, Oily, Combination, Sensitive
    },
    {
        "text": "How does your skin react to skincare products?",
        "options": ["Rarely reacts negatively", "Often feels irritated or stings", "Sometimes feels tight after using certain products", "Gets shiny or greasy quickly", "Varies depending on the area of the face"],
        "response_mapping": [3, 4, 0, 1, 2]  # Normal, Sensitive, Dry, Oily, Combination
    },
    {
        "text": "What is the appearance of your pores?",
        "options": ["Small or barely visible", "Large, especially on the nose and forehead", "Visible in some areas, not in others", "Pores not a major concern, but often red or reactive"],
        "response_mapping": [0, 1, 2, 4]  # Dry, Oily, Combination, Sensitive
    },
    {
        "text": "How does your skin feel after washing it with a cleanser?",
        "options": ["Tight and dry", "Clean and refreshed", "Very oily or greasy again within a few hours", "Sometimes irritated or red"],
        "response_mapping": [0, 3, 1, 4]  # Dry, Normal, Oily, Sensitive
    },
    {
        "text": "Does your skin get flaky or rough in certain areas?",
        "options": ["Often", "Rarely", "Only in certain areas, like the cheeks", "Occasionally, and it's often accompanied by redness"],
        "response_mapping": [0, 3, 2, 4]  # Dry, Normal, Combination, Sensitive
    },
    {
        "text": "How does your skin react to environmental changes (like wind, sun, pollution)?",
        "options": ["Easily irritated or develops rashes", "Becomes tight or rough", "Becomes oilier or develops acne", "Little to no change", "Mixed reactions in different areas"],
        "response_mapping": [4, 0, 1, 3, 2]  # Sensitive, Dry, Oily, Normal, Combination
    }
]

# This will store the score for each skin type
# Order: Dry, Oily, Combination, Normal, Sensitive
scores = [0, 0, 0, 0, 0]

for question in questions:
    choice = ask_question(question["text"], question["options"])
    response_index = question["response_mapping"][choice]
    scores[response_index] += 1

# Determine the skin type with the highest score
skin_types = ["Dry", "Oily", "Combination", "Normal", "Sensitive"]
max_score = max(scores)
skin_type = skin_types[scores.index(max_score)]

print(f"Your skin type is likely: {skin_type}")
