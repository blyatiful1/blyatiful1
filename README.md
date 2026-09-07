<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/blyatiful1/blyatiful1/main/banner-dark.svg">
  <img src="https://raw.githubusercontent.com/blyatiful1/blyatiful1/main/banner-light.svg" width="720" height="208" alt="Iwan Braun, agent infrastructure. I direct AI agents; they write the code; I hold it to a standard. ultraweb, hardmode, gtheme, NightCityMP.">
</picture>

I direct AI agents, and much of what they build is tooling for directing AI agents
better. Almost none of the code in the repos below was written by me. That is the
point of them, not a disclaimer.

## Written by AI, on purpose

Essentially every commit that touches the code in the repos below was made with Claude
Code, and the git history says so: Claude is named as author or co-author on nearly
all of them. Clone any repo and read the log.

What's mine is the part `git log` doesn't record: choosing the problem, writing the
standard down before the model starts, and binning what doesn't meet it. These repos
are where you'd check whether that's worth anything, because their gates either go
green or they don't. So this profile isn't *look what I built*. It's *look what this
produces when someone holds it to a standard*. Judge it on the artifacts.

## Agent infrastructure

### [ultraweb](https://github.com/blyatiful1/ultraweb) · a design studio you can install

A Claude Code plugin that builds production Next.js and Tailwind sites through a
guided design session. Describe the site in a sentence, answer a few scoping
questions (never about colours or fonts), pick from a handful of deliberately
different mockups, and the pipeline builds, tests and ships the rest. By default it
pauses at mockup approval, first-page review and final acceptance. When Vercel is
connected, the first-page review and final acceptance come with a preview URL you can
open on your own phone.

Nothing ships on the model's say-so. The gates run against a production build in a
real browser: compile and typecheck, responsive screenshots, an adversarial design
critique, accessibility, performance, an anti-slop sweep for purple AI gradients and
"Empower your workflow" copy, and a hunt for placeholders and dead links. A failure
never ships; a gate that could not run holds the release until you accept each
named risk.

The `taste` skill is a written design constitution every other skill defers to. Every
phase writes its decisions to `design/*.md`, so every decision is on record.

The showcase, **[ultraweb-site](https://github.com/blyatiful1/ultraweb-site)**, is
what that pipeline produced from one prompt with no human touch-ups. The repo holds
the source and the full paper trail, and the site is live at
**[ultraweb-site.vercel.app](https://ultraweb-site.vercel.app)**. If anything had
been fixed by hand, the history would show it.

### [hardmode](https://github.com/blyatiful1/hardmode) · a discipline floor for Claude Code

Long-horizon agent work fails in repeatable ways: declaring victory without running
the check, wiping uncommitted work with `git reset --hard`, grinding the same failing
command, losing the original request across a compaction, handing work to a "verifier"
that can quietly edit it. Advice alone loses to momentum, so the load-bearing rules
sit behind hooks that cannot be talked out of, and the checks that matter go to
fresh-context agents that are read-only by hook enforcement, not by promise.

One of those hooks, the claim-audit gate, reads the transcript for evidence that a
check ran and passed after the last edit. A per-session ledger records whether those
hooks actually fired, so "the floor is armed" is measured rather than assumed.
`python tools/demo.py` runs the shipped hooks against planted failure modes in a
throwaway sandbox and asserts each one behaves; CI runs it on every push.

## Also

**[gtheme](https://github.com/blyatiful1/gtheme)** — a safe way to change how your
GNOME desktop looks, for people new to Linux. Wallpaper, colours, icons, pointer,
fonts, top bar and add-ons in one window, every switch explained in plain words.
Everything is saved first, changes are all-or-nothing, Ctrl+Z undoes from anywhere,
and a "before gtheme" snapshot is kept forever. Its whole-desktop presets, called
Looks, are settings rather than code, so they cannot run programs. No account, no
server, no telemetry.

**[NightCityMP](https://github.com/blyatiful1/NightCityMP)** — multiplayer for
Cyberpunk 2077. Host and join like Minecraft. A continuation of CyberpunkMP.
