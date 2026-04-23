import anthropic

# Initialize Client
client = anthropic.Anthropic( )
# System prompt (forces summarizer behavior)
SYSTEM_PROMPT = """
You are a strict report summarizer.

Rules: