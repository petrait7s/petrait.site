from lib import *

TABS = [("dashboard", "Home", "home"), ("sales", "Sales", "receipt"), ("inventory", "Stock", "box"), ("purchases", "Buy", "truck"), ("dues", "Dues", "wallet")]
RAIL = [("dashboard", "Dashboard", "home"), ("sales", "Sales", "receipt"), ("inventory", "Inventory", "box"), ("purchases", "Purchases", "truck"), ("dues", "Dues & ledger", "wallet"), (None, "Reports", "chart"), (None, "Customers", "users")]
MENU = [("dashboard", "Dashboard"), ("sales", "Sales"), ("inventory", "Inventory"), ("purchases", "Purchases"), ("dues", "Dues & ledger"), (None, "Expenses"), (None, "Reports")]
BLUE, SKY, VIO = "#2f5fbf", "#8db0f0", "#7a5bd1"


def kpis():
    items = [("Sales today", "৳ 3,84,500", "+9.2% vs yesterday", False), ("Collected", "৳ 2,60,000", "68% of sales", False), ("Total receivable", "৳ 18,42,000", "− ৳ 40,000 this week", False), ("Stock value", "৳ 62,10,000", "1,240 items", False), ("Gross margin", "14.6%", "− 0.3 pt vs last month", True)]
    return '<div class="kpi-strip">' + "".join(f'<div><small>{a}</small><b>{b}</b><em class="{"d" if d else ""}">{c}</em></div>' for a, b, c, d in items) + "</div>"


def dashboard():
    sales = [210, 240, 198, 262, 288, 231, 205, 270, 296, 318, 252, 275, 301, 330, 288, 270, 310, 345, 322, 300, 335, 360, 340, 318, 352, 380, 365, 342, 370, 384]
    coll = [140, 150, 160, 148, 190, 170, 150, 200, 210, 190, 180, 215, 205, 236, 210, 190, 220, 248, 235, 215, 240, 262, 250, 232, 255, 270, 258, 244, 262, 260]
    chart = line_chart([(sales, BLUE), (coll, "#1fa7ab")], h=200, labels=["8 Oct", "15 Oct", "22 Oct", "29 Oct", "5 Nov"], gridc="#e6eaf2")
    routes = [("Dhaka North", 142, "9,84,000", "6,92,500", "2,91,500", 70), ("Dhaka South", 118, "8,12,400", "5,40,000", "2,72,400", 66), ("Gazipur", 76, "5,36,000", "3,98,000", "1,38,000", 74), ("Narayanganj", 64, "4,41,500", "2,85,000", "1,56,500", 65), ("Savar", 52, "3,70,200", "2,60,000", "1,10,200", 70), ("Tongi", 41, "2,88,000", "1,76,000", "1,12,000", 61)]
    pv = '<table class="pivot"><thead><tr><th>Route</th><th>Invoices</th><th>Sales (৳)</th><th>Collected (৳)</th><th>Due (৳)</th><th>Collection</th></tr></thead><tbody>'
    for r, n, s, c, d, p in routes:
        pv += f'<tr><td>{r}</td><td>{n}</td><td>{s}</td><td>{c}</td><td style="color:var(--bad)">{d}</td><td><span style="display:inline-block;width:54px;vertical-align:middle"><div class="meter"><i style="width:{p}%"></i></div></span> {p}%</td></tr>'
    pv += '</tbody><tfoot><tr><td>Total</td><td>493</td><td>34,32,100</td><td>23,51,500</td><td>10,80,600</td><td>69%</td></tr></tfoot></table>'
    aging = '<div class="aging"><div><small class="muted">0-30 days</small><b>৳ 9.2L</b></div><div><small class="muted">31-60</small><b style="color:var(--warn)">৳ 5.1L</b></div><div><small class="muted">61-90</small><b style="color:#d9822b">৳ 2.6L</b></div><div><small class="muted">90+</small><b style="color:var(--bad)">৳ 1.5L</b></div></div>'
    top = '<table><thead><tr><th>Customer</th><th class="r">Due</th><th class="r">Days</th></tr></thead><tbody>' + "".join(f'<tr><td>{a}</td><td class="r">{b}</td><td class="r">{c}</td></tr>' for a, b, c in [("Noor Traders", "৳ 2,45,000", 48), ("Bismillah Mart", "৳ 1,88,000", 33), ("Mim Enterprise", "৳ 1,20,500", 61), ("Alam Store", "৳ 96,000", 19), ("Hasan & Sons", "৳ 84,200", 12)]) + "</tbody></table>"
    low = rows([("Sugar 1 kg · 6 pcs left", chip("Reorder", "bad")), ("Soybean oil 1 L · 28 pcs", chip("Low", "warn")), ("Salt 1 kg · 40 pcs", chip("Low", "warn")), ("Flour 2 kg · 55 pcs", chip("Low", "warn"))])
    return (
        kpis()
        + f'<div class="grid g21 mt"><div class="card"><h3>Sales vs collection<span>Last 30 days · ৳ thousand</span></h3>{chart}<div class="legend"><span><i class="dot" style="background:{BLUE}"></i>Sales</span><span><i class="dot" style="background:#1fa7ab"></i>Collected</span></div></div>'
        f'<div class="card"><h3>Receivables aging<span>Total ৳ 18.4L</span></h3>{aging}<h3 style="margin-top:16px">Top dues<span>Customers</span></h3>{top}</div></div>'
        f'<div class="grid g21 mt"><div class="card"><h3>Sales by route<span>This month</span></h3>{pv}</div><div class="card"><h3>Stock alerts<span>7 items</span></h3>{low}<h3 style="margin-top:16px">Pending deliveries<span>Today</span></h3>{rows([("INV-2038 · Hasan & Sons", chip("Van 2", "info")), ("INV-2040 · Noor Traders", chip("Van 1", "info")), ("INV-2042 · Alam Store", chip("Packing", "warn"))])}</div></div>'
    )


def sales():
    inv = [
        ("INV-2042", "6 Nov", "Alam Store", "Savar", 12, "58,400", "20,000", "38,400", chip("Partial", "warn")),
        ("INV-2041", "6 Nov", "Karim Store", "Dhaka North", 9, "48,200", "48,200", "0", chip("Paid", "ok")),
        ("INV-2040", "6 Nov", "Noor Traders", "Dhaka South", 21, "1,12,500", "50,000", "62,500", chip("Partial", "warn")),
        ("INV-2039", "5 Nov", "Bismillah Mart", "Gazipur", 7, "26,800", "0", "26,800", chip("Due", "bad")),
        ("INV-2038", "5 Nov", "Hasan & Sons", "Narayanganj", 15, "74,000", "74,000", "0", chip("Paid", "ok")),
        ("INV-2037", "5 Nov", "Mim Enterprise", "Tongi", 11, "41,300", "0", "41,300", chip("Due", "bad")),
        ("INV-2036", "4 Nov", "Rahim Bhai Store", "Dhaka North", 6, "19,900", "19,900", "0", chip("Paid", "ok")),
    ]
    t = '<table><thead><tr><th>Invoice</th><th>Date</th><th>Customer</th><th class="hide-m">Route</th><th class="r hide-m">Items</th><th class="r">Total (৳)</th><th class="r hide-m">Paid</th><th class="r">Due</th><th>Status</th></tr></thead><tbody>'
    for i, r in enumerate(inv):
        t += f'<tr class="{"sel" if i == 2 else ""}"><td><b>{r[0]}</b></td><td>{r[1]}</td><td>{r[2]}</td><td class="hide-m">{r[3]}</td><td class="r hide-m">{r[4]}</td><td class="r">{r[5]}</td><td class="r hide-m">{r[6]}</td><td class="r">{r[7]}</td><td>{r[8]}</td></tr>'
    t += "</tbody></table>"
    filt = f'<div class="toolbar"><div class="pills"><span class="on">All</span><span>Paid</span><span>Partial</span><span>Due</span></div><div class="acts"><div class="field">{icon("calendar")}1 – 6 Nov</div><div class="field">{icon("truck")}All routes</div></div></div>'
    lines = [("Basmati rice 5 kg", "2 BB · 1 SB", "4,860", "10,206"), ("Soybean oil 1 L", "1 BB · 3 SB", "1,920", "3,360"), ("Sugar 1 kg", "3 BB", "4,150", "12,450"), ("Lentil (masur) 1 kg", "2 BB · 4 pcs", "1,100", "2,420")]
    doc = (
        '<div class="doc"><div class="top"><div><p class="muted" style="font-size:10.5px;letter-spacing:.12em">SALES INVOICE</p><h2>INV-2040</h2><p class="muted">Noor Traders · Dhaka South · 6 Nov 2026</p></div><span class="stamp">PART PAID</span></div>'
        '<table><thead><tr><th>Item</th><th>Qty (BB · SB · pc)</th><th class="r">Rate</th><th class="r">Amount</th></tr></thead><tbody>'
        + "".join(f'<tr><td>{a}</td><td>{b}</td><td class="r">{c}</td><td class="r">{d}</td></tr>' for a, b, c, d in lines)
        + '</tbody></table><div class="tot"><div><span>Sub-total</span><span>৳ 1,12,500</span></div><div><span>Paid (cash + bKash)</span><span>− ৳ 50,000</span></div><div class="big"><span>Due</span><span>৳ 62,500</span></div></div>'
        f'<div style="display:flex;gap:8px;margin-top:14px;flex-wrap:wrap"><span class="btn p">Record payment</span><span class="btn">{icon("download")}Print</span><span class="btn">Send reminder</span></div></div>'
    )
    return filt + f'<div class="grid g32"><div class="card" style="padding:0;overflow:hidden">{t}</div><div class="hide-m">{doc}<p class="muted" style="margin-top:8px;font-size:10.5px">BB = big box, SB = small box, pc = piece</p></div></div>'


def inventory():
    items = [
        ("Basmati rice 5 kg", "Grains", 24, 6, 18, "1 BB = 6 SB = 60 pc", 4860, "ok", 78), ("Soybean oil 1 L", "Oils", 12, 3, 0, "1 BB = 4 SB = 48 pc", 1920, "warn", 38), ("Sugar 1 kg", "Staples", 4, 1, 7, "1 BB = 5 SB = 50 pc", 4150, "bad", 14),
        ("Lentil (masur) 1 kg", "Pulses", 18, 2, 11, "1 BB = 4 SB = 40 pc", 1100, "ok", 66), ("Detergent 500 g", "Home care", 9, 5, 20, "1 BB = 6 SB = 72 pc", 2300, "ok", 52), ("Flour 2 kg", "Staples", 7, 2, 4, "1 BB = 5 SB = 50 pc", 2140, "warn", 31), ("Tea 400 g", "Beverages", 15, 4, 9, "1 BB = 5 SB = 40 pc", 3280, "ok", 70),
    ]
    t = '<table><thead><tr><th>Item</th><th class="hide-m">Category</th><th class="r">Big box</th><th class="r">Small box</th><th class="r hide-m">Pieces</th><th class="hide-m">Pack size</th><th class="r">Value (৳)</th><th style="width:15%">Level</th></tr></thead><tbody>'
    for n, c, bb, sb, pc, pk, v, st, lv in items:
        col = {"ok": BLUE, "warn": "#d99a1e", "bad": "#d6504b"}[st]
        t += f'<tr><td><b>{n}</b></td><td class="hide-m muted">{c}</td><td class="r">{bb}</td><td class="r">{sb}</td><td class="r hide-m">{pc}</td><td class="hide-m muted">{pk}</td><td class="r">{v * (bb + 3):,}</td><td><div class="meter"><i style="width:{lv}%;background:{col}"></i></div></td></tr>'
    t += "</tbody></table>"
    cats = '<div class="pills" style="margin-bottom:12px"><span class="on">All 1,240</span><span>Grains</span><span>Oils</span><span>Staples</span><span>Pulses</span><span>Home care</span><span>Beverages</span></div>'
    side = (
        '<div class="card"><h3>Stock value by category<span>৳ lakh</span></h3>'
        + "".join(f'<div class="row"><span>{n}</span><span style="width:50%"><div class="meter"><i style="width:{w}%"></i></div></span><b>{v}</b></div>' for n, w, v in [("Grains", 100, "21.4"), ("Staples", 72, "15.8"), ("Oils", 61, "13.1"), ("Pulses", 38, "8.0"), ("Others", 22, "3.8")])
        + '</div><div class="card mt"><h3>Stock movement<span>Last 7 days</span></h3>' + bars([30, 44, 38, 52, 47, 60, 41], ["M", "T", "W", "T", "F", "S", "S"], 5, 110) + "</div>"
    )
    toolbar = f'<div class="toolbar"><div class="field">{icon("search")}Search item, barcode or batch</div><div class="acts"><span class="btn">Stock count</span><span class="btn p">+ Stock in</span></div></div>'
    return toolbar + cats + f'<div class="grid g32"><div class="card" style="padding:0;overflow:hidden">{t}</div><div class="hide-m">{side}</div></div>'


def purchases():
    po = [
        ("PO-0318", "Golden Harvest Ltd.", "Rice, lentil", "5 Nov", "9 Nov", "4,62,000", 40, chip("In transit", "info")),
        ("PO-0317", "Sundarban Oil Mills", "Soybean oil", "4 Nov", "8 Nov", "2,88,000", 60, chip("Packing", "warn")),
        ("PO-0316", "Dhaka Sugar Co.", "Sugar", "3 Nov", "6 Nov", "3,45,000", 100, chip("Received", "ok")),
        ("PO-0315", "Clean Home Supplies", "Detergent", "2 Nov", "7 Nov", "1,12,500", 85, chip("Partly received", "warn")),
        ("PO-0314", "Tea Valley Traders", "Tea 400 g", "1 Nov", "5 Nov", "96,000", 100, chip("Received", "ok")),
    ]
    t = '<table><thead><tr><th>PO</th><th>Supplier</th><th class="hide-m">Items</th><th class="hide-m">Ordered</th><th>Due</th><th class="r">Amount (৳)</th><th style="width:14%" class="hide-m">Progress</th><th>Status</th></tr></thead><tbody>'
    for a, b, c, d, e, f, p, s in po:
        t += f'<tr><td><b>{a}</b></td><td>{b}</td><td class="hide-m">{c}</td><td class="hide-m">{d}</td><td>{e}</td><td class="r">{f}</td><td class="hide-m"><div class="meter"><i style="width:{p}%"></i></div></td><td>{s}</td></tr>'
    t += "</tbody></table>"
    pay = '<div class="card"><h3>Supplier payables<span>Total ৳ 6,35,000</span></h3>' + rows([("Golden Harvest Ltd.", "৳ 2,40,000"), ("Sundarban Oil Mills", "৳ 1,68,000"), ("Dhaka Sugar Co.", "৳ 1,35,000"), ("Others (3)", "৳ 92,000")]) + "</div>"
    recv = '<div class="card mt"><h3>Receive stock<span>PO-0315</span></h3>' + rows([("Detergent 500 g · ordered", "40 BB"), ("Received so far", "34 BB"), ("Remaining", "6 BB")]) + f'<div style="margin-top:12px"><span class="btn p">{icon("check")}Confirm receipt</span></div></div>'
    stats = '<div class="grid g4" style="margin-bottom:14px">' + stat("Open orders", "4", "৳ 12.0L committed", ic="truck") + stat("Due this week", "3", "৳ 8.5L", ic="calendar") + stat("Purchases this month", "৳ 41,20,000", "12 orders", ic="box") + stat("Supplier dues", "৳ 6,35,000", "4 suppliers", True, ic="wallet") + "</div>"
    return stats + f'<div class="grid g32"><div class="card" style="padding:0;overflow:hidden"><h3 style="padding:14px 14px 0">Purchase orders<span>Latest</span></h3>{t}</div><div class="hide-m">{pay}{recv}</div></div>'


def dues():
    aging = '<div class="aging"><div><small class="muted">Current</small><b>৳ 9,20,000</b></div><div><small class="muted">31-60 days</small><b style="color:var(--warn)">৳ 5,10,000</b></div><div><small class="muted">61-90 days</small><b style="color:#d9822b">৳ 2,62,000</b></div><div><small class="muted">Over 90 days</small><b style="color:var(--bad)">৳ 1,50,000</b></div></div>'
    led = [("Noor Traders", "INV-2040", "2,45,000", 48, "30 Oct · ৳ 50,000", "10 Nov"), ("Bismillah Mart", "INV-2039", "1,88,000", 33, "21 Oct · ৳ 40,000", "12 Nov"), ("Mim Enterprise", "INV-2037", "1,20,500", 61, "2 Oct · ৳ 30,000", "9 Nov"), ("Alam Store", "INV-2042", "96,000", 19, "28 Oct · ৳ 20,000", "14 Nov"), ("Hasan & Sons", "INV-2031", "84,200", 12, "3 Nov · ৳ 74,000", "16 Nov"), ("Tongi Wholesale", "INV-2020", "72,000", 95, "9 Aug · ৳ 25,000", "—")]
    t = '<table><thead><tr><th>Customer</th><th class="hide-m">Last invoice</th><th class="r">Balance due (৳)</th><th class="r">Overdue</th><th class="hide-m">Last payment</th><th class="hide-m">Promised</th><th>Action</th></tr></thead><tbody>'
    for a, b, c, d, e, f in led:
        sev = chip(f"{d} days", "bad" if d > 60 else "warn" if d > 30 else "n")
        t += f'<tr><td><b>{a}</b></td><td class="hide-m">{b}</td><td class="r">{c}</td><td class="r">{sev}</td><td class="hide-m muted">{e}</td><td class="hide-m">{f}</td><td><span class="chip info">Remind</span></td></tr>'
    t += "</tbody></table>"
    chart = line_chart([([62, 70, 66, 74, 81, 77, 85, 92, 88, 96, 101, 98, 104, 110], BLUE)], h=140, labels=["w1", "w3", "w5", "w7", "w9", "w11", "w13"], gridc="#e6eaf2")
    side = (
        f'<div class="card"><h3>Collections<span>Weekly · ৳ thousand</span></h3>{chart}</div>'
        '<div class="card mt"><h3>Payment methods<span>This month</span></h3>' + donut_block([(46, BLUE, "Cash"), (34, "#1fa7ab", "bKash"), (20, VIO, "Bank")], size=108, thick=14, center="৳ 23.5L", track="#e6eaf2") + "</div>"
    )
    return f'<div class="card" style="margin-bottom:14px"><h3>Receivables aging<span>Total ৳ 18,42,000</span></h3>{aging}</div><div class="grid g32"><div class="card" style="padding:0;overflow:hidden"><h3 style="padding:14px 14px 0">Customer ledger<span>Highest dues</span></h3>{t}</div><div class="hide-m">{side}</div></div>'


def build():
    views = [
        ("dashboard", "Distribution dashboard", "Sample Trading Co. · all routes", '<span class="btn">Today</span><span class="btn p">+ New invoice</span>', dashboard()),
        ("sales", "Sales invoices", "Invoices, payments and dues", '<span class="btn">Export</span><span class="btn p">+ New invoice</span>', sales()),
        ("inventory", "Inventory", "Multi-unit stock: big box, small box, piece", '', inventory()),
        ("purchases", "Purchases", "Orders, receipts and supplier payables", '<span class="btn p">+ New purchase</span>', purchases()),
        ("dues", "Dues &amp; ledger", "Who owes what, and for how long", '<span class="btn">Send reminders</span><span class="btn p">Record collection</span>', dues()),
    ]
    write("petradms.html", shell_rail("PetraDMS", RAIL, MENU, TABS, "Accounts", views, ("Distribution", "Dashboard")))
