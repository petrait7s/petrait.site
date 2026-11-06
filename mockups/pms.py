from lib import *

TABS = [("dashboard", "Home", "home"), ("reservations", "Bookings", "calendar"), ("rooms", "Rooms", "bed"), ("housekeeping", "Clean", "spark"), ("billing", "Folio", "receipt")]
NAV = [
    ("h", "Front desk"),
    ("dashboard", "Overview", "grid"), ("reservations", "Reservations", "calendar", 14), ("rooms", "Rooms", "bed"), ("housekeeping", "Housekeeping", "spark", 5), ("billing", "Guest billing", "receipt"),
    ("h", "Manage"), (None, "Guests", "users"), (None, "Rates & availability", "tag"), (None, "Reports", "chart"), (None, "Settings", "settings"),
]
DAYS = ["6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19"]


def hero_strip():
    return (
        '<div class="card" style="background:linear-gradient(120deg,#0c1d35 0%,#14405a 55%,#038d91 130%);color:#fff;border:0;padding:22px 24px;display:flex;align-items:center;justify-content:space-between;gap:20px">'
        '<div><p style="font-size:11px;letter-spacing:.14em;color:#8fe3e5;font-weight:600">THURSDAY 6 NOVEMBER · EVENING SHIFT</p>'
        '<h2 style="font-size:21px;letter-spacing:-.02em;margin:6px 0 4px">14 arrivals, 11 departures today</h2>'
        '<p style="color:#b9c9e0;font-size:12px">9 guests already checked in · 3 departures still to settle · 5 rooms waiting for inspection</p>'
        f'<div style="display:flex;gap:8px;margin-top:14px"><span class="btn t">{icon("key")}Check in guest</span><span class="btn" style="background:rgba(255,255,255,.1);color:#fff;border-color:rgba(255,255,255,.25)">{icon("plus")}New reservation</span></div></div>'
        f'<div class="hide-m" style="color:#fff">{ring(78, "#3fd0d3", 128, 12, "occupied", "rgba(255,255,255,.16)")}</div></div>'
    )


def dashboard():
    arrivals = [
        ("14:00", "Anika Rahman", "305 · Deluxe Sea View", "2 adults · 3 nights", chip("Checked in", "ok")),
        ("15:30", "Mahmud Hasan", "212 · Standard Twin", "2 adults · 2 nights", chip("Arriving", "info")),
        ("16:15", "Sadia Karim", "418 · Family Suite", "2 adults, 2 kids · 4 nights", chip("Arriving", "info")),
        ("17:00", "Tanvir Ahmed", "108 · Standard Queen", "1 adult · 1 night", chip("Late", "warn")),
        ("18:30", "Nusrat Jahan", "301 · Deluxe Sea View", "2 adults · 5 nights", chip("Arriving", "info")),
    ]
    tl = "".join(
        f'<div style="display:grid;grid-template-columns:54px 1fr auto;gap:12px;align-items:start;padding:11px 0;border-top:1px solid var(--line)"><b style="font-size:12px;color:var(--teal-d)">{t}</b>'
        f'<div>{who(g, f"{r}")}<small class="muted" style="display:block;margin:3px 0 0 34px;font-size:10.5px">{d}</small></div>{c}</div>'
        for t, g, r, d, c in arrivals
    )
    left = (
        hero_strip()
        + '<div class="grid g3 mt">'
        + stat("ADR", "৳ 6,850", "+4.1% vs last week", ic="tag")
        + stat("RevPAR", "৳ 5,343", "+7.6% vs last week", ic="chart")
        + stat("Revenue today", "৳ 4,12,300", "+৳ 38,000 vs yesterday", ic="wallet")
        + "</div>"
        + f'<div class="card mt"><h3>Arrivals timeline<span>Today</span></h3>{tl}</div>'
        + f'<div class="card mt"><h3>Occupancy forecast<span>Next 30 days · rooms sold</span></h3>{line_chart([([58, 62, 66, 70, 75, 78, 80, 74, 70, 68, 72, 77, 83, 88, 91, 86, 80, 76, 74, 79, 84, 90, 93, 88, 82, 78, 75, 80, 85, 87], "#038d91"), ([50, 52, 55, 58, 60, 62, 64, 62, 60, 59, 61, 64, 68, 72, 74, 71, 67, 64, 62, 65, 69, 73, 76, 72, 68, 65, 63, 66, 70, 72], "#3b6fd4")], h=170, labels=["6 Nov", "13 Nov", "20 Nov", "27 Nov", "4 Dec"])}'
        + '<div class="legend"><span><i class="dot" style="background:#038d91"></i>This year</span><span><i class="dot" style="background:#3b6fd4"></i>Last year</span></div></div>'
    )
    right = (
        f'<div class="card"><h3>Room status<span>40 rooms</span></h3>{donut_block([(31, "#038d91", "Occupied"), (5, "#1f9d6b", "Clean, vacant"), (3, "#d99a1e", "Dirty"), (1, "#d6504b", "Out of order")], size=124, thick=16, center="78%", sub="occupied")}</div>'
        '<div class="card mt"><h3>Housekeeping<span>Shift progress</span></h3>'
        '<div class="row"><span>Rooms cleaned</span><b>22 / 27</b></div><div class="meter"><i style="width:81%"></i></div>'
        '<div class="row" style="margin-top:10px"><span>Inspected</span><b>17 / 22</b></div><div class="meter"><i style="width:77%;background:#3b6fd4"></i></div>'
        '<div class="row" style="margin-top:10px"><span>Turnovers pending</span><b>5</b></div></div>'
        f'<div class="card mt"><h3>Booking sources<span>This month</span></h3>{rows([("Direct", "38%"), ("Booking sites", "34%"), ("Travel agents", "19%"), ("Walk-in", "9%")])}'
        '<div class="meter" style="margin-top:6px"><i style="width:38%"></i></div></div>'
        '<div class="card mt"><h3>Today\'s notes<span>Front desk</span></h3>'
        '<div class="row"><span>Anniversary stay, room 305</span>' + chip("VIP", "vio") + '</div>'
        '<div class="row"><span>Airport pickup 15:00</span>' + chip("2 guests", "info") + '</div>'
        '<div class="row"><span>Extra bed, room 418</span>' + chip("Pending", "warn") + "</div></div>"
    )
    return f'<div class="grid g32">{"<div>" + left + "</div>"}<div class="hide-m">{right}</div></div>'


def reservations():
    bks = {
        0: [(0, 3, "Anika Rahman", "ci")], 1: [(0, 2, "Mahmud Hasan", "cf"), (3, 4, "Rafiq & family", "pn")], 2: [(1, 4, "Sadia Karim", "cf"), (6, 3, "Tour group · Sylhet", "ota")],
        3: [(0, 1, "Tanvir Ahmed", "ci"), (2, 5, "Nusrat Jahan", "cf"), (9, 4, "Imran Khan", "ota")], 4: [(0, 6, "Habib Corporate", "ci")], 5: [(2, 3, "Maintenance block", "blk"), (7, 5, "Farzana Akter", "cf")],
        6: [(0, 2, "Shirin Sultana", "ci"), (4, 3, "Booking site #8841", "ota"), (9, 4, "Kamal Hossain", "pn")], 7: [(1, 5, "Delwar Hossain", "cf"), (8, 5, "Mitu Rahman", "cf")], 8: [(0, 4, "Parvez Alam", "ci"), (5, 6, "Wedding party", "ota")],
    }
    rooms = [("101", "Std Queen"), ("102", "Std Twin"), ("201", "Deluxe"), ("202", "Deluxe"), ("301", "Deluxe SV"), ("302", "Deluxe SV"), ("305", "Deluxe SV"), ("401", "Suite"), ("418", "Family")]
    head = '<div class="tl-head"><div class="tl-label" style="border-bottom:0">Room<small>Nov 2026</small></div><div class="tl-days">' + "".join(f'<span class="{"today" if i == 0 else ""}">{d}<br>{["Thu", "Fri", "Sat", "Sun", "Mon", "Tue", "Wed"][i % 7]}</span>' for i, d in enumerate(DAYS)) + "</div></div>"
    body = ""
    for i, (n, t) in enumerate(rooms):
        cells = "".join(f'<div class="bk {c}" style="left:calc({s}/14*100% + 2px);width:calc({l}/14*100% - 4px)">{g}</div>' for s, l, g, c in bks.get(i, []))
        body += f'<div class="tl-row"><div class="tl-label">{n}<small>{t}</small></div><div class="tl-cells">{cells}</div></div>'
    tl = f'<div class="tl">{head}{body}</div>'
    leg = '<div class="legend"><span><i class="dot" style="background:#14284a"></i>Checked in</span><span><i class="dot" style="background:#038d91"></i>Confirmed</span><span><i class="dot" style="background:#d99a1e"></i>Awaiting deposit</span><span><i class="dot" style="background:#3b6fd4"></i>Booking site</span><span><i class="dot" style="background:#c4ccd8"></i>Blocked</span></div>'
    toolbar = (
        '<div class="toolbar"><div class="tabs"><span class="on">All 86</span><span>Arrivals 14</span><span>In-house 31</span><span>Departures 11</span><span>Cancelled 3</span></div>'
        f'<div class="acts"><div class="field">{icon("calendar")}6 – 19 Nov 2026</div><div class="field">{icon("filter")}All room types</div></div></div>'
    )
    data = [
        ("BK-20418", "Anika Rahman", "Deluxe Sea View", "6 – 9 Nov", 3, "Direct", chip("Checked in", "ok"), "৳ 9,400"),
        ("BK-20419", "Mahmud Hasan", "Standard Twin", "6 – 8 Nov", 2, "Phone", chip("Arriving", "info"), "৳ 0"),
        ("BK-20422", "Sadia Karim", "Family Suite", "7 – 11 Nov", 4, "Booking site", chip("Confirmed", ""), "৳ 12,000"),
        ("BK-20423", "Rafiq family", "Standard Twin", "9 – 13 Nov", 4, "Direct", chip("Deposit due", "warn"), "৳ 11,800"),
        ("BK-20427", "Habib Corporate", "Deluxe", "6 – 12 Nov", 6, "Agent", chip("Checked in", "ok"), "৳ 38,600"),
        ("BK-20431", "Wedding party", "Suite", "11 – 17 Nov", 6, "Booking site", chip("Confirmed", ""), "৳ 54,000"),
    ]
    tbl = '<div class="card mt"><table><thead><tr><th>Booking</th><th>Guest</th><th class="hide-m">Room type</th><th>Stay</th><th class="hide-m">Nights</th><th class="hide-m">Source</th><th>Status</th><th class="r hide-m">Balance</th></tr></thead><tbody>'
    for r in data:
        tbl += f'<tr><td><b>{r[0]}</b></td><td>{who(r[1])}</td><td class="hide-m">{r[2]}</td><td>{r[3]}</td><td class="hide-m">{r[4]}</td><td class="hide-m">{r[5]}</td><td>{r[6]}</td><td class="r hide-m">{r[7]}</td></tr>'
    tbl += "</tbody></table></div>"
    return toolbar + tl + leg + tbl


def rooms_view():
    status = "".join(
        [
            "occ occ occ clean occ occ occ dirty occ occ",
            "occ occ clean occ occ occ occ occ dirty occ",
            "occ occ occ occ occ clean occ occ occ ooo",
            "occ clean occ occ dirty occ occ clean occ occ",
        ]
    )
    floors = ["occ occ occ clean occ occ occ dirty occ occ", "occ occ clean occ occ occ occ occ dirty occ", "occ occ occ occ occ clean occ occ occ ooo", "occ clean occ occ dirty occ occ clean occ occ"]
    col = {"occ": "#038d91", "clean": "#1f9d6b", "dirty": "#d99a1e", "ooo": "#d6504b"}
    types = ["Std", "Std", "Dlx", "Dlx", "Dlx", "Dlx", "Dlx", "Ste", "Ste", "Fam"]
    html = ""
    for fi, f in enumerate([4, 3, 2, 1]):
        html += f'<div class="floor-label">FLOOR {f}</div><div class="rooms">'
        for i, s in enumerate(floors[fi].split()):
            n = f * 100 + i + 1
            html += f'<div class="rm{" sel" if n == 305 else ""}" style="background:{col[s]}">{n}<small>{types[i]}</small></div>'
        html += "</div>"
    legend = '<div class="legend"><span><i class="dot" style="background:#038d91"></i>Occupied 31</span><span><i class="dot" style="background:#1f9d6b"></i>Clean, vacant 5</span><span><i class="dot" style="background:#d99a1e"></i>Dirty 3</span><span><i class="dot" style="background:#d6504b"></i>Out of order 1</span></div>'
    toolbar = f'<div class="toolbar"><div class="tabs"><span>All floors</span><span>Floor 4</span><span class="on">Floor 3</span><span>Floor 2</span><span>Floor 1</span></div><div class="acts"><div class="field">{icon("filter")}Status: all</div></div></div>'
    panel = (
        '<div class="card"><h3>Room 305<span>Deluxe Sea View</span></h3>'
        f'{who("Anika Rahman", "3 nights · 2 adults · VIP")}<div style="height:12px"></div>'
        + rows([("Check-in", "Thu 6 Nov, 14:00"), ("Check-out", "Sun 9 Nov, 11:00"), ("Rate", "৳ 6,850 / night"), ("Folio balance", "৳ 9,400"), ("Housekeeping", chip("Clean", "ok")), ("Maintenance", chip("None", "n"))])
        + '<div class="row"><span>Amenities</span><span class="muted">Sea view · Balcony · Minibar · King bed</span></div>'
        f'<div style="display:flex;gap:8px;margin-top:14px;flex-wrap:wrap"><span class="btn p">{icon("receipt")}Open folio</span><span class="btn">Move room</span><span class="btn">Check out</span></div></div>'
        '<div class="card mt"><h3>Today in 305<span>Activity</span></h3>'
        '<div class="row"><span>14:02</span><span>Checked in by Front desk</span></div><div class="row"><span>14:20</span><span>Welcome drink posted · ৳ 250</span></div><div class="row"><span>16:45</span><span>Late check-out requested</span></div></div>'
    )
    extra = (
        '<div class="grid g3 mt hide-m"><div class="card"><h3>Availability tonight<span>By room type</span></h3>'
        + rows([("Standard Queen", "2 left"), ("Standard Twin", "3 left"), ("Deluxe Sea View", "1 left"), ("Family Suite", "0 left")])
        + '</div><div class="card"><h3>Maintenance requests<span>Open</span></h3>'
        + rows([("210 · Air conditioner", chip("Urgent", "bad")), ("114 · Shower leak", chip("Today", "warn")), ("Lobby lamp", chip("This week", "n"))])
        + '</div><div class="card"><h3>Next arrivals<span>Rooms to prepare</span></h3>'
        + rows([("212 · Mahmud Hasan", "15:30"), ("418 · Sadia Karim", "16:15"), ("108 · Tanvir Ahmed", "17:00")])
        + "</div></div>"
    )
    return toolbar + f'<div class="grid g32"><div class="card">{html}{legend}</div><div class="hide-m">{panel}</div></div>' + extra


def housekeeping():
    def card(room, kind, who_, mins, prio=None, note=""):
        p = f'<span class="chip bad">Priority</span>' if prio else ""
        return f'<div class="kb-card"><b>{room}<span>{p}</span></b><div class="muted" style="margin-top:3px">{kind}{(" · " + note) if note else ""}</div><div class="meta"><span class="who">{av(who_)}{who_.split()[0]}</span><span>{icon("clock").replace("<svg", "<svg style=\"width:12px;height:12px;display:inline;vertical-align:-2px\"")} {mins}</span></div></div>'

    cols = [
        ("Dirty", 3, [card("304", "Checkout clean", "Rina Akter", "45 min", True), card("309", "Stay-over", "Salma Begum", "25 min"), card("118", "Checkout clean", "Rina Akter", "40 min", note="Extra towels")]),
        ("In progress", 2, [card("202", "Deep clean", "Jamal Uddin", "1h 10m", note="Carpet"), card("312", "Checkout clean", "Salma Begum", "20 min left")]),
        ("Ready to inspect", 3, [card("207", "Checkout clean", "Rina Akter", "Done 14:12"), card("311", "Checkout clean", "Jamal Uddin", "Done 14:40"), card("120", "Stay-over", "Salma Begum", "Done 15:05")]),
        ("Clean", 4, [card("101", "Inspected", "Supervisor", "OK"), card("215", "Inspected", "Supervisor", "OK"), card("316", "Inspected", "Supervisor", "OK"), card("405", "Inspected", "Supervisor", "OK")]),
    ]
    kb = '<div class="kb">' + "".join(f'<div class="kb-col"><h4>{t}<span>{n}</span></h4>{"".join(c)}</div>' for t, n, c in cols) + "</div>"
    stats = '<div class="grid g4" style="margin-bottom:14px">' + stat("Rooms to clean", "8", "5 checkouts, 3 stay-overs", ic="spark") + stat("Avg. clean time", "34 min", "−3 min vs last week", ic="clock") + stat("Inspection pass", "96%", "+2% this month", ic="check") + stat("Minibar to restock", "6", "Rooms 207, 311, 120…", True, ic="box") + "</div>"
    staff = (
        '<div class="grid g2 mt"><div class="card"><h3>Staff workload<span>Today</span></h3>'
        + "".join(f'<div class="row"><span class="who">{av(n)}{n}</span><span style="width:46%"><div class="meter"><i style="width:{p}%"></i></div></span><b>{k} rooms</b></div>' for n, p, k in [("Rina Akter", 82, 9), ("Salma Begum", 68, 7), ("Jamal Uddin", 55, 6), ("Supervisor", 30, 5)])
        + '</div><div class="card"><h3>Linen &amp; amenities<span>Stock</span></h3>'
        + rows([("Bath towels", "142 / 160"), ("Bed sheets (queen)", "88 / 100"), ("Toiletry kits", "64 / 120"), ("Minibar water", "36 / 80")])
        + "</div></div>"
    )
    return stats + kb + staff


def billing():
    charges = [
        ("06 Nov", "Room 305 · Deluxe Sea View", "Room charge", "৳ 6,850"), ("06 Nov", "Restaurant · Dinner", "Spice Garden (POS)", "৳ 1,240"), ("07 Nov", "Room 305 · Deluxe Sea View", "Room charge", "৳ 6,850"),
        ("07 Nov", "Laundry", "2 items", "৳ 450"), ("07 Nov", "Spa · Massage 60 min", "Wellness", "৳ 3,200"), ("08 Nov", "Room 305 · Deluxe Sea View", "Room charge", "৳ 6,850"),
    ]
    t = '<table><thead><tr><th>Date</th><th>Description</th><th class="hide-m">Department</th><th class="r">Amount</th></tr></thead><tbody>'
    for d, a, b, c in charges:
        t += f'<tr><td>{d}</td><td>{a}</td><td class="hide-m muted">{b}</td><td class="r">{c}</td></tr>'
    t += '<tr><td>06 Nov</td><td>Deposit · bKash</td><td class="hide-m muted">Payment</td><td class="r" style="color:var(--ok)">− ৳ 5,000</td></tr><tr><td>06 Nov</td><td>City tax 2%</td><td class="hide-m muted">Tax</td><td class="r">৳ 520</td></tr></tbody></table>'
    folio = (
        f'<div class="doc"><div class="top"><div><p class="muted" style="font-size:11px;letter-spacing:.12em">GUEST FOLIO</p><h2>Anika Rahman</h2><p class="muted">Room 305 · Check-in 6 Nov · Check-out 9 Nov</p></div><span class="stamp ok">OPEN</span></div>{t}'
        '<div class="tot"><div><span>Charges</span><span>৳ 25,160</span></div><div><span>Payments</span><span>− ৳ 5,000</span></div><div class="big"><span>Balance due</span><span>৳ 20,160</span></div></div></div>'
    )
    side = (
        '<div class="card"><h3>Settle &amp; check out<span>Folio 1 of 1</span></h3>'
        + rows([("Pay by cash", chip("Select", "n")), ("Pay by bKash", chip("Select", "n")), ("Pay by card", chip("Select", "n")), ("Bill to company", chip("Select", "n"))])
        + f'<div style="display:flex;gap:8px;margin-top:14px;flex-wrap:wrap"><span class="btn t">Settle ৳ 20,160</span><span class="btn">{icon("download")}PDF invoice</span></div></div>'
        '<div class="card mt"><h3>Night audit<span>Tonight 23:30</span></h3><div class="steps"><i class="on"></i><i class="on"></i><i class="on"></i><i></i><i></i></div>'
        + rows([("Post room charges", chip("Done", "ok")), ("Check cash drawer", chip("Done", "ok")), ("Review no-shows", chip("Done", "ok")), ("Roll business date", chip("Waiting", "n"))])
        + "</div>"
    )
    more = (
        '<div class="grid g3 mt hide-m"><div class="card"><h3>Guest details<span>Profile</span></h3>'
        + rows([("Phone", "01712-345678"), ("Nationality", "Bangladesh"), ("Previous stays", "3"), ("Preference", "High floor, sea view")])
        + '</div><div class="card"><h3>Payment history<span>This stay</span></h3>'
        + rows([("06 Nov · bKash deposit", "৳ 5,000"), ("Card pre-authorisation", "৳ 10,000 held")])
        + '</div><div class="card"><h3>Notes<span>Front desk</span></h3><p class="muted" style="line-height:1.6">Anniversary stay. Late check-out requested for Sunday. Quiet room, balcony facing the sea.</p></div></div>'
    )
    return f'<div class="grid g32"><div>{folio}</div><div class="hide-m">{side}</div></div>' + more


def build():
    A = f'<span class="btn">{icon("download")}Export</span>'
    views = [
        ("dashboard", "Overview", "Sea Breeze Resort · front desk", '<span class="btn">Night audit</span><span class="btn p">+ New booking</span>', dashboard()),
        ("reservations", "Reservations", "Bookings, arrivals and availability", A + '<span class="btn p">+ New booking</span>', reservations()),
        ("rooms", "Rooms", "Live room status, floor by floor", '<span class="btn">Block room</span><span class="btn p">Assign room</span>', rooms_view()),
        ("housekeeping", "Housekeeping", "Cleaning board and inspections", '<span class="btn">Assign staff</span><span class="btn p">+ New task</span>', housekeeping()),
        ("billing", "Guest billing", "Folio, payments and night audit", '<span class="btn">Split bill</span><span class="btn p">Add charge</span>', billing()),
    ]
    write("petrapms.html", shell_side("PetraPMS", "Property management", NAV, TABS, "Front desk", views))
