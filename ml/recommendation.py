

def suggest_solution(category):



    solutions={


        "AC Issue":

        "Technician assigned",



        "Food Quality":

        "Catering manager informed",



        "Cleanliness":

        "Cleaning staff dispatched",



        "Security":

        "RPF team alerted",



        "Medical Emergency":

        "Medical team informed",



        "Electrical":

        "Electrician assigned"



    }



    return solutions.get(

    category,

    "Complaint forwarded"

    )


