from lib import *
import art
from web import nav, foot

TABS = [("store", "Home", "home"), ("orders", "Orders", "receipt"), ("catalog", "Catalog", "tag"), ("customers", "People", "users")]
NAV = [("h", "Store"), ("store", "Overview", "grid"), ("orders", "Orders", "receipt", 18), ("catalog", "Products", "tag"), ("customers", "Customers", "users"), ("h", "Grow"), (None, "Discounts", "wallet"), (None, "Analytics", "chart"), (None, "Settings", "settings")]


def th(fn, kind, color, bg=None):
    return fn(kind, color, bg) if bg else fn(kind, color)


def store_admin():
    sales = [38, 44, 41, 52, 49, 61, 58, 66, 62, 74, 70, 82, 79, 91]
    chart = line_chart([(sales, "#7a5bd1"), ([20, 24, 22, 28, 27, 33, 31, 36, 34, 41, 38, 45, 43, 50], "#b8a4f0")], h=180, labels=["24 Oct", "28 Oct", "1 Nov", "6 Nov"], gridc="#ebe7f5")
    orders = [("#5021", "Rifat Hossain", "bKash", "৳ 2,450", chip("Paid", "ok")), ("#5020", "Nusrat Jahan", "Cash on delivery", "৳ 1,890", chip("To ship", "info")), ("#5019", "Imran Khan", "Card", "৳ 5,200", chip("Shipped", "n")), ("#5018", "Tasnim Akter", "Cash on delivery", "৳ 980", chip("Pending", "warn")), ("#5017", "Sabbir Ahmed", "bKash", "৳ 3,150", chip("Paid", "ok"))]
    ot = '<table><thead><tr><th>Order</th><th>Customer</th><th class="hide-m">Payment</th><th class="r">Total</th><th>Status</th></tr></thead><tbody>' + "".join(f'<tr><td><b>{a}</b></td><td>{who(b)}</td><td class="hide-m">{c}</td><td class="r">{d}</td><td>{e}</td></tr>' for a, b, c, d, e in orders) + "</tbody></table>"
    prods = [("Cotton panjabi", "64 sold", "tee", "#7a5bd1"), ("Leather wallet", "41 sold", "bag", "#c9873a"), ("Handloom scarf", "37 sold", "scarf", "#d6504b")]
    tp = "".join(f'<div class="row"><span class="who" style="gap:10px"><span style="width:40px;height:40px;border-radius:10px;overflow:hidden;display:inline-block">{art.garment(k, c)}</span><b style="font-weight:600">{n}</b></span><span class="muted">{s}</span></div>' for n, s, k, c in prods)
    funnel = (
        '<div class="card"><h3>Conversion funnel<span>Last 7 days</span></h3>'
        + "".join(f'<div class="row"><span>{n}</span><span style="width:48%"><div class="meter"><i style="width:{w}%"></i></div></span><b>{v}</b></div>' for n, w, v in [("Visitors", 100, "3,120"), ("Product views", 64, "1,990"), ("Added to cart", 21, "655"), ("Checkout", 11, "340"), ("Paid orders", 7, "218")])
        + "</div>"
    )
    pay = '<div class="card mt"><h3>Payment methods<span>This week</span></h3>' + donut_block([(46, "#7a5bd1", "bKash"), (38, "#b8a4f0", "Cash on delivery"), (16, "#2f9e8f", "Card")], size=110, thick=14, center="৳ 1.9L", track="#ebe7f5") + "</div>"
    return (
        '<div class="grid g4">' + stat("Sales today", "৳ 1,86,400", "+13% vs yesterday", ic="wallet") + stat("Orders", "74", "18 to ship", ic="receipt") + stat("Visitors", "3,120", "Conversion 2.4%", ic="users") + stat("Returns", "3", "− 2 vs last week", True, ic="box") + "</div>"
        f'<div class="grid g32 mt"><div class="card"><h3>Revenue<span>Last 14 days · ৳ thousand</span></h3>{chart}<div class="legend"><span><i class="dot" style="background:#7a5bd1"></i>This period</span><span><i class="dot" style="background:#b8a4f0"></i>Previous</span></div></div><div>{funnel}</div></div>'
        f'<div class="grid g32 mt"><div class="card"><h3>Latest orders<span>Today</span></h3>{ot}</div><div><div class="card"><h3>Top products<span>This week</span></h3>{tp}</div>{pay}</div></div>'
    )


def orders_view():
    rows_ = [("#5021", "Rifat Hossain", "6 Nov, 7:42 PM", "Dhaka", "bKash", "৳ 2,450", chip("Paid", "ok"), chip("Packing", "warn")), ("#5020", "Nusrat Jahan", "6 Nov, 6:58 PM", "Chattogram", "COD", "৳ 1,890", chip("COD", "info"), chip("To ship", "info")), ("#5019", "Imran Khan", "6 Nov, 5:20 PM", "Sylhet", "Card", "৳ 5,200", chip("Paid", "ok"), chip("Shipped", "n")), ("#5018", "Tasnim Akter", "6 Nov, 4:05 PM", "Dhaka", "COD", "৳ 980", chip("COD", "info"), chip("Pending", "warn")), ("#5017", "Sabbir Ahmed", "6 Nov, 3:12 PM", "Khulna", "bKash", "৳ 3,150", chip("Paid", "ok"), chip("Delivered", "ok")), ("#5016", "Farhana Islam", "6 Nov, 1:40 PM", "Dhaka", "Card", "৳ 4,320", chip("Paid", "ok"), chip("Delivered", "ok")), ("#5015", "Mizan Rahman", "5 Nov, 9:15 PM", "Rajshahi", "COD", "৳ 1,260", chip("COD", "info"), chip("Returned", "bad"))]
    t = '<table><thead><tr><th>Order</th><th>Customer</th><th class="hide-m">Placed</th><th class="hide-m">City</th><th class="hide-m">Payment</th><th class="r">Total</th><th class="hide-m">Pay status</th><th>Fulfilment</th></tr></thead><tbody>'
    for r in rows_:
        t += f'<tr><td><b>{r[0]}</b></td><td>{who(r[1])}</td><td class="hide-m">{r[2]}</td><td class="hide-m">{r[3]}</td><td class="hide-m">{r[4]}</td><td class="r">{r[5]}</td><td class="hide-m">{r[6]}</td><td>{r[7]}</td></tr>'
    t += "</tbody></table>"
    tb = f'<div class="toolbar"><div class="tabs"><span class="on">All 74</span><span>To ship 18</span><span>Shipped 31</span><span>Delivered 22</span><span>Returns 3</span></div><div class="acts"><div class="field">{icon("filter")}Courier: all</div></div></div>'
    side = '<div class="card"><h3>Courier pickup<span>Today 5 PM</span></h3>' + rows([("Pathao · 12 parcels", chip("Booked", "ok")), ("RedX · 6 parcels", chip("Booked", "ok")), ("Self delivery · 2", chip("Dhaka", "n"))]) + '</div><div class="card mt"><h3>Needs attention<span>3</span></h3>' + rows([("#5018 address incomplete", chip("Call", "warn")), ("#5015 return requested", chip("Review", "bad")), ("COD not collected · 2", chip("Follow up", "warn"))]) + "</div>"
    return tb + f'<div class="grid g32"><div class="card" style="padding:0;overflow:hidden">{t}</div><div class="hide-m">{side}</div></div>'


def catalog_view():
    items = [("Cotton panjabi", "৳ 1,450", "24 in stock", art.garment("tee", "#7a5bd1")), ("Leather wallet", "৳ 890", "41 in stock", art.garment("bag", "#c9873a")), ("Handloom scarf", "৳ 1,250", "12 in stock", art.garment("scarf", "#d6504b")), ("Silk dupatta", "৳ 2,400", "14 in stock", art.garment("scarf", "#c2569b")),
             ("Jute tote bag", "৳ 650", "58 in stock", art.homeitem("rug", "#c9a46a")), ("Nakshi kantha", "৳ 3,800", "5 in stock", art.homeitem("cushion", "#c2569b")), ("Brass vase", "৳ 2,100", "6 in stock", art.homeitem("vase", "#c9873a")), ("Bamboo lamp", "৳ 1,650", "Out of stock", art.homeitem("lamp", "#f2b84b")),
             ("Cane basket", "৳ 920", "21 in stock", art.homeitem("plant", "#c9a46a")), ("Woven mat", "৳ 1,350", "9 in stock", art.homeitem("rug", "#2f9e8f")), ("Linen shirt", "৳ 1,890", "33 in stock", art.garment("jacket", "#14284a")), ("Denim trousers", "৳ 2,250", "27 in stock", art.garment("pants", "#3b6fd4"))]
    g = '<div class="pgrid">' + "".join(f'<div class="pcard">{s}<div><b>{n}</b><span>{p} · {st}</span></div></div>' for n, p, st, s in items) + "</div>"
    tb = f'<div class="toolbar"><div class="pills"><span class="on">All 186</span><span>Clothing</span><span>Home</span><span>Accessories</span><span>Low stock 6</span></div><div class="acts"><div class="field">{icon("search")}Search products</div></div></div>'
    return tb + g


def customers_view():
    cs = [("Rifat Hossain", "Dhaka", 12, "৳ 28,400", "VIP"), ("Nusrat Jahan", "Chattogram", 8, "৳ 17,250", "Returning"), ("Imran Khan", "Sylhet", 5, "৳ 14,900", "Returning"), ("Tasnim Akter", "Dhaka", 1, "৳ 980", "New"), ("Sabbir Ahmed", "Khulna", 9, "৳ 21,300", "VIP")]
    t = '<table><thead><tr><th>Customer</th><th>City</th><th class="r">Orders</th><th class="r">Spent</th><th>Segment</th></tr></thead><tbody>' + "".join(f'<tr><td>{who(a)}</td><td>{b}</td><td class="r">{c}</td><td class="r">{d}</td><td>{chip(e, "vio" if e == "VIP" else "info" if e == "New" else "n")}</td></tr>' for a, b, c, d, e in cs) + "</tbody></table>"
    seg = '<div class="card"><h3>Segments<span>All customers 1,284</span></h3>' + donut_block([(18, "#7a5bd1", "VIP"), (46, "#b8a4f0", "Returning"), (36, "#2f9e8f", "New")], size=112, thick=14, center="1,284", track="#ebe7f5") + "</div>"
    return f'<div class="grid g32"><div class="card"><h3>Customers<span>Top spenders</span></h3>{t}</div><div class="hide-m">{seg}</div></div>'


# ---------------------------------------------------------------- landing pages
def ann(cls, text):
    return f'<div class="ann">{text}</div>'


def fashion_page():
    hero = f'<section class="s-hero">{art.fashion_hero()}<div class="in"><p class="s-eyebrow">Winter collection 2026</p><h1>Dress warm. Look sharp.</h1><p>Handpicked styles, honest prices and delivery across Bangladesh. Pay by bKash, card or cash on delivery.</p><div style="display:flex;gap:10px"><span class="s-btn">Shop new arrivals</span><span class="s-btn ghost">Shop sale</span></div></div></section>'
    cats = '<section class="s-sec"><p class="s-eyebrow">Shop by category</p><h2 class="s-h2">Find your style</h2><div class="cats">' + "".join(f'<div style="background:{b};color:{c}">{n}</div>' for n, b, c in [("Women", "#f7d9e8", "#8a2a68"), ("Men", "#dbe3f5", "#1d3a7a"), ("Kids", "#fdeec2", "#8a6a12"), ("Accessories", "#dff1e7", "#1d6b4a")]) + "</div></section>"
    items = [("Cotton kurti", "dress", "#c2569b", "৳ 1,850", "", "New"), ("Linen shirt", "jacket", "#14284a", "৳ 1,890", "", ""), ("Everyday tee", "tee", "#2f9e8f", "৳ 650", "৳ 850", "-24%"), ("Winter scarf", "scarf", "#d6504b", "৳ 1,250", "", "New"), ("Denim trousers", "pants", "#3b6fd4", "৳ 2,250", "", ""), ("Tote bag", "bag", "#c9873a", "৳ 990", "৳ 1,290", "-23%"), ("Jacket", "jacket", "#6b2a5a", "৳ 3,450", "", ""), ("Floral dress", "dress", "#f2c94c", "৳ 2,150", "", "New")]
    cards = "".join(
        f'<div class="s-card"><div class="img">{f"<span class=badge>{bd}</span>" if bd else ""}{art.garment(k, c, "#f4ecf0")}</div><div class="bd"><h3 style="font-size:14px">{n}</h3><div style="display:flex;justify-content:space-between;align-items:center;margin-top:8px"><span class="s-price">{p}{f" <s style=font-weight:500;opacity:.5;font-size:12px>{o}</s>" if o else ""}</span><span class="s-btn" style="padding:7px 14px;font-size:11.5px">Add</span></div></div></div>'
        for n, k, c, p, o, bd in items
    )
    new = f'<section class="s-sec" style="padding-top:10px"><p class="s-eyebrow">New &amp; popular</p><h2 class="s-h2">This week\'s picks</h2><div class="s-g4">{cards}</div></section>'
    promo = '<div class="promo"><div><p class="s-eyebrow" style="color:#f2c94c">Winter sale</p><h2>Up to 30% off selected styles</h2><p style="margin-top:6px;opacity:.85;font-size:14px">Free delivery on orders over ৳ 3,000. Ends Sunday.</p></div><span class="s-btn">Shop the sale</span></div>'
    feats = '<section class="s-sec"><div class="feat3"><div>Pay your way<small>bKash, card or cash on delivery</small></div><div>Fast delivery<small>Within 2 days in Dhaka</small></div><div>Easy returns<small>7 days, no questions</small></div></div></section>'
    return hero + cats + new + promo + feats + foot("Nokshi Wear", "Everyday fashion, delivered across Bangladesh.")


def decor_page():
    hero = f'<section class="s-hero">{art.decor_hero()}<div class="in"><p class="s-eyebrow">Ghar Decor · Handmade homeware</p><h1>Make every corner feel like home.</h1><p>Lamps, vases, textiles and small pieces from craft studios across the country. Delivered to your door.</p><span class="s-btn">Shop the collection</span></div></section>'
    coll = '<section class="s-sec"><p class="s-eyebrow">Collections</p><h2 class="s-h2">Shop by room</h2><div class="coll">' + "".join(f'<div class="tile" style="background:linear-gradient(135deg,{a},{b})"><b>{n}</b></div>' for n, a, b in [("Living room", "#e8c9a0", "#a8825a"), ("Bedroom", "#cfe3e6", "#5aa3ad"), ("Garden & balcony", "#cfe6cf", "#4a9a68")]) + "</div></section>"
    items = [("Brass vase", "vase", "#c9873a", "৳ 2,100"), ("Bamboo lamp", "lamp", "#f2b84b", "৳ 1,650"), ("Nakshi cushion", "cushion", "#c2569b", "৳ 780"), ("Wall mirror", "mirror", "#a8825a", "৳ 3,900"), ("Potted fern", "plant", "#c9a46a", "৳ 1,150"), ("Jute rug", "rug", "#c9a46a", "৳ 4,200"), ("Teal vase", "vase", "#038d91", "৳ 1,850"), ("Table lamp", "lamp", "#2f9e8f", "৳ 2,300")]
    cards = "".join(f'<div class="s-card"><div class="img">{art.homeitem(k, c, "#f3e9d8")}</div><div class="bd"><h3 style="font-size:14px">{n}</h3><div style="display:flex;justify-content:space-between;align-items:center;margin-top:8px"><span class="s-price">{p}</span><span class="s-btn" style="padding:7px 14px;font-size:11.5px">Add</span></div></div></div>' for n, k, c, p in items)
    best = f'<section class="s-sec" style="padding-top:10px"><p class="s-eyebrow">Bestsellers</p><h2 class="s-h2">Loved by our customers</h2><div class="s-g4">{cards}</div></section>'
    feats = '<section class="s-sec"><div class="feat3"><div>Handmade in Bangladesh<small>Direct from craft studios</small></div><div>Cash on delivery<small>Or bKash and card</small></div><div>Safe packing<small>Replacement if anything breaks</small></div></div></section>'
    return hero + coll + best + feats + foot("Ghar Decor", "Handmade homeware, delivered.")


def gadget_page():
    hero = f'<section class="s-hero">{art.gadget_hero()}<div class="in"><p class="s-eyebrow">Volt Gadgets · New season</p><h1>Smart tech, smarter prices.</h1><p>Phones, audio and wearables with warranty and fast delivery. Pay on delivery or by bKash.</p><div style="display:flex;gap:10px"><span class="s-btn">Shop now</span><span class="s-btn ghost" style="color:#fff">Today\'s deals</span></div></div></section>'
    deal = '<div class="deal"><div><p class="s-eyebrow">Flash deal</p><h2 style="font-size:26px;letter-spacing:-.03em;margin-top:6px">Wireless earbuds · 35% off</h2><p style="margin-top:6px;opacity:.8;font-size:13.5px">While stock lasts. Warranty included.</p></div><div class="count"><div>08<small>HRS</small></div><div>42<small>MIN</small></div><div>17<small>SEC</small></div></div></div>'
    items = [("Pro earbuds", "buds", "#3fd0d3", "৳ 3,250", "৳ 4,990", "-35%"), ("Smart watch", "watch", "#7a5bd1", "৳ 6,800", "", "New"), ("Bluetooth speaker", "speaker", "#f2a93b", "৳ 4,100", "৳ 5,200", "-21%"), ("Power bank 20k", "power", "#3fd0d3", "৳ 2,450", "", ""), ("Headphones", "head", "#c2569b", "৳ 5,900", "", "New"), ("Smartphone X", "phone", "#7a5bd1", "৳ 28,900", "", ""), ("Mini speaker", "speaker", "#3fd0d3", "৳ 1,850", "৳ 2,400", "-23%"), ("Fitness band", "watch", "#1fa7ab", "৳ 2,990", "", "")]
    cards = "".join(
        f'<div class="s-card"><div class="img">{f"<span class=badge>{bd}</span>" if bd else ""}{art.gadget(k, c)}</div><div class="bd"><h3 style="font-size:14px">{n}</h3><div style="display:flex;justify-content:space-between;align-items:center;margin-top:8px"><span class="s-price">{p}{f"<span class=old>{o}</span>" if o else ""}</span><span class="s-btn" style="padding:7px 14px;font-size:11.5px">Add</span></div></div></div>'
        for n, k, c, p, o, bd in items
    )
    prods = f'<section class="s-sec"><p class="s-eyebrow">Trending</p><h2 class="s-h2">Gear people are buying</h2><div class="s-g4">{cards}</div></section>'
    brands = '<div class="brands"><span>NOVA</span><span>PULSE</span><span>ORBIT</span><span>ZENITH</span><span>KITE</span></div>'
    feats = '<section class="s-sec"><div class="feat3"><div>Official warranty<small>On every product</small></div><div>Cash on delivery<small>Or bKash and card</small></div><div>Same-day Dhaka delivery<small>Order before 2 PM</small></div></div></section>'
    return hero + deal + prods + brands + feats + foot("Volt Gadgets", "Phones, audio and wearables.")


def build():
    A = f'<span class="btn">{icon("download")}Export</span>'
    admin_views = [
        ("store", "Store overview", "Nokshi Wear · online store", '<span class="btn">View store</span><span class="btn p">+ Add product</span>', store_admin()),
        ("orders", "Orders", "Payments, couriers and returns", A + '<span class="btn p">Print labels</span>', orders_view()),
        ("catalog", "Products", "Catalog and stock", '<span class="btn p">+ Add product</span>', catalog_view()),
        ("customers", "Customers", "Who buys, and how often", '<span class="btn p">+ Email customers</span>', customers_view()),
    ]
    admin = shell_side("E-commerce Build", "Online store builder", NAV, TABS, "Store owner", admin_views, "Search orders, products, customers", theme="theme-shop", extra_css=("sites.css",), org="Nokshi Wear")
    write("ecommerce.html", admin)
    # the three sample storefronts live in their own page so each can scroll like a real site
    fashion = site_view("fashion", "s-fashion", ann("", "Free delivery over ৳ 3,000 · Cash on delivery available") + nav("Nokshi Wear", ["Women", "Men", "Kids", "Sale"], "Cart (2)"), fashion_page(), "Fashion store")
    decor = site_view("decor", "s-decor", ann("", "Handmade in Bangladesh · Free delivery over ৳ 4,000") + nav("Ghar Decor", ["Living", "Bedroom", "Garden", "Gifts"], "Cart (1)"), decor_page(), "Home decor store")
    gadget = site_view("gadgets", "s-gadget", ann("", "Flash deals end tonight · Cash on delivery available") + nav("Volt Gadgets", ["Phones", "Audio", "Wearables", "Deals"], "Cart (3)"), gadget_page(), "Gadget store")
    write("stores.html", shell_plain("E-commerce Build", "theme-site", fashion + decor + gadget))
