import openai
import os

# Set OpenAI API Key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Generate content using OpenAI API
response = openai.Completion.create(
    engine="text-davinci-003",  # Using GPT-3
    prompt="Write a blog post about the future of artificial intelligence.",
    max_tokens=500
)

# Get the generated text from OpenAI
generated_text = response.choices[0].text.strip()

# Your Amazon Affiliate Tracking ID (Replace this with your actual tracking ID)
affiliate_tracking_id = "your_tracking_id"

# Construct the Amazon Affiliate link
affiliate_link = f"https://www.amazon.com/dp/B08R6V2V9Y?tag={affiliate_tracking_id}"

# Update the index.html with the generated content and affiliate link
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
    <div id="affiliate-link">
        <p>Check out the latest deals on Amazon: 
            <a href="{affiliate_link}" target="_blank">Amazon Affiliate Link</a>
        </p>
    </div>
</body>
</html>
"""

# Save the updated content back to index.html
with open("index.html", "w") as file:
    file.write(html_content)

print("index.html updated with new AI-generated content and affiliate link.")
