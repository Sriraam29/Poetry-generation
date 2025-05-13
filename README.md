AI Poetry Generator Project
Overview
This project consists of two main components: a Flask application (poetry.py) that uses a pre-trained GPT-2 model to generate poetry, and an HTML interface (poetry.html) for interacting with the poetry generation system. The Flask app leverages the transformers library from Hugging Face to generate poems based on user prompts, while the HTML interface provides a simple front-end for users to generate and copy the generated poetry.
Project Structure

poetry.py: A Python script that sets up a Flask web server, loads the GPT-2 model via the transformers library, and provides an API endpoint to generate poetry based on user input.
poetry.html: An HTML file embedded within poetry.py that serves as the front-end interface for users to input prompts, generate poetry, and copy the output.

Prerequisites
To run this project, you'll need the following installed on your system:

Python 3.8+
pip (Python package manager)
A web browser (to interact with the Flask app)

Required Python Libraries

flask (for the web server)
transformers (for the GPT-2 model)
torch (required by transformers for model inference)

Setup Instructions
1. Clone or Download the Project
Download the project files (poetry.py and poetry.html) to your local machine. Note that poetry.html is embedded as a string within poetry.py, so you only need to manage poetry.py.
2. Set Up a Python Environment
It’s recommended to use a virtual environment to manage dependencies:
# Create a virtual environment
python -m venv poetry_env

# Activate the virtual environment
# On Windows
poetry_env\Scripts\activate
# On macOS/Linux
source poetry_env/bin/activate

3. Install Dependencies
Install the required Python libraries:
pip install flask transformers torch

4. Run the Flask Application
Execute the poetry.py script to start the Flask server:
python poetry.py


The server will start on http://0.0.0.0:5000 (accessible as http://localhost:5000 in your browser).
Open your web browser and navigate to http://localhost:5000 to access the poetry generator interface.

Usage
Generating Poetry

Access the Interface: Open http://localhost:5000 in your web browser.
Generate a Poem:
The interface displays a button labeled "Generate Poem."
Click the button to generate a poem. The default prompt is "Write a poem about nature," but this can be modified in the JavaScript section of the HTML template if desired.
The generated poem will appear in the <pre> element below the button.


Copy the Poem:
Click the "Copy Poem" button to copy the generated poem to your clipboard.



Customizing the Prompt
To generate poetry with a different theme:

Modify the prompt value in the JavaScript section of the HTML_TEMPLATE string within poetry.py. For example, change "Write a poem about nature" to "Write a poem about love":fetch("/generate_poem", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({ prompt: "Write a poem about love", max_length: 100 }),
})


Save the file and restart the Flask server to apply the changes.

Technical Details
Backend (poetry.py)

Flask Server: The app serves a single-page web interface at the root URL (/) and provides an API endpoint (/generate_poem) to handle poem generation requests.
Model: Uses the GPT-2 model from the transformers library (pipeline("text-generation", model="gpt2")) to generate text based on the provided prompt.
API Endpoint: The /generate_poem endpoint accepts POST requests with a JSON body containing prompt (the starting text) and max_length (the maximum length of the generated text). It returns the generated poem as a JSON response.

Frontend (poetry.html within poetry.py)

HTML Structure: A simple page with a title, a "Generate Poem" button, a <pre> element to display the poem, and a "Copy Poem" button.
JavaScript:
The "Generate Poem" button triggers a fetch request to the /generate_poem endpoint, sending the prompt and receiving the generated poem.
The "Copy Poem" button uses the navigator.clipboard API to copy the poem text to the clipboard.



Current Limitations

Static Prompt: The prompt is hardcoded in the JavaScript code. To allow users to input custom prompts, you’d need to add an input field to the HTML and update the JavaScript to use that input.
Model Performance: GPT-2 may not always produce high-quality poetry, as it’s a general-purpose text generation model. Fine-tuning on a poetry-specific dataset could improve results.
Error Handling: Basic error handling is implemented, but the UI doesn’t display error messages from the server (e.g., if the model fails to generate text).

Future Improvements

Add a text input field to the HTML interface to allow users to specify custom prompts.
Fine-tune the GPT-2 model on a poetry dataset for better poem quality.
Enhance error handling in the UI to display server-side errors to the user.
Add styling (e.g., CSS) to improve the visual appeal of the interface.
Include options to adjust the max_length parameter via the UI.

Troubleshooting

Server Not Starting: Ensure all dependencies are installed (flask, transformers, torch). Check for errors in the terminal when running poetry.py.
No Poem Generated: Verify that the browser’s developer console (F12) shows successful requests to /generate_poem. Check for CORS or network issues.
Copy Button Not Working: The navigator.clipboard API requires a secure context (HTTPS or localhost). Ensure you’re accessing the app via http://localhost:5000.

License
This project is open-source and available under the MIT License. Feel free to use, modify, and distribute it as needed.
Contact
For questions or contributions, please reach out via email at sriraamhari04@gmail.com  or open an issue on the project repository (if hosted on GitHub).
