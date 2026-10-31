"""Turns 1-3 still images into a 9:16 Reel with slow zoom, crossfades, hook text and music.
Uses only ffmpeg + Pillow (free, preinstalled on GitHub Actions)."""
import pathlib
import random
import re
import subprocess
import tempfile

from PIL import Image, ImageDraw, ImageFont

W, H, FPS = 1080, 1920, 30
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
MUSIC_DIR = pathlib.Path(__file__).parent / "music"


def _strip_emoji(text: str) -> str:
    return re.sub(r"[^\w\s\-\?\!\.,'&:>+=/]", "", text).strip()


def _text_overlay(text: str, path: pathlib.Path) -> None:
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(FONT, 64)
    words, lines, line = _strip_emoji(text).split(), [], ""
    for w in words:  # wrap to ~900px
        trial = f"{line} {w}".strip()
        if draw.textlength(trial, font=font) > 900 and line:
            lines.append(line)
            line = w
        else:
            line = trial
    lines.append(line)
    y = int(H * 0.16)
    for ln in lines:
        tw = draw.textlength(ln, font=font)
        x = (W - tw) / 2
        draw.rounded_rectangle([x - 24, y - 12, x + tw + 24, y + 80], radius=18, fill=(0, 0, 0, 140))
        draw.text((x, y), ln, font=font, fill="white")
        y += 100
    img.save(path)


def make_reel(images: list[str], hook: str | None, out: str, seconds_per_image: float = 2.6) -> str:
    n, fade = len(images), 0.4
    total = n * seconds_per_image - (n - 1) * fade
    with tempfile.TemporaryDirectory() as tmp:
        overlay = pathlib.Path(tmp) / "text.png"
        _text_overlay(hook or "", overlay)

        cmd = ["ffmpeg", "-y", "-loglevel", "error"]
        for img in images:
            cmd += ["-loop", "1", "-t", str(seconds_per_image), "-i", img]
        cmd += ["-i", str(overlay)]
        tracks = sorted(MUSIC_DIR.glob("*.mp3")) + sorted(MUSIC_DIR.glob("*.m4a"))
        if tracks:
            cmd += ["-stream_loop", "-1", "-i", str(random.choice(tracks))]
        else:
            cmd += ["-f", "lavfi", "-i", "anullsrc=r=44100:cl=stereo"]

        frames = int(seconds_per_image * FPS)
        parts = []
        for i in range(n):
            zoom_in = i % 2 == 0
            z = "min(zoom+0.0009,1.15)" if zoom_in else "if(eq(on,0),1.15,max(zoom-0.0009,1.0))"
            parts.append(
                f"[{i}:v]scale={W*2}:{H*2}:force_original_aspect_ratio=increase,crop={W*2}:{H*2},"
                f"zoompan=z='{z}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={frames}:s={W}x{H}:fps={FPS},"
                f"setsar=1,format=yuv420p[v{i}]"
            )
        last = "v0"
        for i in range(1, n):
            offset = i * (seconds_per_image - fade)
            parts.append(f"[{last}][v{i}]xfade=transition=fade:duration={fade}:offset={offset:.2f}[x{i}]")
            last = f"x{i}"
        parts.append(f"[{last}][{n}:v]overlay=0:0,format=yuv420p[vout]")
        parts.append(f"[{n+1}:a]atrim=0:{total:.2f},afade=t=out:st={total-1:.2f}:d=1[aout]")

        cmd += [
            "-filter_complex", ";".join(parts), "-map", "[vout]", "-map", "[aout]",
            "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-r", str(FPS),
            "-c:a", "aac", "-b:a", "128k", "-t", f"{total:.2f}", "-movflags", "+faststart", out,
        ]
        subprocess.run(cmd, check=True)
    return out


def make_post_image(src: str, out: str) -> str:
    """Center-crops to Instagram's 4:5 portrait (1080x1350) JPEG."""
    img = Image.open(src).convert("RGB")
    target = 1080 / 1350
    w, h = img.size
    if w / h > target:
        nw = int(h * target)
        img = img.crop(((w - nw) // 2, 0, (w - nw) // 2 + nw, h))
    else:
        nh = int(w / target)
        img = img.crop((0, (h - nh) // 2, w, (h - nh) // 2 + nh))
    img.resize((1080, 1350), Image.LANCZOS).save(out, "JPEG", quality=92)
    return out
