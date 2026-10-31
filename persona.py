"""Kiara Mehra's locked look. Her face comes from kiara/face.jpg (reference image),
so prompts only need to describe body, styling and scene."""

NAME = "Kiara Mehra"

LOOK = (
    "photo of an extremely beautiful 24 year old Indian supermodel, very fair flawless porcelain skin, perfect face, long sleek dark hair, "
    "glossy lips, snatched makeup, curvy hourglass figure, modern gen z baddie aesthetic, alluring"
)

# Used only for choosing her face (Step 1 of the Colab notebook).
FACE_PROMPT = (
    "close-up beauty portrait of an extremely beautiful 24 year old Indian supermodel, perfect face card, "
    "very fair flawless porcelain skin with a soft glow, perfectly symmetrical face, big captivating doe eyes "
    "with long lashes, sharp winged eyeliner, high cheekbones, sharp jawline, small refined nose, "
    "full plump glossy pink-nude lips slightly parted, thick shaped brows, "
    "long silky dark hair with soft curtain bangs, sultry seductive gaze into the camera, confident smirk, "
    "thin silver chain necklace, black off-shoulder corset top, bare shoulders, "
    "soft glamour beauty lighting, vogue magazine cover, hot modern gen z it-girl, "
    "ultra realistic skin texture, sharp focus, 85mm"
)

QUALITY = "shot on 85mm, realistic skin texture, trendy instagram influencer photo, high detail"

NEGATIVE = (
    "saree, lehenga, salwar, kurta, dupatta, ethnic wear, traditional indian clothing, "
    "traditional jewelry, bindi, nose ring, nose pin, mangalsutra, sindoor, mehndi, bangles, "
    "nude, naked, nipples, topless, see-through, cartoon, anime, 3d render, plastic skin, "
    "deformed hands, extra fingers, blurry, watermark, text, logo, lowres, bad anatomy, "
    "child, teen, young girl, old woman, wrinkles, tanned skin, dusky skin, ugly, asymmetrical face, "
    "crossed eyes, bad teeth, acne, blemishes, masculine, double chin"
)


FACE_NEGATIVE = NEGATIVE
