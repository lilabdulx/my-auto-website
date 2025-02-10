import openai
import os

# Set up OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")  # GitHub Secrets for security

# Generate content using OpenAI API
response = openai.Completion.create(
    engine="text-davinci-003",
    prompt="Write a blog post about the future of artificial intelligence.",
    max_tokens=500
)

# Get the generated text
generated_text = response.choices[0].text.strip()

# Create new HTML content
html_content = f"""
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
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

# Write the content back to index.html
with open("index.html", "w") as file:
    file.write(html_content)
