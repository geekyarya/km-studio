"""Uses Claude to decide today's post, avoiding repeats of recent posts."""
import datetime
import json

import anthropic

import persona

MODEL = "claude-opus-5-5"

SCHEMA = {
    "type": "object",
    "properties": {
        "pillar": {"type": "string"},
        "title": {"type": "string", "description": "Short internal name for this post"},
        "outfit": {"type": "string"},
        "location": {"type": "string"},
        "pose_expression": {"type": "string"},
        "video_motion": {"type": "string", "description": "Camera + subject motion for a 5s clip"},
        "on_screen_text": {"type": "string", "description": "Hook text overlay, max 8 words"},
        "caption": {"type": "string"},
        "hashtags": {"type": "array", "items": {"type": "string"}},
        "suggested_audio": {"type": "string", "description": "Kind of trending audio to add"},
    },
    "required": [
        "pillar", "title", "outfit", "location", "pose_expression", "video_motion",
        "on_screen_text", "caption", "hashtags", "suggested_audio",
    ],
    "additionalProperties": False,
}


def plan_today(history: list[dict]) -> dict:
    client = anthropic.Anthropic()
    today = datetime.date.today()
    recent = [f"{h['date']}: [{h['pillar']}] {h['title']}" for h in history[-21:]]

    prompt = f"""You are the content director for an AI virtual influencer.

PERSONA:{persona.PERSONA}
CONTENT PILLARS: {json.dumps(persona.PILLARS)}
RULES:{persona.RULES}

Today is {today:%A, %d %B %Y}. Consider Indian festivals, seasons and weekday mood
(e.g. Monday motivation, weekend outings) happening around this date.

Recently posted (do not repeat ideas, rotate pillars evenly):
{chr(10).join(recent) or "nothing yet - this is the first post, make it a strong intro"}

Plan today's single Instagram Reel for Kiara."""

    response = client.beta.messages.create(
        model=MODEL,
        max_tokens=16000,
        betas=["server-side-fallback-2026-07-01"],
        fallbacks="default",
        output_config={"effort": "medium", "format": {"type": "json_schema", "schema": SCHEMA}},
        messages=[{"role": "user", "content": prompt}],
    )
    if response.stop_reason == "refusal":
        raise RuntimeError(f"Planner declined: {response.stop_details}")
    text = next(b.text for b in response.content if b.type == "text")
    plan = json.loads(text)
    if "#AIgenerated" not in plan["caption"] and "#AIgenerated" not in plan["hashtags"]:
        plan["hashtags"].append("#AIgenerated")
    return plan
