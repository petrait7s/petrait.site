"""Hand-made SVG illustrations for the sample websites and stores (no stock photos, no licences)."""

_n = [0]


def _id(p):
    _n[0] += 1
    return f"{p}{_n[0]}"


def _wrap(inner, defs="", vb="0 0 800 480"):
    return f'<svg class="art" viewBox="{vb}" preserveAspectRatio="xMidYMid slice" aria-hidden="true"><defs>{defs}</defs>{inner}</svg>'


def resort():
    s, w = _id("s"), _id("w")
    defs = (
        f'<linearGradient id="{s}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffd9a0"/><stop offset=".5" stop-color="#ff9f80"/><stop offset="1" stop-color="#7fc9d8"/></linearGradient>'
        f'<linearGradient id="{w}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#27b0bf"/><stop offset="1" stop-color="#0a5f78"/></linearGradient>'
    )
    waves = "".join(f'<path d="M0 {y} q50 -12 100 0 t100 0 t100 0 t100 0 t100 0 t100 0 t100 0 t100 0" fill="none" stroke="#fff" stroke-opacity="{o}" stroke-width="2.5"/>' for y, o in [(318, .35), (344, .28), (376, .22), (410, .16)])
    glints = "".join(f'<rect x="{560 - wd / 2}" y="{y}" width="{wd}" height="4" rx="2" fill="#fff3d6" opacity=".55"/>' for y, wd in [(302, 110), (318, 84), (336, 64), (356, 44), (378, 28)])
    fronds = "".join(f'<path d="M175 262 C{175 + dx1} {262 + dy1} {175 + dx2} {262 + dy2} {175 + dx3} {262 + dy3} C{175 + dx2} {262 + dy2 - 16} {175 + dx1} {262 + dy1 - 10} 175 262Z" fill="{c}"/>' for dx1, dy1, dx2, dy2, dx3, dy3, c in [(-50, -34, -96, -20, -128, 22, "#1d6b4a"), (-20, -62, -40, -78, -48, -40, "#2c8a5e"), (30, -52, 70, -62, 112, -28, "#1d6b4a"), (60, -14, 100, 6, 128, 46, "#2c8a5e"), (-60, 6, -108, 30, -126, 70, "#25784f")])
    inner = (
        f'<rect width="800" height="480" fill="url(#{s})"/><circle cx="560" cy="200" r="120" fill="#fff3d6" opacity=".18"/><circle cx="560" cy="200" r="64" fill="#fff3d6"/>'
        '<path d="M0 282 Q110 236 230 276 T470 268 T800 262 V320 H0Z" fill="#3b7f8f" opacity=".55"/>'
        f'<rect y="296" width="800" height="184" fill="url(#{w})"/>{glints}{waves}'
        '<path d="M0 440 Q200 408 400 430 T800 418 V480 H0Z" fill="#f2d9a8"/><path d="M0 462 Q220 440 440 456 T800 448 V480 H0Z" fill="#e9c98c"/>'
        '<path d="M118 476 C128 410 140 340 175 262" stroke="#5a3a22" stroke-width="10" fill="none" stroke-linecap="round"/>'
        f'{fronds}<circle cx="168" cy="278" r="6" fill="#7a4a2b"/><circle cx="182" cy="282" r="6" fill="#7a4a2b"/>'
        '<path d="M640 470 l12 -46 l12 46z" fill="#fff" opacity=".0"/><path d="M690 290 l16 -26 l16 26z" fill="#fff" opacity=".9"/><path d="M706 264 v-18" stroke="#fff" stroke-width="2"/>'
    )
    return _wrap(inner, defs)


def food():
    g = _id("f")
    defs = f'<radialGradient id="{g}" cx=".7" cy=".45" r=".9"><stop offset="0" stop-color="#5a2b17"/><stop offset=".6" stop-color="#27120a"/><stop offset="1" stop-color="#120805"/></radialGradient>'
    steam = "".join(f'<path d="M{x} {y} c-14 -18 14 -30 0 -50 c-12 -16 10 -28 0 -44" fill="none" stroke="#fff" stroke-opacity=".28" stroke-width="5" stroke-linecap="round"/>' for x, y in [(520, 150), (566, 140), (612, 152)])
    herbs = "".join(f'<ellipse cx="{x}" cy="{y}" rx="9" ry="4.5" fill="#5fae4a" transform="rotate({r} {x} {y})"/>' for x, y, r in [(530, 238, 20), (592, 224, -30), (560, 262, 60), (618, 262, 10), (516, 276, -40)])
    inner = (
        f'<rect width="800" height="480" fill="url(#{g})"/><circle cx="570" cy="250" r="196" fill="#f3efe6"/><circle cx="570" cy="250" r="170" fill="#e8e1d2"/><circle cx="570" cy="250" r="128" fill="#c96a1f"/>'
        '<path d="M470 250c20 -42 80 -64 130 -44 40 16 56 54 40 90 -24 -30 -62 -44 -100 -34 -30 8 -52 -4 -70 -12z" fill="#e8a24a" opacity=".85"/><circle cx="548" cy="268" r="14" fill="#a64b1e" opacity=".45"/><circle cx="604" cy="246" r="10" fill="#a64b1e" opacity=".4"/>'
        f'{herbs}{steam}'
        '<circle cx="270" cy="340" r="88" fill="#f6f1e3"/><path d="M196 336a74 62 0 0 1 148 0z" fill="#fffdf6"/><circle cx="270" cy="336" r="64" fill="none" stroke="#e6dfd0" stroke-width="3"/>'
        '<path d="M392 392c14 -26 40 -34 62 -26-10 22 -32 36 -62 26z" fill="#d6332a"/><path d="M450 366c8 -8 16 -10 22 -8" stroke="#2a8a3a" stroke-width="5" fill="none" stroke-linecap="round"/>'
        '<path d="M96 120 L104 380" stroke="#d8dde6" stroke-width="12" stroke-linecap="round"/><path d="M60 120 l0 70 a14 14 0 0 0 28 0 l0 -70" fill="none" stroke="#d8dde6" stroke-width="7" stroke-linecap="round"/>'
        '<ellipse cx="190" cy="420" rx="40" ry="18" fill="#000" opacity=".25"/>'
    )
    return _wrap(inner, defs)


def tour():
    g = _id("t")
    defs = f'<linearGradient id="{g}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#16314f"/><stop offset=".55" stop-color="#5c7aa6"/><stop offset="1" stop-color="#f0a47e"/></linearGradient>'
    pines = "".join(f'<path d="M{x} {y} l{s} {-s * 2.2} l{s} {s * 2.2}z M{x + 4} {y - s} l{s - 4} {-s * 2} l{s - 4} {s * 2}z" fill="#10351f"/>' for x, y, s in [(40, 470, 26), (88, 480, 20), (680, 474, 28), (740, 482, 22), (610, 480, 18)])
    inner = (
        f'<rect width="800" height="480" fill="url(#{g})"/><circle cx="170" cy="150" r="46" fill="#fff4d8" opacity=".95"/><circle cx="170" cy="150" r="82" fill="#fff4d8" opacity=".14"/>'
        '<path d="M0 330 L120 220 L190 280 L300 160 L420 300 L520 210 L640 310 L720 240 L800 300 V480 H0Z" fill="#2c4a73"/>'
        '<path d="M300 160 L270 196 L292 188 L304 206 L322 186 L346 196z" fill="#fff"/><path d="M520 210 L498 238 L516 232 L526 246 L540 230 L556 238z" fill="#fff" opacity=".95"/>'
        '<path d="M0 380 L90 300 L170 350 L280 270 L400 360 L520 290 L640 370 L800 310 V480 H0Z" fill="#1b3558"/>'
        '<path d="M0 430 Q200 380 380 430 T800 410 V480 H0Z" fill="#12291f"/><path d="M360 480 C380 450 400 440 430 420 C470 400 520 400 560 380" stroke="#9fd8e6" stroke-width="12" fill="none" stroke-linecap="round" opacity=".75"/>'
        f'{pines}<path d="M300 466 l22 -36 l22 36z" fill="#e8c27a"/><path d="M322 430 v-12" stroke="#8a5a2b" stroke-width="3"/><circle cx="322" cy="468" r="4" fill="#d6504b"/>'
    )
    return _wrap(inner, defs)


def fashion_hero():
    g = _id("h")
    defs = f'<linearGradient id="{g}" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#f7e4dc"/><stop offset="1" stop-color="#e7d4f0"/></linearGradient>'
    inner = (
        f'<rect width="800" height="480" fill="url(#{g})"/><circle cx="600" cy="230" r="190" fill="#fff" opacity=".45"/><circle cx="170" cy="120" r="70" fill="#f2b8a8" opacity=".5"/>'
        '<path d="M380 120 L420 96 Q440 120 470 96 L510 120 L520 150 Q500 190 520 240 L560 420 H330 L368 240 Q392 190 372 150Z" fill="#c2569b"/><path d="M420 96 Q440 126 470 96" fill="none" stroke="#a63f82" stroke-width="5"/><path d="M372 240 Q445 262 520 240" fill="none" stroke="#e9a0cf" stroke-width="5"/>'
        '<path d="M120 190 L168 164 Q196 186 224 164 L272 190 L300 270 L262 290 L256 250 V420 H138 V250 L132 290 L94 270Z" fill="#14284a"/><path d="M196 186 V420" stroke="#2a4a7a" stroke-width="4"/><circle cx="196" cy="230" r="5" fill="#8db0f0"/><circle cx="196" cy="280" r="5" fill="#8db0f0"/><circle cx="196" cy="330" r="5" fill="#8db0f0"/>'
        '<path d="M600 190 L646 168 Q668 186 690 168 L736 190 L762 262 L728 280 L722 252 V420 H614 V252 L608 280 L574 262Z" fill="#f2c94c"/><path d="M646 168 Q668 196 690 168" fill="none" stroke="#d8a92a" stroke-width="5"/>'
        '<ellipse cx="450" cy="440" rx="190" ry="14" fill="#000" opacity=".08"/>'
    )
    return _wrap(inner, defs)


def decor_hero():
    g = _id("d")
    defs = f'<linearGradient id="{g}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f1e6d6"/><stop offset="1" stop-color="#d8c2a2"/></linearGradient>'
    leaves = "".join(f'<path d="M180 270 C{180 + dx} {270 + dy} {180 + dx2} {270 + dy2} 180 270Z" fill="{c}"/>' for dx, dy, dx2, dy2, c in [(-90, -90, -30, -150, "#3f8a5a"), (-20, -130, 40, -170, "#2f7a4a"), (60, -90, 120, -120, "#4a9a68"), (-70, -40, -130, -60, "#2f7a4a"), (80, -30, 140, -20, "#3f8a5a")])
    inner = (
        f'<rect width="800" height="480" fill="url(#{g})"/><rect x="0" y="360" width="800" height="120" fill="#b89268" opacity=".55"/><rect x="60" y="300" width="400" height="16" rx="6" fill="#8a6a46"/>'
        f'<path d="M150 300 C130 270 138 230 160 218 L200 218 C222 230 230 270 210 300Z" fill="#038d91"/><rect x="160" y="206" width="40" height="14" rx="5" fill="#026f73"/>{leaves}'
        '<path d="M300 300 L316 230 H382 L398 300Z" fill="#f2b84b"/><path d="M308 232 H390 L396 218 H302Z" fill="#e8a02a"/><path d="M349 218 V150" stroke="#6b5a3a" stroke-width="6"/><circle cx="349" cy="142" r="14" fill="#fff3c8"/><circle cx="349" cy="142" r="40" fill="#fff3c8" opacity=".25"/>'
        '<rect x="520" y="130" width="190" height="260" rx="95" fill="#f7f1e6" stroke="#b89268" stroke-width="12"/><rect x="540" y="150" width="150" height="220" rx="75" fill="#cfe3e6"/><path d="M570 330 q60 -80 90 -150" stroke="#fff" stroke-opacity=".5" stroke-width="10" fill="none" stroke-linecap="round"/>'
        '<rect x="470" y="372" width="260" height="22" rx="8" fill="#a8825a"/><circle cx="560" cy="420" r="30" fill="#c2569b"/><circle cx="640" cy="424" r="26" fill="#14284a"/>'
    )
    return _wrap(inner, defs)


def gadget_hero():
    g = _id("g")
    defs = (
        f'<radialGradient id="{g}" cx=".65" cy=".4" r=".9"><stop offset="0" stop-color="#3b2a7a"/><stop offset=".55" stop-color="#14183f"/><stop offset="1" stop-color="#080c22"/></radialGradient>'
        f'<linearGradient id="{g}s" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#3fd0d3"/><stop offset="1" stop-color="#7a5bd1"/></linearGradient>'
    )
    inner = (
        f'<rect width="800" height="480" fill="url(#{g})"/><circle cx="560" cy="240" r="190" fill="#7a5bd1" opacity=".18"/><circle cx="560" cy="240" r="120" fill="#3fd0d3" opacity=".12"/>'
        f'<rect x="440" y="70" width="170" height="340" rx="30" fill="#0b1020" stroke="#4a5a8a" stroke-width="4"/><rect x="452" y="84" width="146" height="312" rx="20" fill="url(#{g}s)"/><rect x="498" y="92" width="54" height="12" rx="6" fill="#0b1020"/>'
        '<circle cx="525" cy="190" r="40" fill="#fff" opacity=".22"/><rect x="470" y="262" width="110" height="10" rx="5" fill="#fff" opacity=".55"/><rect x="470" y="284" width="80" height="10" rx="5" fill="#fff" opacity=".35"/>'
        '<path d="M170 250 C170 140 270 120 320 170 C370 120 470 140 470 250" fill="none" stroke="#e8ecf7" stroke-width="22" stroke-linecap="round" transform="translate(-30 20) scale(.85)"/><rect x="108" y="244" width="46" height="96" rx="22" fill="#14284a" stroke="#3fd0d3" stroke-width="5"/><rect x="316" y="244" width="46" height="96" rx="22" fill="#14284a" stroke="#3fd0d3" stroke-width="5"/>'
        '<rect x="640" y="150" width="86" height="100" rx="24" fill="#0b1020" stroke="#4a5a8a" stroke-width="4"/><rect x="650" y="162" width="66" height="76" rx="16" fill="#101a3a"/><circle cx="683" cy="200" r="22" fill="none" stroke="#3fd0d3" stroke-width="5"/><path d="M683 186 v14 l10 6" stroke="#fff" stroke-width="3" fill="none" stroke-linecap="round"/><path d="M660 150 l6 -50 h34 l6 50 M660 250 l6 50 h34 l6 -50" fill="#1a2550"/>'
    )
    return _wrap(inner, defs)


def garment(kind, color, bg="#f4ecf0"):
    """Small product thumbnails, 120x120."""
    shapes = {
        "tee": f'<path d="M34 24 L50 18 Q60 30 70 18 L86 24 L102 40 L90 52 L84 46 V100 H36 V46 L30 52 L18 40Z" fill="{color}"/>',
        "dress": f'<path d="M48 16 L72 16 L76 40 Q70 52 78 64 L96 104 H24 L42 64 Q50 52 44 40Z" fill="{color}"/><path d="M44 40 Q60 48 76 40" stroke="#fff" stroke-opacity=".5" stroke-width="3" fill="none"/>',
        "jacket": f'<path d="M36 22 L52 16 L60 26 L68 16 L84 22 L104 44 L92 58 L86 52 V102 H34 V52 L28 58 L16 44Z" fill="{color}"/><path d="M60 26 V102" stroke="#fff" stroke-opacity=".5" stroke-width="3"/>',
        "pants": f'<path d="M38 16 H82 L88 104 H66 L60 54 L54 104 H32Z" fill="{color}"/><path d="M38 16 H82 V24 H38Z" fill="#000" opacity=".12"/>',
        "bag": f'<rect x="26" y="44" width="68" height="56" rx="8" fill="{color}"/><path d="M42 44 V34 a18 18 0 0 1 36 0 V44" fill="none" stroke="{color}" stroke-width="7"/><rect x="26" y="60" width="68" height="6" fill="#fff" opacity=".25"/>',
        "scarf": f'<path d="M30 28 Q60 8 90 28 L84 44 Q60 32 36 44Z" fill="{color}"/><path d="M42 44 L36 100 H54 L56 52Z M78 44 L84 100 H66 L64 52Z" fill="{color}" opacity=".9"/>',
    }
    return f'<svg viewBox="0 0 120 120" aria-hidden="true"><rect width="120" height="120" fill="{bg}"/>{shapes[kind]}</svg>'


def homeitem(kind, color, bg="#efe4d3"):
    shapes = {
        "vase": f'<path d="M48 18 H72 V30 C84 40 90 56 84 78 C80 92 70 100 60 100 C50 100 40 92 36 78 C30 56 36 40 48 30Z" fill="{color}"/><rect x="46" y="14" width="28" height="8" rx="3" fill="#000" opacity=".15"/>',
        "lamp": f'<path d="M40 20 H80 L90 54 H30Z" fill="{color}"/><path d="M60 54 V94" stroke="#6b5a3a" stroke-width="5"/><rect x="40" y="94" width="40" height="8" rx="4" fill="#6b5a3a"/><ellipse cx="60" cy="56" rx="26" ry="4" fill="#fff" opacity=".5"/>',
        "cushion": f'<path d="M20 36 Q60 22 100 36 Q108 60 100 84 Q60 98 20 84 Q12 60 20 36Z" fill="{color}"/><path d="M34 44 Q60 36 86 44 M34 76 Q60 84 86 76" stroke="#fff" stroke-opacity=".4" stroke-width="3" fill="none"/>',
        "mirror": f'<rect x="30" y="14" width="60" height="92" rx="30" fill="{color}"/><rect x="38" y="22" width="44" height="76" rx="22" fill="#dfeef1"/><path d="M48 80 q14 -30 26 -52" stroke="#fff" stroke-opacity=".7" stroke-width="5" fill="none" stroke-linecap="round"/>',
        "plant": f'<path d="M60 84 C40 70 36 40 54 22 C60 40 60 62 60 84Z M60 84 C80 66 86 40 70 22 C62 40 60 62 60 84Z" fill="#3f8a5a"/><path d="M44 84 H76 L72 104 H48Z" fill="{color}"/>',
        "rug": f'<rect x="16" y="34" width="88" height="52" rx="6" fill="{color}"/><rect x="26" y="44" width="68" height="32" rx="3" fill="none" stroke="#fff" stroke-opacity=".5" stroke-width="3"/><path d="M26 44 L94 76 M94 44 L26 76" stroke="#fff" stroke-opacity=".3" stroke-width="2"/>',
    }
    return f'<svg viewBox="0 0 120 120" aria-hidden="true"><rect width="120" height="120" fill="{bg}"/>{shapes[kind]}</svg>'


def gadget(kind, color, bg="#161d45"):
    shapes = {
        "phone": f'<rect x="38" y="12" width="44" height="96" rx="10" fill="#0b1020" stroke="#5a6aa0" stroke-width="2"/><rect x="42" y="18" width="36" height="82" rx="6" fill="{color}"/><rect x="54" y="20" width="12" height="4" rx="2" fill="#0b1020"/>',
        "buds": f'<rect x="28" y="40" width="26" height="46" rx="13" fill="{color}"/><rect x="66" y="40" width="26" height="46" rx="13" fill="{color}"/><circle cx="41" cy="52" r="5" fill="#fff" opacity=".6"/><circle cx="79" cy="52" r="5" fill="#fff" opacity=".6"/>',
        "watch": f'<rect x="44" y="6" width="32" height="24" fill="#2a3470"/><rect x="44" y="90" width="32" height="24" fill="#2a3470"/><rect x="34" y="28" width="52" height="64" rx="14" fill="#0b1020" stroke="#5a6aa0" stroke-width="2"/><circle cx="60" cy="60" r="18" fill="none" stroke="{color}" stroke-width="4"/><path d="M60 50 v10 l8 4" stroke="#fff" stroke-width="3" fill="none" stroke-linecap="round"/>',
        "speaker": f'<rect x="30" y="22" width="60" height="78" rx="14" fill="#0b1020" stroke="#5a6aa0" stroke-width="2"/><circle cx="60" cy="48" r="12" fill="{color}"/><circle cx="60" cy="78" r="16" fill="{color}" opacity=".85"/><circle cx="60" cy="78" r="7" fill="#0b1020"/>',
        "power": f'<rect x="32" y="26" width="56" height="70" rx="10" fill="{color}"/><rect x="42" y="40" width="36" height="6" rx="3" fill="#fff" opacity=".7"/><rect x="42" y="54" width="24" height="6" rx="3" fill="#fff" opacity=".45"/><path d="M60 70 l-8 14 h10 l-4 12 14 -18 h-10z" fill="#fff" opacity=".9"/>',
        "head": f'<path d="M24 74 C24 30 96 30 96 74" fill="none" stroke="{color}" stroke-width="9" stroke-linecap="round"/><rect x="18" y="66" width="22" height="34" rx="10" fill="#0b1020" stroke="{color}" stroke-width="3"/><rect x="80" y="66" width="22" height="34" rx="10" fill="#0b1020" stroke="{color}" stroke-width="3"/>',
    }
    return f'<svg viewBox="0 0 120 120" aria-hidden="true"><rect width="120" height="120" fill="{bg}"/>{shapes[kind]}</svg>'
