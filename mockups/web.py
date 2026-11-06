from lib import *
import art
import pos as _pos


def lscape(c1, c2, m1, m2, sun="#fff4d8"):
    return (
        f'<svg viewBox="0 0 400 240" preserveAspectRatio="xMidYMid slice" aria-hidden="true"><defs><linearGradient id="l{abs(hash(c1 + c2)) % 9999}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{c1}"/><stop offset="1" stop-color="{c2}"/></linearGradient></defs>'
        f'<rect width="400" height="240" fill="url(#l{abs(hash(c1 + c2)) % 9999})"/><circle cx="310" cy="70" r="26" fill="{sun}" opacity=".9"/>'
        f'<path d="M0 170 L80 100 L140 150 L220 70 L300 150 L360 110 L400 140 V240 H0Z" fill="{m1}"/><path d="M0 200 L90 150 L170 190 L260 140 L340 190 L400 160 V240 H0Z" fill="{m2}"/></svg>'
    )


def nav(name, links, cta, dot_cls=""):
    return f'<header class="s-nav"><div class="logo"><i></i>{name}</div><nav>{"".join(f"<span>{l}</span>" for l in links)}</nav><div class="sp"></div><span class="menu"></span><span class="s-btn">{cta}</span></header>'


def foot(name, tag):
    return (
        f'<footer class="s-foot"><div><div class="logo" style="font-weight:800;font-size:18px;margin-bottom:10px">{name}</div><span style="max-width:34ch">{tag}</span></div>'
        '<div><b>Explore</b><span>Home</span><span>About</span><span>Offers</span></div><div><b>Help</b><span>Contact</span><span>FAQ</span><span>Policies</span></div><div><b>Visit</b><span>Cox\'s Bazar</span><span>+880 1XXX-XXXXXX</span><span>hello@example.com</span></div></footer>'
    )


# ---------------------------------------------------------------- resort
def resort_page():
    hero = (
        f'<section class="s-hero">{art.resort()}<div class="in"><p class="s-eyebrow" style="color:#ffd9a0">Coral Bay Resort · Cox\'s Bazar</p><h1>Wake up to the sound of the sea.</h1>'
        '<p>Beachfront rooms, slow mornings and sunsets that stay with you. Book direct for the best rate and free airport pickup.</p>'
        '<span class="s-btn">Explore rooms</span></div></section>'
        '<div style="padding:0 44px;margin-top:-34px;position:relative;z-index:3"><div class="s-search"><div><small>Check-in</small>14 Nov</div><div><small>Check-out</small>17 Nov</div><div><small>Guests</small>2 adults</div><div><small>Room</small>Any</div><span class="s-btn" style="background:#ff7a59;color:#fff">Check rates</span></div></div>'
    )
    amen = '<div class="amen">' + "".join(f"<div>{icon(i)}{l}</div>" for i, l in [("globe", "Beachfront"), ("spark", "Spa &amp; wellness"), ("utensils", "Three restaurants"), ("truck", "Airport pickup")]) + "</div>"
    rooms = [("Deluxe Sea View", "Balcony, king bed, sunrise over the bay", "৳ 6,850", "#ff9f80", "#27b0bf"), ("Family Suite", "Two bedrooms, living area, kids' corner", "৳ 11,200", "#f7c46a", "#e0644a"), ("Garden Cottage", "Private garden and outdoor shower", "৳ 8,400", "#7fd6a8", "#1d6b4a")]
    rc = "".join(
        f'<div class="s-card"><div class="img" style="background:linear-gradient(135deg,{a},{b})"><svg viewBox="0 0 400 240" preserveAspectRatio="xMidYMid slice" aria-hidden="true"><rect x="70" y="120" width="260" height="70" rx="12" fill="#fff" opacity=".9"/><rect x="86" y="96" width="90" height="34" rx="10" fill="#fff" opacity=".95"/><rect x="190" y="96" width="90" height="34" rx="10" fill="#fff" opacity=".95"/><rect x="60" y="190" width="280" height="10" rx="4" fill="#000" opacity=".12"/></svg></div>'
        f'<div class="bd"><h3>{n}</h3><p>{d}</p><div style="display:flex;justify-content:space-between;align-items:center;margin-top:14px"><span class="s-price">{p}<small style="font-weight:500;color:#7a8696"> / night</small></span><span class="s-btn" style="padding:8px 16px;font-size:12px">Details</span></div></div></div>'
        for n, d, p, a, b in rooms
    )
    rooms_sec = f'<section class="s-sec"><p class="s-eyebrow">Stay</p><h2 class="s-h2">Rooms made for slowing down</h2><div class="s-g3">{rc}</div></section>'
    exp = [("Sunset dining on the sand", "#ff9f80", "#7a4a8a"), ("Spa by the sea", "#7fd6d9", "#0b6f86"), ("Snorkelling trips", "#27b0bf", "#0a3140")]
    ex = "".join(f'<div class="tile" style="background:linear-gradient(135deg,{a},{b});min-height:170px"><b>{n}</b></div>' for n, a, b in exp)
    exp_sec = f'<section class="s-sec" style="padding-top:20px"><p class="s-eyebrow">Experiences</p><h2 class="s-h2">More than a room</h2><div class="s-g3">{ex}</div></section>'
    offer = '<div class="offer"><div><p class="s-eyebrow" style="color:#d6f4f4">Direct booking offer</p><h2>Stay 3 nights, pay for 2</h2><p style="margin-top:6px;opacity:.9;font-size:14px">Valid on weekdays until 20 December. Free breakfast included.</p></div><span class="s-btn">Book direct</span></div>'
    gal = '<section class="s-sec"><p class="s-eyebrow">Gallery</p><h2 class="s-h2">A few moments from the bay</h2><div class="s-g4">' + "".join(f'<div class="tile" style="background:linear-gradient(135deg,{a},{b})"><b>{n}</b></div>' for n, a, b in [("Sunrise", "#ffd9a0", "#ff7a59"), ("Pool", "#7fd6d9", "#1b9aaa"), ("Palms", "#7fd6a8", "#1d6b4a"), ("Lounge", "#f7c46a", "#c2569b")]) + "</div></section>"
    return hero + amen + rooms_sec + exp_sec + offer + gal + foot("Coral Bay", "A beachfront resort. Book direct for the best rate.")


def resort():
    return site_view("resort", "s-resort", nav("Coral Bay", ["Rooms", "Dining", "Experiences", "Offers", "Contact"], "Book now"), resort_page(), "Resort website")


# ---------------------------------------------------------------- restaurant
def food_page():
    hero = (
        f'<section class="s-hero">{art.food()}<div class="in"><p class="s-eyebrow">Spice Garden · Dhanmondi</p><h1>Fire, spice and slow-cooked comfort.</h1>'
        '<p>Family recipes, clay-pot biryani and a kitchen that never rushes. Dine in, take away or order for your next gathering.</p><div style="display:flex;gap:10px"><span class="s-btn">Reserve a table</span><span class="s-btn ghost" style="color:#fff">View menu</span></div></div></section>'
    )

    def col(title, items):
        return f'<div class="menu-col"><h3>{title}</h3>' + "".join(f'<div class="menu-item"><span><b>{n}</b><small>{d}</small></span><i></i><b>{p}</b></div>' for n, d, p in items) + "</div>"

    menu = (
        '<section class="s-sec"><p class="s-eyebrow">The menu</p><h2 class="s-h2">Favourites from our kitchen</h2><div class="s-g3">'
        + col("Starters", [("Chicken tikka", "Charcoal grilled, mint chutney", "৳ 380"), ("Samosa (4)", "Beef and potato", "৳ 120"), ("Seekh kabab", "Hand-minced, smoky", "৳ 340")])
        + col("Mains", [("Kacchi biryani", "Slow-cooked in a clay pot", "৳ 450"), ("Beef rezala", "Rich white gravy", "৳ 520"), ("Butter chicken", "Tomato, cream, fenugreek", "৳ 420")])
        + col("Sweets &amp; drinks", [("Firni", "Rice pudding, rose water", "৳ 150"), ("Mango lassi", "Fresh pulp, yoghurt", "৳ 160"), ("Masala tea", "Cardamom, ginger", "৳ 90")])
        + "</div></section>"
    )
    picks = '<section class="s-sec alt"><p class="s-eyebrow">Chef\'s picks</p><h2 class="s-h2">Dishes people come back for</h2><div class="s-g3">' + "".join(
        f'<div class="s-card"><div class="img" style="background:{bg}"><svg viewBox="0 0 64 64" style="padding:14px">{_pos.ART[a]}</svg></div><div class="bd"><h3>{n}</h3><p>{d}</p><div class="s-price" style="margin-top:12px;color:#e8a24a">{p}</div></div></div>'
        for n, d, a, p, bg in [("Kacchi biryani", "Layered rice and tender mutton, slow-cooked for hours.", "bowl", "৳ 450", "#2a1a12"), ("Beef burger", "House-ground patty on a toasted bun.", "burger", "৳ 450", "#2a2418"), ("Pasta alfredo", "Creamy, garlicky, finished with parmesan.", "pasta", "৳ 420", "#1f2a2a")]
    ) + "</div></section>"
    info = (
        '<section class="s-sec"><div class="s-g3">'
        '<div class="s-card" style="padding:22px"><p class="s-eyebrow">Opening hours</p><h3 style="margin:10px 0 8px">Every day</h3><p>Lunch 12:00 – 3:30 PM<br>Dinner 6:30 – 11:30 PM</p></div>'
        '<div class="s-card" style="padding:22px"><p class="s-eyebrow">Find us</p><h3 style="margin:10px 0 8px">Dhanmondi 27</h3><p>Road 12, House 40<br>Dhaka 1209</p></div>'
        '<div class="s-card" style="padding:22px"><p class="s-eyebrow">Catering</p><h3 style="margin:10px 0 8px">Events &amp; parties</h3><p>Custom menus for 20 to 300 guests.</p></div></div></section>'
    )
    res = '<section class="s-sec" style="padding-top:10px"><div class="res-bar"><div><small>Date</small>Fri, 14 Nov</div><div><small>Time</small>8:00 PM</div><div><small>Guests</small>4 people</div><div><small>Seating</small>Terrace</div><span class="s-btn">Reserve</span></div></section>'
    return hero + menu + picks + info + res + foot("Spice Garden", "Family recipes, cooked slowly.")


def food():
    return site_view("restaurant", "s-food", nav("Spice Garden", ["Menu", "Reservations", "Catering", "Locations"], "Reserve a table"), food_page(), "Restaurant website")


# ---------------------------------------------------------------- tours
def tour_page():
    hero = (
        f'<section class="s-hero">{art.tour()}<div class="in"><p class="s-eyebrow" style="color:#ffd9a0">Hill &amp; Haze Tours · Bangladesh</p><h1>Small-group trips to the quiet corners.</h1>'
        '<p>From the tea hills of Sylhet to the mangroves of the Sundarbans: local guides, simple plans, honest prices.</p><span class="s-btn">Find a tour</span></div></section>'
        '<div style="padding:0 44px;margin-top:-34px;position:relative;z-index:3"><div class="s-search"><div><small>Where</small>Sylhet</div><div><small>When</small>Dec 2026</div><div><small>Travellers</small>4 people</div><div><small>Length</small>3 days</div><span class="s-btn">Search</span></div></div>'
    )
    tours = [("Sylhet tea hills", "3 days · Small group", "৳ 14,500", ("#f6c27a", "#5aa37a"), ("#2f7a5a", "#1d5a3f")), ("Sundarbans by boat", "4 days · Boat stay", "৳ 22,000", ("#f0a47e", "#2c6a7a"), ("#1f5a63", "#12414a")), ("Bandarban hills", "3 days · Trek", "৳ 16,800", ("#9ab8e8", "#e8a27a"), ("#3b5a8a", "#27456f"))]
    cards = "".join(
        f'<div class="s-card"><div class="img">{lscape(a[0], a[1], m[0], m[1])}</div><div class="bd"><h3>{n}</h3><p>{d}</p><div class="price-row"><span class="s-price">{p} <small style="font-weight:500;color:#7a8696">per person</small></span><span class="s-btn" style="padding:8px 16px;font-size:12px">View</span></div></div></div>'
        for n, d, p, a, m in tours
    )
    pop = f'<section class="s-sec"><p class="s-eyebrow">Popular tours</p><h2 class="s-h2">Pick a trip, we handle the rest</h2><div class="s-g3">{cards}</div></section>'
    steps = (
        '<section class="s-sec" style="padding-top:10px"><p class="s-eyebrow">How it works</p><h2 class="s-h2">Three simple steps</h2><div class="steps3">'
        '<div><b>01</b><h3>Choose</h3><p>Pick a tour or tell us what you have in mind.</p></div><div><b>02</b><h3>Confirm</h3><p>We confirm dates, guide and stay, and share the plan.</p></div><div><b>03</b><h3>Travel</h3><p>Meet your guide and enjoy. We stay on call all trip.</p></div></div></section>'
    )
    cta = '<section class="s-sec" style="padding-top:10px"><div class="offer" style="margin:0;border-radius:22px;padding:38px 44px;background:linear-gradient(110deg,#16314f,#2c4a73 60%,#f08a4b);color:#fff;display:flex;justify-content:space-between;align-items:center;gap:20px"><div><h2 style="font-size:28px;letter-spacing:-.03em">Planning a group trip?</h2><p style="margin-top:6px;opacity:.9;font-size:14px">Tell us your dates and group size. We reply within a day.</p></div><span class="s-btn" style="background:#fff;color:#16314f">Get a quote</span></div></section>'
    return hero + pop + steps + cta + foot("Hill & Haze", "Small-group trips with local guides.")


def tours():
    return site_view("tours", "s-tour", nav("Hill & Haze", ["Tours", "Destinations", "Groups", "About"], "Plan a trip"), tour_page(), "Tour operator website")


# ---------------------------------------------------------------- builder
def editor():
    blocks = [("Hero", "layers", True), ("Rooms", "bed", False), ("Gallery", "grid", False), ("Offers", "tag", False), ("Booking form", "calendar", False), ("Map", "globe", False), ("Footer", "layers", False)]
    left = '<div class="ed-left"><h4>Pages</h4>' + "".join(f'<div class="blk{" on" if n == "Home" else ""}">{icon("globe")}{n}</div>' for n in ["Home", "Rooms", "Dining", "Contact"]) + '<h4 style="margin-top:14px">Sections</h4>' + "".join(f'<div class="blk{" on" if on else ""}">{icon(i)}{n}</div>' for n, i, on in blocks) + f'<span class="btn" style="width:100%;justify-content:center;margin-top:6px">{icon("plus")}Add section</span></div>'
    props = (
        '<div class="ed-right"><h4>Hero section</h4><div class="prop"><span>Layout</span><b>Left aligned</b></div><div class="prop"><span>Heading</span><b>Wake up to the sea</b></div><div class="prop"><span>Button</span><b>Explore rooms</b></div>'
        '<div class="prop"><span>Overlay</span><b>Teal gradient</b></div><div class="prop"><span>Text colour</span><b>White <i class="sw" style="background:#fff"></i></b></div><div class="prop"><span>Accent</span><b>Coral <i class="sw" style="background:#ff7a59"></i></b></div>'
        '<h4 style="margin-top:14px">Hero image</h4><div style="height:92px;border-radius:12px;overflow:hidden;position:relative">' + art.resort() + '</div>'
        '<div class="prop" style="margin-top:8px"><span>Animation</span><b>Fade up</b></div><div class="prop"><span>SEO title</span><b>Coral Bay Resort</b></div></div>'
    )
    page = resort_page()
    center = f'<div class="ed-canvas"><div class="win"><div class="bar"><i></i><i></i><i></i><span style="margin-left:8px">coralbay.example/home</span></div><div class="viewport" style="padding:0"><div class="scroller" style="padding:0"><div class="s-resort">{page}</div></div></div></div></div>'
    top = (
        f'<div class="ed-top"><div class="brand"><img src="/brand/petra-mark.png" alt="" style="width:26px;height:26px;border-radius:7px"><span style="margin-left:8px">WEBSITE BUILD</span></div><span style="font-weight:700;font-size:13px">Home · Coral Bay Resort</span><span class="chip ok">Draft saved</span><div class="sp"></div>'
        f'<div class="seg"><span class="on">Desktop</span><span>Tablet</span><span>Mobile</span></div><div class="sp"></div><span class="btn" style="background:#232944;color:#fff;border-color:#3b4373">Preview</span><span class="btn t">Publish</span></div>'
    )
    return f'<section data-v="editor" style="flex:1;display:flex;flex-direction:column;min-height:0;background:#eef0f5"><span data-title hidden>Page editor</span>{top}<div class="ed">{left}{center}{props}</div></section>\n'


def build():
    sections = editor() + resort() + food() + tours()
    write("website.html", shell_plain("Website Build", "theme-site theme-web", sections))
