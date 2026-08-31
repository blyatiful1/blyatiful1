#!/usr/bin/env python3
"""Emit the light and dark blueprint banners for the GitHub profile README.

One template, two colourways -- so the variants can never drift apart.

Two constraints drive every number here:
  * GitHub serves README images through camo as <img>: no webfonts, no external
    refs, no currentColor. Self-contained, system font stacks only.
  * GitHub scales the image to the column width. At a ~330px mobile column a
    720-wide banner renders at ~46%, so anything under ~12px in here is a smudge
    on a phone. The graphic therefore carries only headline-weight text; the
    README prose below it carries the detail.
"""
import pathlib
import xml.etree.ElementTree as ET

W, H = 720, 316

SANS = "ui-sans-serif,-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif"
MONO = "ui-monospace,SFMono-Regular,'SF Mono',Menlo,Consolas,'Liberation Mono',monospace"

THEMES = {
    "light": dict(ink="#1f2328", muted="#59636e", line="#d1d9e0",
                  accent="#BC4C00", slab="#f6f8fa", dot="#d0d7de"),
    "dark": dict(ink="#f0f6fc", muted="#9198a1", line="#3d444d",
                 accent="#F0883E", slab="#161b22", dot="#30363d"),
}

# geometry -- box centres are derived, never hand-typed, so the connectors
# below the boxes cannot drift off-centre again
PAD, GAP = 32, 24
BOX_W = (W - 2 * PAD - GAP) // 2          # 316
BOX_Y, BOX_H = 110, 98
SLAB_Y, SLAB_H = 232, 40

BOXES = [
    ("ultraweb", "design studio", "80 skills · 7 gates"),
    ("hardmode", "discipline floor", "hooks · verification"),
]

BOX_TPL = """  <g>
    <rect x="{x}" y="{by}" width="{bw}" height="{bh}" rx="7" fill="none" stroke="{line}" stroke-width="1.25"/>
    <text x="{tx}" y="{ty}" font-family="{sans}" font-size="23" font-weight="700" fill="{ink}">{title}</text>
    <line x1="{tx}" y1="{ly}" x2="{lx2}" y2="{ly}" stroke="{line}" stroke-width="1"/>
    <text x="{tx}" y="{sy}" font-family="{mono}" font-size="12.5" fill="{muted}"><tspan fill="{accent}">{role}</tspan> · {stat}</text>
  </g>
  <path d="M {cx} {bb} L {cx} {sy2}" stroke="{line}" stroke-width="1.25" fill="none"/>
"""

TPL = """<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="{aria}">
  <title>{aria}</title>
  <defs>
    <pattern id="grid" width="22" height="22" patternUnits="userSpaceOnUse">
      <circle cx="1" cy="1" r="1" fill="{dot}" opacity="0.6"/>
    </pattern>
    <marker id="tip" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M 0 1 L 9 5 L 0 9 z" fill="{accent}"/>
    </marker>
  </defs>

  <rect x="0" y="0" width="{W}" height="{H}" fill="url(#grid)"/>

  <text x="{pad}" y="48" font-family="{sans}" font-size="36" font-weight="700" letter-spacing="4.5" fill="{ink}">IWAN BRAUN</text>
  <text x="{pad2}" y="72" font-family="{mono}" font-size="11.5" letter-spacing="3.2" fill="{muted}">AGENT INFRASTRUCTURE</text>
  <line x1="{pad}" y1="90" x2="{right}" y2="90" stroke="{line}" stroke-width="1"/>

{boxes}
  <rect x="{pad}" y="{slab_y}" width="{slab_w}" height="{slab_h}" rx="7" fill="{slab}" stroke="{line}" stroke-width="1"/>
  <text x="{mid}" y="{slab_t}" text-anchor="middle" font-family="{mono}" font-size="14" font-weight="600" letter-spacing="5.5" fill="{ink}">CLAUDE CODE</text>

  <path d="M {mid} {out_a} L {mid} {out_b}" stroke="{accent}" stroke-width="1.5" fill="none" marker-end="url(#tip)"/>
  <text x="{mid}" y="{out_t}" text-anchor="middle" font-family="{mono}" font-size="12.5" fill="{muted}">ultraweb-site · <tspan fill="{accent}">7/7 gates green</tspan></text>
</svg>
"""


def render(theme: str) -> str:
    c = THEMES[theme]
    aria = ("Iwan Braun, agent infrastructure. A blueprint: two Claude Code plugins, ultraweb "
            "(design studio, 80 skills, 7 gates) and hardmode (discipline floor, hooks, "
            "verification), seated on Claude Code, shipping ultraweb-site with 7 of 7 gates green.")

    boxes = "".join(
        BOX_TPL.format(
            x=(x := PAD + i * (BOX_W + GAP)), bw=BOX_W, by=BOX_Y, bh=BOX_H,
            tx=x + 18, ty=BOX_Y + 36, ly=BOX_Y + 52, lx2=x + BOX_W - 18, sy=BOX_Y + 76,
            cx=x + BOX_W // 2, bb=BOX_Y + BOX_H, sy2=SLAB_Y,
            title=title, role=role, stat=stat,
            line=c["line"], ink=c["ink"], muted=c["muted"], accent=c["accent"],
            sans=SANS, mono=MONO,
        )
        for i, (title, role, stat) in enumerate(BOXES)
    )

    return TPL.format(
        W=W, H=H, aria=aria, sans=SANS, mono=MONO, boxes=boxes,
        pad=PAD, pad2=PAD + 3, right=W - PAD, mid=W // 2,
        slab_y=SLAB_Y, slab_h=SLAB_H, slab_w=W - 2 * PAD, slab_t=SLAB_Y + 26,
        out_a=SLAB_Y + SLAB_H, out_b=SLAB_Y + SLAB_H + 18, out_t=SLAB_Y + SLAB_H + 42,
        **c,
    )


def main() -> None:
    out = pathlib.Path(__file__).parent
    for theme in THEMES:
        svg = render(theme)
        ET.fromstring(svg)  # fails loudly on malformed XML rather than shipping it
        (out / f"banner-{theme}.svg").write_text(svg, encoding="utf-8")
        print(f"banner-{theme}.svg: {len(svg)} bytes, XML OK")
    print(f"box centres: {PAD + BOX_W // 2}, {PAD + BOX_W + GAP + BOX_W // 2}  (slab spans {PAD}..{W - PAD})")


if __name__ == "__main__":
    main()
