from flask import Flask, request, jsonify, render_template_string
from transformers import pipeline

# Initialize Flask app
app = Flask(__name__)

# Load the text generation model (GPT-2)
generator = pipeline("text-generation", model="gpt2")

# HTML + JavaScript for frontend
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI Poetry Generator</title>
    <style>
        body { font-family: Arial, sans-serif; text-align: center; padding: 20px; background: #f4f4f4; }
        #container { background: white; padding: 20px; max-width: 500px; margin: auto; border-radius: 10px; box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1); }
        textarea { width: 100%; padding: 10px; margin-top: 10px; border-radius: 5px; }
        button { padding: 10px 15px; background: #007BFF; color: white; border: none; border-radius: 5px; margin-top: 10px; cursor: pointer; }
        button:hover { background: #0056b3; }
        #poem { margin-top: 20px; white-space: pre-wrap; background: #e9ecef; padding: 10px; border-radius: 5px; }
    </style>
</head>
<body>
    <div id="container">
        <h2>AI Poetry Generator</h2>
        <textarea id="prompt" rows="3" placeholder="Enter a topic for your poem..."></textarea>
        <button onclick="generatePoem()">Generate Poem</button>
        <div id="poem"></div>
    </div>

    <script>
        function generatePoem() {
            let prompt = document.getElementById("prompt").value || "Write a poem about nature";
            fetch("/generate_poem", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ prompt: prompt, max_length: 100 })
            })
            .then(response => response.json())
            .then(data => {
                document.getElementById("poem").innerText = data.poem;
            })
            .catch(error => console.error("Error:", error));
        }
    </script>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route("/generate_poem", methods=["POST"])
def generate_poem():
    try:
        data = request.get_json()
        prompt = data.get("prompt", "Write a poem about nature")
        max_length = data.get("max_length", 100)

        # Generate text
        generated_text = generator(prompt, max_length=max_length, num_return_sequences=1)[0]["generated_text"]

        return jsonify({"poem": generated_text})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
