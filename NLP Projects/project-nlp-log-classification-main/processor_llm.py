from dotenv import load_dotenv
from groq import Groq
import json

# Load environment variables from .env
load_dotenv()

# Initialize Groq client
groq = Groq()

def classify_with_llm(log_msg):
    """
    Classify a log message into one of four categories:
    1. Workflow Error — unexpected errors in workflows, processes, or system operations.
    2. Deprecation Warning — notifications about features/modules being deprecated.
    3. User Action — intentional actions performed by users (e.g., system reboot, manual task execution).
    4. Unclassified — anything that does not match the above categories.
    """
    # Fixed prompt
    prompt = f"""Classify the log message into one of these categories:
1. "Workflow Error" — unexpected errors in workflows, processes, or system operations.
2. "Deprecation Warning" — notifications about features/modules being deprecated.
3. "User Action" — intentional actions performed by users (e.g., system reboot, manual task execution).
If it doesn't match any of the above, use "Unclassified".
Return only valid JSON like this: {{ "category": "..." }}.
Do not include any extra text or explanation.
Log message: {log_msg}"""

    # Call the LLM
    chat_completion = groq.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="llama-3.3-70b-versatile",
        temperature=0.5
    )

    content = chat_completion.choices[0].message.content.strip()

    # Parse JSON safely
    try:
        data = json.loads(content)
        category = data.get("category", "Unclassified")
    except json.JSONDecodeError:
        category = "Unclassified"

    return category

if __name__ == "__main__":
    logs = [
        "Case escalation for ticket ID 7324 failed because the assigned support agent is no longer active.",
        "The 'ReportGenerator' module will be retired in version 4.0. Please migrate to the 'AdvancedAnalyticsSuite' by Dec 2025",
        "System reboot initiated by user 12345."
    ]

    for log in logs:
        print(classify_with_llm(log))
