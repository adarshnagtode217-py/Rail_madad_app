# from flask import Flask, render_template, request
# import joblib

# app = Flask(__name__)

# model = joblib.load("model.pkl")
# vectorizer = joblib.load("vectorizer.pkl")


# @app.route("/", methods=["GET", "POST"])
# def home():

#     prediction = ""

#     if request.method == "POST":

#         complaint = request.form["complaint"]

#         x = vectorizer.transform([complaint])

#         prediction = model.predict(x)[0]

#     return render_template("index.html",
#                            prediction=prediction)


# if __name__ == "__main__":
#     app.run(debug=True)

# from flask import Flask, render_template, request
# import joblib

# app = Flask(__name__)

# model = joblib.load("model.pkl")
# vectorizer = joblib.load("vectorizer.pkl")


# @app.route("/", methods=["GET", "POST"])
# def home():

#     prediction = ""

#     if request.method == "POST":

#         complaint = request.form["complaint"]

#         x = vectorizer.transform([complaint])

#         prediction = model.predict(x)[0]

#     return render_template("index.html",
#                            prediction=prediction)


# @app.route("/login")
# def login():

#     return render_template("login.html")


# @app.route("/dashboard")
# def dashboard():

#     return render_template("dashboard.html")


# @app.route("/result")
# def result():

#     return render_template("result.html")


# if __name__ == "__main__":
#     app.run(debug=True)

from flask import Flask, render_template, request
import joblib
import sqlite3

from ml.sentiment import analyze_sentiment
from ml.priority import get_priority
from ml.recommendation import suggest_solution


app = Flask(__name__)


model = joblib.load("model.pkl")

vectorizer = joblib.load(

"vectorizer.pkl"

)



@app.route("/", methods=["GET","POST"])

def home():


    if request.method=="POST":


        complaint=request.form["complaint"]



        x=vectorizer.transform(

        [complaint]

        )



        prediction=model.predict(

        x

        )[0]



        sentiment=analyze_sentiment(

        complaint

        )



        priority=get_priority(

        complaint

        )



        solution=suggest_solution(

        prediction

        )



        conn=sqlite3.connect(

        "database/complaints.db"

        )



        cursor=conn.cursor()



        cursor.execute(

        '''

        INSERT INTO complaints(

        complaint,

        category,

        sentiment,

        priority,

        solution

        )



        VALUES(?,?,?,?,?)

        ''',

        (

        complaint,

        prediction,

        sentiment,

        priority,

        solution

        )



        )



        conn.commit()



        conn.close()



        return render_template(

        "result.html",


        prediction=prediction,


        sentiment=sentiment,


        priority=priority,


        solution=solution


        )




    return render_template(

    "index.html"

    )





@app.route("/login")

def login():

    return render_template(

    "login.html"

    )





@app.route("/dashboard")

def dashboard():



    conn=sqlite3.connect(

    "database/complaints.db"

    )



    cursor=conn.cursor()



    cursor.execute(

    "SELECT COUNT(*) FROM complaints"

    )



    total=cursor.fetchone()[0]



    cursor.execute(

    '''

    SELECT COUNT(*)

    FROM complaints


    WHERE priority='High'

    '''

    )



    high=cursor.fetchone()[0]




    conn.close()



    return render_template(

    "dashboard.html",


    total=total,


    high=high


    )






if __name__=="__main__":

    app.run(

    debug=True

    )