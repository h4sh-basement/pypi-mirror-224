from pathlib import Path

import pycbzhelper

PARENT = Path(__file__).resolve().parent

if __name__ == "__main__":
    pages = []
    for i in range(11):
        pages.append({"File": (PARENT / "images" / f"page-{i:03d}.jpg")})

    metadata = {
        "Title": "T1 - Arrête de me chauffer, Nagatoro",
        "Series": "Arrête de me chauffer, Nagatoro",
        "Number": "1",
        "Count": 8,
        "Volume": 1,
        "Summary": "Nagatoro est en seconde. Pleine d\u2019assurance, joueuse, moqueuse, elle se d\u00e9couvre un jour un passe-temps favori : martyriser son \u201cSenpai\u201d, lyc\u00e9en de premi\u00e8re timide et mal dans sa peau. Nagatoro taquine, agace, aguiche, va parfois trop loin... mais qu\u2019a-t-elle vraiment derri\u00e8re la t\u00eate ? Et si derri\u00e8re ses moqueries elle cachait une v\u00e9ritable affection ?  Et si finalement, ses farces permettaient \u00e0 Senpai de s\u2019affirmer ?",
        "Year": 2021,
        "Month": 3,
        "Day": 12,
        "Writer": "Nanashi",
        "Inker": "Nanashi",
        "Editor": "Noeve Grafx",
        "Publisher": "Noeve Grafx",
        "Imprint": "Noeve Grafx",
        "Genre": "Shonen",
        "Web": "http://www.izneo.com/en/manga/shonen/arrete-de-me-chauffer-nagatoro-37560/arrete-de-me-chauffer-nagatoro-86232",
        "LanguageISO": "fr",
        "Format": "Preview",
        "BlackAndWhite": True,
        "Manga": "YesAndRightToLeft",
        "AgeRating": "Everyone 10+",
        "CommunityRating": "5.0",
        "ean": "9782490676569",
        "Pages": pages
    }

    path = PARENT / "eBooks" / "Arrête de me chauffer, Nagatoro.cbz"
    helper = pycbzhelper.Helper(metadata)
    helper.create_cbz(path=path)
    print(f"I: File created: {path}")
