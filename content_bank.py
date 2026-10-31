"""Offline content libraries. Combinations of these produce thousands of unique posts,
so no paid AI is needed for planning. Add your own lines anytime to keep it fresh."""

# Each pillar: outfits, locations, poses (one per image of a reel), reel hooks, captions.
PILLARS = {
    "desi_glam": {
        "outfits": [
            "deep maroon silk saree with gold border and sleeveless blouse, gold jhumkas",
            "emerald green chiffon saree, statement choker, hair in loose waves",
            "pastel pink lehenga with mirror work, maang tikka",
            "black sequin saree with halter blouse, minimal gold earrings",
            "ivory chikankari anarkali, silver jhumkas, open hair",
            "mustard yellow organza saree, gajra in hair",
            "royal blue velvet lehenga, kundan necklace",
            "red banarasi saree, bindi, glass bangles",
            "lavender sharara set with dupatta, pearl earrings",
            "bottle green bandhani lehenga, oxidised silver jewellery",
        ],
        "locations": [
            "a palace courtyard in Jaipur with arches", "a decorated wedding mandap with marigold flowers",
            "a heritage haveli balcony at golden hour", "a rooftop with fairy lights at dusk",
            "a mirror-lined royal hall", "a lotus pond at a palace garden",
            "a vintage wooden jharokha window", "a festive living room with diyas",
        ],
        "poses": [
            "twirling with saree pallu flowing, laughing", "looking over shoulder, soft smile",
            "adjusting earring, eyes to camera", "walking towards camera confidently",
            "sitting gracefully on steps, chin on hand", "holding dupatta in the wind, side profile",
        ],
        "hooks": ["Saree > everything", "Desi girl mode: ON", "Shaadi season ready?", "Rate this look 1-10",
                  "Main aur meri saree", "Lehenga or saree?"],
        "captions": [
            "Saree pehen ke attitude free mein aata hai 😌 Rate karo 1-10?",
            "Desi heart, global vibe ✨ Kaisa laga yeh look?",
            "Kisi ki shaadi mein aise jaun toh? 👀 Honest answers only",
            "Some days you just need to feel like royalty 👑 Agree?",
            "Mummy ne bola 'beta saree mein hi sundar lagti ho'… was she right? 🥹",
        ],
        "tags": ["#saree", "#sareelove", "#desigirl", "#indianwear", "#lehenga", "#ethnicwear", "#sareelovers",
                 "#indianfashion", "#weddingseason", "#desistyle"],
    },
    "city_girl": {
        "outfits": [
            "white linen shirt and denim shorts, gold hoops", "black bodycon midi dress, strappy heels",
            "oversized blazer with crop top and wide-leg trousers", "floral sundress, straw bag",
            "beige co-ord set, sunglasses on head", "red satin slip dress, minimal jewellery",
            "denim jacket over little black dress", "off-shoulder white top with high-waist jeans",
        ],
        "locations": [
            "Marine Drive at sunset with the sea behind", "a cozy Bandra cafe with plants",
            "a colourful Bandra street with graffiti walls", "inside a yellow-black Mumbai auto rickshaw",
            "a rooftop bar overlooking the Mumbai skyline at night", "Bandstand promenade in the evening",
            "a rainy Mumbai street with an umbrella", "Colaba causeway street market",
        ],
        "poses": [
            "walking and laughing candidly", "sipping coffee, looking out the window",
            "leaning on railing, wind in hair", "turning back to camera with a playful smile",
            "sitting cross-legged, holding sunglasses", "mid-step on the street, hair flip",
        ],
        "hooks": ["Mumbai nights hit different", "Bandra girl things", "POV: date with a Mumbai girl",
                  "Weekend plans?", "Sunset > everything", "City of dreams 🌆"],
        "captions": [
            "Mumbai ki shaam aur main 🌆 Tumhara favourite spot kaunsa hai?",
            "Late as always, cute as always 😌 Who else is never on time?",
            "Bandra ki galiyan aur meri vibe ✨ Coffee pe chaloge?",
            "Sea breeze therapy 🌊 Marine Drive ya Bandstand?",
            "Main-character energy only 💅 Weekend plans batao",
        ],
        "tags": ["#mumbai", "#mumbaigirl", "#bandra", "#marinedrive", "#mumbaidiaries", "#citygirl",
                 "#ootd", "#streetstyle", "#mumbaiblogger", "#weekendvibes"],
    },
    "fitness": {
        "outfits": [
            "black sports bra and high-waist leggings", "pastel matching gym set",
            "oversized tee and biker shorts", "white yoga set", "olive green athleisure set",
        ],
        "locations": [
            "a modern gym with mirrors", "a sunrise beach in Juhu doing yoga", "a rooftop yoga mat at sunrise",
            "a running track in the morning", "a home workout corner with plants",
        ],
        "poses": [
            "mirror selfie with phone, confident smile", "stretching on a yoga mat, serene",
            "lifting dumbbells, focused", "drinking water, sweaty and happy", "doing a yoga pose at sunrise",
        ],
        "hooks": ["Leg day? Never heard of her", "5am club ☀️", "Gym crush energy", "Consistency > motivation",
                  "Monday motivation"],
        "captions": [
            "Leg day pe bhi smile 😅 Tumhara favourite workout?",
            "Discipline wali vibe 💪 Kaun kaun gym gaya aaj?",
            "Sunrise yoga > alarm snooze 🌅 Try karoge kal?",
            "Healthy is the new sexy ✨ Agree or disagree?",
        ],
        "tags": ["#fitness", "#gymgirl", "#fitnessmotivation", "#yoga", "#indianfitness", "#workout",
                 "#healthylifestyle", "#fitgirl", "#gymlife"],
    },
    "pov_flirty": {
        "outfits": [
            "red bodycon dress with gold earrings", "black saree with sleeveless blouse",
            "white shirt dress, messy bun", "lilac satin co-ord", "little black dress with heels",
        ],
        "locations": [
            "a candle-lit restaurant table", "a fancy party with bokeh lights", "a wedding sangeet stage",
            "a car passenger seat at night with city lights", "a hotel balcony at night",
        ],
        "poses": [
            "looking at camera with a teasing smile", "biting lip slightly, playful eyes",
            "whispering towards camera, finger on lips", "laughing and looking away shyly",
            "raising one eyebrow, smirking",
        ],
        "hooks": ["POV: you meet me at a Mumbai wedding", "POV: our first date", "When he says 'I'll call at 9'",
                  "POV: you made me laugh", "Tell me you're in love without telling me"],
        "captions": [
            "Itna mat dekho, pyaar ho jayega 😏",
            "First date pe kahan le chaloge? Best answer gets a reply 💌",
            "Tum 9 baje call karne wale the… it's 11 😒",
            "Main real hoon ya dream? Tum decide karo 😉",
        ],
        "tags": ["#pov", "#reels", "#relatable", "#desigirl", "#flirty", "#trending", "#reelsindia",
                 "#explorepage", "#instareels"],
    },
    "soft_real": {
        "outfits": [
            "oversized hoodie and shorts, hair in a messy bun", "cotton kurta and pyjama",
            "comfy cardigan over a white tee", "simple yellow salwar suit",
        ],
        "locations": [
            "a rainy window with a cup of chai", "a cozy bed with fairy lights", "her grandmother's kitchen in Jaipur",
            "a balcony with plants on a monsoon evening", "a bookstore corner",
        ],
        "poses": [
            "holding chai with both hands, gazing outside", "smiling softly, no makeup look",
            "reading a book, relaxed", "wrapped in a blanket, sleepy smile",
        ],
        "hooks": ["Chai + baarish = therapy", "Missing home today", "Soft girl era", "Sunday reset"],
        "captions": [
            "Baarish, chai aur purane gaane ☕🌧️ Perfect combo, haan?",
            "Kabhi kabhi ghar ki bahut yaad aati hai 🥹 Tum kahan se ho?",
            "No makeup, no filter mood today ✨",
            "Sunday = chai, books aur zero plans 📚",
        ],
        "tags": ["#chai", "#chailover", "#softgirl", "#homesick", "#jaipur", "#cozyvibes",
                 "#sundayvibes", "#selfcare"],
    },
}

ALWAYS_TAGS = ["#AIgenerated", "#kiaramehra"]

SIGN_OFFS = ["Milte hain, jaan 💋", "", "", "✨", "💋"]

# Festival overrides by month-day (IST). Change pillar mood on these days.
FESTIVALS = {
    "01-14": "Makar Sankranti kite-flying on a rooftop",
    "01-26": "Republic Day look with tricolour accessories",
    "02-14": "Valentine's Day red outfit",
    "08-15": "Independence Day white outfit with tricolour dupatta",
    "12-25": "Christmas party look with fairy lights",
    "12-31": "New Year's Eve party sequins",
}

# Festivals whose date moves every year (full dates). Double-check and add next year's.
MOVABLE_FESTIVALS = {
    "2026-11-08": "Diwali night with diyas and rangoli",
    "2027-03-22": "Holi celebration with colours on face",
    "2027-10-29": "Diwali night with diyas and rangoli",
}
