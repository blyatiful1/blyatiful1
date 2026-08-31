<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/blyatiful1/blyatiful1/main/banner-dark.svg">
  <img src="https://raw.githubusercontent.com/blyatiful1/blyatiful1/main/banner-light.svg" width="720" alt="Iwan Braun — agent infrastructure. A blueprint: two Claude Code plugins, ultraweb (design studio, 80 skills, 7 gates) and hardmode (discipline floor, hooks, verification), seated on Claude Code, shipping ultraweb-site with 7 of 7 gates green.">
</picture>

I build the layer between an AI agent and work you'd actually defend — harnesses that make a model
produce something inspectable, and hooks that stop it declaring a victory it hasn't earned.

## Agent infrastructure

### [ultraweb](https://github.com/blyatiful1/ultraweb) · a design studio you can install

A short scoping interview, three mockups to pick from, then a production-grade Next.js 16 site —
built through the review checkpoints a real studio would give you, with preview URLs you check on
your own phone.

80 skills · 3 model-routed subagents · 7 screenshot-verified quality gates · a written taste
constitution that every other skill defers to.

```text
/plugin marketplace add blyatiful1/ultraweb
/plugin install ultraweb@ultraweb
```

The showcase — **[ultraweb-site](https://github.com/blyatiful1/ultraweb-site)** — was built by that
pipeline from one prompt, with no human touch-ups. Every decision it made on the way is committed in
`design/*.md`, so if the site were bad you could prove it from the repo:
**[ultraweb-site.vercel.app](https://ultraweb-site.vercel.app)**

### [hardmode](https://github.com/blyatiful1/hardmode) · a discipline floor for Claude Code

Long-horizon agent work fails in repeatable ways: declaring victory without running the check,
`git reset --hard` over uncommitted work, grinding the same failing command, losing the original
request across a compaction. Advice loses to momentum — so the load-bearing rules sit behind hooks
that cannot be talked out of, and the checks that matter go to fresh-context agents that owe the
work no loyalty.

`python tools/demo.py` runs the actual shipped hooks against planted failure modes and asserts each
one blocks. CI runs it on every push.

## Also

**[gtheme](https://github.com/blyatiful1/gtheme)** — a GNOME theme manager for people who are
nervous about breaking their desktop. Wallpaper, colours, icons, pointer, shell and add-ons in one
window, explained in plain words, with an undo that always works. Pure-Python CLI + TUI, no
telemetry.

**[NightCityMP](https://github.com/blyatiful1/NightCityMP)** — multiplayer for Cyberpunk 2077
(patch 2.31a). Host and join like Minecraft. A continuation of CyberpunkMP.
