import openai
import os

# Load the OpenAI API Key from GitHub Secrets
openai.api_key = os.getenv("OPENAI_API_KEY")

# Generate content using OpenAI API
response = openai.Completion.create(
    engine="text-davinci-003",  # You can use another model if you'd like
    prompt="Write a blog post about the future of artificial intelligence.",
    max_tokens=500
)

# Get the generated text from OpenAI
generated_text = response.choices[0].text.strip()

# Update the index.html with the generated content
html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>AI Generated Blog</title>
</head>
<body>
  <h1>Welcome to My AI-Generated Blog</h1>
  <div id="generated-content">
    <p>{generated_text}</p>
  </div>
</body>
</html>
"""

# Save the updated content back to index.html
with open("index.html", "w") as file:
    file.write(html_content)

print("index.html updated with new AI-generated content.")
