import anthropic

# Initialize Client
client = anthropic.Anthropic( )

# System prompt (forces summarizer behavior)
SYSTEM_PROMPT = """
You are a strict report summarizer.

Rules:
- Only summarize reports, articles, or long-form informational text.
- If the input is not a report or is too short, respond with:
  "Please provide a valid report or long text to summarize."
- Do NOT answer questions.
- Output only a concise summary.

Format:
- Title (if available)
- 3–5 bullet key points
- Short conclusion (1–2 sentences)
"""

# Simple validation
def is_valid_report(text):
    return len(text.split()) > 50

print("AI Summarizer is ready!\n")

while True:
    user_input = input("Hi, What are we summarizing:\n> ")

    if not is_valid_report(user_input):
        print("\nSummarizer: Please provide a valid report or long text to summarize.\n")
        continue
    
    # Send request
    response = client.messages.create(