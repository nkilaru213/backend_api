def get_ai_context(query, results):
    if not results:
        return "No relevant files found. (Dummy AI response — will improve with OpenAI)"
    return f"Dummy AI summary: Based on '{query}', we found {len(results)} matching files. Future versions will use embeddings + LLM."
