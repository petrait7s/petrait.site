from lib import *

TABS = [("floor", "Floor", "grid"), ("order", "Order", "utensils"), ("kitchen", "Kitchen", "flame"), ("sales", "Sales", "chart"), ("stock", "Stock", "box")]
TOPNAV = [("floor", "Floor", "grid"), ("order", "New order", "utensils"), ("kitchen", "Kitchen", "flame"), ("sales", "Sales", "chart"), ("stock", "Stock", "box")]
GRID = "#1c2d4a"

ART = {
    "burger": '<path d="M8 28a24 18 0 0 1 48 0z" fill="#e8a24a"/><rect x="6" y="30" width="52" height="5" rx="2.5" fill="#6fbf4a"/><rect x="8" y="35" width="48" height="8" rx="4" fill="#6b3a24"/><path d="M8 45h48v2a6 6 0 0 1-6 6H14a6 6 0 0 1-6-6z" fill="#e8a24a"/>',
    "wrap": '<rect x="9" y="22" width="46" height="22" rx="11" transform="rotate(-20 32 32)" fill="#e9c98a"/><path d="M14 38c10-7 26-15 38-15" stroke="#6fbf4a" stroke-width="5" fill="none" stroke-linecap="round"/><path d="M16 42c10-6 24-12 34-13" stroke="#d6504b" stroke-width="3" fill="none" stroke-linecap="round"/>',
    "bowl": '<path d="M8 30h48a24 22 0 0 1-48 0z" fill="#d9822b"/><path d="M12 30c4-13 36-13 40 0z" fill="#f2c96a"/><circle cx="26" cy="23" r="3" fill="#a64b2a"/><circle cx="38" cy="21" r="3" fill="#6fbf4a"/><circle cx="32" cy="26" r="2.5" fill="#fff" opacity=".8"/>',
    "sandwich": '<path d="M7 40L32 11l25 29z" fill="#e8c27a"/><path d="M14 40l18-22 18 22z" fill="#6fbf4a"/><path d="M21 40l11-14 11 14z" fill="#d6504b"/><rect x="7" y="42" width="50" height="7" rx="3.5" fill="#e8a24a"/>',
    "coffee": '<path d="M13 22h34v14a15 15 0 0 1-15 15h-4a15 15 0 0 1-15-15z" fill="#f4f6f9"/><path d="M47 26h4a6 6 0 0 1 0 12h-5" stroke="#f4f6f9" stroke-width="4" fill="none"/><rect x="15" y="24" width="30" height="8" rx="4" fill="#7a4a2b"/><path d="M24 14c-2-3 2-5 0-8M34 14c-2-3 2-5 0-8" stroke="#9db0cf" stroke-width="2" fill="none" stroke-linecap="round"/>',
    "juice": '<path d="M16 12h32l-4 38a4 4 0 0 1-4 4H24a4 4 0 0 1-4-4z" fill="#cdeccf" opacity=".9"/><path d="M19 26h26l-3 24a2 2 0 0 1-2 2H24a2 2 0 0 1-2-2z" fill="#6fcf6a"/><circle cx="42" cy="14" r="7" fill="#f2c94c"/><path d="M38 6l8 16" stroke="#6b3a24" stroke-width="2.5"/>',
    "fries": '<rect x="14" y="10" width="7" height="30" rx="2" fill="#f2c94c" transform="rotate(-10 17 25)"/><rect x="23" y="8" width="7" height="32" rx="2" fill="#f7d76a"/><rect x="32" y="9" width="7" height="31" rx="2" fill="#f2c94c" transform="rotate(8 35 25)"/><rect x="41" y="12" width="7" height="28" rx="2" fill="#f7d76a" transform="rotate(14 44 26)"/><path d="M11 34h42l-4 21H15z" fill="#d6504b"/>',
    "brownie": '<rect x="9" y="24" width="46" height="26" rx="7" fill="#5b3523"/><rect x="9" y="21" width="46" height="12" rx="6" fill="#7a4a30"/><circle cx="23" cy="40" r="3" fill="#3a2217"/><circle cx="40" cy="42" r="3.5" fill="#3a2217"/><path d="M18 16c4-6 24-6 28 0" stroke="#f4f6f9" stroke-width="3" fill="none" stroke-linecap="round" opacity=".7"/>',
    "tea": '<path d="M14 26h32v10a13 13 0 0 1-13 13h-6a13 13 0 0 1-13-13z" fill="#f4f6f9"/><path d="M46 29h3a5 5 0 0 1 0 10h-4" stroke="#f4f6f9" stroke-width="4" fill="none"/><rect x="16" y="28" width="28" height="6" rx="3" fill="#c98d2a"/><path d="M48 10c-8 0-12 6-12 12 8 0 12-5 12-12z" fill="#6fbf4a"/>',
    "pasta": '<ellipse cx="32" cy="43" rx="25" ry="10" fill="#f4f6f9"/><path d="M13 40c4-16 34-16 38 0-11 7-27 7-38 0z" fill="#f2c96a"/><path d="M20 36c8-6 18-6 26 0M22 41c7-4 14-4 21 0" stroke="#d9a53c" stroke-width="2" fill="none"/><circle cx="28" cy="30" r="3.5" fill="#d6504b"/><circle cx="38" cy="29" r="3" fill="#6fbf4a"/>',
    "lassi": '<path d="M17 10h30l-3 40a5 5 0 0 1-5 5H25a5 5 0 0 1-5-5z" fill="#f6dfa0"/><path d="M19 22h26l-2 28a2 2 0 0 1-2 2H23a2 2 0 0 1-2-2z" fill="#f2b84b"/><circle cx="38" cy="14" r="5" fill="#f2c94c"/><path d="M36 4l6 14" stroke="#d6504b" stroke-width="2.5"/>',
    "samosa": '<path d="M6 46L32 8l26 38a4 4 0 0 1-3.4 6H9.4A4 4 0 0 1 6 46z" fill="#d9a53c"/><path d="M14 44L32 18l18 26z" fill="#e8bb58"/><path d="M20 44l12-17 12 17" stroke="#b9842b" stroke-width="2" fill="none"/>',
}
TINT = ["#2a2f4a", "#23364a", "#2f2b3c", "#1f3a3e", "#33302a", "#242f45"]


def dish(name, price, art, qty=0, i=0):
    on = " on" if qty else ""
    q = f'<span class="q">{qty}</span>' if qty else ""
    return f'<div class="dish{on}">{q}<div class="art" style="background:{TINT[i % len(TINT)]}"><svg viewBox="0 0 64 64">{ART[art]}</svg></div><b>{name}</b><span>৳ {price}</span></div>'


def floor():
    def tb(n, st, sub, t=""):
        tt = f'<span class="t">{t}</span>' if t else ""
        return f'<div class="tb {st}">{tt}<b>T{n}</b><small>{sub}</small></div>'

    tables = (
        tb(1, "busy", "4 guests · ৳ 2,840", "38m") + tb(2, "", "Free") + tb(3, "bill", "2 guests · ৳ 1,365", "Bill") + tb(4, "busy", "3 guests · ৳ 1,980", "12m") + tb(5, "res", "Reserved 8:30 PM") + tb(6, "", "Free")
        + tb(7, "busy", "2 guests · ৳ 1,140", "21m") + tb(8, "bill", "5 guests · ৳ 4,260", "Bill") + tb(9, "", "Free") + tb(10, "busy", "6 guests · ৳ 5,420", "52m") + tb(11, "res", "Reserved 9:00 PM") + tb(12, "", "Free")
        + '<div class="tb wide busy"><span class="t">Terrace</span><b>Terrace · 8 seats</b><small>Family of 6 · ৳ 6,900</small></div><div class="tb wide"><b>Private room</b><small>Free · seats 14</small></div><div class="tb wide res"><b>Bar</b><small>3 of 10 seats taken</small></div>'
    )
    legend = '<div class="legend"><span><i class="dot" style="background:#1fa7ab"></i>Dining</span><span><i class="dot" style="background:#f2a93b"></i>Waiting for bill</span><span><i class="dot" style="background:#7a5bd1"></i>Reserved</span><span><i class="dot" style="background:#2b4570"></i>Free</span></div>'
    left = f'<div class="card"><h3>Dining room<span>Spice Garden · 12 tables</span></h3><div class="tbl">{tables}</div>{legend}</div>'
    orders = [("#2041", "T10", "6 items", "৳ 5,420", chip("Preparing", "warn")), ("#2040", "T8", "9 items", "৳ 4,260", chip("Bill", "info")), ("#2039", "T1", "5 items", "৳ 2,840", chip("Preparing", "warn")), ("#2038", "T3", "3 items", "৳ 1,365", chip("Bill", "info")), ("#2037", "T4", "4 items", "৳ 1,980", chip("Ready", "ok"))]
    o = '<table><thead><tr><th>Order</th><th>Table</th><th>Items</th><th class="r">Total</th><th>Status</th></tr></thead><tbody>' + "".join(f'<tr><td><b>{a}</b></td><td>{b}</td><td>{c}</td><td class="r">{d}</td><td>{e}</td></tr>' for a, b, c, d, e in orders) + "</tbody></table>"
    right = (
        '<div class="grid g2 one-m" style="gap:12px">' + stat("Sales this shift", "৳ 58,640", "+11% vs yesterday", ic="wallet") + stat("Covers", "142", "Avg ticket ৳ 413", ic="users") + "</div>"
        f'<div class="card mt"><h3>Open orders<span>5 active</span></h3>{o}</div>'
        '<div class="card mt"><h3>On shift<span>7 staff</span></h3>' + rows([("Rafi · Floor captain", chip("Active", "ok")), ("Mina · Cashier", chip("Active", "ok")), ("Chef Kabir · Kitchen", chip("Active", "ok")), ("Sumon · Bar", chip("Break 8:15", "warn"))]) + "</div>"
    )
    return f'<div class="grid g32"><div>{left}</div><div>{right}</div></div>'


def order():
    dishes = [("Beef burger", 450, "burger", 2), ("Chicken wrap", 320, "wrap", 0), ("Biryani set", 380, "bowl", 1), ("Club sandwich", 360, "sandwich", 0), ("Cold coffee", 220, "coffee", 1), ("Lemon mint", 140, "juice", 0),
              ("Fries", 180, "fries", 1), ("Brownie", 210, "brownie", 0), ("Green tea", 90, "tea", 0), ("Pasta alfredo", 420, "pasta", 0), ("Mango lassi", 160, "lassi", 0), ("Samosa (4)", 120, "samosa", 0)]
    grid = '<div class="menu-grid">' + "".join(dish(n, p, a, q, i) for i, (n, p, a, q) in enumerate(dishes)) + "</div>"
    cats = '<div class="pills" style="margin-bottom:14px"><span class="on">All items</span><span>Burgers</span><span>Mains</span><span>Wraps</span><span>Drinks</span><span>Desserts</span><span>Sides</span></div>'
    cart = (
        '<div class="card cart"><h3>Table 7<span>Dine in · 2 guests · Rafi</span></h3>'
        '<div class="line"><span>2 × Beef burger</span><b>৳ 900</b><small>No onion · extra cheese</small></div>'
        '<div class="line"><span>1 × Biryani set</span><b>৳ 380</b><small>Medium spicy</small></div>'
        '<div class="line"><span>1 × Cold coffee</span><b>৳ 220</b><small>Less sugar</small></div>'
        '<div class="line"><span>1 × Fries</span><b>৳ 180</b><small></small></div>'
        + rows([("Subtotal", "৳ 1,680"), ("Discount 5%", "− ৳ 84"), ("Service charge 5%", "৳ 80"), ("<b>Total</b>", "<b>৳ 1,676</b>")])
        + '<div class="tender"><span class="on">Cash</span><span>bKash</span><span>Card</span></div>'
        '<div style="display:flex;gap:8px;margin-top:12px"><span class="btn" style="flex:1;justify-content:center">Send to kitchen</span><span class="btn t" style="flex:2;justify-content:center">Charge ৳ 1,676</span></div></div>'
    )
    bar = '<div class="show-m ticketbar" style="display:none;position:absolute;left:12px;right:12px;bottom:92px;z-index:5;background:#f2a93b;color:#1b1200;border-radius:16px;padding:12px 16px;font-weight:700"><span style="display:flex;justify-content:space-between"><span>5 items · Table 7</span><span>Charge ৳ 1,676</span></span></div>'
    return f'<div class="pos"><div>{cats}{grid}</div><div class="hide-m">{cart}</div></div>{bar}'


def kitchen():
    def tk(num, table, mins, items, cls=""):
        li = "".join(f'<li><b>{q}×</b><span>{n}{"<small>" + m + "</small>" if m else ""}</span></li>' for q, n, m in items)
        return f'<div class="ticket {cls}"><header><span>#{num} · {table}</span><span class="chip {"bad" if cls == "bad" else "warn" if cls == "warn" else ""}">{mins}</span></header><ul>{li}</ul></div>'

    new = (
        tk(2043, "T9", "0:42", [(2, "Chicken wrap", "No mayo"), (1, "Club sandwich", ""), (2, "Fries", "")])
        + tk(2044, "Takeaway", "0:15", [(1, "Pasta alfredo", "Extra cheese"), (1, "Brownie", "")])
        + tk(2045, "T12", "0:05", [(3, "Samosa (4)", ""), (2, "Lemon mint", "")])
    )
    prep = (
        tk(2041, "T10", "11:30", [(2, "Beef burger", "Well done"), (2, "Biryani set", "Spicy"), (1, "Pasta alfredo", ""), (1, "Club sandwich", "")], "bad")
        + tk(2039, "T1", "8:10", [(2, "Biryani set", ""), (1, "Chicken wrap", "No onion"), (2, "Cold coffee", "")], "warn")
        + tk(2042, "T7", "3:20", [(1, "Beef burger", "No onion"), (1, "Fries", "")])
    )
    ready = tk(2037, "T4", "Ready 2:10", [(2, "Biryani set", ""), (1, "Mango lassi", "")], "ok") + tk(2036, "T6", "Ready 4:45", [(1, "Pasta alfredo", ""), (1, "Green tea", "")], "ok")
    cols = f'<div class="kds"><div><p class="muted" style="font-weight:700;margin-bottom:10px">NEW · 3</p>{new}</div><div><p class="muted" style="font-weight:700;margin-bottom:10px">PREPARING · 3</p>{prep}</div><div><p class="muted" style="font-weight:700;margin-bottom:10px">READY TO SERVE · 2</p>{ready}</div></div>'
    top = '<div class="grid g4" style="margin-bottom:14px">' + stat("Avg. prep time", "9:40", "Target 10:00", ic="clock") + stat("Orders in queue", "8", "3 new, 3 cooking", ic="flame") + stat("Late tickets", "1", "Order #2041", True, ic="bell") + stat("Served today", "132", "+9% vs yesterday", ic="check") + "</div>"
    return top + cols


def sales():
    hours = [8, 14, 31, 52, 40, 22, 18, 26, 44, 63, 58, 35]
    chart = line_chart([(hours, "#f2a93b")], h=190, gridc=GRID, labels=["10 AM", "12", "2 PM", "4", "6", "8 PM", "10"])
    pay = donut_block([(42, "#f2a93b", "Cash"), (33, "#3fd0d3", "bKash"), (25, "#7a5bd1", "Card")], size=120, thick=15, center="৳ 58.6k", sub="today", track=GRID)
    top = "".join(f'<div class="row"><span>{n}</span><span style="width:45%"><div class="meter"><i style="width:{w}%"></i></div></span><b>{k}</b></div>' for n, w, k in [("Beef burger", 100, 38), ("Cold coffee", 82, 31), ("Biryani set", 71, 27), ("Chicken wrap", 55, 21), ("Pasta alfredo", 42, 16)])
    recent = '<table><thead><tr><th>Order</th><th>Time</th><th class="hide-m">Table</th><th class="hide-m">Payment</th><th class="r">Total</th></tr></thead><tbody>' + "".join(f"<tr><td><b>{a}</b></td><td>{b}</td><td class='hide-m'>{c}</td><td class='hide-m'>{d}</td><td class='r'>{e}</td></tr>" for a, b, c, d, e in [("#2040", "8:02 PM", "T8", "Card", "৳ 4,260"), ("#2036", "7:41 PM", "T6", "bKash", "৳ 860"), ("#2035", "7:30 PM", "Takeaway", "Cash", "৳ 640"), ("#2034", "7:12 PM", "T2", "Cash", "৳ 1,920")]) + "</tbody></table>"
    return (
        '<div class="grid g4">' + stat("Sales today", "৳ 58,640", "+11% vs yesterday", ic="wallet") + stat("Orders", "142", "Avg ৳ 413", ic="receipt") + stat("Top hour", "8 PM", "63 orders", ic="clock") + stat("Voids", "2", "−1 vs yesterday", True, ic="bell") + "</div>"
        f'<div class="grid g21 mt"><div class="card"><h3>Sales by hour<span>Today</span></h3>{chart}</div><div class="card"><h3>Payment mix</h3>{pay}</div></div>'
        f'<div class="grid g2 mt"><div class="card"><h3>Top items<span>Units sold</span></h3>{top}</div><div class="card"><h3>Recent orders</h3>{recent}</div></div>'
    )


def stock():
    items = [("Beef patties", "Meat", 38, 120, "ok", "kg"), ("Chicken breast", "Meat", 14, 60, "bad", "kg"), ("Basmati rice", "Dry", 72, 100, "ok", "kg"), ("Cooking oil", "Dry", 21, 80, "warn", "L"), ("Burger buns", "Bakery", 64, 150, "warn", "pcs"), ("Fresh cream", "Dairy", 9, 40, "bad", "L"), ("Coffee beans", "Dry", 26, 40, "ok", "kg"), ("Mango pulp", "Drinks", 18, 30, "ok", "L")]
    t = '<table><thead><tr><th>Ingredient</th><th class="hide-m">Group</th><th>On hand</th><th style="width:26%">Level</th><th>Status</th></tr></thead><tbody>'
    for n, g, q, mx, st, u in items:
        pct = round(q / mx * 100)
        col = {"ok": "#1fa7ab", "warn": "#f2a93b", "bad": "#d6504b"}[st]
        lab = {"ok": "Good", "warn": "Low", "bad": "Reorder"}[st]
        t += f'<tr><td><b>{n}</b></td><td class="hide-m muted">{g}</td><td>{q} {u}</td><td><div class="meter"><i style="width:{pct}%;background:{col}"></i></div></td><td>{chip(lab, st if st != "ok" else "ok")}</td></tr>'
    t += "</tbody></table>"
    side = (
        '<div class="card"><h3>Reorder suggestions<span>3 items</span></h3>' + rows([("Chicken breast · 46 kg", chip("Order", "bad")), ("Fresh cream · 31 L", chip("Order", "bad")), ("Cooking oil · 59 L", chip("Soon", "warn"))])
        + f'<div style="margin-top:12px"><span class="btn t">{icon("truck")}Create purchase order</span></div></div>'
        '<div class="card mt"><h3>Deliveries<span>This week</span></h3>' + rows([("Fresh Farm Co. · Fri", chip("Confirmed", "ok")), ("City Bakery · Sat", chip("Confirmed", "ok")), ("Dairy Direct · Sun", chip("Pending", "warn"))]) + "</div>"
        '<div class="card mt"><h3>Wastage<span>This week</span></h3>' + rows([("Spoiled produce", "৳ 2,140"), ("Kitchen waste", "৳ 1,320"), ("Returned dishes", "৳ 640")]) + "</div>"
    )
    stats = '<div class="grid g4" style="margin-bottom:14px">' + stat("Stock value", "৳ 3,42,000", "112 items", ic="box") + stat("Low stock", "5", "2 need reorder now", True, ic="bell") + stat("Food cost", "31.4%", "−0.8% vs last week", ic="chart") + stat("Waste", "৳ 4,100", "−12% vs last week", ic="spark") + "</div>"
    return stats + f'<div class="grid g32"><div class="card"><h3>Ingredients<span>Live stock</span></h3>{t}</div><div class="hide-m">{side}</div></div>'


def build():
    views = [
        ("floor", "Floor overview", "Spice Garden · dinner service", '<span class="btn">Open drawer</span><span class="btn t">+ New order</span>', floor()),
        ("order", "New order", "Table 7 · dine in", '<span class="btn">Hold</span><span class="btn p">Split bill</span>', order()),
        ("kitchen", "Kitchen display", "Live tickets, oldest first", '<span class="btn">Recall</span><span class="btn p">Bump all ready</span>', kitchen()),
        ("sales", "Sales", "Today so far", '<span class="btn">Z-report</span><span class="btn p">Export</span>', sales()),
        ("stock", "Stock", "Ingredients, deliveries and waste", '<span class="btn">Stock count</span><span class="btn t">+ Purchase</span>', stock()),
    ]
    write("petrapos.html", shell_top("PetraPOS", TOPNAV, TABS, "Mina Cashier", views))
