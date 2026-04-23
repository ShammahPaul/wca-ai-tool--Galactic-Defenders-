import anthropic

# Initialize Client
client = anthropic.Anthropic( )
# System prompt (forces summarizer behavior)
SYSTEM_PROMPT = """
