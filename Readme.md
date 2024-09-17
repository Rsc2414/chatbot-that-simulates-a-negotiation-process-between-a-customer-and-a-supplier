# Negotiation Chatbot

This is a simple web application built with Flask that simulates a negotiation process between a customer and a supplier. It uses a natural language processing model from Hugging Face to analyze and respond to price offers.

## Features

- **Negotiate Prices:** The chatbot allows users to make price offers and receives a response based on predefined pricing logic.
- **Sentiment Analysis:** Utilizes Hugging Face's API to analyze the sentiment of the response (or other natural language processing tasks).
- **Simple UI:** Clean and attractive design with a color scheme using #4aabff.

## Prerequisites

- Python 3.x
- Flask
- Requests
- A Hugging Face API key

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/negotiation-chatbot.git
   cd negotiation-chatbot
Usage
Run the Application

Start the Flask server by running:
python app.py

Access the Web Application

Open your web browser and go to http://127.0.0.1:5000/ to interact with the chatbot.

Enter Your Offer

Input your price offer in the form provided.
Submit the form to receive a response from the chatbot.
Code Explanation
Flask Web Application: Provides the web interface and handles user inputs.
Pricing Logic: Determines the counteroffer based on the user’s offer.
Hugging Face API: Analyzes the response sentiment (or other NLP tasks).
HTML Template: Simple design with CSS styling for an attractive user interface.
Error Handling
Rate Limit Errors: The application handles API rate limit errors by retrying after a delay.
Input Validation: Ensures that only numeric values are processed for price offers.
Contributing
Feel free to fork the repository and submit pull requests. If you have any suggestions or find bugs, please open an issue on the GitHub repository.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
Flask for the web framework.
Hugging Face for providing the natural language processing APIs.


Replace `YOUR_HUGGINGFACE_API_KEY` with your actual Hugging Face API key and update the repository URL to match your own if you are hosting the project on GitHub. This `README.md` file provides a comprehensive overview of your project and instructions for setup and usage.

