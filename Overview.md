Project Overview
This project is a Flask-based web application that simulates a negotiation process between a customer and a supplier. The application allows users to make a price offer and receive a response based on predefined pricing logic.

Key Components
Flask Web Application

Framework: Flask is used to create the web application.
Routes: There is a single route (/) that handles both GET and POST requests.
Pricing Logic

Initial Price: $200
Minimum Price: $150
Discount Threshold: $10 (maximum discount based on politeness)
Functions

calculate_counteroffer(user_offer): Calculates the counteroffer based on the user’s offer and predefined discount logic.
generate_response(user_offer): Generates a response message based on the user’s offer.
query_huggingface_api(text): Sends a request to the Hugging Face API to analyze the sentiment of the response (or other processing depending on the model used).
Hugging Face API Integration

API Key: Required to access the Hugging Face API.
Model: Sentiment analysis or other natural language processing model from Hugging Face is used to process the generated response.
HTML Template

Design: Simple and clean design with a color scheme using #4aabff.
Form: Allows users to input their price offer.
Response Display: Shows the chatbot’s response and the sentiment analysis result.
Error Handling

Rate Limit and API Errors: Handles errors from the Hugging Face API, such as rate limits and failed requests.
Value Errors: Ensures that only valid numeric inputs are processed.
How It Works
User Interaction

Users visit the web application, input their price offer, and submit the form.
Processing

The application calculates a counteroffer based on the user’s offer.
It then queries the Hugging Face API to analyze the sentiment of the response.
Response Generation

Based on the user’s offer, the application generates a response message.
The response, along with any sentiment analysis from the Hugging Face API, is displayed to the user.
Deployment

The application is set up to run locally with Flask's built-in server.
Setup Instructions
Install Dependencies

Flask: pip install flask
Requests: pip install requests
API Key

Replace YOUR_HUGGINGFACE_API_KEY with your actual Hugging Face API key.
Run the Application

Execute the script to start the Flask server: python your_script_name.py.
Access the App

Open a web browser and navigate to http://127.0.0.1:5000/ to interact with the chatbot.
This project demonstrates basic integration of a web application with a natural language processing API and provides a foundation for building more complex negotiation or conversational systems.
