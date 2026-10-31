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
- Week 1: 2 Reels + 2 posts a day
- Week 2: 4 + 3
- Week 3: 6 + 4
- Day 21 onwards: 8 Reels + 5 posts a day

Change the numbers in `ramp` in `config.json` to post more or less.

## Setup (once)
1. **GitHub:** create a **public** repo with a neutral name (for example `km-studio`) and push this folder. Photos must be publicly reachable for Instagram to fetch them, and public repos get unlimited Actions minutes.
2. **GitHub token for Colab:** Settings → Developer settings → Fine-grained tokens → this repo only → *Contents: Read and write*.
3. **Instagram API token (free, never expires):** in Kiara's own business portfolio ("Kiara Mehra Studio"), with Meta app "KM Studio":
   1. Business settings → Accounts → Instagram accounts → connect Kiara's Instagram.
   2. Users → System users → add `km-autopost` (Employee). Assign assets: the KM Studio app plus Kiara's Instagram account.
   3. Generate token → app KM Studio → expiration **Never** → permissions `instagram_basic` and `instagram_content_publish` only.
   4. `IG_USER_ID` = Kiara's Instagram account ID (shown in Business settings → Instagram accounts).
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
