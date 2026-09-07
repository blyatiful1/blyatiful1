#!/usr/bin/env python3
"""Generates the profile banner.

Three directions are kept below; LIVE picks the one written to
banner-{light,dark}.svg. Swapping the banner is a one-word edit.

Hard constraints, shared by every direction: system font stacks only (camo
loads no webfonts), no external refs, valid XML, no numbers in the visible
text, and legible when GitHub scales the banner to a narrow mobile column.
"""
import pathlib
import re
import xml.etree.ElementTree as ET

W = 720
SANS = "ui-sans-serif,-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif"
MONO = "ui-monospace,SFMono-Regular,'SF Mono',Menlo,Consolas,'Liberation Mono',monospace"

THEMES = {
    "light": dict(ink="#1f2328", muted="#59636e", line="#d1d9e0",
                  accent="#BC4C00", slab="#f6f8fa", dot="#d0d7de"),
    "dark": dict(ink="#f0f6fc", muted="#9198a1", line="#3d444d",
                 accent="#F0883E", slab="#161b22", dot="#30363d"),
}

PAD = 4
REPOS = "ultraweb · hardmode · gtheme · NightCityMP"

HEAD = ('<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
        'viewBox="0 0 {w} {h}" role="img" aria-label="{aria}"><title>{aria}</title>'
        '<defs><pattern id="g" width="22" height="22" patternUnits="userSpaceOnUse">'
        '<circle cx="1" cy="1" r="1" fill="{dot}" opacity="0.6"/></pattern>'
        '<marker id="t" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" '
        'markerHeight="7" orient="auto-start-reverse">'
        '<path d="M 0 1 L 9 5 L 0 9 z" fill="{accent}"/></marker></defs>'
        '<rect width="{w}" height="{h}" fill="url(#g)"/>')


def masthead(c, sub="AGENT INFRASTRUCTURE", y=48, size=36):
    return (f'<text x="{PAD}" y="{y}" font-family="{SANS}" font-size="{size}" '
            f'font-weight="700" letter-spacing="4.5" fill="{c["ink"]}">IWAN BRAUN</text>'
            f'<text x="{PAD+3}" y="{y+24}" font-family="{MONO}" font-size="11.5" '
            f'letter-spacing="3.2" fill="{c["muted"]}">{sub}</text>')


def rule(c, y):
    return f'<line x1="{PAD}" y1="{y}" x2="{W-PAD}" y2="{y}" stroke="{c["line"]}" stroke-width="1"/>'


# ---------------------------------------------------------------- A: blueprint
def variant_a(c):
    h = 316
    aria = ("Iwan Braun, agent infrastructure. ultraweb and hardmode seated on Claude Code, "
            "which writes the code in these repos.")
    s = [HEAD.format(w=W, h=h, aria=aria, **c), masthead(c), rule(c, 90)]
    boxes = [("ultraweb", "design studio", "browser-verified gates"),
             ("hardmode", "discipline floor", "hooks · verifiers")]
    bw, gap, by, bh = (W - 2 * PAD - 24) // 2, 24, 110, 98
    for i, (title, role, stat) in enumerate(boxes):
        x = PAD + i * (bw + gap)
        s.append(
            f'<rect x="{x}" y="{by}" width="{bw}" height="{bh}" rx="7" fill="none" '
            f'stroke="{c["line"]}" stroke-width="1.25"/>'
            f'<text x="{x+18}" y="{by+36}" font-family="{SANS}" font-size="23" '
            f'font-weight="700" fill="{c["ink"]}">{title}</text>'
            f'<line x1="{x+18}" y1="{by+52}" x2="{x+bw-18}" y2="{by+52}" stroke="{c["line"]}" stroke-width="1"/>'
            f'<text x="{x+18}" y="{by+76}" font-family="{MONO}" font-size="12.5" fill="{c["muted"]}">'
            f'<tspan fill="{c["accent"]}">{role}</tspan> · {stat}</text>'
            f'<path d="M {x+bw//2} {by+bh} L {x+bw//2} 232" stroke="{c["line"]}" stroke-width="1.25" fill="none"/>')
    s.append(f'<rect x="{PAD}" y="232" width="{W-2*PAD}" height="40" rx="7" fill="{c["slab"]}" '
             f'stroke="{c["line"]}" stroke-width="1"/>'
             f'<text x="{W//2}" y="258" text-anchor="middle" font-family="{MONO}" font-size="14" '
             f'font-weight="600" letter-spacing="5.5" fill="{c["ink"]}">CLAUDE CODE</text>'
             f'<path d="M {W//2} 272 L {W//2} 290" stroke="{c["accent"]}" stroke-width="1.5" '
             f'fill="none" marker-end="url(#t)"/>'
             f'<text x="{W//2}" y="312" text-anchor="middle" font-family="{MONO}" font-size="12.5" '
             f'fill="{c["muted"]}">it writes <tspan fill="{c["accent"]}">the code</tspan> in these repos</text>')
    return "".join(s) + "</svg>"


# -------------------------------------------------------- C: provenance label
def variant_c(c):
    h = 262
    aria = ("Iwan Braun, agent infrastructure. A provenance label: written by Claude Code, "
            "directed by Iwan Braun, held to a standard written down before the model starts.")
    rows = [("WRITTEN BY", "Claude Code", True),
            ("DIRECTED BY", "Iwan Braun", False),
            ("STANDARD", "written down before the model starts", True)]
    s = [HEAD.format(w=W, h=h, aria=aria, **c), masthead(c), rule(c, 90),
         f'<rect x="{PAD}" y="106" width="{W-2*PAD}" height="124" rx="7" fill="{c["slab"]}" '
         f'stroke="{c["line"]}" stroke-width="1.25"/>',
         f'<text x="{PAD+22}" y="132" font-family="{MONO}" font-size="11" letter-spacing="2.8" '
         f'fill="{c["accent"]}">PROVENANCE</text>']
    for i, (k, v, hi) in enumerate(rows):
        y = 160 + i * 26
        s.append(f'<text x="{PAD+22}" y="{y}" font-family="{MONO}" font-size="11.5" '
                 f'letter-spacing="1.6" fill="{c["muted"]}">{k}</text>'
                 f'<text x="{PAD+170}" y="{y}" font-family="{MONO}" font-size="13" '
                 f'fill="{c["accent"] if hi else c["ink"]}">{v}</text>')
    s.append(f'<text x="{PAD}" y="252" font-family="{MONO}" font-size="12" fill="{c["muted"]}">'
             f'{REPOS}</text>')
    return "".join(s) + "</svg>"


# ------------------------------------------------------------- D: typographic
def variant_d(c):
    h = 208
    aria = ("Iwan Braun, agent infrastructure. I direct AI agents; they write the code; "
            f"I hold it to a standard. {REPOS.replace(' · ', ', ')}.")
    s = [HEAD.format(w=W, h=h, aria=aria, **c),
         masthead(c, sub="AGENT INFRASTRUCTURE", y=64, size=46), rule(c, 108),
         f'<text x="{PAD}" y="140" font-family="{SANS}" font-size="19" fill="{c["ink"]}">'
         f'I direct AI agents. <tspan fill="{c["muted"]}">They write the code.</tspan> '
         f'<tspan fill="{c["accent"]}" font-weight="700">I hold it to a standard.</tspan></text>',
         f'<text x="{PAD}" y="176" font-family="{MONO}" font-size="12.5" fill="{c["muted"]}">'
         f'{REPOS}</text>']
    return "".join(s) + "</svg>"


VARIANTS = {"a-blueprint": variant_a, "c-label": variant_c, "d-type": variant_d}

# which direction is live on the profile
LIVE = "d-type"


def visible_text(root) -> str:
    """Every character a reader can see or a screen reader will speak."""
    parts = [root.get("aria-label", "")]
    for el in root.iter():
        parts.append(el.text or "")
        parts.append(el.tail or "")
    return "".join(parts)


def main() -> None:
    out = pathlib.Path(__file__).parent
    fn = VARIANTS[LIVE]
    for theme, c in THEMES.items():
        svg = fn(c)
        root = ET.fromstring(svg)  # refuse to ship malformed XML
        digits = re.findall(r"\d", visible_text(root))
        if digits:  # the profile makes its case in words, not counts
            raise SystemExit(f"banner-{theme}.svg: numbers in visible text: {digits}")
        (out / f"banner-{theme}.svg").write_text(svg, encoding="utf-8")
        print(f"banner-{theme}.svg  <- {LIVE}  ({len(svg)} bytes, XML OK, no numbers)")
        h = re.search(r'height="(\d+)"', svg).group(1)
    # the README hardcodes the banner height so GitHub reserves the slot; a
    # variant swap that forgets this leaves a gap under the image
    print(f'reminder: README <img> must read height="{h}" for LIVE={LIVE}')


if __name__ == "__main__":
    main()
