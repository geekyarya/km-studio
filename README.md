# Kiara Autopilot (100% free)

| Job | Free tool |
|---|---|
| Content planning (outfits, locations, hooks, Hinglish captions, hashtags, festivals) | `make_plans.py`, offline content bank, no AI API |
| Images of Kiara with a consistent face | Google Colab free T4 GPU, RealVisXL + IP-Adapter face (`notebooks/weekly_studio.ipynb`) |
| Reels (zoom + crossfade + hook text + music) | ffmpeg on GitHub Actions |
| Posting Reels and photos | Instagram Graph API |
| Scheduler | GitHub Actions, hourly (unlimited free minutes on a **public** repo) |

## Daily volume (ramps up to protect the new account)
Set in `config.json`:
- Week 1: 1 Reel + 1 post a day
- Week 2: 2 + 1
- Week 3: 3 + 2
- Week 4: 4 + 3
- Day 30 onwards: 5 Reels + 3 posts a day

Raise the numbers in `ramp` if you want more. Up to 6 Reels and 4 posts a day fit the time slots.

## Setup (once)
1. **GitHub:** create a **public** repo with a neutral name (for example `km-studio`) and push this folder. Photos must be publicly reachable for Instagram to fetch them, and public repos get unlimited Actions minutes.
2. **GitHub token for Colab:** Settings → Developer settings → Fine-grained tokens → this repo only → *Contents: Read and write*.
3. **Instagram API token (free, no Facebook Page needed):**
   1. Go to developers.facebook.com, log in, then **My Apps → Create app**. Choose "Other", then type **Business**, and name it `KM Studio`.
   2. Add the product **Instagram → API setup with Instagram login**.
   3. Under "Generate access tokens", click **Add account**, log in as Kiara and allow it. Then click **Generate token** and copy it. It lasts 60 days, and you press the same button to renew it.
   4. Get `IG_USER_ID`: open `https://graph.instagram.com/v21.0/me?fields=user_id,username&access_token=YOUR_TOKEN` and copy `user_id`.
   5. While the app is in development mode, Kiara's account must be added as an Instagram tester under **App roles → Roles**, and the invite accepted in Instagram under Settings → Website permissions → Apps and websites → Tester invites.
4. **Repo settings → Secrets → Actions:** `IG_USER_ID`, `IG_ACCESS_TOKEN`.
5. **Repo settings → Variables:** `DRY_RUN=true` for the first test, then delete it.
6. **Music (optional but recommended):** put royalty-free `.mp3` files from the YouTube Audio Library or Pixabay Music in `music/`. Reels pick one at random.
7. Set `start_date` in `config.json` to your launch day.

## Weekly routine (about 30–60 minutes, mostly waiting)
Open `notebooks/weekly_studio.ipynb` in Colab → T4 GPU → Run all. It plans the next 8 days, generates every image and pushes them. The first time, it also asks you to pick Kiara's face.

## Tweaks
- Edit any day: change `plans/YYYY-MM-DD.json` (captions, outfits, slots) before the time comes.
- Add new outfits, locations, hooks or captions to `content_bank.py`. More lines give more variety.
- Add festival dates to `MOVABLE_FESTIVALS` each year.
- Test locally: `DRY_RUN=true python run_daily.py`
