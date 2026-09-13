# Changelog

All notable changes to button-app. Format: `## [vX] - YYYY-MM-DD - changes`.
On each version bump: update `#version` footer in `index.html` + add entry here.

## [v0.0.32] - 2026-09-13 - Remember last level across reloads
- Persist `currentParentId` in `root-current-parent` (+ `page` in `root-current-page`) via new `savePlace()` on every `navigateTo` (now `navigateTo(parentId, opts)` with `{page, focus, animate}`), pager `page-up/down`, `+` add, arrow-nav page turns (`focusById`), and prune-triggered `clampPage`/`render`; `readSavedPlace()` parses both keys (int-clamped page).
- `loadNodes()` restores saved parent/page after `loadGraph` migration, then full `pruneEmptiesToOne()`, re-validates (`saved id still exists else roots fallback`), `clampPage()` + `savePlace()`; init no longer resets to `null/0` (removed `currentParentId=null; page=0`), just `loadNodes(); clampPage(); render('first-empty-visible')`.
- Kept: arrow nav, paging, validation, prune empty leaf, drill open `›`, home/back-bottom, crumbs toggle hidden, mono/darkmode, Alt peek, hot reload, ripple off.

## [v0.0.31] - 2026-09-13 - Remove top back button
- Removed top `#back-btn` (`← Back`) from `#nav-bar` (kept `#nav-bar` for `#crumbs` + `#level-title`); removed its `#back-btn` CSS (light + darkmode), `backBtn` const/wiring (`backBtn.addEventListener('click', goBack)`), `updateNav` display toggle, and Alt peek `back-top` push.
- Bottom `#level-back-btn` kept as the single back control (`goBack` wiring unchanged); Alt peek renamed `back-bottom` -> `back-btn` (single again, no duplicate).
- Kept: `goBack` fn, arrow nav, drill, paging, validation, prune, crumbs toggle, home, mono/darkmode, hot reload, ripple off.

## [v0.0.30] - 2026-09-13 - Keyboard up/down navigation
- ArrowUp/ArrowDown move focus across all nodes in the current level (`currentParentId` scope, `computePages` paging): Down from outside focuses node 1, then node 2/3, then turns the page to node 4, etc.; Up reverses (last node when entering from outside, page-back jumps like node 4 -> render 1-3 + focus node 3).
- Typing never hijacked: arrows inside a non-empty input keep caret behavior (ignored); empty waiting inputs still navigate (no caret to protect). Solids are `tabindex=0` (`role=button`, `Edit <word>` label) with a mono 2px `currentColor` focus ring (darkmode-safe); Enter on a focused solid opens edit like click.
- Blur/prune-safe: targets resolve by node id with retry, so blur-triggered empty-leaf auto-remove during page turns can't strand focus.
- Kept: mono, drill, crumbs toggle, home/back, paging, validation, prune, Alt peek (no new buttons/IDs), hot reload, ripple off.

## [v0.0.29] - 2026-09-13 - Unique back peek IDs
- Alt peek: top `#back-btn` -> `back-top`, bottom `#level-back-btn` -> `back-bottom` (was duplicate `back-btn` twice); both buttons still work (`goBack`), both stay visible when inside.
- Kept: mono, drill, crumbs hidden default + toggle, paging, validation, prune, hot reload, ripple off.

## [v0.0.28] - 2026-09-13 - Crumbs hidden behind toggle
- `#crumbs` hidden by default (`style="display:none"`, `crumbsVisible=false` reset on each `navigateTo`); new `#crumb-toggle-btn` (`⋯` U+22EF, mono 24px rounded 8px like home/back) in `#level-nav` row toggles `crumbsVisible` + `updateNav()`.
- `updateNav`: inside shows `crumbsEl` only when `crumbsVisible`, root stays hidden; `#nav-bar`/`#level-title`/backs unchanged.
- Alt peek adds `crumb-toggle-btn` badge; kept mono/darkmode, drill, paging, validation, prune, hot reload, ripple off.

## [v0.0.27] - 2026-09-13 - Level nav row below add button
- New `#level-nav` flex row (centered, gap 8px) below `#add-node-btn`, visible only when inside (`currentParentId!=null`, hidden at root via `updateNav`).
- `#home-btn` (`⌂`, mono 24px rounded) -> `navigateTo(null)` (roots, page 0); `#level-back-btn` (`‹`, mono 24px rounded) -> `goBack()` (parent of current); top `#back-btn` kept, both backs work; prune/ensure, paging reset, focus logic preserved via shared `navigateTo`/`goBack`.
- Alt peek: `home-btn` + `back-btn` (bottom back badge copies `back-btn`) alongside existing top `back-btn`; mono B/W + darkmode invert, validation, thick caret, blur/fade, hot reload, ripple off, centered baseline kept.

## [v0.0.26] - 2026-09-13 - Auto-remove empty childless nodes
- `pruneEmptiesToOne(opts)`: any node with `trim==''` AND `getChildren(id).length===0` auto-removes (iterative, empty WITH children kept as structural parents); per-level steady state is `>=1` non-empty -> zero empties (no waiting until `+`), zero nodes -> one empty waiting; `opts.preserveCurrent` skips the current view level so transient `+` typing/paging survives `render`, full prune on `load`/`navigateTo`.
- `pruneEmptyNodeById` + new `autoRemoveEmptyLeaf(id)`: child check first, sole-node level keeps waiting input, otherwise silent remove + `clampPage`/`render` (no shake); structural empty parents fall through to validation shake.
- Enter/blur with empty trim: childless leaf with siblings auto-removes, sole waiting or parent-with-children keeps `rejectEmpty` shake + `Type a word first` hint; over-long still `Keep it under 60 chars`; `+` single-waiting validation unchanged.
- Kept: mono, drill nav clean, paging, thick caret, blur/fade, Alt peek, hot reload, ripple off, small add, centered baseline.

## [v0.0.25] - 2026-09-13 - Centered node text baseline
- `.solid-wrap` keeps `align-items:center`; `.solid-text` adds `line-height:1` + `display:inline-flex` + `align-items:center` + `vertical-align:middle` + `margin:0` + `padding:0` so text baseline sits centered vs button.
- `.letter` spans add `line-height:1` + `vertical-align:middle`; `.open-btn` adds `align-self:center`.
- Kept: mono + darkmode, drill nav, paging, validation, Alt peek, hot reload, ripple off, 24px add-btn.

## [v0.0.24] - 2026-09-13 - Smaller centered open button
- `.open-btn` 28px -> 18px, font 16px -> 12px, radius 8px -> 6px, padding `0 4px`, `display:inline-flex` + `align-items:center` + `justify-content:center` (`line-height:1`) so `›` is vertically centered with `.solid-text`.
- `.solid-wrap` gap 10px -> 8px, keeps `align-items:center` + `justify-content:center` (wrap + text + button centered vertically).
- Kept: mono + darkmode, drill nav clean (no root/count), paging, validation, Alt peek, hot reload, ripple off.

## [v0.0.23] - 2026-09-13 - Remove nav clutter at root
- `updateNav`: at root (`currentParentId=null`) hides `#nav-bar`/`#crumbs` entirely (no `crumb-0`, no `Root` crumb); inside shows parent-word crumb trail only (no `Root` prefix, indices `crumb-0..n-1` over `crumbPath()`).
- `#level-title`: root clears + hides; inside shows parent word only, no `(N children)`/`(N nodes)` count anywhere; CSS switches to `system-ui, sans-serif` (no monospace).
- Kept: back button when inside, drill `›` open, paging, validation, mono crumbs/buttons, darkmode, Alt peek (auto-hides with `display:none`/empty rects, no code change needed), hot reload, ripple flag off, 24px add-btn.

## [v0.0.22] - 2026-09-13 - Ripple behind flag (off by default)
- `FEATURES = { ripple: false }` near top of script + `shouldRipple()` helper (reads `localStorage 'feat-ripple'` override: `'1'`/`'true'` on, else flag; default off); `console.log('[features] ripple off')` when disabled; turn on by setting `FEATURES.ripple = true` or `localStorage feat-ripple=1`.
- `showSolidNow`: flag off skips ripple restart (`animation='none'`, `display='none'`), keeps together-press thicken + `solid-unblur` fade; flag on restores existing 0.6s ripple animation. All else unchanged: mono, drill nav, paging, validation, thick caret, blur/fade, title-case, hot reload, 24px add-btn.

## [v0.0.21] - 2026-09-13 - Smaller add button
- `#add-node-btn` 36px -> 24px, font 20px -> 14px, radius 12px -> 8px; mono font-family, darkmode invert kept, aria/title + focus behavior unchanged; bounce stays within 3px; Alt `add-btn` badge follows new size (rect-based).

## [v0.0.20] - 2026-09-13 - Child nodes + drill-in
- Tree store: node `{id, word, parentId (null = root), createdAt, order}`; `order` global insertion order, siblings derive by filtering on `parentId`; edges parent->child only; persist `{version: 2, nodes, edges, order}` in `root-graph-json` (v1 flat migrates to `parentId=null`, dangling refs nulled, parent edges rebuilt).
- `Graph.getChildren/count/pathTo`, cascade `removeNode` (deletes descendants), per-level `pruneEmptiesToOne`/`ensureLevelHasNode` (each level keeps max 1 empty, auto one waiting input when empty).
- UI drill: solid nodes show mono `›` `.open-btn`; click drills (`navigateTo`), `#back-btn` to parent, `#crumbs` (`Root / Parent / ...`, `crumb-i` buttons) + `#level-title` parent word + count; same flow per level (input/solid, title-case, thick caret, blur/fade, ripple, `isValidWord` shake, paging 3/last-4, bouncing `+` adds child).
- Context: placeholder `Add to Parent...`, `#status`/`+` aria/title include parent word, Alt peek adds `back-btn`, `level-title`, `crumb-i`, `open-node-i`.

## [v0.0.19] - 2026-09-13 - Block empty root nodes
- `isValidWord(word)`: trimmed length 1..60 (`MAX_WORD_LEN = 60`); wired to Enter, blur, and `+` add button.
- Solidify (Enter/blur): empty or over-long input is rejected — `inputShake` 0.3s (via `translate`, no fight with grow scale), `#status` hint (`Type a word first` / `Keep it under 60 chars`), input stays focused; no solid, no graph write.
- Add (`+`): creates 1 empty waiting input only if no other empty waiting exists; if one is open, jumps to its page and focuses + shakes it instead of duplicating.
- `input.maxLength = 60` guards typing; `Graph.removeNode` + load `pruneEmptiesToOne` kept for legacy cleanup.

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
