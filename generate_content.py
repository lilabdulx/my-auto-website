import openai
import random

# OpenAI API Key (get a free one at platform.openai.com)
OPENAI_API_KEY = "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"

# List of topics for affiliate blog posts
topics = [
    "Best Budget Laptops for 2025",
    "Top 10 Gadgets You Must Have",
    "Affordable Gaming Accessories",
    "Best Amazon Deals This Month",
    "Wireless Headphones Under £50"
]

def generate_post():
    topic = random.choice(topics)
    prompt = f"Write a 500-word blog post about {topic} and include Amazon affiliate links."
    
    openai.api_key = OPENAI_API_KEY
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    post_content = response["choices"][0]["message"]["content"]

    filename = topic.replace(" ", "_").lower() + ".html"
    with open(filename, "w", encoding="utf-8") as file:
        file.write(f"<html><head><title>{topic}</title></head><body><h1>{topic}</h1><p>{post_content}</p></body></html>")

    print(f"Generated: {filename}")

generate_post()
