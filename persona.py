"""Kiara Mehra's locked look. Her face comes from kiara/face.jpg (reference image),
so prompts only need to describe body, styling and scene."""

NAME = "Kiara Mehra"

LOOK = (
    "photo of a beautiful elegant 24 year old Indian woman, clearly a grown adult woman in her mid twenties, "
    "mature refined facial features, defined cheekbones and jawline, fair glowing skin, dark brown eyes, "
    "long thick dark hair, polished makeup, confident poised adult presence, fit womanly figure, "
    "modern professional fashion influencer"
)

# Used only for choosing her face (Step 1 of the Colab notebook).
FACE_PROMPT = (
    "close-up editorial portrait of a beautiful elegant 24 year old Indian woman from Delhi, "
    "clearly a grown adult woman in her mid twenties, mature refined facial features, defined cheekbones, "
    "strong jawline, fair glowing skin, dark brown almond eyes, groomed brows, polished soft glam makeup, "
    "long thick dark hair, confident poised expression, subtle smile, small silver hoop earrings, "
    "black blazer over a simple black top, soft studio lighting, fashion magazine portrait of a "
    "successful modern woman, ultra realistic skin texture, sharp focus, 85mm"
)

QUALITY = "shot on 85mm, realistic skin texture, trendy instagram influencer photo, high detail"

NEGATIVE = (
    "saree, lehenga, salwar, kurta, dupatta, ethnic wear, traditional indian clothing, "
    "traditional jewelry, bindi, nose ring, nose pin, mangalsutra, sindoor, mehndi, bangles, "
    "nude, naked, nipples, topless, see-through, cartoon, anime, 3d render, plastic skin, "
    "deformed hands, extra fingers, blurry, watermark, text, logo, lowres, bad anatomy, "
    "child, teen, teenager, young girl, schoolgirl, baby face, childlike, young-looking, petite, "
    "underage, kid, adolescent, old woman, wrinkles, tanned skin, dusky skin, ugly, asymmetrical face, "
    "crossed eyes, bad teeth, acne, blemishes, masculine, double chin, "
    "east asian, european, caucasian, blonde hair, light brown hair, blue eyes, green eyes, grey eyes"
)


FACE_NEGATIVE = NEGATIVE
