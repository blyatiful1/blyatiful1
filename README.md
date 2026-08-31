<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/blyatiful1/blyatiful1/main/banner-dark.svg">
  <img src="https://raw.githubusercontent.com/blyatiful1/blyatiful1/main/banner-light.svg" width="720" height="208" alt="Iwan Braun — agent infrastructure. I direct AI agents; they write the code — 254 of 256 commits. ultraweb, hardmode, gtheme, NightCityMP.">
</picture>

I direct AI agents, and most of what they build is tooling for directing AI agents
better. Almost none of the code in these repos was written by me. That is the point
of them, not a disclaimer.

## Written by AI, on purpose

**254 of the 256 content commits across the four repos below carry a Claude Code
authorship marker.** The two that don't are an MIT licence file and a bulk first
import of files an AI had already generated — so the honest summary is not "mostly",
it's *essentially all of it*.

| repo | AI-marked commits |
|---|---|
| ultraweb | 60 / 62 |
| hardmode | 39 / 39 |
| gtheme | 124 / 124 |
| NightCityMP | 31 / 31 |

Don't take my word for it — clone any of them and run:

```bash
git log --no-merges --format='%an|%(trailers:key=Co-authored-by,valueonly,separator=;)' | grep -ci claude
```

If anything the number **understates** it: a commit made under my own git identity
can still be AI-written, and plenty are.

What's mine is the part `git log` doesn't record — choosing the problem, writing the
standard down before the model starts, and binning what doesn't meet it. Whether
that's worth much is a fair question, and these repos are exactly where you'd check,
because the gates either go green or they don't.

So this profile isn't *look what I built*. It's **look what this produces when
someone holds it to a standard instead of shipping the first output.** Judge it on
the artifacts.

## Agent infrastructure

### [ultraweb](https://github.com/blyatiful1/ultraweb) · a design studio you can install

A short scoping interview, three mockups to pick from, then a production-grade
Next.js 16 site — built through the review checkpoints a real studio would give you,
with preview URLs you check on your own phone.

80 skills · 3 model-routed subagents · 7 screenshot-verified quality gates · a
written taste constitution that every other skill defers to.

The showcase — **[ultraweb-site](https://github.com/blyatiful1/ultraweb-site)** — was
built by that pipeline from one prompt, with no human touch-ups. Every decision it
made on the way is committed in `design/*.md`, so if the site were bad you could
prove it from the repo: **[ultraweb-site.vercel.app](https://ultraweb-site.vercel.app)**

### [hardmode](https://github.com/blyatiful1/hardmode) · a discipline floor for Claude Code

Long-horizon agent work fails in repeatable ways: declaring victory without running
the check, `git reset --hard` over uncommitted work, grinding the same failing
command, losing the original request across a compaction. Advice loses to momentum —
so the load-bearing rules sit behind hooks that cannot be talked out of, and the
checks that matter go to fresh-context agents that owe the work no loyalty.

`python tools/demo.py` runs the actual shipped hooks against planted failure modes
and asserts each one blocks. CI runs it on every push.

## Also

**[gtheme](https://github.com/blyatiful1/gtheme)** — a GNOME theme manager for people
who are nervous about breaking their desktop. Wallpaper, colours, icons, pointer,
shell and add-ons in one window, explained in plain words, with an undo that always
works. Pure-Python CLI + TUI, no telemetry.

**[NightCityMP](https://github.com/blyatiful1/NightCityMP)** — multiplayer for
Cyberpunk 2077 (patch 2.31a). Host and join like Minecraft. A continuation of
CyberpunkMP.
