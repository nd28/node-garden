# Changelog

All notable changes to button-app. Format: `## [vX] - YYYY-MM-DD - changes`.
On each version bump: update `#version-inline` + tip card version in `index.html` + add entry here.

## [v0.0.79] - 2026-09-14 - cleared leaf moves to trash (not vanish)

- `Graph` gains trash: node `{trashed:false, trashedAt:0}`; new `trashNode(id)` (leaf-only, keeps `id/word/body/parentId` for restore, no cascade), `getTrash()` (by `trashedAt`), `trashSize`, future `restoreNode(id)` (untrash, re-root when parent missing); `size` now counts active only; `getOrderedNodes`/`getChildren` exclude `trashed` so trash stays out of `currentList/count/paging/render`; `toJSON` persists trash, `fromJSON` restores `trashed/trashedAt` (old saves without fields migrate to active).
- `autoRemoveEmptyLeaf(nid)`: was `removeNode` destroy (and refused stored-non-empty, so solid-cleared only shook); now leaf with zero active children -> `trashNode` + `console.log('[trash] moved to trash', {id, word, parentId})` + `status 'Moved to trash'`: solid cleared to empty (stored word kept as last word) trashes even when sole, empty waiting with siblings trashes (was silent destroy), sole waiting empty + structural parent (has children) still shake as before; after trash, `childCount(pid)===0` adds a waiting node so the level never strands.
- `pruneEmptyNodeById(id)`: same `removeNode` -> `trashNode` + console + `Moved to trash` (dead code, no callers, kept consistent); bulk `pruneEmptiesToOne` still destroys never-typed empty dups (no word to keep, avoids trash noise), trashed already excluded.
- No new UI (restore UI later); Alt peek untouched; `v0.0.78` -> `v0.0.79` (`#version-inline` + tip card + header comment).

## [v0.0.78] - 2026-09-14 - credit+version inside ? card, version below status

- `#keys-tip-card` gains footer below shortcut list: divider (`.tip-divider`, full-width `1px` `currentColor` at `0.25`, `4px 0 2px` margin) + `.tip-credit` (`made by nd28 with opencode + muse spark 1.3`, dimmest silent tiny `10px` mono `opacity:0.3`) + `.tip-version` (`v0.0.78` link to `CHANGELOG.md`, `11px` dim `0.9`); shortcuts list untouched first.
- New in-flow `#version-inline` directly below `#status` in `#stage` (centered `11px` dim `#888` link `v0.0.78` -> `CHANGELOG.md`, `opacity:0.9`); version now appears twice (card + below status), credit only in card.
- `#foot-right` drops `#credit` + old `#version` (removed, no duplicate IDs) — `?` button alone fixed `bottom:8px right:12px`; stale `#version`/`#credit` CSS replaced by `#version-inline` + `.tip-credit`/`.tip-version` (light + dark).
- Alt peek: `version` badge -> `version-inline` (same rect-follow/copy behavior).
- Kept: all features, mono/darkmode, tip toggle/dismiss, peek badges.

## [v0.0.77] - 2026-09-13 - credit mentions opencode

- `#credit` text -> `made by nd28 with opencode + muse spark 1.3` (same `#foot-right` cluster beside `#version`, dimmest silent tiny `10px` mono `opacity:0.3`, no link).
- Kept: all features, foot cluster position, mono/darkmode.

## [v0.0.76] - 2026-09-13 - status in-flow below nav buttons

- `#status` moved in-flow directly below `#level-nav` row (inside `#stage`, after nav): drops fixed `bottom:24px` center (`position/left/transform` removed) for `margin-top:12px`, centered by `#stage` flex; keeps pill style (dim `12px`, `radius:999px`, `4px 10px` padding, ellipsis, `pointer-events:none`).
- No overlap with fixed `#foot-right` cluster (status now flows with stage, foot stays `bottom:8px right:12px`).
- Kept: all status messages/flashes, mono/darkmode, all features.

## [v0.0.75] - 2026-09-13 - credit beside version in foot cluster

- New `#foot-right` cluster (fixed `bottom:8px` `right:12px`, flex row `gap:8px`): `?` button + `#credit` + `#version` side by side, credit left of version, tiny `10px` mono `opacity:0.3` silent; old bottom-left `#credit` fixed removed so nothing overlaps `?`.
- `#keys-tip-btn` is now the first item in the cluster (`position:static`, was fixed `right:64px`); tip card position/behavior untouched.
- Kept: mono/darkmode, all features.

## [v0.0.74] - 2026-09-13 - credit footer

- New dimmest silent `#credit` footer (`made by nd28 with muse spark 1.3`, tiny `10px` mono, `opacity:0.3`, fixed bottom-left above style toggle, `pointer-events:none`, no link): inherits body color so mono/darkmode just works.
- Kept: all features, style knobs position, version footer.

## [v0.0.73] - 2026-09-13 - "?" key toggles tip card

- Global `keydown` `?` (shift+/) toggles `#keys-tip-card` like the `?` button (`setOpen(!open)`): skips Alt/Ctrl/Meta, ignores non-empty `INPUT`/`TEXTAREA` (lets user type `?`); empty waiting input `preventDefault`s (no `?` char) and toggles.
- Kept: button toggle, outside-click/Esc dismiss, all shortcuts, all features.

## [v0.0.72] - 2026-09-13 - Keys distinct from meaning in tip card

- `#keys-tip-card` lines split into `<span class="tip-key">` pills (mono bold, `1px` bordered, `4px` radius, `0 4px` padding, subtle bg, full `opacity:1`) + `<span class="tip-def">` meaning (`opacity:0.6`); e.g. `Up / Down — move` -> two key pills + dim def.
- Kept: card position/style, all shortcuts, toggle/dismiss, all features.

## [v0.0.71] - 2026-09-13 - Key shortcuts tip card

- New tiny ghost `#keys-tip-btn` (`?`, 24px rounded 8px, fixed `bottom:8px` `right:64px` next to `#version` footer, page-font label, darkmode invert): toggles floating `#keys-tip-card` shortcut list (`aria-expanded` + `aria-haspopup`, `role="dialog"`).
- `#keys-tip-card` mono pill card (`position:fixed` `bottom:40px` `right:12px`, `z-index:5000`, `12px` radius, `1px` border, `8px 12px` padding, `0 8px 24px` shadow, dim text `#555` light / `#999` dark, `12px` page font, `line-height:1.6`, `white-space:nowrap`): lines `Up / Down — move`, `Right — open`, `Left — back`, `+ — add`, `Enter — edit / save`, `Alt (hold) — peek IDs`, `Esc — close`; overlays content so toggle never shifts layout.
- Dismiss on outside click (`document` click skips btn + card) + `Esc` (own `keydown` listener, crumbs/peek handlers untouched); Alt peek adds `keys-tip-btn` badge.
- Kept: even stage spacing, arrows Up/Down walk, Right open, Left back, + add, Enter edit/solidify, Alt peek, Esc closes crumbs, all features.

## [v0.0.70] - 2026-09-13 - Even stage spacing top + list + nav

- `#stage` `gap: 12px` -> `gap: clamp(12px, 3vh, 28px)` so top/list/nav breathe evenly on short/tall viewports; `body overflow:hidden` (no scroll) + paging fit kept.
- `#nodes` gains `margin: 4px 0`; `#add-node-btn` gains `margin: 6px auto`; `#level-nav` gains `margin-top: 8px`; `#level-title` gains `margin-bottom: 6px`; `#node-body` gains `margin-bottom: 8px`.
- Kept: responsive clamped node gaps, drill, body, knobs, mono/darkmode, corners glide, validation, Alt peek, hot reload.

## [v0.0.69] - 2026-09-13 - Corner focus translate glide

- Focus corners glide outward on focus: unfocused corners sit 4px inward (`tl translate(4px,4px)`, `tr (-4px,4px)`, `bl (4px,-4px)`, `br (-4px,-4px)`) + small `10px`, focused settles to `translate(0,0)` + larger `14px` + outward offsets (`-6px`/`-10px`); `transform 0.2s ease` added to the existing `opacity/width/height/top/right/bottom/left` transition, animate-in only.
- Kept: per-letter glow, shrink `0.98` + lift, mono/darkmode, `prefers-reduced-motion` disables transition, all features.

## [v0.0.68] - 2026-09-13 - Polish status hint as centered pill

- `#status` polished from plain fixed-bottom gray to minimal centered pill: `bottom:24px` (kept clear of `#level-nav`/`#add-node-btn` flow + `#version` bottom-right) + `left:50%` + `transform:translateX(-50%)`, page font `12px`, `letter-spacing:0.02em`, `opacity:0.6`, subtle bg `rgba(0,0,0,0.04)` light / `rgba(255,255,255,0.06)` dark, `padding:4px 10px`, `radius:999px`, no border, single-line ellipsis (`white-space:nowrap`, `max-width:92vw`, `pointer-events:none`).
- Kept: all messages unchanged (`Waiting`, `Editing`, click text, `Font/Spacing/Leading/Weight/Size` flashes), colors `#555` light / `#999` dark.

## [v0.0.67] - 2026-09-13 - Animate focus corners in (fade + grow, no loop)
- Focus corners animate in only (no pulse loop, avoids distraction): `opacity 0->1` + size `10px->14px` + slight outward move (base `top/bottom:-4px`, `left/right:-8px` -> focused `top/bottom:-6px`, `left/right:-10px`), `0.2s ease` via `transition: opacity, width, height, top, right, bottom, left`; `prefers-reduced-motion: reduce` disables the transition.
- Base `.corner` stays rendered at `opacity:0` (`display:block`, was `display:none`/`block` toggle) so the transition can run; `:focus-within` flips to `opacity:1` + `14px` + outward offsets; `pointer-events:none`, `2px` L borders, dim `rgba(0,0,0,0.35)` light / `rgba(255,255,255,0.35)` dark unchanged.
- Kept: per-letter glow, shrink `0.98` + lift, mono/darkmode, responsive clamped gaps, drill, body, knobs, arrows, validation, Alt peek, hot reload. Loop-later flag: add a `cornerPulse` keyframes + `animation` on `:focus-within .corner` if a gentle pulse is ever wanted.
- Rollback: revert this entry + the `v0.0.67` corner CSS (base/positions/transition + `prefers-reduced-motion`) back to the `v0.0.66` `display:none/block` block.

## [v0.0.66] - 2026-09-13 - EXPERIMENTAL focus corners (bottom off, rollback ready)
- EXPERIMENTAL (awaiting feedback, rollback ready in a single commit): camera-shutter corner focus UI replaces the bottom outline — 4 child `.corner` L shapes per `.root-node` (`tl/tr/bl/br`, `14px`, `2px` borders, `dim rgba(0,0,0,0.35)` light / `rgba(255,255,255,0.35)` dark, `position:absolute` outside node padding `top/bottom:-6px`, `left/right:-10px`), rest invisible; shown only on `body.focus-corners .root-node:focus-within .corner` (`display:block`, else `display:none`, `pointer-events:none`).
- Gated by `const FEATURES.focusCorners = true` (easy off: set `false`, optional `localStorage 'feat-focus-corners'` override `'1'/'true'`); JS adds `body.focus-corners` only when on, same pattern as underline gate.
- Bottom underline OFF: `FEATURES.focusUnderline = true` -> `false` (light + dark `body.focus-underline .root-node:focus-within::after` blocks + flag/JS gate kept for rollback).
- Kept: no container `box-shadow` (per-letter glow only), shrink `0.98` + lift `translateY(-2px)`, responsive clamped gaps, drill, body, knobs, mono, arrows, validation, Alt peek, hot reload.
- Rollback: set `focusCorners false` (+ optionally `focusUnderline true`) + delete the two `EXPERIMENTAL v0.0.66` corner CSS blocks (light + dark) + flag/JS gate + corner divs in `createNodeEl` + this entry.

## [v0.0.65] - 2026-09-13 - Fix focus underline gap + 80px height floor
- `body.focus-underline .root-node:focus-within::after` `margin-top:6px` -> `margin-top:2px` (`width:60%`, `height:4px`, `border-radius:2px` unchanged) so the dim thick outline sits close to text.
- `.root-node` `min-height:80px` -> `min-height:0` (fit content; `align-items:center`, `justify-content:center`, `flex-direction:column` unchanged) so focused/empty height goes below 80px; `.solid-wrap` `min-height:80px` -> `min-height:40px`; `#nodes.show-4` `60px` floors kept.
- Kept: experimental flag (`FEATURES.focusUnderline` + `body.focus-underline` gate), per-letter glow, shrink `0.98` + lift, responsive clamped gaps, drill, body, knobs, mono, arrows, validation, Alt peek, hot reload.
- Rollback: set flag `false` + delete the two `EXPERIMENTAL v0.0.64, v0.0.65 gap fix` CSS blocks (light + dark) + flag/JS gate + v0.0.64/v0.0.65 entries.

## [v0.0.64] - 2026-09-13 - EXPERIMENTAL focused-node bottom outline (rollback ready)
- EXPERIMENTAL (awaiting feedback, rollback ready in a single commit): dim thick bottom outline under the focused node via `body.focus-underline .root-node:focus-within::after` (`content:''`, `display:block`, `width:60%`, `height:4px`, `margin-top:6px`, `border-radius:2px`, `background:rgba(0,0,0,0.25)` light / `rgba(255,255,255,0.25)` dark).
- Gated by `const FEATURES.focusUnderline = true` (easy off: set `false`, optional `localStorage 'feat-focus-underline'` override); JS adds `body.focus-underline` only when on, so `false` removes the underline entirely.
- Kept: no container `box-shadow` (per-letter glow only), shrink `0.98` + lift `translateY(-2px)`, responsive clamped gaps, drill, body, knobs, mono, arrows, validation, Alt peek, hot reload.
- Rollback: set flag `false` + delete the two `EXPERIMENTAL v0.0.64` CSS blocks (light + dark) + flag/JS gate + this entry.

## [v0.0.63] - 2026-09-13 - Responsive clamped node gap
- `#nodes` `gap: 18px` -> `gap: clamp(8px, 2.5vh, 24px)` (min 8px, preferred 2.5vh, max 24px) so paging 3 fits without scroll on short/tall viewports.
- `#nodes.show-4` `gap: 8px` -> `gap: clamp(4px, 1.5vh, 12px)` (min 4px, max 12px) to keep 4-up compact without overflow.
- Kept: `body overflow:hidden` (no scroll), drill, body, knobs, mono, arrows, validation, Alt peek, hot reload.
- `#node-body` `opacity: 0.85` -> `0.6` light + explicit `opacity: 0.6` dark (was inheriting light value); typed body text sits dimmer below the title; `::placeholder` stays dim `0.35` (`#888` light / `#666` dark) untouched.
- `#level-title` `opacity: 0.8` -> `1` full bright so the parent word stays prominent above the dimmed body.
- Kept: knobs collapse, drill, body save/autogrow, mono/darkmode, Alt peek, hot reload.

## [v0.0.61] - 2026-09-13 - Tighter body line height
- `#node-body` `line-height: var(--node-leading)` -> fixed `1.2` (decoupled from the node leading cycler so body text stays tight); `font-size: 1rem` + `max-width min(70vw,480px)` unchanged, `min-height 1.4em` -> `1.2em` to match; `autoGrow` (scrollHeight) untouched.
- Kept: knobs collapse, drill, body save, mono/darkmode, Alt peek, hot reload.

## [v0.0.60] - 2026-09-13 - Collapsible style knobs
- Font/text knobs (`#font-btn Aa`, `#spacing-btn ↔`, `#leading-btn ↕`, `#weight-btn B`, `#size-btn A+`) collapse into `#style-knobs` row behind `#style-toggle` (`T`, 24px ghost, fixed bottom-left at `left:12px`, `aria-expanded` + `aria-controls="style-knobs"`): click expands to show all 5 knobs right of the toggle (`left:42px` flex row, `gap:6px`), click again collapses to single button; simple show/hide via `.open` (`#style-knobs:not(.open)` `display:none`).
- Default collapsed (clean page), persists open state in `localStorage 'style-knobs-open'` (`'1'` open, else closed, validated on load); knob buttons drop `position:fixed` for in-row static layout, same 24px ghost style light + darkmode (toggle inverts too); Alt peek adds `style-toggle` badge (knob badges auto-hide when collapsed).
- Kept: lazy fonts/weights, wrap, drill, paging, arrows, validation, body, hot reload, ripple off.

## [v0.0.59] - 2026-09-13 - Node body about-text
- Each graph node gains `body` string (`''` default, migrated `''` for old nodes in `Graph.fromJSON`); persisted via `root-graph-json` (`toJSON` serializes nodes incl `body`, `updateBody(id, body)` setter).
- Inside a node (`currentParentId != null`) `#nav-bar` shows `#node-body` textarea below `#level-title`: always-editable, multiline (`Enter` = newline, no solidify), natural case (no title-case), empty allowed (no shake), dim `Write about...` placeholder, page font `1rem` / `opacity 0.85` / `max-width min(70vw,480px)` + shared `--node-leading/--node-spacing/--node-weight`, `autoGrow` on input/nav/resize/font cycles; hidden at root; saves on `input`/`blur` via `saveGraph()`.
- Alt peek adds `node-body` badge; darkmode inverts text/caret/placeholder.
- Kept: drill, paging, arrows, validation, fonts/weights/sizes, hot reload, ripple off.

## [v0.0.58] - 2026-09-13 - Font-size cycler
- New tiny ghost `#size-btn` (`A+`, 24px rounded 8px, fixed bottom-left at `left:132px` next to `#weight-btn`, page-font label, darkmode invert): cycles node size `1.4rem -> 1.6rem -> 2rem -> 2.6rem -> back`, default `2rem` (idx 2, matches prior hardcoded `2rem`).
- `.root-input` + `.solid-text` `font-size:2rem` -> `var(--node-size)`; `:root` gains `--node-size:2rem`; `#nodes.show-4` overrides `1.6rem` -> `calc(var(--node-size)*0.8)` so compact scales proportionally.
- Persists in `localStorage 'node-size-idx'` (validated int, applied on load), click shows `Size <val>` (e.g. `Size 2rem`) in `#status` for ~1.2s then `updateStatus()` restores, `autoGrow` + `updateCaret` re-run (caret height follows computed `fontSize`/`lineHeight`); Alt peek adds `size-btn` badge.
- Kept: all features.

## [v0.0.57] - 2026-09-13 - Chevron pagers
- `#page-up`/`#page-down` glyphs `▲ U+25B2` (`&#9650;`) / `▼ U+25BC` (`&#9660;`) -> `˄ U+02C4` (`&#708;`) / `˅ U+02C5` (`&#709;`) to match `‹ U+2039` back chevron style; 24px ghost mono buttons, `aria-label`s, order, and row visibility untouched.
- Kept: all features.

## [v0.0.56] - 2026-09-13 - Pagers in level-nav row
- `#page-up` + `#page-down` moved from `#stage` (top/bottom of `#nodes`) into `#level-nav` between `#level-back-btn` and `#crumb-toggle-btn`: row order now `home, back, page-up, page-down, crumb-toggle`.
- `.pager-btn` resized `36x28`/`10px radius` -> `24x24`/`8px` ghost (`inline-flex` centered, `padding:0`) to match `home/back/crumb-toggle`; `#level-nav` + hover/active selectors extended to `#page-up/#page-down` (light + darkmode); gap stays `8px`.
- `updateNav()` owns all row visibility: row shows when inside (`currentParentId`) OR paging needed (`page>0` or `page<pages-1`); `home/back/crumb-toggle` only when inside, pagers only when their turn exists; `render()` drops its direct pager toggles and delegates to `updateNav()` so root paging stays reachable while the row hides when idle at root.
- Kept: drill, paging math (`computePages`/`clampPage`), arrows, validation, fonts/weights lazy whole-page, wrap, Alt peek ids (`page-up/page-down`) unchanged, hot reload, ripple off.

## [v0.0.55] - 2026-09-13 - Lazy-load font weights per weight
- `NODE_FONTS` drops multi-weight `css` slugs for per-weight `fam` + `weights` (`JetBrains+Mono [300,400,600,800]`, `IBM+Plex+Mono [300,400,600,700]`, `Space+Mono [400,700]`, `Lexend`/`Inter+Tight [300,400,600,800]`, `System UI/Mono/Georgia fam:null` no load); new `fontWeightFor(font, want)` nearest-match map (exact wins, else closest: `Space 300->400`, `600/800->700`, `Plex 800->700`) + `fontCssFor(font, want)` single-`wght` slug (`Fam:wght@400`).
- `ensureWebfont(i, wantWeight)` loads only the active weight's sheet (`css2?family=<fam>:wght@<mapped>&display=swap`, `data-lazy-font="<name>:<mapped>"`, cache per family+weight in `loadedFontCss`, `onerror` retry); defaults to `NODE_WEIGHTS[weightIdx]` (default `400` only when a non-system font is chosen, never upfront for system stacks).
- Weight state (`LS_WEIGHT`/`NODE_WEIGHTS`/`weightIdx`) moved above fonts so the initial `ensureWebfont(fontIdx)` loads the persisted weight only; `applyFont` passes `NODE_WEIGHTS[weightIdx]`, `applyWeight` calls `ensureWebfont(fontIdx, ...)` + `document.fonts.ready` reflow (`autoGrow`/`updateCaret`) like `applyFont`.
- Kept: whole-page var, wrap, spacing/leading/weight cycle, drill, paging, arrows, validation, prune, crumbs, Alt peek, hot reload, ripple off.

## [v0.0.54] - 2026-09-13 - System UI default, page-wide font cycle
- Default stack is now System UI (`system-ui, -apple-system, sans-serif`): `:root` gains `--page-font` (same value in `--node-font`), `body` + `#status` + `#level-title` + all buttons/crumbs/badges (`pager`, `add`, `home/back/crumb-toggle`, `font/spacing/leading/weight`, `crumb-btn`, `open-btn`, `version`, `id-badge`) use `var(--page-font)` instead of hardcoded mono/system stacks; fresh load fetches zero Google Fonts.
- `NODE_FONTS` reordered System UI first (`System UI -> System Mono -> JetBrains Mono -> IBM Plex Mono -> Space Mono -> Lexend -> Inter Tight -> Georgia -> back`); `applyFont` + load set both `--page-font` and `--node-font` to the same stack so nodes/inputs keep sharing for caret while the whole page follows; lazy `ensureWebfont` + `document.fonts.ready` + `autoGrow`/`updateCaret` unchanged.
- Persists in same `localStorage 'node-font-idx'` (validated int), click still flashes `Font: <name>` in `#status` for ~1.2s; note old idx values now map to the new order (e.g. stored `0` was System Mono, now System UI).
- Kept: wrap, spacing/leading/weight vars, drill, paging, arrows, validation, prune, crumbs floating, Alt peek, hot reload, ripple off, B/W mono colors (only fonts change).

## [v0.0.53] - 2026-09-13 - Font-weight cycler
- New tiny ghost `#weight-btn` (`B`, 24px rounded 8px, fixed bottom-left at `left:102px` next to `#leading-btn`, mono label, darkmode invert): cycles base node weight `300 -> 400 -> 600 -> 800 -> back`, default `400` (idx 1).
- `.root-input` + `.solid-text` gain `font-weight:var(--node-weight)`; `:root` gains `--node-weight:400`; `.letter` base + `thicken-press`/`thicken-press-dark` `from` use the var so the press starts at the cycled base and still thickens to `800` max; reload solids (`animate:false`) keep `800` like the animated end.
- Persists in `localStorage 'node-weight-idx'` (validated int, applied on load), click shows `Weight <val>` (e.g. `Weight 600`) in `#status` for ~1.2s then `updateStatus()` restores, `autoGrow` + `updateCaret` re-run (caret canvas/mirror already copy `fontWeight`); Alt peek adds `weight-btn` badge.
- Lazy fonts untouched: only loaded weights render natively (e.g. JetBrains 800, Plex 700), missing steps synthesize via the stack fallback.
- Kept: all features.

## [v0.0.52] - 2026-09-13 - Dim input placeholder
- `.root-input::placeholder` now dim mono gray at `opacity:0.35` with `font-style:normal` so typed text stands out: light `color:#888`, dark `color:#666` (was dark-only `#888` full opacity, light inherited full black/white).
- Kept: title-case placeholder text, wrap, fonts var, spacing/leading, validation, drill, paging, arrows, Alt peek, hot reload, ripple off.

## [v0.0.51] - 2026-09-13 - Crumbs floating dropdown menu
- `#crumbs` is now a floating dropdown menu anchored on `#crumb-toggle-btn`: `position:fixed` + `z-index:5000`, mono pill container (`12px` radius, `1px` border, `6px` padding, `0 8px 24px` shadow, light `#fff`/dark `#000`), vertical list (`column`, full-width left-aligned `.crumb-btn`, `/` separators hidden, `40vh` scroll), positioned via `positionCrumbMenu()` drop-up above the toggle (centered, viewport-clamped, re-run on open/`updateNav`/`resize`).
- Behavior: toggle click `stopPropagation` + `setCrumbsVisible(!)` opens/closes (syncs `aria-expanded`, `aria-haspopup` on button); crumb click `navigateTo` navigates + closes; `document` outside click + `Escape` close; `navigateTo` reset still closes; overlays content so open/close never shifts `#level-title` layout.
- Kept: badge count, mono/darkmode, drill, paging, arrows, validation, fonts/spacing/leading, hot reload, ripple off.

## [v0.0.50] - 2026-09-13 - Tight leading step
- `NODE_LEADINGS` gains `0.85` tight step: cycle now `0.85 -> 1.0 -> 1.3 -> 1.6 -> 2.0 -> back`, default idx still `1.3` (now idx 2).
- Caret mirror already copies computed `lineHeight` and `autoGrow` re-runs on cycle, so textarea grow + wrap caret stay aligned at tight leading; acceptable tight, no overlap break.
- Kept: all features.

## [v0.0.49] - 2026-09-13 - "+" key adds node
- Global `keydown` `+` / `=` (shift+=) triggers `addBtn.click()` (same single-waiting validation, jump to last page, focus new): skips Alt/Ctrl/Meta, ignores non-empty `INPUT`/`TEXTAREA` (lets user type `+`); empty waiting input `preventDefault`s (no `+` char) and reuses button flow (focus + shake existing empty instead of dup).
- Kept: all features.

## [v0.0.48] - 2026-09-13 - Auto-focus first node on load/level open
- New `focusFirstVisible()`: after `render('first-empty-visible')` + load/`navigateTo` rAF, focuses first visible node — empty waiting `.root-input` (caret via `autoGrow` + `hideCaretDelayed`) if present, else first `.solid-text` via `focusableForNodeEl` (tabindex focus only, no edit open).
- `render` `'first-empty-visible'` branch now calls the helper (solid fallback added); `navigateTo` rAF + init rAF call it then `updateStatus()`; explicit `o.focus` in `navigateTo` skips the rAF refocus so paging/`stepFocus` behavior is untouched.
- Guard: skips when Alt peek badges (`.id-badge`) are visible.
- Kept: all features.

## [v0.0.47] - 2026-09-13 - Line-height cycler
- New tiny ghost `#leading-btn` (`↕`, 24px rounded 8px, fixed bottom-left at `left:72px` next to `#spacing-btn`, mono label, darkmode invert): cycles node line-height `1.0 -> 1.3 -> 1.6 -> 2.0 -> back`, default `1.3` (idx 1, matches wrap).
- `.solid-text` + `.root-input` `line-height:1.3` -> `var(--node-leading)`; `:root` gains `--node-leading:1.3`; caret mirror already copies `lineHeight` + `autoGrow` re-run so wrap caret stays aligned.
- Persists in `localStorage 'node-leading-idx'` (validated int, applied on load), click shows `Leading <val>` (e.g. `Leading 1.6`) in `#status` for ~1.2s then `updateStatus()` restores; Alt peek adds `leading-btn` badge.
- Kept: all features.

## [v0.0.46] - 2026-09-13 - Negative spacing step
- `NODE_SPACINGS` gains `-0.02em` tight step: cycle now `-0.02em -> 0em -> 0.04em -> 0.08em -> 0.12em -> back`, default idx still `0.04em` (now idx 2).
- Caret mirror already copies `letterSpacing` and canvas fallback adds `letterSpacing*len`, so negative spacing stays aligned; no layout change.
- Kept: all features.

## [v0.0.45] - 2026-09-13 - Letter-spacing cycler
- New tiny ghost `#spacing-btn` (`↔`, 24px rounded 8px, fixed bottom-left at `left:42px` side by side with `#font-btn`, mono label, darkmode invert): cycles node letter-spacing `0em -> 0.04em -> 0.08em -> 0.12em -> back`.
- `.solid-text` `letter-spacing:0.04em` -> `var(--node-spacing)`; `.root-input` gains `letter-spacing:var(--node-spacing)`; `:root` gains `--node-spacing:0.04em` default; fake-caret canvas fallback adds `letterSpacing*len`, mirror already copies `letterSpacing` so wrap caret stays aligned.
- Persists in `localStorage 'node-spacing-idx'` (validated int, applied on load), click shows `Spacing <val>` (e.g. `Spacing 0.08em`) in `#status` for ~1.2s then `updateStatus()` restores; Alt peek adds `spacing-btn` badge.
- Kept: fonts lazy, wrap textarea, mono, drill, paging, arrows, validation, prune, crumbs badge, primary/ghost, hot reload, ripple off.

## [v0.0.44] - 2026-09-13 - Lexend + Inter Tight font trials
- `NODE_FONTS` trial list gains `Lexend` (readable, wide: stack `"Lexend", system-ui, sans-serif`, css `Lexend:wght@400;700`) + `Inter Tight` (stack `"Inter Tight", system-ui, sans-serif`, css `Inter+Tight:wght@400;700`); cycle order now `System Mono -> JetBrains Mono -> IBM Plex Mono -> Space Mono -> System UI -> Georgia -> Lexend -> Inter Tight -> back`.
- Lazy `ensureWebfont` mechanism unchanged (per-family sheet + on-demand preconnect, `loadedFontCss` once-guard, system fallback offline); shared `var(--node-font)` caret alignment kept; `document.fonts.ready` + rAF re-runs `autoGrow` + `updateCaret` so wrap textarea auto-grow stays correct with new fonts.
- Kept: persist `node-font-idx`, `Font: <name>` status flash, Alt `font-btn` badge, all features.

## [v0.0.43] - 2026-09-13 - Word wrap for node text
- `.solid-text` wraps: `display:inline-block`, `white-space:normal`, `overflow-wrap:break-word`, `word-break:break-word`, `max-width:min(70vw,480px)`, `text-align:center`, `line-height:1.3`; spaces render as plain breaking text nodes (was `\u00A0` no-break) so lines break between words, letters stay `inline-block` (thicken transform kept) with break opportunities between them for long words; `.letter` uses `line-height:inherit`; `.solid-wrap` gains `max-width:92vw`.
- `.root-input` is now `<textarea rows=1 wrap=soft>` (was `<input type=text>`): `resize:none`, `overflow:hidden`, `pre-wrap` + `break-word`, same `max-width`, `line-height:1.3`, `field-sizing:content` + JS `autoGrow()` (height follows `scrollHeight`, called on input/focus/show/render/resize/font-switch); `Enter` solidifies via `preventDefault` (no newlines, pasted `\r\n` collapsed to space), title-case/caret preservation, `maxLength=60` validation, `Enter`/blur/arrows (`TEXTAREA.root-input` empty-check like `INPUT`) all kept.
- Fake caret goes multiline via hidden mirror (`caretPosWrapped`: same width/font/align/break rules, marker at caret for wrapped x/y, single-line `lineHeight*0.85` bar); canvas single-line math kept as fallback.
- Kept: mono, `var(--node-font)`, thick caret, blur/fade, validation max 60, paging, drill, crumbs, Alt peek, hot reload, ripple off.

## [v0.0.42] - 2026-09-13 - Lazy-load node webfonts
- Removed blocking Google Fonts `<link>` (+ head preconnects) from `index.html` head: initial paint uses system mono only, zero font CSS fetched upfront.
- `#font-btn` cycle order unchanged (`System Mono -> JetBrains Mono -> IBM Plex Mono -> Space Mono -> System UI -> Georgia`): first switch to a webfont injects that family's sheet only (`css2?family=<fam>&display=swap`, `data-lazy-font`), plus on-demand `preconnect` to `fonts.googleapis.com` / `fonts.gstatic.com` (`data-lazy-preconnect`); each family loads once (`loadedFontCss` guard).
- `NODE_FONTS` gains per-entry `css` slug (`null` for system stacks); `ensureWebfont(i)` before `--node-font` set in `applyFont` + on load for persisted `node-font-idx`; `document.fonts.ready` re-runs `updateCaret`; shared `var(--node-font)` caret alignment kept; offline keeps system-mono fallback via stack (`onerror` just allows retry).
- Kept: persist `node-font-idx`, `Font: <name>` status flash, Alt `font-btn` badge, all features.

## [v0.0.41] - 2026-09-13 - Font trial switcher
- New tiny ghost `#font-btn` (`Aa`, 24px rounded 8px, fixed bottom-left footer, mono label, darkmode invert): cycles node font `System Mono -> JetBrains Mono -> IBM Plex Mono -> Space Mono -> System UI -> Georgia -> back`.
- Node + input share `var(--node-font)` (`.root-input` + `.solid-text` both use it, so canvas-measured fake caret stays aligned); webfonts via Google Fonts `display=swap` link (JetBrains Mono 400/800, IBM Plex Mono 400/700, Space Mono 400/700) with system-mono fallbacks.
- Persists in `localStorage 'node-font-idx'` (validated int, applied on load), click shows `Font: <name>` in `#status` for ~1.2s then `updateStatus()` restores; Alt peek adds `font-btn` badge.
- Kept: mono colors, drill, paging, arrows, validation, prune, crumbs badge, primary/ghost, hot reload, ripple off.

## [v0.0.40] - 2026-09-13 - Crumb toggle depth badge
- `#crumb-toggle-btn` gets tiny `#crumb-count` badge (`absolute -4px` top-right, `12px` circle, mono `9px/12px`, filled black/white text light, inverted dark, `pointer-events:none` on ghost button): shows depth level `= crumbPath().length` (`1,2,...` inside, cleared at root where toggle is hidden), updated in `updateNav`.
- Kept: mono, per-letter glow, shrink/lift, drill, paging, arrows, validation, prune, crumbs toggle, Alt peek, hot reload, ripple off.

## [v0.0.39] - 2026-09-13 - Lighten unfocused dim
- `.root-node` unfocused `opacity:0.5` -> `0.75` (v0.0.38 too dim); `:focus-within`/`:hover`/`:active` still `opacity:1`, `transition: opacity 0.18s ease` unchanged.
- Kept: mono, per-letter glow, shrink/lift, drill, paging, arrows, validation, prune, Alt peek, hot reload, ripple off.

## [v0.0.38] - 2026-09-13 - Dim unfocused nodes
- `.root-node` defaults to `opacity:0.5` with `transition: opacity 0.18s ease`; `:focus-within`/`:hover`/`:active` restores `opacity:1` so only the focused/hovered/active node is full-strength (solid/input inherit via container compositing, inner blur/unblur opacities still multiply).
- Kept: mono, per-letter glow, shrink/lift, drill, paging, arrows, validation, prune, Alt peek, hot reload, ripple off.

## [v0.0.37] - 2026-09-13 - Per-letter focus glow, no container box
- Removed container `box-shadow` on focus (`.solid-text:focus`, `.root-input:focus`, `.root-node:focus` now `box-shadow:none`): no invisible-box look.
- Focus cue keeps tiny shrink `scale(0.98)` + lift `translateY(-2px)` on the container (`outline:none`, 8px radius kept).
- Glow moved to each letter: `.solid-text:focus .letter` adds `0 2px 6px rgba(0,0,0,0.25)` on top of the engraved shadow light / `rgba(255,255,255,0.25)` dark, `0.18s` `text-shadow` transition on `.letter`.
- `.root-input:focus` (single element) also uses `text-shadow` glow instead of `box-shadow`; container transitions switched `box-shadow` -> `text-shadow`.
- Kept: mono, primary/ghost, drill, paging, arrows incl Right/Left, stepFocus nav, validation, prune, crumbs toggle, Alt peek, hot reload, ripple off.

## [v0.0.36] - 2026-09-13 - Subtle focus shrink+glow, no ring
- Removed keyboard focus rings (`.solid-text:focus` / `.root-input:focus-visible` 2px `currentColor` outline): focused states now `outline:none`, no border.
- Focused node cue (input + solid): tiny shrink `scale(0.98)`, lift `translateY(-2px)`, soft glow `box-shadow 0 4px 12px rgba(0,0,0,0.12)` light / `rgba(255,255,255,0.12)` dark, `0.18s` transition, 8px radius.
- Input uses individual `scale`/`translate` props under `@supports` so the cue composes with (not overridden by) the `grow`/`edit-pop` `transform` fill animations; older engines fall back to `transform`.
- Kept: mono, primary/ghost, drill, paging, arrows incl Right/Left, stepFocus nav, validation, prune, crumbs toggle, Alt peek, hot reload, ripple off.

## [v0.0.35] - 2026-09-13 - ArrowLeft back to parent
- Global `keydown` `ArrowLeft` (same guard as up/down/right: skips Alt/Ctrl/Meta, `TEXTAREA`, non-empty `INPUT` caret): when inside (`currentParentId != null`) calls `goBack()` (up one level, same as bottom `‹` back button); at root does nothing.
- Kept: mono, primary/ghost hierarchy, drill, paging, arrows up/down/right, validation, prune, crumbs toggle, home/back-bottom, Alt peek, hot reload, ripple off.

## [v0.0.34] - 2026-09-13 - ArrowRight drills inside focused node
- Global `keydown` `ArrowRight` (same guard as up/down: skips Alt/Ctrl/Meta, `TEXTAREA`, non-empty `INPUT` caret): `openFocusedNode()` resolves focused `.root-node` via `data-node-id` (fallback `data-idx` -> `nodeIdAt`) and calls `navigateTo(id)`, same as clicking `›`.
- Only solids with a word drill; empty waiting boxes shake via `shakeInput` and stay; focus outside the list does nothing.
- Kept: mono, primary/ghost hierarchy, drill, paging, arrows up/down, validation, prune, crumbs toggle, home/back-bottom, Alt peek, hot reload, ripple off.

## [v0.0.33] - 2026-09-13 - Button hierarchy: sole primary add, rest ghost
- `#add-node-btn` is the only primary: filled black/white text light (white/black text dark), bold (`font-weight:800`), keeps 24px + bounce.
- Default/ghost (transparent, 1px mono border, no fill): `.pager-btn`, `#home-btn`, `#level-back-btn`, `#crumb-toggle-btn`, `.open-btn` — black border/text light, white border/text dark; hover `#eee` light / `#222` dark; same sizes/positions.
- Kept: focus rings, mono, darkmode, drill, paging, arrows, validation, prune, crumbs toggle, Alt peek, hot reload, ripple off.

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
