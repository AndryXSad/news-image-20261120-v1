#!/usr/bin/env python3
"""Render the 20 November 2026 world-news poster (1024x1024 PNG).

Drawn from scratch with PIL: masthead, two lead stories, a markets
strip, cyclone + climate panels, an Around-the-World grid, and a
sports ticker. Deterministic output: no timestamps, no randomness.

Layout budget (1024 tall): masthead 0-118, leads 136-400,
markets 412-500, weather/climate 512-644, world grid 656-928,
sport 938-1000, footer 1008-1024.
"""
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "entry.png")

PAPER = (247, 243, 232)
INK = (18, 24, 34)
NAVY = (15, 42, 74)
NAVY2 = (23, 63, 105)
RED = (176, 30, 36)
GOLD = (198, 148, 44)
TEAL = (14, 110, 110)
GREY = (90, 96, 104)
LIGHT = (233, 228, 214)
WHITE = (255, 255, 255)
GREEN = (24, 120, 60)
DARKRED = (150, 20, 25)

FDIR = "/usr/share/fonts/truetype/dejavu"


def font(name, size):
    return ImageFont.truetype(os.path.join(FDIR, name), size)


SERIF_B = lambda s: font("DejaVuSerif-Bold.ttf", s)
SANS_B = lambda s: font("DejaVuSans-Bold.ttf", s)
SANS = lambda s: font("DejaVuSans.ttf", s)


def wrap(draw, text, fnt, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=fnt) <= max_w:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def text_block(draw, x, y, text, fnt, fill, max_w, leading=None):
    lh = leading or int(fnt.size * 1.28)
    for ln in wrap(draw, text, fnt, max_w):
        draw.text((x, y), ln, font=fnt, fill=fill)
        y += lh
    return y


def tag(draw, x, y, label, bg, fg=WHITE, size=16):
    f = SANS_B(size)
    w = int(draw.textlength(label, font=f) + 16)
    draw.rounded_rectangle([x, y, x + w, y + size + 11], radius=4, fill=bg)
    draw.text((x + 8, y + 5), label, font=f, fill=fg)
    return w


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # ---------- masthead ----------
    d.rectangle([0, 0, W, 118], fill=NAVY)
    d.rectangle([0, 118, W, 124], fill=RED)
    d.text((16, 8), "THE WORLD TODAY", font=SERIF_B(58), fill=WHITE)
    d.text((16, 74), "FRIDAY  •  20 NOVEMBER 2026", font=SANS_B(30), fill=(255, 214, 90))
    d.text((700, 20), "ONE DAY.", font=SANS_B(26), fill=WHITE)
    d.text((700, 52), "ONE PLANET.", font=SANS_B(26), fill=WHITE)
    d.text((700, 84), "EVERY STORY.", font=SANS_B(26), fill=(255, 214, 90))

    # ---------- lead row (136-400) ----------
    d.rectangle([16, 136, 500, 400], outline=NAVY, width=2, fill=WHITE)
    tag(d, 28, 148, "LEAD  •  SHENZHEN, CHINA", RED)
    for i, c1 in enumerate([(178, 34, 52), (222, 41, 16), (255, 255, 255)]):
        x0 = 30 + i * 62
        d.rectangle([x0, 184, x0 + 52, 208], fill=c1, outline=INK, width=1)
        if i == 0:
            d.text((x0 + 4, 186), "★", font=SANS_B(16), fill=WHITE)
        if i == 1:
            for s in range(5):
                d.text((x0 + 4 + s * 9, 186), "★", font=SANS_B(9), fill=(255, 222, 0))
        if i == 2:
            d.rectangle([x0, 184, x0 + 52, 192], fill=(0, 57, 166))
            d.rectangle([x0, 192, x0 + 52, 200], fill=WHITE)
            d.rectangle([x0, 200, x0 + 52, 208], fill=(213, 0, 50))
    d.text((224, 186), "USA  •  CHINA  •  RUSSIA", font=SANS_B(17), fill=NAVY)
    y = text_block(d, 28, 218, "Trump, Xi and Putin hold first-ever three-way summit", SERIF_B(27), INK, 452, leading=33)
    text_block(d, 28, y + 4, "Joint peace declaration signed in Shenzhen, covering Ukraine, nuclear arms and trade. Trump puts Ukraine first.", SANS(17), INK, 452, leading=21)
    d.text((28, 374), "Sources: Reuters, TASS, AFP  •  19 Nov, reported 20 Nov", font=SANS(13), fill=GREY)

    d.rectangle([516, 136, 1008, 400], outline=NAVY, width=2, fill=WHITE)
    tag(d, 528, 148, "JUSTICE  •  THE HAGUE", NAVY2)
    cx, cy = 948, 196
    d.line([cx, cy - 16, cx, cy + 16], fill=GOLD, width=4)
    d.line([cx - 28, cy - 16, cx + 28, cy - 16], fill=GOLD, width=4)
    d.line([cx - 28, cy - 16, cx - 28, cy + 4], fill=GOLD, width=3)
    d.line([cx + 28, cy - 16, cx + 28, cy + 4], fill=GOLD, width=3)
    d.arc([cx - 40, cy - 2, cx - 16, cy + 14], 0, 180, fill=GOLD, width=3)
    d.arc([cx + 16, cy - 2, cx + 40, cy + 14], 0, 180, fill=GOLD, width=3)
    d.rectangle([cx - 32, cy + 16, cx + 32, cy + 22], fill=GOLD)
    y = text_block(d, 528, 218, "World Court: Myanmar committed genocide against the Rohingya", SERIF_B(27), INK, 452, leading=33)
    text_block(d, 528, y + 4, "ICJ rules 9–6 in The Gambia v. Myanmar — the first time a state is found responsible for genocide.", SANS(17), INK, 452, leading=21)
    d.text((528, 374), "Sources: ICJ, UN, Reuters  •  19 Nov 2026", font=SANS(13), fill=GREY)

    # ---------- markets strip (412-500) ----------
    d.rectangle([16, 412, 1008, 500], fill=(20, 28, 40))
    d.text((28, 420), "MARKETS IN TURMOIL — Anthropic's record IPO fails to calm the AI sell-off", font=SANS_B(18), fill=(255, 214, 90))
    chips = [
        ("S&P -2.0%", DARKRED), ("NASDAQ -2.3%", DARKRED),
        ("NIKKEI -4.5%", DARKRED), ("KOSPI -4.7%", DARKRED),
        ("ANTHROPIC +17%", GREEN), ("GOLD LOW", DARKRED),
        ("BRENT $92", TEAL), ("DOLLAR HIGH", TEAL),
    ]
    x = 28
    for label, col in chips:
        f = SANS_B(14)
        w = int(d.textlength(label, font=f)) + 14
        if x + w > 996:
            break
        d.rounded_rectangle([x, 448, x + w, 472], radius=4, fill=col)
        d.text((x + 7, 453), label, font=f, fill=WHITE)
        x += w + 7
    d.text((28, 478), "Dow -1,101 pts  •  Anthropic debut $97  •  Brent $92.22  •  Dollar 19-mo high  •  Asia worst week since 2020",
           font=SANS_B(15), fill=WHITE)

    # ---------- cyclone + climate (512-644) ----------
    d.rectangle([16, 512, 500, 644], outline=TEAL, width=2, fill=WHITE)
    tag(d, 28, 524, "WEATHER  •  INDIA", TEAL)
    text_block(d, 28, 552, "Cyclone Akvan hits Odisha coast", SERIF_B(23), INK, 452, leading=28)
    cx, cy = 72, 606
    for r in (28, 21, 14, 8):
        d.arc([cx - r, cy - r, cx + r, cy + r], 20, 300, fill=TEAL, width=4)
    d.ellipse([cx - 5, cy - 5, cx + 5, cy + 5], fill=RED)
    text_block(d, 124, 588, "Landfall near Gopalpur, winds 100 km/h. 300,000+ evacuated; 69 trains cancelled.", SANS(16), INK, 352, leading=20)

    d.rectangle([516, 512, 1008, 644], outline=NAVY, width=2, fill=WHITE)
    tag(d, 528, 524, "CLIMATE  •  ANTALYA", NAVY2)
    y = text_block(d, 528, 556, "COP31 closes today — draft drops fossil-fuel phase-out", SERIF_B(22), INK, 452, leading=27)
    text_block(d, 528, y + 2, "Draft cut 144 → 80 paragraphs; fossil fuels dropped.", SANS(16), INK, 452, leading=20)

    # ---------- around the world grid (656-928) ----------
    d.rectangle([16, 656, 1008, 664], fill=RED)
    d.text((16, 670), "AROUND THE WORLD", font=SERIF_B(25), fill=NAVY)
    d.text((720, 676), "Friday 20 November 2026", font=SANS_B(15), fill=GREY)
    items = [
        ("MIDDLE EAST", "Houthis strike 4 Saudi targets incl. Riyadh airport; tanker hits mine near Hormuz."),
        ("UKRAINE", "Kyiv hit by four ballistic missiles; attack on Crimean Bridge disrupts rail."),
        ("EUROPE", "Genoa airport shut 4 hours after mystery drones; Israel strikes Hezbollah site."),
        ("ASIA", "Seoul upholds Kakao founder's acquittal; S. Korea clears ex-PM Han Duck-soo."),
        ("ASIA", "Japan core inflation 2.2%; yen near 160/$. China holds loan rates 3.00% / 3.50%."),
        ("TECH", "Anthropic Australia data centre opposed by 595 of ~600 locals."),
        ("USA", "Congress back facing Dec 11 funding cliff; US–Venezuela restore military ties."),
        ("AFRICA", "Congo Ebola passes 10,600 cases, 5,198 dead; Fiji drought disaster."),
        ("SCIENCE", "NASA pauses Mars rover Perseverance science after radio fault."),
        ("WORLD", "N. Korea expands uranium enrichment at Yongbyon, watchdog says."),
        ("ENERGY", "IEA: data centres need $3.9 trillion by 2030; power is the bottleneck."),
        ("FRANCE", "One dead, 15 hurt in fire at 18-storey block; Europe weighs talks with Russia."),
    ]
    col_w, row_h = 318, 56
    for i, (region, txt) in enumerate(items):
        cx0 = 16 + (i % 3) * 330
        cy0 = 706 + (i // 3) * row_h
        d.text((cx0, cy0), region, font=SANS_B(14), fill=RED)
        text_block(d, cx0, cy0 + 18, txt, SANS(15), INK, col_w, leading=18)

    # ---------- sports + footer ----------
    d.rectangle([16, 938, 1008, 1000], fill=NAVY)
    d.text((28, 946), "SPORT", font=SANS_B(17), fill=(255, 214, 90))
    text_block(d, 28, 968, "ATP Finals: Zverev first into semis; Alcaraz unbeaten  •  Cricket: Phillips 118, NZ 317-6 v India  •  NFL: Texans lead Colts 17-3  •  Rugby: Boks v All Blacks for final spot",
               SANS(15), WHITE, 952, leading=18)
    d.rectangle([0, 1008, W, H], fill=RED)
    d.text((16, 1011), "THE WORLD TODAY  •  FRIDAY 20 NOVEMBER 2026  •  ALL THE DAY'S NEWS IN ONE PAGE", font=SANS_B(12), fill=WHITE)

    img.save(OUT, "PNG", optimize=True)


if __name__ == "__main__":
    main()
    print("wrote", OUT)
