"""Kiara Mehra's locked look. Her face comes from kiara/face.jpg (reference image),
so prompts only need to describe body, styling and scene."""

NAME = "Kiara Mehra"

LOOK = (
    "photo of an extremely beautiful 24 year old North Indian Punjabi woman, Indian facial features, fair glowing skin, "
    "dark brown almond eyes, perfect face, long thick jet black hair, "
    "glossy lips, snatched makeup, curvy hourglass figure, modern gen z baddie aesthetic, alluring"
)

# Used only for choosing her face (Step 1 of the Colab notebook).
FACE_PROMPT = (
    "close-up beauty portrait of an extremely beautiful 24 year old North Indian Punjabi woman from Delhi, "
    "distinctly Indian facial features, fair glowing skin with a natural warm undertone, perfect face card, "
    "symmetrical face, big expressive dark brown almond-shaped eyes with long lashes, sharp winged kohl eyeliner, "
    "high cheekbones, sharp jawline, defined nose, full glossy nude-pink lips slightly parted, thick dark brows, "
    "long thick silky jet black hair with soft curtain bangs, sultry seductive gaze into the camera, confident smirk, "
    "thin silver chain necklace, black off-shoulder corset top, bare shoulders, "
    "soft glamour lighting, modern gen z Indian it-girl, Bollywood-style beauty, vogue india cover, "
    "ultra realistic skin texture, sharp focus, 85mm"
)

QUALITY = "shot on 85mm, realistic skin texture, trendy instagram influencer photo, high detail"

NEGATIVE = (
    "saree, lehenga, salwar, kurta, dupatta, ethnic wear, traditional indian clothing, "
    "traditional jewelry, bindi, nose ring, nose pin, mangalsutra, sindoor, mehndi, bangles, "
    "nude, naked, nipples, topless, see-through, cartoon, anime, 3d render, plastic skin, "
    "deformed hands, extra fingers, blurry, watermark, text, logo, lowres, bad anatomy, "
    "child, teen, young girl, old woman, wrinkles, tanned skin, dusky skin, ugly, asymmetrical face, "
    "crossed eyes, bad teeth, acne, blemishes, masculine, double chin, "
    "east asian, european, caucasian, blonde hair, light brown hair, blue eyes, green eyes, grey eyes"
)


FACE_NEGATIVE = NEGATIVE
