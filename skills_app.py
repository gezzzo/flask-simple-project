# import Flask
from flask import Flask
from flask.templating import render_template

# To name app
skills_app = Flask(__name__)

# To set the path
@skills_app.route("/") # url/
def homepage(): # this is a function return data in the path
    return render_template("home.html", user = "visitor") 

@skills_app.route("/about") # url/about
def aboutpage():
    return render_template("about.html")

@skills_app.route("/add") # url/add
def addpage():
    return render_template("add.html")
    
My_skills = [("html",90),("css",30),("python",94)]

@skills_app.route("/skills") # url/skills
def skillspage():
    return render_template("skills.html",skills = My_skills)

if __name__=="__main__": 
    skills_app.run(debug=True,port=9000) # Debug mode: on
                                         # port = 9000
