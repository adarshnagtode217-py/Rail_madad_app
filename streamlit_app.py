# import streamlit as st
# import joblib
# import sqlite3

# from ml.sentiment import analyze_sentiment
# from ml.priority import get_priority
# from ml.recommendation import suggest_solution

# # Load Models
# model = joblib.load("model.pkl")
# vectorizer = joblib.load("vectorizer.pkl")

# st.title("🚆 AI-Driven Rail Madad Complaint System")

# complaint = st.text_area("Enter Complaint")

# if st.button("Analyze Complaint"):

#     x = vectorizer.transform([complaint])

#     prediction = model.predict(x)[0]

#     sentiment = analyze_sentiment(complaint)

#     priority = get_priority(complaint)

#     solution = suggest_solution(prediction)

#     conn = sqlite3.connect("database/complaints.db")

#     cursor = conn.cursor()

#     cursor.execute(
#         '''
#         INSERT INTO complaints(
#         complaint,
#         category,
#         sentiment,
#         priority,
#         solution
#         )

#         VALUES(?,?,?,?,?)
#         ''',

#         (
#             complaint,
#             prediction,
#             sentiment,
#             priority,
#             solution
#         )
#     )

#     conn.commit()
#     conn.close()

#     st.success("Complaint Submitted Successfully")

#     st.write("Category :", prediction)
#     st.write("Sentiment :", sentiment)
#     st.write("Priority :", priority)
#     st.write("Solution :", solution)

#     # ==========================
#     # Dashboard Metric
#     # ==========================

#     conn = sqlite3.connect("database/complaints.db")

#     cursor = conn.cursor()

#     cursor.execute(
#         "SELECT COUNT(*) FROM complaints"
#     )

#     total = cursor.fetchone()[0]

#     conn.close()

#     st.metric(
#         "Total Complaints",
#         total
#     )

import streamlit as st
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import joblib
import uuid
from datetime import datetime

from ml.sentiment import analyze_sentiment
from ml.priority import get_priority
from ml.recommendation import suggest_solution

st.set_page_config(
    page_title="Rail Madad AI",
    page_icon="🚆",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>

.stApp{
background:linear-gradient(135deg,#020617,#081028,#0f172a);
color:white;
}

[data-testid="stSidebar"]{
background:linear-gradient(180deg,#030712,#0f172a);
border-right:1px solid rgba(255,255,255,0.08);
}

[data-testid="stSidebar"] *{
color:white;
}

.main-title{
font-size:48px;
font-weight:700;
color:#38bdf8;
margin-bottom:5px;
}

.sub-title{
font-size:20px;
color:#cbd5e1;
margin-bottom:40px;
}

.metric-card{
padding:20px;
border-radius:18px;
background:rgba(255,255,255,0.05);
backdrop-filter:blur(15px);
border:1px solid rgba(255,255,255,0.1);
box-shadow:0px 0px 25px rgba(0,255,255,0.10);
text-align:center;
}

.metric-number{
font-size:40px;
font-weight:bold;
color:white;
}

.metric-text{
font-size:18px;
color:#94a3b8;
}

.complaint-box{
padding:25px;
background:rgba(255,255,255,0.04);
border-radius:20px;
border:1px solid rgba(255,255,255,0.1);
box-shadow:0px 0px 15px rgba(0,255,255,0.08);
}

.result-box{
padding:25px;
background:rgba(255,255,255,0.04);
border-radius:20px;
border:1px solid rgba(56,189,248,0.4);
box-shadow:0px 0px 20px rgba(56,189,248,0.20);
}

.result-title{
font-size:28px;
color:#38bdf8;
font-weight:600;
}

.result-text{
font-size:20px;
margin-top:15px;
color:white;
}

textarea{
background:#0f172a !important;
color:white !important;
border-radius:15px !important;
border:1px solid rgba(255,255,255,0.1) !important;
}

.stButton>button{
width:100%;
height:55px;
border-radius:12px;
border:none;
font-size:20px;
font-weight:bold;
color:white;
background:linear-gradient(90deg,#9333ea,#06b6d4);
transition:0.3s;
}

.stButton>button:hover{
transform:scale(1.02);
box-shadow:0px 0px 25px rgba(0,255,255,0.30);
}

hr{
border:1px solid rgba(255,255,255,0.05);
}

</style>
""",unsafe_allow_html=True)

st.markdown("""
<div class='main-title'>
🚆 AI-Driven Rail Madad
</div>

<div class='sub-title'>
Intelligent Complaint Management System
</div>
""",unsafe_allow_html=True)

# ============================
# Sidebar
# ============================

with st.sidebar:

    st.markdown("## 🚆 Rail Madad AI")

    st.markdown("---")

    st.markdown("### 🏠 Dashboard")

    st.markdown("### 📝 New Complaint")

    st.markdown("### 📊 Analytics")

    st.markdown("### ⚙️ Settings")

    st.markdown("---")

    st.markdown("""

<div style='text-align:center;'>

<h1 style='font-size:90px;'>

🚄

</h1>

<p style='color:#94a3b8;'>

Indian Railways

Complaint System

</p>

</div>

""",unsafe_allow_html=True)


# ============================
# Load Dashboard Statistics
# ============================


conn=sqlite3.connect(

"database/complaints.db"

)

cursor=conn.cursor()


cursor.execute(

"SELECT COUNT(*) FROM complaints"

)

total=cursor.fetchone()[0]



cursor.execute(

"""

SELECT COUNT(*)

FROM complaints

WHERE priority='High'

"""

)

high=cursor.fetchone()[0]



cursor.execute(

"""

SELECT COUNT(*)

FROM complaints

WHERE priority='Medium'

"""

)

medium=cursor.fetchone()[0]



cursor.execute(

"""

SELECT COUNT(*)

FROM complaints

WHERE priority='Low'

"""

)

low=cursor.fetchone()[0]


conn.close()



# ============================
# Metric Cards
# ============================


c1,c2,c3,c4=st.columns(4)



with c1:

    st.markdown(

f"""

<div class='metric-card'>


<div class='metric-number'>

{total}

</div>



<div class='metric-text'>

Total Complaints

</div>



</div>

""",

unsafe_allow_html=True

)



with c2:


    st.markdown(

f"""

<div class='metric-card'>


<div class='metric-number'>

{high}

</div>



<div class='metric-text'>

High Priority

</div>



</div>

""",

unsafe_allow_html=True

)




with c3:


    st.markdown(

f"""

<div class='metric-card'>


<div class='metric-number'>

{medium}

</div>



<div class='metric-text'>

Medium Priority

</div>



</div>

""",

unsafe_allow_html=True

)




with c4:


    st.markdown(

f"""

<div class='metric-card'>


<div class='metric-number'>

{low}

</div>



<div class='metric-text'>

Low Priority

</div>



</div>

""",

unsafe_allow_html=True

)



st.markdown("<br>",unsafe_allow_html=True)

model=joblib.load("model.pkl")
vectorizer=joblib.load("vectorizer.pkl")

left,right=st.columns([1.2,1])

with left:

    st.markdown("""
    <div class='complaint-box'>
    <h2>📝 New Complaint</h2>
    </div>
    """,unsafe_allow_html=True)

    complaint=st.text_area("",height=220,placeholder="Enter passenger complaint here...")

    analyze=st.button("🔍 Analyze Complaint")

with right:

    st.markdown("""
    <div class='result-box'>
    <h2 class='result-title'>🤖 AI Analysis</h2>
    </div>
    """,unsafe_allow_html=True)

    if analyze and complaint:

        x=vectorizer.transform([complaint])

        prediction=model.predict(x)[0]

        sentiment=analyze_sentiment(complaint)

        priority=get_priority(complaint)

        solution=suggest_solution(prediction)

        conn=sqlite3.connect("database/complaints.db")
        cursor=conn.cursor()

        cursor.execute("""
        INSERT INTO complaints(
        complaint,
        category,
        sentiment,
        priority,
        solution
        )
        VALUES(?,?,?,?,?)
        """,
        (
        complaint,
        prediction,
        sentiment,
        priority,
        solution
        ))

        conn.commit()
        conn.close()

        st.markdown(f"""
        <div class='result-box'>

        <p class='result-text'>
        📂 <b>Category</b><br>{prediction}
        </p>

        <p class='result-text'>
        😊 <b>Sentiment</b><br>{sentiment}
        </p>

        <p class='result-text'>
        ⚡ <b>Priority</b><br>{priority}
        </p>

        <p class='result-text'>
        🛠 <b>Solution</b><br>{solution}
        </p>

        </div>
        """,unsafe_allow_html=True)

st.markdown("<br>",unsafe_allow_html=True)

col1,col2=st.columns(2)

with col1:

    st.markdown("""
    <div class='complaint-box'>
    <h2>📊 Priority Distribution</h2>
    </div>
    """,unsafe_allow_html=True)

    fig,ax=plt.subplots(figsize=(4,4))

    labels=["High","Medium","Low"]

    values=[high,medium,low]

    colors=["#ef4444","#f59e0b","#22c55e"]

    ax.pie(
        values,
        labels=labels,
        autopct="%1.1f%%",
        colors=colors
    )

    st.pyplot(fig)


with col2:

    st.markdown("""
    <div class='complaint-box'>
    <h2>📈 Complaint Statistics</h2>
    </div>
    """,unsafe_allow_html=True)

    chart_data=pd.DataFrame({

        "Priority":[

        "High",
        "Medium",
        "Low"

        ],

        "Count":[

        high,
        medium,
        low

        ]

    })

    st.bar_chart(
        chart_data.set_index(
        "Priority"
        )
    )


st.markdown("<br>",unsafe_allow_html=True)


st.markdown("""
<div class='complaint-box'>
<h2>📜 Complaint History</h2>
</div>
""",unsafe_allow_html=True)



conn=sqlite3.connect(
"database/complaints.db"
)


df=pd.read_sql(

"""

SELECT *

FROM complaints

ORDER BY id DESC

LIMIT 10

"""

,

conn

)


conn.close()


st.dataframe(

df,

use_container_width=True,

hide_index=True

)

import uuid
from datetime import datetime

st.markdown("<br>",unsafe_allow_html=True)

st.markdown("""
<style>

.footer{
margin-top:30px;
padding:15px;
border-radius:15px;
background:rgba(255,255,255,0.03);
text-align:center;
font-size:16px;
color:#94a3b8;
}

.track-card{
padding:20px;
border-radius:15px;
background:rgba(56,189,248,0.08);
border:1px solid rgba(56,189,248,0.3);
box-shadow:0px 0px 15px rgba(56,189,248,0.2);
}

</style>
""",unsafe_allow_html=True)

if analyze and complaint:

    tracking_id="RM-"+str(uuid.uuid4())[:8].upper()

    current_time=datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    st.success("✅ Complaint Registered Successfully")

    st.markdown(f"""
    <div class='track-card'>

    <h3>🎫 Complaint Tracking Details</h3>

    <p><b>Tracking ID :</b> {tracking_id}</p>

    <p><b>Submitted :</b> {current_time}</p>

    <p><b>Status :</b> Pending</p>

    </div>

    """,unsafe_allow_html=True)

st.markdown("""

<div class='footer'>

🚆 AI Driven Rail Madad Complaint Management System<br>

Developed using Streamlit | Machine Learning | SQLite

</div>

""",unsafe_allow_html=True)

st.markdown("<br>",unsafe_allow_html=True)

left,right=st.columns([3,1])

with left:
    search=st.text_input("🔍 Search Complaint")

with right:
    priority_filter=st.selectbox(
        "Priority",
        ["All","High","Medium","Low"]
    )


conn=sqlite3.connect(
"database/complaints.db"
)

query="""
SELECT *
FROM complaints
"""

df=pd.read_sql(
query,
conn
)

conn.close()


if search:

    df=df[

    df["complaint"]

    .str.contains(

    search,

    case=False,

    na=False

    )

    ]



if priority_filter!="All":

    df=df[

    df["priority"]

    ==

    priority_filter

    ]




st.markdown("""

<div class='complaint-box'>

<h2>

📋 Filtered Complaints

</h2>

</div>

""",

unsafe_allow_html=True

)



st.dataframe(

df,

use_container_width=True,

hide_index=True

)



csv=df.to_csv(

index=False

)



st.download_button(

label="📥 Download CSV",

data=csv,

file_name="complaints.csv",

mime="text/csv"

)



if st.button(

"🔄 Refresh Dashboard"

):


    st.rerun()



st.markdown("""

<hr>


<center>


<p style='color:#64748b;'>


Made with ❤️ using

Streamlit • Scikit-Learn • SQLite • Python


</p>


</center>

""",

unsafe_allow_html=True

)