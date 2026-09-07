<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/blyatiful1/blyatiful1/main/banner-dark.svg">
  <img src="https://raw.githubusercontent.com/blyatiful1/blyatiful1/main/banner-light.svg" width="720" height="208" alt="Iwan Braun, agent infrastructure. I direct AI agents; they write the code; I hold it to a standard. ultraweb, hardmode, gtheme, NightCityMP.">
</picture>

I direct AI agents, and most of what they build is tooling for directing AI agents
better. Almost none of the code in these repos was written by me. That is the point
of them, not a disclaimer.

## Written by AI, on purpose

Essentially every commit in the repos below was made with Claude Code and carries its
co-author trailer, so the authorship is in the git history, not on a profile page.
Clone any of them and read the log. The authorship is not hidden; it is the method.

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
different mockups, and the pipeline builds, tests and ships the rest. It stops for
review where a studio would, at mockup approval, first-page review and final
acceptance, with preview URLs you can open on your own phone.

Nothing ships on the model's say-so. The gates run against a production build in a
real browser: build and typecheck, responsive screenshots, an adversarial design
critique, accessibility, performance, an anti-slop sweep for purple AI gradients and
"Empower your workflow" copy, and a hunt for placeholders and dead links. A failed
gate blocks the release. A gate that could not run blocks it too, until you accept
each named risk.

The `taste` skill is a written design constitution every other skill defers to, and
every phase writes its decisions to `design/*.md`. The showcase,
**[ultraweb-site](https://github.com/blyatiful1/ultraweb-site)**, was built by that
pipeline from one prompt with no human touch-ups, paper trail included. If the site
were bad, you could prove it from the source: **[ultraweb-site.vercel.app](https://ultraweb-site.vercel.app)**

### [hardmode](https://github.com/blyatiful1/hardmode) · a discipline floor for Claude Code

Long-horizon agent work fails in repeatable ways: declaring victory without running
the check, `git reset --hard` over uncommitted work, grinding the same failing
command, losing the original request across a compaction, handing the work to a
"verifier" that can quietly edit it. Advice loses to momentum, so the load-bearing
rules sit behind hooks that cannot be talked out of, and the checks that matter go to
fresh-context agents that are read-only by hook enforcement, not by promise.

One of those hooks, the claim-audit gate, reads the transcript for evidence a check
ran and passed after the last edit. A per-session ledger records whether the floor
actually fired, so "the floor is armed" is measured rather than assumed.
`python tools/demo.py` runs the actual shipped hooks against planted failure modes
in a throwaway sandbox and asserts each one behaves; CI runs it on every push.

## Also

**[gtheme](https://github.com/blyatiful1/gtheme)** — change how your GNOME desktop
looks, safely, for people new to Linux. Wallpaper, colours, icons, pointer, fonts,
top bar and add-ons in one window, every switch explained in plain words.
Everything is saved before it changes, changes are all-or-nothing, Ctrl+Z undoes
from anywhere, a "before gtheme" snapshot is kept forever, and Looks are settings
rather than code, so they cannot run programs. No account, no server, no telemetry.

**[NightCityMP](https://github.com/blyatiful1/NightCityMP)** — multiplayer for
Cyberpunk 2077. Host and join like Minecraft. A continuation of CyberpunkMP.
