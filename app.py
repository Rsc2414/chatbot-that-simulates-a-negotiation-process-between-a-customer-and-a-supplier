from flask import Flask, request, render_template_string
import requests

app = Flask(__name__)

INITIAL_PRICE = 200
MIN_PRICE = 150
DISCOUNT_THRESHOLD = 10

HUGGINGFACE_API_KEY = 'YOUR_HUGGINGFACE_API_KEY'

def calculate_counteroffer(user_offer):
    polite_score = 1
    discount = min(DISCOUNT_THRESHOLD * polite_score, DISCOUNT_THRESHOLD)
    counteroffer = INITIAL_PRICE - discount
    if user_offer >= counteroffer:
        return user_offer
    elif user_offer < MIN_PRICE:
        return MIN_PRICE
    else:
        return counteroffer

def generate_response(user_offer):
    counteroffer = calculate_counteroffer(user_offer)
    if user_offer >= INITIAL_PRICE:
        return f"Your offer of ${user_offer} is accepted!"
    elif user_offer >= counteroffer:
        return f"Your offer of ${user_offer} is accepted. I can offer you the product at this price."
    else:
        return f"Your offer of ${user_offer} is too low. The best price I can offer is ${counteroffer}."

def query_huggingface_api(text):
    headers = {
        'Authorization': f'Bearer {HUGGINGFACE_API_KEY}',
    }
    data = {
        'inputs': text,
    }
    response = requests.post(
        'https://api-inference.huggingface.co/models/distilbert-base-uncased-finetuned-sst-2-english',
        headers=headers,
        json=data
    )
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Failed to get response from Hugging Face API"}

HTML_TEMPLATE = """
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Negotiation Chatbot</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background-color: #f4f4f4;
      color: #333;
      margin: 0;
      padding: 0;
    }
    .container {
      width: 80%;
      max-width: 800px;
      margin: auto;
      padding: 20px;
      background: #fff;
      box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
      border-radius: 8px;
    }
    h1 {
      text-align: center;
      color: #4aabff;
    }
    form {
      display: flex;
      flex-direction: column;
    }
    label {
      margin-bottom: 10px;
      font-weight: bold;
    }
    input[type="text"] {
      padding: 10px;
      border: 1px solid #ddd;
      border-radius: 4px;
      margin-bottom: 20px;
      font-size: 16px;
    }
    button {
      padding: 10px;
      background-color: #4aabff;
      color: #fff;
      border: none;
      border-radius: 4px;
      font-size: 16px;
      cursor: pointer;
    }
    button:hover {
      background-color: #3a8bf5;
    }
    .response {
      margin-top: 20px;
      padding: 10px;
      background-color: #e9ecef;
      border-left: 5px solid #4aabff;
      border-radius: 4px;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>Welcome to the Product Price Negotiation Chatbot!</h1>
    <form action="/" method="post">
      <label for="offer">Enter your price offer:</label>
      <input type="text" id="offer" name="offer" placeholder="$200" required>
      <button type="submit">Submit</button>
    </form>
    {% if response %}
    <div class="response">
      <h2>Response:</h2>
      <p>{{ response }}</p>
    </div>
    {% endif %}
  </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    response = None
    if request.method == "POST":
        try:
            user_offer = float(request.form["offer"].replace('$', '').strip())
            local_response = generate_response(user_offer)
            sentiment_response = query_huggingface_api(local_response)
            response = local_response + f" (Sentiment: {sentiment_response.get('label', 'unknown')})"
        except ValueError:
            response = "Invalid input. Please enter a numeric value for the price offer."
    return render_template_string(HTML_TEMPLATE, response=response)

if __name__ == "__main__":
    app.run(debug=True)
