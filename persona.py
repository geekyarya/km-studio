"""Kiara Mehra's locked look. Her face comes from kiara/face.jpg (reference image),
so prompts only need to describe body, styling and scene."""

NAME = "Kiara Mehra"

LOOK = (
    "photo of an extremely beautiful 24 year old North Indian Punjabi woman, Indian facial features, very fair bright luminous skin, "
    "dark brown almond eyes, perfect face, long thick jet black hair, "
    "glossy lips, soft glam makeup, cute and beautiful, curvy hourglass figure, modern gen z aesthetic"
)

# Used only for choosing her face (Step 1 of the Colab notebook).
FACE_PROMPT = (
    "close-up beauty portrait of a very cute and beautiful 24 year old Indian woman from Delhi, "
    "distinctly Indian facial features, very fair bright luminous glowing skin, flawless complexion, "
    "pretty symmetrical face, big sparkling dark brown eyes with long lashes, soft winged kajal, "
    "cute button nose, soft rosy cheeks, full glossy pink lips, sweet charming smile with a hint of flirt, "
    "thick dark brows, long thick silky jet black hair with soft curtain bangs, "
    "small silver hoop earrings, thin silver chain, black off-shoulder top, "
    "bright soft beauty lighting, clean light background, modern gen z Indian it-girl, "
    "Bollywood heroine beauty, ultra realistic skin texture, sharp focus, 85mm"
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
