# Frontend Design System

One source of truth for the dashboard UI. **Before writing any Tailwind classes,
reuse a primitive or copy a sibling component's classes. Never invent widths,
colors, or arbitrary values.**

## Where things live

- **Design tokens** — `dashboard/frontend/app/globals.css` under `@theme`. Colors,
  the 5-tier type scale, and animations are all defined here.
- **UI primitives** — `dashboard/frontend/components/ui/`. Reusable building blocks:
  `Button`, `Tag`, `Badge` (`StatusBadge`), `ModelBadge`, `ListRow`, `RepoSelector`,
  `ModelSelector`, `CopyButton`, etc.
- **Constants** (labels, maxlengths, provider lists) — `dashboard/frontend/lib/constants.ts`.

## Type scale (use these, not raw `text-[13px]`)

| Class          | Size | Use                                   |
| -------------- | ---- | ------------------------------------- |
| `text-title`   | 14px | Section / card titles                 |
| `text-body`    | 13px | Body copy                             |
| `text-content` | 12px | Default UI text (rows, inputs, labels)|
| `text-meta`    | 11px | Secondary metadata                    |
| `text-caption` | 10px | Chips, tags, tiny labels              |

## Color tokens

Text: `text` · `text-secondary` · `text-muted` · `text-dim` · `accent` · `accent-hover`.
Surfaces: `bg` · `bg-card` · `bg-hover` · `bg-input` · `bg-elevated`.
Borders: `border` · `border-hover` · `border-active` · `border-subtle` · `border-muted`.
Semantic: `success` (#00ff88) · `warning` (#ffaa00) · `error` (#ff4444) · `info` (#88ccff).

> **Known debt:** many existing components hardcode the semantic hexes inline
> (e.g. `text-[#00ff88]`) instead of `text-success`, and use arbitrary values
> like `bg-black/30`. This is being tracked as a separate frontend cleanup +
> lint-enforcement refactor. For **new** code, prefer the tokens above; when
> editing an existing component, match whatever that component already does so a
> single file stays internally consistent.

## Common patterns (copy these — don't reinvent)

**Chip / tag** — use the `<Tag>` primitive, never hand-write the classes:

```tsx
import { Tag } from "@/components/ui/Tag";
<Tag>Anthropic</Tag>
```

`ModelBadge` and the provider chip both render `<Tag>` — it is the single source
of chip styling (`bg-white/[0.04]`, `text-caption`, `px-1.5 py-0`, rounded).

**List row** — settings lists (tokens, repos, sandboxes) use `<ListRow>`; columns
are content-sized flex children (`shrink-0` for fixed content, `flex-1 min-w-0
truncate` for the growing column). Do not add fixed pixel widths to line up
columns — the app sizes to content.

**Text input** — the canonical settings input:

```
bg-black/30 border border-border rounded px-3 py-2 text-content text-accent-hover
placeholder:text-text-secondary focus-visible:outline-none
focus-visible:border-[#00ff88]/30 focus-visible:ring-1 focus-visible:ring-[#00ff88]/40
transition-all
```

An inline-edit input and its add-form counterpart must share these classes so
adding and editing look identical.

**Dropdown selector** — model the structure on `RepoSelector` / `ProviderSelector`
(button → animated `framer-motion` listbox, `w-1.5 h-1.5` active dot, checkmark,
`bg-white/[0.04]` hover, `bg-bg-card` panel).

**Empty cell** — render an em-dash `—` in `text-text-dim`, not "N/A" or a blank.

## Rule of thumb

If you're about to type `w-24`, `bg-black/20`, `#00ff88`, or `text-center` into a
component: stop. Either a primitive already does it, or a sibling component in the
same folder already has the exact classes to copy. Guessing produces drift.
