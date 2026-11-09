"""Offline content library. Topic mix (weights in config.json "pillar_weights"):
cricket > bollywood > rahasyamai > news. Kiara appears in a scene that matches each topic.
Cricket / Bollywood / news items get a fresh real headline from Google News at posting time
(see news.py); rahasyamai uses the evergreen mysteries below.
Never depict real players or celebrities - images show only Kiara."""

PILLARS = {
    "cricket": {
        "news_query": "cricket India",
        "outfits": [
            "blue cricket fan jersey and denim shorts", "oversized blue fan jersey and a white cap",
            "white t-shirt with a small tricolour painted on her cheek", "orange and blue fan t-shirt and jeans",
            "blue jersey tied at the waist with white sneakers",
        ],
        "locations": [
            "packed cricket stadium stands at night under floodlights", "a sports bar watching cricket on a big screen",
            "living room watching a cricket match on TV with snacks", "a gully cricket street in Mumbai at golden hour",
            "a cricket ground boundary rope at sunset",
        ],
        "poses": [
            "cheering with both arms raised, excited", "holding a cricket bat on her shoulder, confident smile",
            "biting her nails nervously watching the match", "celebrating with a fist pump and big smile",
            "waving a small tricolour flag and cheering",
        ],
        "hooks": ["Match day mood 🏏", "Who's watching today?", "Cricket > everything"],
        "reactions": [
            "Tumhara kya prediction hai? 👇", "Main toh full support mein hoon 💙 Tum?",
            "Aaj ka man of the match kaun? Comment karo 🏏", "Dil thaam ke baitho guys 😮‍💨",
        ],
        "tags": ["#cricket", "#teamindia", "#cricketlovers", "#indiancricket", "#cricketfans", "#bleedblue",
                 "#cricketnews", "#reelsindia"],
    },
    "bollywood": {
        "news_query": "Bollywood",
        "outfits": [
            "glamorous red evening gown", "black blazer dress", "retro polka dot dress",
            "white shirt and oversized sunglasses", "champagne satin dress",
        ],
        "locations": [
            "a movie theatre seat holding popcorn", "a red carpet with camera flashes",
            "a vintage film set with a clapperboard and spotlights", "a home movie night with a projector",
            "a film studio backdrop with director chairs",
        ],
        "poses": [
            "eating popcorn reacting with surprise", "filmy pose with arms open wide, smiling",
            "holding a clapperboard, playful smile", "looking over her shoulder on the red carpet",
        ],
        "hooks": ["Bollywood tea ☕", "Filmy update 🎬", "Did you hear this?"],
        "reactions": [
            "Tumhara kya reaction hai? 🍿", "Yeh dekhoge ya skip? Comment karo 🎬",
            "Filmy log, opinions do 👇", "Main toh excited hoon 😍 Tum?",
        ],
        "tags": ["#bollywood", "#bollywoodnews", "#filmy", "#bollywoodupdates", "#moviebuff", "#cinema",
                 "#reelsindia", "#entertainment"],
    },
    "rahasyamai": {
        "news_query": None,
        "outfits": [
            "black leather jacket and jeans", "dark trench coat and boots", "black hoodie and cargo pants",
            "olive jacket with a small backpack",
        ],
        "locations": [
            "ruins of an abandoned old fort at night in fog", "a deserted village of stone houses at dusk",
            "a foggy forest under moonlight", "a dark old haveli corridor lit by a lantern",
            "a candle-lit room with old maps and books",
        ],
        "poses": [
            "holding a flashlight, looking around cautiously", "looking back over her shoulder, suspicious",
            "reading an old map by candlelight", "finger on lips, mysterious look",
        ],
        "hooks": [
            "Bhangarh Fort: India's most haunted?", "Kuldhara: the village emptied overnight",
            "Roopkund: the lake of skeletons", "Jatinga: where birds fall from the sky",
            "Magnetic Hill: do cars roll uphill?", "Barog tunnel's unsolved story",
            "Lonar Lake: a crater from space", "Shaniwarwada's midnight legend",
            "Dumas Beach: why locals avoid it at night", "Kodinhi: India's village of twins",
        ],
        "reactions": [
            "Kya tum yahan raat ko jaoge? 👀", "Sach ya kahani? Comment karo 👇",
            "Part 2 chahiye? 'Haan' likho 🕯️", "Is jagah ka koi aur rahasya pata hai? 👇",
        ],
        "tags": ["#rahasya", "#mystery", "#unsolvedmysteries", "#hauntedplaces", "#indianmysteries", "#horror",
                 "#facts", "#reelsindia"],
    },
    "news": {
        "news_query": "",  # empty = India top stories
        "outfits": [
            "navy blazer and white blouse", "beige blazer over a black top", "white shirt with rolled sleeves",
            "grey blazer and black trousers",
        ],
        "locations": [
            "a modern TV news studio with screens behind", "a news desk with a microphone",
            "a podcast studio with a mic and headphones", "a city street holding a newspaper",
        ],
        "poses": [
            "sitting at a news desk talking to camera", "holding a microphone, serious expression",
            "reading a newspaper, raising an eyebrow", "pointing at a screen behind her",
        ],
        "hooks": ["Today's big news 📰", "Aaj ki khabar", "Quick news update"],
        "reactions": [
            "Is par tumhari kya raay hai? 👇", "Share karo jinko pata hona chahiye 📢",
            "Aise updates daily chahiye? Follow karo ✨",
        ],
        "tags": ["#news", "#indianews", "#breakingnews", "#todaynews", "#newsupdate", "#dailynews",
                 "#reelsindia"],
    },
}

ALWAYS_TAGS = ["#AIgenerated", "#kiaramehra"]

SIGN_OFFS = ["Milte hain, jaan 💋", "", "", "✨"]

# Special days (MM-DD) - replaces the scene for the first item of the day.
FESTIVALS = {
    "01-01": "a New Year's brunch with champagne and a sequin outfit",
    "12-25": "a Christmas party with fairy lights",
    "12-31": "a New Year's Eve party with confetti",
}
MOVABLE_FESTIVALS = {
    "2027-03-22": "a Holi party with colour powder on a white t-shirt",
    "2027-10-29": "a Diwali night party with fairy lights and sparklers",
}
