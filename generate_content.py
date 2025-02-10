import openai
import os

# Set your OpenAI API Key
openai.api_key = os.getenv('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')  # This should be set as a GitHub secret

# Generate content with OpenAI
def generate_content():
    prompt = "Write a blog post about the future of AI and automation."  # Modify this prompt as needed
    response = openai.Completion.create(
        model="text-davinci-003",  # You can change the model if needed
        prompt=prompt,
        max_tokens=500  # Adjust the token count based on the amount of content you want
    )
    return response.choices[0].text.strip()

# Update the HTML content
def update_html(content):
    with open("index.html", "r") as file:
        html_content = file.read()

    # Replace the placeholder with generated content
    new_html_content = html_content.replace("<!-- GENERATED CONTENT -->", content)

    with open("index.html", "w") as file:
        file.write(new_html_content)

if __name__ == "__main__":
    content = generate_content()  # Generate the content
    update_html(content)  # Update the index.html file with the generated content
