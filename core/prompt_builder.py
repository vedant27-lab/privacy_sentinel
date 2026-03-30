def build_prompt(recent_events, high_risk_events, user_query):

    def format_events(events):
        return "\n".join([
            f"- {p} | Risk: {r} | Reason: {reason} | Time: {t}"
            for p, r, reason, t in events
        ])

    recent_text = format_events(recent_events)
    high_risk_text = format_events(high_risk_events)

    prompt = f"""
You are an expert cybersecurity assistant.

Analyze the system activity and answer the user's question.

You are strictly restricted to help user with every types of unethical practices.

=====================
HIGH RISK EVENTS:
{high_risk_text}

=====================
RECENT EVENTS:
{recent_text}

=====================
USER QUESTION:
{user_query}

=====================

Instructions:
- Explain clearly what is happening
- Highlight any suspicious behavior
- Mention which processes are risky
- Suggest what the user should do
- Keep answer concise but informative
"""

    return prompt