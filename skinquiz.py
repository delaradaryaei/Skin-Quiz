def ask_question(question, options):
    print("\n" + question)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    while True:
        try:
            choice = int(input("Enter the number of your choice: "))
            if 1 <= choice <= len(options):
                return choice - 1  # Convert to zero-based index
            else:
                print("Please enter a number between 1 and " + str(len(options)))
        except ValueError:
            print("Please enter a valid number.")

questions = [
    {
        "text": "How does your skin feel when you wake up in the morning?",
        "options": ["Tight and uncomfortable", "Shiny or greasy", "Oily in some areas, dry in others", "No discomfort or shine", "Red or irritated"],
        "response_mapping": [0, 1, 2, 3, 4]
    },
    {
        "text": "How often do you experience breakouts?",
        "options": ["Rarely", "Often, especially in the T-zone", "Occasionally", "Often accompanied by redness or irritation", "Frequently in various areas"],
        "response_mapping": [3, 1, 2, 4, 1]
    },
    {
        "text": "What best describes the texture of your skin?",
        "options": ["Rough and flaky", "Smooth with oily patches", "Smooth and well-balanced", "Sensitive and sometimes bumpy", "Combination of dry and oily"],
        "response_mapping": [0, 1, 3, 4, 2]
    },
    {
        "text": "How does your skin react to skincare products?",
        "options": ["Rarely reacts negatively", "Often feels irritated or stings", "Sometimes feels tight after using certain products", "Gets shiny or greasy quickly", "Varies depending on the area of the face"],
        "response_mapping": [3, 4, 0, 1, 2]
    },
    {
        "text": "What is the appearance of your pores?",
        "options": ["Small or barely visible", "Large, especially on the nose and forehead", "Visible in some areas, not in others", "Pores not a major concern, but often red or reactive", "Very large and noticeable across most of the face"],
        "response_mapping": [0, 1, 2, 4, 1]
    },
    {
        "text": "How does your skin feel after washing it with a cleanser?",
        "options": ["Tight and dry", "Clean and refreshed", "Very oily or greasy again within a few hours", "Sometimes irritated or red", "It varies, depending on the cleanser"],
        "response_mapping": [0, 3, 1, 4, 2]
    },
    {
        "text": "Does your skin get flaky or rough in certain areas?",
        "options": ["Often", "Rarely", "Only in certain areas, like the cheeks or nose", "Occasionally, and it's often accompanied by redness", "Never, it's mostly oily"],
        "response_mapping": [0, 3, 2, 4, 1]
    },
    {
        "text": "How does your skin react to environmental changes (like wind, sun, pollution)?",
        "options": ["Easily irritated or develops rashes", "Becomes tight or rough", "Becomes oilier or develops acne", "Little to no change", "Mixed reactions in different areas"],
        "response_mapping": [4, 0, 1, 3, 2]
    },
    {
        "text": "How does your skin feel by midday?",
        "options": ["Still tight or dry", "Comfortably hydrated", "Begins to look oily or shiny", "T-zone gets oily but cheeks remain dry", "Noticeably oily or greasy"],
        "response_mapping": [0, 3, 1, 2, 1]  # Dry, Normal, Oily, Combination, Oily
    },
    {
        "text": "How does your skin typically react to sun exposure?",
        "options": ["Burns easily", "Tans gradually", "Rarely burns, tans easily", "Sensitive reaction or rash", "No noticeable change"],
        "response_mapping": [4, 3, 3, 4, 3]  # Sensitive, Normal, Normal, Sensitive, Normal
    },
    {
        "text": "How would you describe the firmness of your skin?",
        "options": ["Loose or sagging in some areas", "Firm and bounces back quickly", "Starting to notice some loss of elasticity", "Varies across different areas", "Very firm and elastic"],
        "response_mapping": [0, 3, 2, 2, 3]  # Dry, Normal, Combination, Combination, Normal
    },
    {
        "text": "Do you have concerns with hyperpigmentation or skin discoloration?",
        "options": ["Yes, I have noticeable dark spots", "Occasionally, especially after sun exposure", "Rarely or never", "Yes, but mainly redness or rosacea", "I have uneven skin tone in some areas"],
        "response_mapping": [4, 4, 3, 4, 2]  # Sensitive, Sensitive, Normal, Sensitive, Combination
    },
    {
        "text": "What long-term skin concern are you most interested in addressing?",
        "options": ["Preventing or reducing wrinkles", "Managing acne or breakouts", "Reducing redness or sensitivity", "Hydrating dry skin", "Controlling oiliness"],
        "response_mapping": [3, 1, 4, 0, 1]  # Normal, Oily, Sensitive, Dry, Oily
    }
    
]

# This will store the score for each skin type
scores = [0, 0, 0, 0, 0]

for question in questions:
    choice = ask_question(question["text"], question["options"])
    response_index = question["response_mapping"][choice]
    scores[response_index] += 1

# Checking if the dry and oily score is close together 
dry_score = scores[0]  # Score for Dry skin type
oily_score = scores[1]  # Score for Oily skin type

# Determine the skin type with the highest score among the initial skin type categories
skin_types = ["Dry", "Oily", "Combination", "Normal", "Sensitive"]
skin_type_scores = scores[:5]  # Only consider the first five scores for skin type determination
max_score = max(skin_type_scores)
index_of_max_score = skin_type_scores.index(max_score)
skin_type = skin_types[index_of_max_score]

# Implementing logic for close Dry and Oily scores
threshold = 1  # threshold 

# Adjusting for Combination if Dry and Oily are within the threshold
if abs(dry_score - oily_score) <= threshold and (index_of_max_score == 0 or index_of_max_score == 1):
    skin_type = "Combination"

print(f"\nYour primary skin type is likely: {skin_type}.")