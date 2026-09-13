# Changelog

All notable changes to button-app. Format: `## [vX] - YYYY-MM-DD - changes`.
On each version bump: update `#version` footer in `index.html` + add entry here.

## [v0.0.18] - 2026-09-13 - Prune empty waiting nodes
- `Graph.removeNode(id)`: splice from `order`, drop out/in edges, bridge prev->next chain gap, reindex `order` fields.
- Blur/Enter with empty trim removes that node (keeps it if sole node; ensures >=1 node so typing is always possible).
- Load cleanup: `pruneEmptiesToOne()` filters `''` nodes down to max 1 empty (keeps first).

## [v0.0.17] - 2026-09-13 - Graph DSA store + Alt peek IDs
- `Graph` class: `nodes Map<id, {id, word, createdAt, order}>`, `adj Map<id, Set<id>>`, `order [id]`; linear chain edges, `toJSON`/`fromJSON` with legacy migration.
- Persist to `root-graph-json`; migrate `root-nodes-json` list and `root-node-word` single key.
- Alt-key ID peek: mono pills for visible targets (`write-btn`, `stage`, `page-up/down`, `add-btn`, `status`, `version`, `node-i-box/text`); click badge copies ID, Esc/Alt-up hides.

## [v0.0.16] - 2026-09-13 - Node list + bouncing + paging
- Multi root-node list via `#stage` / `#nodes`; `+` add-node button jumps to last page and focuses new input.
- Add-button newborn bounce: random translate within 3px radius every 800ms.
- Paging: `computePages()` — total<=4 shows all, else chunks of 3 with last page taking remainder (e.g. 7->[3,4]); pager `▲/▼` buttons, `show-4` compact layout.

## [v0.0.15] - 2026-09-13 - Symmetric fade + root node + localStorage
- Symmetric 0.25s fade/blur both ways: `fade-blur-out` (input->solid) mirrors `solid-unblur` / `editUnblur`.
- Single root node (`root-node-word` key): empty shows input, saved word shows engraved solid on load; autofocus first empty.

## [v0.0.14] - 2026-09-13 - Thick caret
- 4px fake caret (`#fake-caret`): native caret transparent, canvas-measured block bar follows true caret, blinks 1.06s steps(1); hides on range selection, blur, solidify.

## [v0.0.13] - 2026-09-13 - Blur/fade edit
- Click solid text blurs out (`blur-out` 0.25s), then input pops back via `edit-pop`; status hints update (`Editing...`, `Waiting...`, `Click text to edit`).

## [v0.0.12] - 2026-09-13 - Blur = Enter
- Input `blur` commits like Enter: non-empty title-cases to solid, empty stays waiting; guards `_solidifying` and already-solid states.

## [v0.0.11] - 2026-09-13 - Mono B/W + darkmode
- Strict black/white mono palette; `prefers-color-scheme: dark` inverts button, input, caret, ripple, engraved text, pager/add buttons, badges.

## [v0.0.10] - 2026-09-13 - Edit-pop from size
- Re-edit uses `editUnblur` keyframes: blur 8px->0 with 1.05 scale pop (0.25s), distinct from first `grow` animation.

## [v0.0.9] - 2026-09-13 - Semver footer
- Fixed `#version` footer (11px, bottom-right) showing current semver, e.g. `v0.0.9`.

## [v0.0.8] - 2026-09-13 - Hot reload
- Dev hot reload: `HEAD` poll every 1s on `location.pathname`, reloads on `Last-Modified`/`ETag`/`Content-Length` change.

## [v0.0.7] - 2026-09-13 - Together thicken
- Solid letters animate together: per-`.letter` `thicken-press` 0.45s (400->800 weight, 1.18->1.0 scale) with engraved shadow.

## [v0.0.6] - 2026-09-13 - Write label
- Round button label set to `Write`; hidden once node UI takes over (kept for peek target).

## [v0.0.5] - 2026-09-13 - Engraved press + ripple
- Engraved `.solid-text` style (letter-spacing, dual text-shadow) + expanding `.ripple` circle on solidify; press scale feedback.

## [v0.0.4] - 2026-09-13 - Caps then title-case
- Uppercase input first, then title-case (`toTitleCase`) preserving caret; Enter trims and solidifies.

## [v0.0.3] - 2026-09-13 - Auto reload
- Auto-focus waiting input on load; auto-solidify saved word without animation.

## [v0.0.2] - 2026-09-13 - Shrink to input
- Round button shrinks (`scale(0)`, fade) into growing centered input (`grow` 0.3s).

## [v0.0.1] - 2026-09-13 - Button center
- Initial centered 160px round black button on white, hover/active scale feedback.
