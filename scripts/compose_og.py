"""Compose the OG / Twitter card image (1200x630) and favicon set for the
portfolio. Uses only PIL — no external API — so the output mirrors the site's
exact palette (--accent indigo / --accent-secondary purple / --accent-tertiary
pink on --bg-primary navy).

Outputs:
    assets/images/og-card.png        (1200x630, social link previews)
    assets/images/favicon-32.png     (32x32, browser tab)
    assets/images/favicon-180.png    (180x180, apple-touch-icon)
    assets/images/favicon.ico        (multi-size .ico)

Usage:
    python scripts/compose_og.py
"""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter, ImageFont


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "images"

# Site palette (from assets/css/styles.css :root)
BG_PRIMARY = (10, 10, 15)        # #0a0a0f
BG_CARD = (26, 26, 38)           # #1a1a26
ACCENT = (99, 102, 241)          # #6366f1 indigo
ACCENT_SEC = (139, 92, 246)      # #8b5cf6 purple
ACCENT_TER = (236, 72, 153)      # #ec4899 pink
TEXT_PRIMARY = (255, 255, 255)
TEXT_SECONDARY = (180, 180, 200) # #b4b4c8


def find_font(size: int, candidates: list[str]) -> ImageFont.FreeTypeFont:
    win_fonts = Path(r"C:\Windows\Fonts")
    for name in candidates:
        for p in [win_fonts / name, Path(name)]:
            if p.exists():
                return ImageFont.truetype(str(p), size)
    return ImageFont.load_default()


def soft_orb(canvas: Image.Image, *, cx: int, cy: int, radius: int,
             color: tuple[int, int, int], alpha: int) -> None:
    """Soft glowing orb, mirrors .gradient-orb (radial gradient + blur)."""
    size = radius * 4
    layer = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(layer)
    # Radial fade by drawing concentric circles with decreasing alpha
    for r in range(radius * 2, 0, -1):
        t = r / (radius * 2)
        a = int(alpha * (1 - t) ** 2)
        if a <= 0:
            continue
        draw.ellipse(
            (size // 2 - r, size // 2 - r, size // 2 + r, size // 2 + r),
            fill=color + (a,),
        )
    layer = layer.filter(ImageFilter.GaussianBlur(radius // 8))
    canvas.alpha_composite(layer, (cx - size // 2, cy - size // 2))


def vertical_gradient(w: int, h: int, top: tuple, bottom: tuple) -> Image.Image:
    img = Image.new("RGBA", (1, h))
    px = img.load()
    for y in range(h):
        t = y / (h - 1)
        c = tuple(int(top[i] + (bottom[i] - top[i]) * t) for i in range(3)) + (255,)
        px[0, y] = c
    return img.resize((w, h))


def text_with_gradient(draw_target: Image.Image, text: str,
                       font: ImageFont.FreeTypeFont, *, x: int, y: int,
                       gradient_colors: list[tuple[int, int, int]]) -> None:
    """Render text filled with a horizontal gradient across the text bounding
    box. Mirrors the site's .hero-name webkit-background-clip trick."""
    tmp = Image.new("RGBA", draw_target.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(tmp)
    d.text((x, y), text, font=font, fill=(255, 255, 255, 255))
    bbox = d.textbbox((x, y), text, font=font)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    if tw <= 0 or th <= 0:
        return
    # Build horizontal gradient strip across the text box width.
    grad = Image.new("RGB", (tw, 1))
    gp = grad.load()
    n = len(gradient_colors)
    for i in range(tw):
        t = i / max(tw - 1, 1)
        seg = t * (n - 1)
        idx = int(seg)
        frac = seg - idx
        if idx >= n - 1:
            c = gradient_colors[-1]
        else:
            a = gradient_colors[idx]
            b = gradient_colors[idx + 1]
            c = tuple(int(a[k] + (b[k] - a[k]) * frac) for k in range(3))
        gp[i, 0] = c
    grad = grad.resize((tw, th)).convert("RGBA")
    # Mask gradient by the white text alpha
    mask = tmp.crop(bbox).split()[-1]
    grad.putalpha(mask)
    draw_target.alpha_composite(grad, dest=(bbox[0], bbox[1]))


def make_og_card() -> Image.Image:
    W, H = 1200, 630
    canvas = Image.new("RGBA", (W, H), BG_PRIMARY + (255,))

    # Subtle vertical gradient — bg_primary at top, bg_card at bottom
    canvas.alpha_composite(vertical_gradient(W, H, BG_PRIMARY, BG_CARD))

    # Three gradient orbs mirroring orb-1 / orb-2 / orb-3
    soft_orb(canvas, cx=-50, cy=80, radius=420, color=ACCENT, alpha=110)
    soft_orb(canvas, cx=W + 60, cy=H // 2, radius=340, color=ACCENT_SEC, alpha=100)
    soft_orb(canvas, cx=W // 2 + 100, cy=H + 80, radius=380, color=ACCENT_TER, alpha=85)

    # Vignette / floor darkening at edges
    vignette = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    vd = ImageDraw.Draw(vignette)
    vd.rectangle((0, 0, W, H), fill=(0, 0, 0, 60))
    inner = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    id_ = ImageDraw.Draw(inner)
    pad = 40
    id_.rounded_rectangle((pad, pad, W - pad, H - pad), radius=24,
                          fill=(0, 0, 0, 0))
    # Skip vignette — orbs already provide focus

    # Top-left tag — monospaced label
    label_font = find_font(22, ["JetBrainsMono-Regular.ttf", "consola.ttf",
                                "cour.ttf"])
    draw = ImageDraw.Draw(canvas)
    draw.text((80, 70), "// PORTFOLIO · 2026", font=label_font,
              fill=ACCENT + (220,))

    # Greeting (small, accent color)
    greet_font = find_font(28, ["Inter-SemiBold.ttf", "seguisb.ttf",
                                "segoeui.ttf", "arialbd.ttf"])
    draw.text((80, 200), "Hi, I'm", font=greet_font, fill=ACCENT + (255,))

    # Name — huge, with horizontal gradient fill
    name_font = find_font(180, ["Inter-Black.ttf", "arialbd.ttf",
                                "impact.ttf"])
    text_with_gradient(canvas, "Cameron", name_font, x=80, y=240,
                       gradient_colors=[ACCENT, ACCENT_SEC, ACCENT_TER])

    # Subtitle
    sub_font = find_font(34, ["Inter-Regular.ttf", "segoeui.ttf",
                              "arial.ttf"])
    draw.text((80, 460),
              "I build things that probably shouldn't exist,",
              font=sub_font, fill=TEXT_SECONDARY + (255,))
    draw.text((80, 502),
              "and a few that should.",
              font=sub_font, fill=TEXT_SECONDARY + (255,))

    # URL bottom-right
    url_font = find_font(24, ["JetBrainsMono-Regular.ttf", "consola.ttf"])
    url = "cameronmcainsh.com"
    bbox = draw.textbbox((0, 0), url, font=url_font)
    uw = bbox[2] - bbox[0]
    draw.text((W - 80 - uw, H - 80), url, font=url_font,
              fill=ACCENT + (220,))

    # Decorative dot before URL (matches .badge-dot)
    dot_r = 6
    dot_x = W - 80 - uw - 18
    dot_y = H - 80 + 12
    draw.ellipse((dot_x - dot_r, dot_y - dot_r, dot_x + dot_r, dot_y + dot_r),
                 fill=ACCENT + (255,))

    return canvas.convert("RGB")


def make_favicon(size: int) -> Image.Image:
    canvas = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    # Rounded gradient square background
    bg = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    bd = ImageDraw.Draw(bg)
    radius = int(size * 0.22)
    bd.rounded_rectangle((0, 0, size, size), radius=radius,
                         fill=ACCENT + (255,))
    # Diagonal gradient fill via overlay
    overlay = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    od = ImageDraw.Draw(overlay)
    # 3-stop horizontal gradient strip
    grad = Image.new("RGB", (size, 1))
    gp = grad.load()
    stops = [ACCENT, ACCENT_SEC, ACCENT_TER]
    for i in range(size):
        t = i / max(size - 1, 1)
        seg = t * (len(stops) - 1)
        idx = int(seg)
        frac = seg - idx
        if idx >= len(stops) - 1:
            c = stops[-1]
        else:
            a, b = stops[idx], stops[idx + 1]
            c = tuple(int(a[k] + (b[k] - a[k]) * frac) for k in range(3))
        gp[i, 0] = c
    grad = grad.resize((size, size)).convert("RGBA")
    # Apply rounded corner mask from bg
    mask = Image.new("L", (size, size), 0)
    md = ImageDraw.Draw(mask)
    md.rounded_rectangle((0, 0, size, size), radius=radius, fill=255)
    grad.putalpha(mask)
    canvas.alpha_composite(grad)

    # "CM" monogram in white
    fs = int(size * 0.55)
    font = find_font(fs, ["Inter-Black.ttf", "arialbd.ttf", "impact.ttf"])
    draw = ImageDraw.Draw(canvas)
    text = "CM"
    bbox = draw.textbbox((0, 0), text, font=font)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    # Optical-correct vertical centering uses the bbox y-offset
    tx = (size - tw) // 2 - bbox[0]
    ty = (size - th) // 2 - bbox[1]
    draw.text((tx, ty), text, font=font, fill=(255, 255, 255, 245))

    return canvas


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)

    og = make_og_card()
    og_path = OUT / "og-card.png"
    og.save(og_path, "PNG", optimize=True)
    print(f"wrote {og_path} ({og_path.stat().st_size // 1024} KB)")

    fav32 = make_favicon(32)
    fav32_path = OUT / "favicon-32.png"
    fav32.save(fav32_path, "PNG", optimize=True)
    print(f"wrote {fav32_path}")

    fav180 = make_favicon(180)
    fav180_path = OUT / "favicon-180.png"
    fav180.save(fav180_path, "PNG", optimize=True)
    print(f"wrote {fav180_path}")

    # Multi-size .ico (16, 32, 48)
    fav16 = make_favicon(16)
    fav48 = make_favicon(48)
    ico_path = OUT / "favicon.ico"
    fav32.save(ico_path, format="ICO",
               sizes=[(16, 16), (32, 32), (48, 48)],
               append_images=[fav16, fav48])
    print(f"wrote {ico_path}")


if __name__ == "__main__":
    main()
