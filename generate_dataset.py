import pandas as pd
import random

categories = {
    "AC Issue": "Technician assigned",
    "Cleanliness": "Cleaning team dispatched",
    "Food Quality": "Catering manager informed",
    "Security": "RPF team alerted",
    "Medical Emergency": "Medical team alerted",
    "Water Problem": "Vendor informed",
    "Electrical": "Electrician assigned",
    "Delay": "Delay notification sent",
    "Coach Damage": "Maintenance team assigned",
    "Reservation": "Reservation department informed",
    "Ticket Issue": "Refund process initiated",
    "Washroom Problem": "Cleaning staff informed",
    "Staff Behaviour": "Supervisor informed",
    "WiFi Issue": "Technical support informed",
    "Theft": "RPF complaint registered",
    "Luggage": "Lost and found informed",
    "Women Safety": "RPF escort assigned",
    "Bedroll Missing": "Housekeeping informed",
    "Noise Complaint": "Coach attendant informed",
    "Catering Issue": "Vendor contacted"
}

complaints = [
    "AC not working in coach B2",
    "Washroom is dirty",
    "Food served was stale",
    "Charging point not working",
    "Passenger lost luggage",
    "Train delayed by 3 hours",
    "Blanket not provided",
    "WiFi not available",
    "Unauthorized person entered coach",
    "Medical assistance required urgently"
]

sentiments = ["Negative", "Neutral", "Very Negative"]
priorities = ["Low", "Medium", "High"]
statuses = ["Pending", "Resolved"]

data = []

for i in range(1, 5001):

    category = random.choice(list(categories.keys()))

    complaint = random.choice(complaints)

    sentiment = random.choice(sentiments)

    priority = random.choice(priorities)

    status = random.choice(statuses)

    resolution = categories[category]

    data.append([
        i,
        complaint,
        category,
        sentiment,
        priority,
        resolution,
        status
    ])

df = pd.DataFrame(data, columns=[
    "Complaint_ID",
    "Complaint_Text",
    "Category",
    "Sentiment",
    "Priority",
    "Resolution",
    "Status"
])

df.to_csv("complaints.csv", index=False)

print("5000 complaints dataset generated successfully!")