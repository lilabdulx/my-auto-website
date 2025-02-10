import openai
import os

# Load your OpenAI API Key from your GitHub Secrets
openai.api_key = os.getenv("OPENAI_API_KEY")

# Call OpenAI's API to generate content
response = openai.Completion.create(
    engine="text-davinci-003",  # You can use a different model
    prompt="Write a blog post about the future of artificial intelligence.",  # The prompt to generate the blog
    max_tokens=500  # Number of tokens (words) the content can have
)

# Get the generated text
generated_text = response.choices[0].text.strip()

# Check if the content was generated
if not generated_text:
    print("No content generated!")
else:
    # If content is generated, create the HTML content
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

    # Write the HTML content to the index.html file
    with open("index.html", "w") as file:
        file.write(html_content)

    print("index.html has been updated with new AI-generated content.")
