from flask import Flask,render_template

app = Flask(__name__)
    
@app.route("/")
def index():
    return render_template("faq.html")

@app.route("/faq")
def faq():

    faqs = [
        {
            "question": "What is Flask?",
            "answer": "Flask is a lightweight Python web framework that helps you build web applications quickly."
        },
        {
            "question": "How do I add more questions?",
            "answer": "Add more <details> blocks in the HTML or extend the faqs list in app.py and loop over it in the template."
        }

    ]
    return render_template("faq.html", faqs=faqs)

if __name__ == "__main__":
    app.run(debug=True)