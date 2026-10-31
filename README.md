# Kiara Autopilot

Every day: Claude picks Kiara's post (pillar rotation, festivals, no repeats) → Flux makes the image with her face LoRA → Kling animates it → it posts to Instagram, or waits for your review.

## One-time setup
1. **Train her face:** generate ~30 images with `persona.LOOK`, keep the 20 most consistent, train a Flux LoRA on fal.ai (`fal-ai/flux-lora-fast-training`). Its URL goes in `KIARA_LORA_URL`.
2. **Instagram:** create Kiara's account → switch to a Creator/Business account → link a Facebook Page → create a Meta developer app → get `IG_USER_ID` and a long-lived `IG_ACCESS_TOKEN`. Turn on the "AI info" label in the account settings.
3. **Keys:** `ANTHROPIC_API_KEY` (console.anthropic.com), `FAL_KEY` (fal.ai).
4. Push this folder to a private GitHub repo and add the five values above under **Settings → Secrets → Actions**.

## Running
- Automatic: GitHub Actions runs daily at 5:47 PM IST. Download the result from the run's artifacts.
- Start in **review mode** (default). Once the posts look right, add a repository *variable* `AUTO_POST=true` for fully hands-off posting.
- Local test: `python run_daily.py --plan-only` (only needs `ANTHROPIC_API_KEY`).
