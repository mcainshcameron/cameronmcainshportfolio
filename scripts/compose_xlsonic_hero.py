"""Compose a featured-card hero image for xlsonic that captures its
satirical-enterprise-SaaS aesthetic (cyan + purple on near-black, big bold
"TRANSFORM DATA INTO SOUND." display, fake stats, waveform).

Outputs:
    assets/images/xlsonic-hero.png  (1600x900)

Usage:
    python scripts/compose_xlsonic_hero.py
"""

from pathlib import Path
import math
import random

from PIL import Image, ImageDraw, ImageFilter, ImageFont


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "images"

# xlsonics palette (from xlsonics/style.css :root)
BG = (10, 10, 10)              # #0a0a0a
BG_GRADIENT_END = (18, 18, 22) # subtle bottom gradient
TEXT = (224, 224, 224)         # #e0e0e0
CYAN = (0, 255, 255)           # #00ffff primary
PURPLE = (151, 71, 255)        # #9747FF secondary

CANVAS_W, CANVAS_H = 1600, 900


def find_font(size: int, candidates: list[str]) -> ImageFont.FreeTypeFont:
    win_fonts = Path(r"C:\Windows\Fonts")
    for name in candidates:
        for p in [win_fonts / name, Path(name)]:
            if p.exists():
                return ImageFont.truetype(str(p), size)
    return ImageFont.load_default()


def vertical_gradient(w: int, h: int, top: tuple, bottom: tuple) -> Image.Image:
    img = Image.new("RGBA", (1, h))
    px = img.load()
    for y in range(h):
        t = y / (h - 1)
        c = tuple(int(top[i] + (bottom[i] - top[i]) * t) for i in range(3)) + (255,)
        px[0, y] = c
    return img.resize((w, h))


def draw_particles(canvas: Image.Image, *, count: int = 80) -> None:
    """Mirror xlsonic's particles-js layer with sparse cyan/purple dots."""
    rng = random.Random(42)  # deterministic
    layer = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(layer)
    for _ in range(count):
        x = rng.randint(0, CANVAS_W)
        y = rng.randint(0, CANVAS_H)
        r = rng.randint(1, 3)
        color = CYAN if rng.random() < 0.65 else PURPLE
        a = rng.randint(60, 180)
        draw.ellipse((x - r, y - r, x + r, y + r), fill=color + (a,))
    canvas.alpha_composite(layer)


def draw_grid_lines(canvas: Image.Image) -> None:
    """Faint connecting lines between particles (data-network feel)."""
    layer = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(layer)
    rng = random.Random(7)
    for _ in range(18):
        x1 = rng.randint(0, CANVAS_W)
        y1 = rng.randint(0, CANVAS_H)
        x2 = x1 + rng.randint(-220, 220)
        y2 = y1 + rng.randint(-220, 220)
        draw.line((x1, y1, x2, y2), fill=CYAN + (28,), width=1)
    canvas.alpha_composite(layer)


def draw_waveform(canvas: Image.Image, *, baseline_y: int) -> None:
    """A long audio-waveform stripe across the bottom band."""
    layer = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(layer)
    rng = random.Random(11)
    # Many vertical bars with seeded amplitudes — looks like an FFT bar chart
    bar_count = 200
    margin = 80
    avail = CANVAS_W - margin * 2
    bar_w = avail // bar_count
    for i in range(bar_count):
        # Layered sine waves create the rhythmic envelope
        env = (
            math.sin(i / 7.0) * 0.5
            + math.sin(i / 23.0) * 0.3
            + math.sin(i / 3.0) * 0.2
        )
        amp = abs(env) * 60 + rng.uniform(2, 20)
        x = margin + i * bar_w
        # Cyan→purple horizontal gradient across the waveform
        t = i / max(bar_count - 1, 1)
        color = (
            int(CYAN[0] + (PURPLE[0] - CYAN[0]) * t),
            int(CYAN[1] + (PURPLE[1] - CYAN[1]) * t),
            int(CYAN[2] + (PURPLE[2] - CYAN[2]) * t),
        )
        draw.rectangle(
            (x, int(baseline_y - amp), x + bar_w - 2, int(baseline_y + amp)),
            fill=color + (220,),
        )
    # Soft glow pass
    glow = layer.filter(ImageFilter.GaussianBlur(6))
    canvas.alpha_composite(glow)
    canvas.alpha_composite(layer)


def draw_stat_pill(canvas: Image.Image, *, x: int, y: int, value: str,
                   label: str) -> None:
    draw = ImageDraw.Draw(canvas)
    val_font = find_font(40, ["Inter-Black.ttf", "arialbd.ttf", "impact.ttf"])
    label_font = find_font(16, ["JetBrainsMono-Regular.ttf", "consola.ttf",
                                "cour.ttf"])

    # Compute pill width from contents
    val_bbox = draw.textbbox((0, 0), value, font=val_font)
    label_bbox = draw.textbbox((0, 0), label, font=label_font)
    inner_w = max(val_bbox[2] - val_bbox[0], label_bbox[2] - label_bbox[0])
    pad_x = 28
    pad_y = 18
    pill_w = inner_w + pad_x * 2
    pill_h = (val_bbox[3] - val_bbox[1]) + (label_bbox[3] - label_bbox[1]) + pad_y * 2 + 6

    # Pill background
    bg = Image.new("RGBA", (pill_w, pill_h), (0, 0, 0, 0))
    bd = ImageDraw.Draw(bg)
    bd.rounded_rectangle((0, 0, pill_w, pill_h), radius=14,
                         fill=(0, 255, 255, 18),
                         outline=CYAN + (140,), width=1)
    canvas.alpha_composite(bg, dest=(x, y))

    # Text inside
    draw.text((x + pad_x - val_bbox[0], y + pad_y - val_bbox[1]),
              value, font=val_font, fill=CYAN + (255,))
    label_y = y + pad_y + (val_bbox[3] - val_bbox[1]) + 6
    draw.text((x + pad_x - label_bbox[0], label_y - label_bbox[1]),
              label, font=label_font, fill=TEXT + (200,))


def draw_title(canvas: Image.Image) -> None:
    draw = ImageDraw.Draw(canvas)

    # Logo word "xlsonics" — small, top-left, cyan, monospaced/heavy
    logo_font = find_font(38, ["Inter-Black.ttf", "arialbd.ttf", "impact.ttf"])
    draw.text((80, 80), "xlsonics", font=logo_font, fill=CYAN + (255,))

    # Eyebrow tag — monospaced, faint
    eyebrow_font = find_font(20, ["JetBrainsMono-Regular.ttf", "consola.ttf",
                                  "cour.ttf"])
    draw.text((80, 240), "// NEURAL-ACOUSTIC INTELLIGENCE PLATFORM",
              font=eyebrow_font, fill=PURPLE + (220,))

    # Title — two lines, "TRANSFORM DATA" white, "INTO SOUND." cyan
    title_font = find_font(140, ["Inter-Black.ttf", "arialbd.ttf",
                                 "impact.ttf"])
    draw.text((76, 280), "Transform Data", font=title_font,
              fill=TEXT + (255,))
    draw.text((76, 430), "Into Sound.", font=title_font,
              fill=CYAN + (255,))

    # Subtitle — small, faint
    sub_font = find_font(22, ["Inter-Regular.ttf", "segoeui.ttf",
                              "arial.ttf"])
    draw.text(
        (80, 600),
        "AI converts complex datasets into intuitive audio experiences.",
        font=sub_font, fill=TEXT + (210,),
    )


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    canvas = Image.new("RGBA", (CANVAS_W, CANVAS_H), BG + (255,))
    canvas.alpha_composite(vertical_gradient(CANVAS_W, CANVAS_H, BG, BG_GRADIENT_END))

    # Subtle radial cyan glow behind the title
    glow_layer = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
    gd = ImageDraw.Draw(glow_layer)
    gd.ellipse((-200, 100, 1000, 1000), fill=CYAN + (40,))
    glow_layer = glow_layer.filter(ImageFilter.GaussianBlur(140))
    canvas.alpha_composite(glow_layer)

    purple_glow = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
    pd = ImageDraw.Draw(purple_glow)
    pd.ellipse((900, -150, 1700, 700), fill=PURPLE + (60,))
    purple_glow = purple_glow.filter(ImageFilter.GaussianBlur(160))
    canvas.alpha_composite(purple_glow)

    draw_grid_lines(canvas)
    draw_particles(canvas)

    draw_title(canvas)

    # Stats pills — top-right, the absurd numbers
    draw_stat_pill(canvas, x=1120, y=240,
                   value="2.3B+", label="DATA POINTS PROCESSED")
    draw_stat_pill(canvas, x=1120, y=380,
                   value="847%", label="FASTER PATTERN RECOGNITION")

    # Waveform along the bottom
    draw_waveform(canvas, baseline_y=800)

    # Bottom-right URL with cyan dot
    draw = ImageDraw.Draw(canvas)
    url_font = find_font(22, ["JetBrainsMono-Regular.ttf", "consola.ttf"])
    url = "xlsonic.com"
    bbox = draw.textbbox((0, 0), url, font=url_font)
    uw = bbox[2] - bbox[0]
    draw.text((CANVAS_W - 80 - uw, CANVAS_H - 60), url,
              font=url_font, fill=CYAN + (220,))
    dot_r = 5
    dot_x = CANVAS_W - 80 - uw - 14
    dot_y = CANVAS_H - 60 + 11
    draw.ellipse((dot_x - dot_r, dot_y - dot_r, dot_x + dot_r, dot_y + dot_r),
                 fill=CYAN + (255,))

    out_path = OUT / "xlsonic-hero.png"
    canvas.convert("RGB").save(out_path, "PNG", optimize=True)
    print(f"wrote {out_path} ({out_path.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
