"""Shared helpers for the sample product interfaces (written to public/demo/*.html by build.py).

All names, numbers and brands are made up. Every page says "sample data".
"""
import math
import pathlib

OUT = pathlib.Path(__file__).resolve().parent.parent / "public" / "demo"

ICONS = {
    "grid": '<rect x="3" y="3" width="7" height="7" rx="1.5"/><rect x="14" y="3" width="7" height="7" rx="1.5"/><rect x="3" y="14" width="7" height="7" rx="1.5"/><rect x="14" y="14" width="7" height="7" rx="1.5"/>',
    "calendar": '<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/>',
    "bed": '<path d="M3 18V7M3 14h18v4M21 14v-2a3 3 0 0 0-3-3h-7v5"/><circle cx="7" cy="11" r="1.5"/>',
    "spark": '<path d="M12 3l1.8 5.2L19 10l-5.2 1.8L12 17l-1.8-5.2L5 10l5.2-1.8z"/>',
    "receipt": '<path d="M6 3h12v18l-3-2-3 2-3-2-3 2z"/><path d="M9 8h6M9 12h6"/>',
    "users": '<circle cx="9" cy="8" r="3.5"/><path d="M2.5 20c.6-3.4 3.2-5 6.5-5s5.9 1.6 6.5 5"/><path d="M16 5a3.2 3.2 0 0 1 0 6M18 15c2 .5 3.2 2 3.5 5"/>',
    "chart": '<path d="M4 20V4M4 20h16"/><path d="M8 16l4-5 3 3 5-7"/>',
    "box": '<path d="M3 7l9-4 9 4v10l-9 4-9-4z"/><path d="M3 7l9 4 9-4M12 11v10"/>',
    "cart": '<circle cx="9" cy="20" r="1.6"/><circle cx="18" cy="20" r="1.6"/><path d="M2 3h3l2.6 12h11l2-8H6.5"/>',
    "settings": '<circle cx="12" cy="12" r="3"/><path d="M12 2v3M12 19v3M2 12h3M19 12h3M4.9 4.9l2.1 2.1M17 17l2.1 2.1M4.9 19.1L7 17M17 7l2.1-2.1"/>',
    "bell": '<path d="M6 16V11a6 6 0 0 1 12 0v5l2 2H4z"/><path d="M10 21h4"/>',
    "search": '<circle cx="11" cy="11" r="7"/><path d="M20 20l-4-4"/>',
    "truck": '<path d="M2 6h12v10H2zM14 9h4l4 4v3h-8"/><circle cx="7" cy="17.5" r="1.8"/><circle cx="17" cy="17.5" r="1.8"/>',
    "utensils": '<path d="M5 3v8a2 2 0 0 0 2 2v8M9 3v8M7 3v8M17 3c-2 2-3 5-3 8h3v10"/>',
    "flame": '<path d="M12 3c1 4 5 5 5 10a5 5 0 0 1-10 0c0-2 1-3 2-4 0 2 1 3 2 3 0-4-1-6 1-9z"/>',
    "tag": '<path d="M3 12V4h8l10 10-8 8z"/><circle cx="7.5" cy="8.5" r="1.3"/>',
    "wallet": '<path d="M3 7h16a2 2 0 0 1 2 2v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><path d="M3 7l12-3v3M17 14h2"/>',
    "plus": '<path d="M12 5v14M5 12h14"/>',
    "filter": '<path d="M3 5h18l-7 8v6l-4-2v-4z"/>',
    "download": '<path d="M12 3v12m0 0l-4-4m4 4l4-4M4 21h16"/>',
    "home": '<path d="M3 11l9-8 9 8M5 10v10h14V10"/>',
    "key": '<circle cx="8" cy="15" r="4"/><path d="M11 12l9-9M16 7l3 3"/>',
    "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
    "layers": '<path d="M12 3l9 5-9 5-9-5z"/><path d="M3 13l9 5 9-5"/>',
    "check": '<path d="M5 12l5 5 9-10"/>',
    "star": '<path d="M12 3l2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1L3.2 9.5l6.1-.9z"/>',
    "globe": '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3 3 3 15 0 18M12 3c-3 3-3 15 0 18"/>',
    "edit": '<path d="M4 20h4L19 9l-4-4L4 16z"/>',
    "eye": '<path d="M2 12s4-7 10-7 10 7 10 7-4 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/>',
}


def icon(name):
    return f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[name]}</svg>'


STATUS = '<div class="statusbar"><span>10:24</span><span><svg viewBox="0 0 18 11"><rect x="0" y="7" width="3" height="4" rx="1" fill="#0c1d35"/><rect x="5" y="5" width="3" height="6" rx="1" fill="#0c1d35"/><rect x="10" y="2.5" width="3" height="8.5" rx="1" fill="#0c1d35"/><rect x="15" y="0" width="3" height="11" rx="1" fill="#0c1d35"/></svg><svg viewBox="0 0 28 12"><rect x=".5" y=".5" width="23" height="11" rx="3.5" fill="none" stroke="#0c1d35" opacity=".5"/><rect x="2" y="2" width="18" height="8" rx="2" fill="#0c1d35"/><rect x="25" y="4" width="2" height="4" rx="1" fill="#0c1d35" opacity=".5"/></svg></span></div>'

COLORS = ["#038d91", "#3b6fd4", "#7a5bd1", "#d9822b", "#d6504b", "#1f9d6b", "#14284a", "#c2569b"]


def av(name, i=None):
    parts = name.split()
    ini = (parts[0][0] + (parts[1][0] if len(parts) > 1 else "")).upper()
    c = COLORS[(sum(map(ord, name)) if i is None else i) % len(COLORS)]
    return f'<span class="av" style="background:{c}">{ini}</span>'


def who(name, sub=None):
    s = f'<span><b style="font-weight:600">{name}</b>' + (f'<small class="muted" style="display:block;font-size:10.5px">{sub}</small>' if sub else "") + "</span>"
    return f'<span class="who">{av(name)}{s}</span>'


def chip(t, c=""):
    return f'<span class="chip {c}">{t}</span>'


def stat(label, value, delta, down=False, ic=None):
    i = f'<span class="ico">{icon(ic)}</span>' if ic else ""
    return f'<div class="card stat"><small>{label}{i}</small><b>{value}</b><em class="{"d" if down else ""}">{delta}</em></div>'


def rows(items):
    return "".join(f'<div class="row"><span>{a}</span><span>{b}</span></div>' for a, b in items)


def bars(vals, labels=None, hi=None, h=None):
    m = max(vals)
    out = '<div class="bars"' + (f' style="height:{h}px"' if h else "") + ">"
    for i, v in enumerate(vals):
        cls = ' class="m"' if hi is not None and i != hi else ""
        out += f'<i{cls} style="height:{round(v / m * 100)}%;animation-delay:{i * 40}ms"></i>'
    out += "</div>"
    if labels:
        out += '<div class="axis">' + "".join(f"<span>{l}</span>" for l in labels) + "</div>"
    return out


_uid = [0]


def _smooth(pts):
    if len(pts) < 3:
        return "M" + " L".join(f"{x:.1f} {y:.1f}" for x, y in pts)
    d = f"M{pts[0][0]:.1f} {pts[0][1]:.1f}"
    for i in range(len(pts) - 1):
        p0 = pts[i - 1] if i > 0 else pts[i]
        p1, p2 = pts[i], pts[i + 1]
        p3 = pts[i + 2] if i + 2 < len(pts) else p2
        c1 = (p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6)
        c2 = (p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6)
        d += f" C{c1[0]:.1f} {c1[1]:.1f} {c2[0]:.1f} {c2[1]:.1f} {p2[0]:.1f} {p2[1]:.1f}"
    return d


def line_chart(series, w=640, h=190, fill=True, grid=4, ymax=None, labels=None, gridc="#e3e8ef"):
    """series: list of (values, color). Returns an SVG chart plus optional x labels."""
    _uid[0] += 1
    uid = _uid[0]
    top = ymax or max(max(v) for v, _ in series) * 1.12
    pad = 6
    out = f'<svg class="chart" viewBox="0 0 {w} {h}" preserveAspectRatio="none" role="img" aria-hidden="true">'
    out += "<defs>" + "".join(f'<linearGradient id="g{uid}{k}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{c}" stop-opacity=".28"/><stop offset="1" stop-color="{c}" stop-opacity="0"/></linearGradient>' for k, (_, c) in enumerate(series)) + "</defs>"
    for g in range(grid + 1):
        y = pad + (h - 2 * pad) * g / grid
        out += f'<line x1="0" x2="{w}" y1="{y:.1f}" y2="{y:.1f}" stroke="{gridc}" stroke-width="1"/>'
    for k, (vals, c) in enumerate(series):
        n = len(vals)
        pts = [(i * w / (n - 1), pad + (h - 2 * pad) * (1 - v / top)) for i, v in enumerate(vals)]
        path = _smooth(pts)
        if fill:
            out += f'<path d="{path} L{w} {h} L0 {h} Z" fill="url(#g{uid}{k})"/>'
        out += f'<path d="{path}" fill="none" stroke="{c}" stroke-width="2.4" stroke-linecap="round" vector-effect="non-scaling-stroke"/>'
    out += "</svg>"
    if labels:
        out += '<div class="axis">' + "".join(f"<span>{l}</span>" for l in labels) + "</div>"
    return out


def donut(parts, size=120, thick=15, center=None, sub=None, track="#e6ebf2"):
    """parts: list of (value, color, label). center: big text in the middle."""
    r = (size - thick) / 2
    c = 2 * math.pi * r
    tot = sum(p[0] for p in parts)
    out = f'<svg viewBox="0 0 {size} {size}" role="img" aria-hidden="true"><circle cx="{size / 2}" cy="{size / 2}" r="{r}" fill="none" stroke="{track}" stroke-width="{thick}"/>'
    off = 0
    for v, color, _ in parts:
        ln = c * v / tot
        out += f'<circle cx="{size / 2}" cy="{size / 2}" r="{r}" fill="none" stroke="{color}" stroke-width="{thick}" stroke-dasharray="{max(ln - 2, 0):.1f} {c - max(ln - 2, 0):.1f}" stroke-dashoffset="{-off:.1f}" transform="rotate(-90 {size / 2} {size / 2})" stroke-linecap="butt"/>'
        off += ln
    if center:
        out += f'<text x="50%" y="{"46%" if sub else "52%"}" text-anchor="middle" dominant-baseline="middle" font-size="{size * 0.2:.0f}" font-weight="700" fill="currentColor">{center}</text>'
        if sub:
            out += f'<text x="50%" y="63%" text-anchor="middle" font-size="{size * 0.085:.0f}" fill="#8a97ab">{sub}</text>'
    return out + "</svg>"


def donut_block(parts, **kw):
    leg = "".join(f'<div><span><i class="dot" style="background:{c}"></i>{l}</span><b>{v}</b></div>' for v, c, l in parts)
    return f'<div class="donut-wrap">{donut(parts, **kw)}<div class="donut-leg">{leg}</div></div>'


def ring(pct, color="#038d91", size=150, thick=14, label="", track="#e3e9f0"):
    r = (size - thick) / 2
    c = 2 * math.pi * r
    return (
        f'<svg viewBox="0 0 {size} {size}" width="{size}" height="{size}" role="img" aria-hidden="true"><circle cx="{size / 2}" cy="{size / 2}" r="{r}" fill="none" stroke="{track}" stroke-width="{thick}"/>'
        f'<circle cx="{size / 2}" cy="{size / 2}" r="{r}" fill="none" stroke="{color}" stroke-width="{thick}" stroke-linecap="round" stroke-dasharray="{c * pct / 100:.1f} {c:.1f}" transform="rotate(-90 {size / 2} {size / 2})"/>'
        f'<text x="50%" y="48%" text-anchor="middle" dominant-baseline="middle" font-size="{size * 0.24:.0f}" font-weight="700" fill="currentColor">{pct}%</text>'
        f'<text x="50%" y="66%" text-anchor="middle" font-size="{size * 0.08:.0f}" fill="#8a97ab">{label}</text></svg>'
    )


def spark(vals, color="#038d91", w=90, h=28):
    top, lo = max(vals), min(vals)
    pts = [(i * w / (len(vals) - 1), 3 + (h - 6) * (1 - (v - lo) / ((top - lo) or 1))) for i, v in enumerate(vals)]
    return f'<svg viewBox="0 0 {w} {h}" width="{w}" height="{h}" aria-hidden="true"><path d="{_smooth(pts)}" fill="none" stroke="{color}" stroke-width="2" stroke-linecap="round"/></svg>'


def _views_html(views):
    out = ""
    for key, title, subtitle, acts, body in views:
        out += (
            f'<section data-v="{key}"><header class="head"><div><h1 data-title>{title}</h1><p>{subtitle}</p></div><div class="acts">{acts}</div></header>'
            f'<div class="viewport"><div class="scroller">{body}</div></div></section>\n'
        )
    return out


def _tabbar(tabs):
    return '<nav class="tabbar">' + "".join(f'<a data-nav="{k}" href="#{k}">{icon(i)}{l}</a>' for k, l, i in tabs) + "</nav>"


def _doc(title, theme, extra_css, body):
    css = '<link rel="stylesheet" href="base.css">' + "".join(f'<link rel="stylesheet" href="{c}">' for c in extra_css)
    return (
        f'<!doctype html>\n<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">'
        f'<meta name="robots" content="noindex"><title>{title} (sample interface)</title>{css}</head>\n<body class="{theme}">{body}<script src="app.js"></script></body></html>\n'
    )


def topbar(user, placeholder="Search guests, bookings, rooms"):
    return (
        f'<div class="topbar"><div class="search">{icon("search")}{placeholder}</div><div class="sp"></div><span class="tag">SAMPLE DATA</span>'
        f'<div class="icon-btn">{icon("bell")}<i></i></div><span class="who">{av(user)}<span style="font-weight:600;font-size:12px">{user}</span></span></div>'
    )


def shell_side(name, sub, nav, tabs, user, views, search="Search guests, bookings, rooms", theme="theme-pms", extra_css=(), org="Sea Breeze Resort"):
    """PMS shell: wide navy sidebar, light workspace."""
    side = ""
    for it in nav:
        if it[0] == "h":
            side += f'<div class="nav-h">{it[1]}</div>'
            continue
        key, label, ic = it[0], it[1], it[2]
        badge = f'<span class="n">{it[3]}</span>' if len(it) > 3 else ""
        side += f'<a {"data-nav=" + chr(34) + key + chr(34) + " href=" + chr(34) + "#" + key + chr(34) if key else "href=" + chr(34) + "#" + chr(34)}>{icon(ic)}{label}{badge}</a>'
    body = (
        f'<div class="app"><aside class="side"><div class="brand"><img src="/brand/petra-mark.png" alt=""><div>{name.upper()}<small>{sub}</small></div></div>{side}<div class="sp"></div>'
        f'<div class="user">{av(user)}<div>{user}<br><span style="color:#8fa3c2;font-size:11px">{org}</span></div></div></aside>'
        f'<div class="main">{STATUS}{topbar(user, search)}{_views_html(views)}</div>{_tabbar(tabs)}</div>'
    )
    return _doc(name, theme, list(extra_css), body)


def shell_top(name, tabs_nav, tabs, user, views, extra_css=()):
    """POS shell: dark, touch-first, top bar navigation."""
    nav = "".join(f'<a data-nav="{k}" href="#{k}">{icon(i)}{l}</a>' for k, l, i in tabs_nav)
    body = (
        f'<div class="app"><header class="ptop"><div class="brand"><img src="/brand/petra-mark.png" alt=""><div>{name.upper()}</div></div><nav>{nav}</nav><div class="sp"></div>'
        f'<span class="tag">SAMPLE DATA</span><span class="chip ok"><i class="live"></i>Shift open</span><div class="clock"><b>7:42 PM</b>Thu 6 Nov</div>{av(user)}</header>'
        f'<div class="main">{STATUS}{_views_html(views)}</div>{_tabbar(tabs)}</div>'
    )
    return _doc(name, "theme-pos", list(extra_css), body)


def shell_rail(name, rail, menu, tabs, user, views, crumbs=("Distribution", "Dashboard")):
    """DMS shell: narrow icon rail plus a module menu bar, dense workspace."""
    r = f'<img src="/brand/petra-mark.png" alt="">' + "".join(
        f'<a {"data-nav=" + chr(34) + k + chr(34) + " href=" + chr(34) + "#" + k + chr(34) if k else "href=" + chr(34) + "#" + chr(34)} title="{l}">{icon(i)}</a>' for k, l, i in rail
    )
    m = "".join(f'<a {"data-nav=" + chr(34) + k + chr(34) + " href=" + chr(34) + "#" + k + chr(34) if k else "href=" + chr(34) + "#" + chr(34)}>{l}</a>' for k, l in menu)
    body = (
        f'<div class="app"><aside class="rail">{r}<div class="sp"></div><a href="#">{icon("settings")}</a></aside>'
        f'<div class="col"><header class="menubar"><b>{name.upper()}</b>{m}<div class="sp"></div><div class="field">{icon("search")}Search invoice, customer, item</div><span class="tag" style="margin-left:8px">SAMPLE DATA</span><span class="who" style="margin-left:10px">{av(user)}</span></header>'
        f'<div class="crumbs"><span>{crumbs[0]} / <b style="color:var(--ink)">{crumbs[1]}</b></span><span>Branch: Main warehouse · FY 2026-27</span></div>'
        f'<div class="main">{STATUS}{_views_html(views)}</div></div>{_tabbar(tabs)}</div>'
    )
    return _doc(name, "theme-dms", [], body)


def write(name, html):
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / name).write_text(html)
    print("wrote", name, len(html) // 1024, "KB")


def shell_plain(name, theme, sections, extra_css=("sites.css",)):
    """Full-bleed pages (sample websites, builder): no app chrome of their own."""
    body = f'<div class="app" style="display:block"><div class="main" style="height:100vh">{STATUS}{sections}</div></div>'
    return _doc(name, theme, list(extra_css), body)


def site_view(key, cls, nav_html, page_html, title):
    """One sample website: a fixed top bar, then a page that scrolls on its own."""
    return (
        f'<section data-v="{key}" class="site-view {cls}"><span data-title hidden>{title}</span>{nav_html}'
        f'<div class="viewport" style="padding:0"><div class="scroller" style="padding:0">{page_html}</div></div><span class="s-tag">SAMPLE WEBSITE</span></section>\n'
    )
