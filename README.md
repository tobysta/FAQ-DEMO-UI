# Flask FAQ Web Application

A lightweight, clean **Frequently Asked Questions (FAQ)** web application built using Python, Flask, Jinja templates, semantic HTML5 tags, and custom CSS styling.

---

## 📂 Project Structure

Ensure your project files are organized exactly like this within your workspace:
```text
faq/
│
├── app.py              # Main Flask application with routing
├── README.md           # Project documentation (this file)
│
├── static/
│   └── style.css       # Custom CSS styling for the FAQ layout
│
└── templates/
    └── faq.html        # HTML structure using semantic tags
```

---

## 💻 Code Repositories

### 1. Main Application (`app.py`)
```python
from flask import Flask, render_template

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
```

### 2. HTML Template (`templates/faq.html`)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>FAQ UI</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <div class="container">
        <h1>Frequently Asked Questions</h1>

        <details class="faq-item">
            <summary class="faq-question">What is Flask?</summary>
            <div class="faq-answer">
                Flask is a lightweight Python web framework that helps you build web applications quickly.
            </div>
        </details>

        <details class="faq-item">
            <summary class="faq-question">Do I need JavaScript for an FAQ page?</summary>
            <div class="faq-answer">
                No. You can use the HTML &lt;details&gt; and &lt;summary&gt; tags to make collapsible FAQs without JavaScript.
            </div>
        </details>

        <details class="faq-item">
            <summary class="faq-question">How do I add more questions?</summary>
            <div class="faq-answer">
                Add more &lt;details&gt; blocks in the HTML or extend the faqs list in app.py and loop over it in the template.
            </div>
        </details>
    </div>
</body>
</html>
```

### 3. Stylesheet (`static/style.css`)
```css
* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

body {
    font-family: Arial, sans-serif;
    background: #f5f5f5;
    padding: 40px 20px;
}

.container {
    max-width: 700px;
    margin: 0 auto;
    background: #ffffff;
    padding: 30px;
    border-radius: 8px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.08);
}

h1 {
    text-align: center;
    margin-bottom: 30px;
    color: #333;
}

.faq-item {
    border-bottom: 1px solid #e0e0e0;
}

.faq-item:last-child {
    border-bottom: none;
}

.faq-question {
    list-style: none;           /* remove default triangle in some browsers */
    cursor: pointer;
    padding: 16px 10px;
    font-weight: 600;
    color: #222;
    position: relative;
    padding-right: 40px;
}

/* Custom +/- icon */
.faq-question::after {
    content: "+";
    position: absolute;
    right: 10px;
    top: 50%;
    transform: translateY(-50%);
    font-size: 20px;
    color: #555;
}

details[open] .faq-question::after {
    content: "−";
}

.faq-answer {
    padding: 0 10px 16px 10px;
    color: #444;
    line-height: 1.5;
}

/* Optional: smoother open/close on some browsers */
details > summary {
    outline: none;
}
```

---

## 🚀 How to Setup and Run Locally

1. **Install Flask dependency:**
   ```bash
   pip install flask
   ```

2. **Execute the project:**
   ```bash
   python app.py
   ```

3. **View the live app:**
   Open your browser and navigate to `http://127.0.0`.
