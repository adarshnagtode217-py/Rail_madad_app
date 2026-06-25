
def get_priority(text):

    text=text.lower()



    high_words=[

        "fire",

        "medical",

        "accident",

        "theft",

        "harassment",

        "security",

        "injury"

    ]



    medium_words=[

        "ac",

        "washroom",

        "food",

        "water"

    ]




    for word in high_words:

        if word in text:

            return "High"



    for word in medium_words:

        if word in text:

            return "Medium"



    return "Low"
