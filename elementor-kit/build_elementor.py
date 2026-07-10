#!/usr/bin/env python3
"""
Generator for the Catch AI Elementor page template + global styles.

Produces (in this folder):
  catch-ai-elementor-template.json  -> importable Elementor page template
  catch-ai-global-styles.json       -> global colors + typography (for the applier)
  catch-ai-elementor-data.json      -> raw _elementor_data array (for WP-CLI seeding)

Design tokens (OKLCH -> sRGB hex) captured from the reference site.
"""
import json, os

# ---------------------------------------------------------------- palette
SKY   = "#91d0fc"   # hero / demo background
SKY2  = "#aedeff"   # outgoing chat bubble
INK   = "#181f2e"   # primary dark (stats, testimonials, footer, buttons text-on-lime)
INK2  = "#0e141f"   # darker (the difference)
BG    = "#fbfaf6"   # page off-white background
FG    = "#161b24"   # foreground text (near-black)
ACCENT= "#cafacb"   # light green (hot-lead box)
LIME  = "#d5f64e"   # accent / primary buttons
MINT  = "#d3edd3"   # who-it's-for background
MUTED = "#505561"   # muted grey text
BORDER= "#e0ded7"   # hairline border
CARD  = "#ffffff"   # card surface
AVATAR= "#6fa5cb"   # testimonial avatar
GREEN = "#1e6626"   # hot-lead label text
WHITE = "#ffffff"
W70   = "rgba(255,255,255,0.66)"   # muted text on dark
W55   = "rgba(255,255,255,0.55)"
W10   = "rgba(255,255,255,0.10)"
K06   = "rgba(0,0,0,0.06)"

SERIF = "Fraunces"
SANS  = "Inter"

ASSET = "https://catch-ai-web-production.up.railway.app/wp-content/themes/catch-ai/assets"

# ---------------------------------------------------------------- id gen
_counter = [0x100000]
def nid():
    _counter[0] += 1
    return format(_counter[0], "07x")

# ---------------------------------------------------------------- primitives
def W(wtype, settings):
    return {"id": nid(), "elType": "widget", "widgetType": wtype,
            "settings": settings, "elements": []}

def C(settings, elements, inner=False):
    return {"id": nid(), "elType": "container", "isInner": inner,
            "settings": settings, "elements": elements}

def px(*vals, linked=False):
    if len(vals) == 1:
        t = r = b = l = vals[0]
        linked = True
    else:
        t, r, b, l = vals
    return {"unit": "px", "top": t, "right": r, "bottom": b, "left": l,
            "isLinked": linked}

def sz(n, unit="px"):
    return {"unit": unit, "size": n, "sizes": []}

def gap(n):
    return {"unit": "px", "size": n, "column": str(n), "row": str(n)}

# ---------------------------------------------------------------- widgets
def heading(text, tag="h2", color=FG, size=None, weight="500", family=SERIF,
            align="left", lh=None, ls=None, mobile=None, tablet=None, extra=None,
            width_auto=False):
    s = {"title": text, "header_size": tag, "align": align, "title_color": color,
         "typography_typography": "custom", "typography_font_family": family,
         "typography_font_weight": weight}
    if size:   s["typography_font_size"] = sz(size)
    if tablet: s["typography_font_size_tablet"] = sz(tablet)
    if mobile: s["typography_font_size_mobile"] = sz(mobile)
    if lh:     s["typography_line_height"] = sz(lh, "em")
    if ls:     s["typography_letter_spacing"] = sz(ls)
    if width_auto: s["_element_width"] = "auto"
    if extra:  s.update(extra)
    return W("heading", s)

def para(html, color=MUTED, size=16, align="left", family=SANS, weight="400",
         lh=1.6, mobile=None, extra=None, width_auto=False):
    s = {"editor": "<p>%s</p>" % html, "align": align, "text_color": color,
         "typography_typography": "custom", "typography_font_family": family,
         "typography_font_size": sz(size), "typography_font_weight": weight,
         "typography_line_height": sz(lh, "em")}
    if mobile: s["typography_font_size_mobile"] = sz(mobile)
    if width_auto: s["_element_width"] = "auto"
    if extra: s.update(extra)
    return W("text-editor", s)

def button(text, url="#", bg=LIME, color=INK, size=16, radius=999, pad=(15,28,15,28),
           align=None, width_auto=True, extra=None):
    s = {"text": text, "link": {"url": url, "is_external": "", "nofollow": ""},
         "background_color": bg, "button_text_color": color,
         "typography_typography": "custom", "typography_font_family": SANS,
         "typography_font_size": sz(size), "typography_font_weight": "600",
         "border_radius": px(radius), "text_padding": px(*pad),
         "hover_color": color, "button_background_hover_color": bg}
    if align: s["align"] = align
    if width_auto: s["_element_width"] = "auto"
    if extra: s.update(extra)
    return W("button", s)

def image(url, width=None, align="center", radius=None, extra=None):
    s = {"image": {"url": url, "id": ""}, "align": align}
    if width: s["width"] = sz(width, "%")
    if radius: s["image_border_radius"] = px(radius)
    if extra: s.update(extra)
    return W("image", s)

def icon_list(items, color=FG, icon="fas fa-check-circle", icon_color=None, size=15):
    lst = []
    for it in items:
        lst.append({"text": it, "_id": nid()[:7],
                    "selected_icon": {"value": icon, "library": "fa-solid"}})
    s = {"icon_list": lst, "space_between": gap(10), "icon_color": icon_color or INK,
         "text_color": color, "icon_size": sz(18),
         "text_indent": sz(8),
         "typography_typography": "custom", "typography_font_family": SANS,
         "typography_font_size": sz(size), "typography_line_height": sz(1.45, "em")}
    return W("icon-list", s)

def html_widget(code):
    return W("html", {"html": code})

# Custom CSS that ships inside the template (in a small HTML widget) for the two
# things free Elementor can't do from the UI: a sticky translucent header, and
# the overlapping hero composition (phone over van photo, floating cards).
HERO_CSS = """<style>
/* --- Sticky translucent header (the reference header "follows anywhere") --- */
#site-header{position:-webkit-sticky;position:sticky;top:0;z-index:999;
  padding-top:12px!important;padding-bottom:12px!important;
  background:rgba(190,222,252,.9)!important;
  -webkit-backdrop-filter:saturate(140%) blur(10px);backdrop-filter:saturate(140%) blur(10px)}
/* remove Elementor's default 10px container padding inside the header so it stays compact */
#site-header .e-con,#site-header .e-con-inner{padding-top:0!important;padding-bottom:0!important}
#site-header .elementor-heading-title{white-space:nowrap}
/* --- Hero layered composition: large van photo, smaller phone overlapping
       its lower-left, notification card clear at top-right, replied badge --- */
#ca-hero-visual{position:relative}
#ca-hero-visual,#ca-hero-visual>.e-con-inner{min-height:600px}
#ca-hero-visual>.e-con-inner{position:relative;width:100%}
#ca-van{position:absolute;right:0;top:24px;width:min(86%,420px);height:410px;
  border-radius:24px;overflow:hidden;box-shadow:0 30px 60px -20px rgba(20,30,60,.4);z-index:1}
#ca-van>.e-con-inner,#ca-van .elementor-widget-image,#ca-van .elementor-widget-container{height:100%!important;margin:0;padding:0}
#ca-van img{width:100%;height:100%;object-fit:cover;display:block;border-radius:24px}
#ca-notif{position:absolute;right:0;top:0;width:auto;max-width:258px;z-index:8}
#ca-replied{position:absolute;left:21%;top:34px;z-index:8;width:-webkit-max-content;width:max-content}
#ca-phone{position:absolute;left:0;bottom:0;width:min(66%,325px)!important;z-index:5}
@media(max-width:1024px){
  #ca-hero-visual,#ca-hero-visual>.e-con-inner{min-height:560px}
  #ca-van{width:min(90%,380px);height:360px}
  #ca-replied{left:24%}
}
@media(max-width:767px){
  #ca-hero-visual,#ca-hero-visual>.e-con-inner{min-height:0}
  #ca-hero-visual>.e-con-inner{display:flex;flex-direction:column;align-items:center;padding-top:8px}
  #ca-notif{position:relative;top:0;right:0;width:100%;max-width:320px;margin:0 0 12px}
  #ca-van{position:relative;top:0;right:0;width:100%;max-width:340px;height:200px!important}
  #ca-phone{position:relative;left:0;bottom:0;width:100%!important;max-width:280px;margin-top:-120px}
  #ca-replied{display:none}
}
</style>"""

# ---------------------------------------------------------------- layout
def container(elements, direction="column", align=None, justify=None, gap_px=24,
              bg=None, bg_image=None, pad=None, radius=None, width=None, width_unit="%",
              boxed=False, max_w=None, wrap="wrap", extra=None, inner=False,
              stack_mobile=True, border=None):
    s = {"flex_direction": direction,
         "flex_gap": gap(gap_px),
         "flex_wrap": wrap}
    if boxed:
        s["content_width"] = "boxed"
        if max_w: s["width"] = sz(max_w)
    else:
        s["content_width"] = "full"
    if align:   s["flex_align_items"] = align
    if justify: s["flex_justify_content"] = justify
    if width is not None:
        s["width"] = sz(width, width_unit)
        # When a %-width child sits in a row that stacks on mobile, make it
        # full-width on mobile so it never renders as a thin strip.
        if width_unit == "%":
            s["width_mobile"] = sz(100, "%")
    if bg:
        s["background_background"] = "classic"; s["background_color"] = bg
    if bg_image:
        s["background_background"] = "classic"
        s["background_image"] = {"url": bg_image, "id": ""}
        s["background_size"] = "cover"; s["background_position"] = "center center"
    if pad is not None: s["padding"] = pad
    if radius is not None: s["border_radius"] = px(radius)
    if border:
        s["border_border"] = "solid"; s["border_width"] = px(1)
        s["border_color"] = border
    if direction == "row" and stack_mobile:
        s["flex_direction_mobile"] = "column"
    if extra: s.update(extra)
    return C(s, elements, inner=inner)

def section(children, bg=None, bg_image=None, pad_y=96, pad_y_tab=80, pad_y_mob=64,
            max_w=1200, inner_dir="column", inner_align="stretch", inner_gap=24,
            align=None, extra=None, inner_extra=None, el_id=None):
    inner_s = {"content_width": "boxed", "width": sz(max_w),
               "flex_direction": inner_dir, "flex_gap": gap(inner_gap),
               "flex_align_items": inner_align, "flex_wrap": "wrap"}
    if inner_dir == "row":
        inner_s["flex_direction_mobile"] = "column"
    if inner_extra: inner_s.update(inner_extra)
    inner = C(inner_s, children, inner=True)
    s = {"content_width": "full", "flex_direction": "column",
         "padding": px(pad_y, 20, pad_y, 20),
         "padding_tablet": px(pad_y_tab, 24, pad_y_tab, 24),
         "padding_mobile": px(pad_y_mob, 16, pad_y_mob, 16)}
    if align:
        s["flex_align_items"] = align
    if bg:
        s["background_background"] = "classic"; s["background_color"] = bg
    if bg_image:
        s["background_background"] = "classic"
        s["background_image"] = {"url": bg_image, "id": ""}
        s["background_size"] = "cover"; s["background_position"] = "center center"
    if el_id: s["_element_id"] = el_id
    if extra: s.update(extra)
    return C(s, [inner])

def pill(label, bg, color, size=12, weight="700", ls=1.0):
    # A content-hugging pill: a heading widget styled via its Advanced tab, with
    # _element_width:auto so it shrinks to its text instead of stretching full width.
    return heading(label, "div", color, size, weight, SANS, "center",
                   ls=ls, width_auto=True,
                   extra={"_background_background": "classic",
                          "_background_color": bg,
                          "_border_radius": px(999),
                          "_padding": px(7, 16, 7, 16)})

def eyebrow(label, dark=False, align="left"):
    color = WHITE if dark else INK
    bgp = W10 if dark else K06
    return pill(label.upper(), bgp, color, 12, "600", 1.4)

def sec_head(eyebrow_label, title_widget, sub=None, dark=False, max_w=760):
    kids = [eyebrow(eyebrow_label, dark, "center"), title_widget]
    if sub is not None:
        kids.append(sub)
    return container(kids, direction="column", align="center", gap_px=20,
                     boxed=True, max_w=max_w,
                     extra={"text_align": "center", "flex_align_items": "center"})

# ================================================================ SECTIONS
def header():
    logo_c = container([
        container([heading("C", "div", WHITE, 15, "600", SANS, "center")],
                  direction="row", justify="center", align="center", bg=INK,
                  radius=999, width=30, width_unit="px",
                  extra={"height": sz(30), "min_height": sz(30)}, gap_px=0, wrap="nowrap"),
        heading("Catch AI", "div", FG, 22, "500", SERIF, "left", width_auto=True),
    ], direction="row", align="center", gap_px=10, wrap="nowrap",
        extra={"_element_width": "auto"})
    def navlink(t, url):
        return heading(t, "div", FG, 15, "400", SANS, "left", width_auto=True,
                       extra={"link": {"url": url}})
    nav = container([
        navlink("How it works", "#how"), navlink("Who it's for", "#who"),
        navlink("Pricing", "#pricing"), navlink("FAQ", "#faq"),
    ], direction="row", align="center", gap_px=34, wrap="nowrap",
        extra={"_element_width": "auto"})
    actions = container([
        heading("Login", "div", FG, 15, "400", SANS, "left", width_auto=True),
        button("Try the demo", "#demo", LIME, INK, 15, 999, (11,22,11,22)),
    ], direction="row", align="center", gap_px=20, wrap="nowrap",
        extra={"_element_width": "auto"})
    bar = container([logo_c, nav, actions], direction="row", align="center",
                    justify="space-between", boxed=True, max_w=1200, wrap="nowrap",
                    extra={"flex_direction_mobile": "column", "flex_gap": gap(16)})
    return section([bar], bg=SKY, pad_y=18, pad_y_tab=18, pad_y_mob=16, max_w=1200,
                   el_id="site-header", inner_extra={"width": sz(1200)})

def hero():
    left = container([
        eyebrow("For Australian Tradies & Small Businesses"),
        heading('Every missed call is a job going to <i>someone else.</i>', "h1",
                FG, 64, "500", SERIF, "left", lh=1.05, tablet=52, mobile=40),
        para("Catch AI texts your missed callers back in 10 seconds — automatically, "
             "in your business name. They wait for you instead of moving on.",
             FG, 20, "left", lh=1.55, extra={"text_color": "#2b3340"}),
        container([
            button("Get it on my phone", "#demo", LIME, INK),
            button("Get it on my phone".replace("Get it on my phone", "How it works"),
                   "#how", "rgba(0,0,0,0)", INK, extra={
                    "border_border": "solid", "border_width": px(1),
                    "border_color": "rgba(0,0,0,0.18)"}),
        ], direction="row", gap_px=14, wrap="wrap", stack_mobile=False),
        para("• No contract&nbsp;&nbsp;&nbsp; • Works on any phone&nbsp;&nbsp;&nbsp; "
             "• Setup in 15 minutes&nbsp;&nbsp;&nbsp; • Australian numbers",
             "#39404d", 15, "left", lh=1.8),
    ], direction="column", gap_px=26, width=50, extra={"flex_align_items": "flex-start", "width_tablet": sz(100,"%")})

    # phone chat card
    def bubble(text, me=False):
        return container([para(text, INK, 13.5, "left", lh=1.45)],
                         direction="column",
                         bg=(SKY2 if me else "#f0f0ee"),
                         radius=16, pad=px(10, 13, 10, 13),
                         width=82, extra={"align_self": "flex-end" if me else "flex-start",
                                          "_element_width": "auto"})
    screen = container([
        container([
            heading("9:41", "div", MUTED, 12, "400", SANS, "left", width_auto=True),
            heading("Dave's Plumbing", "div", INK, 12, "600", SANS, "center", width_auto=True),
            heading("•••", "div", MUTED, 12, "400", SANS, "right", width_auto=True),
        ], direction="row", justify="space-between", align="center", wrap="nowrap",
            pad=px(12, 16, 8, 16)),
        heading("● Missed call · 0412 345 678", "div", "#c33", 12, "400", SANS,
                "left", extra={"margin": px(0,0,4,14)}),
        bubble("Hi! Sorry we missed your call — this is Dave's Plumbing. What can we help with today? 🔧"),
        bubble("need someone to replace a hot water system asap", me=True),
        bubble("Absolutely — that's our bread and butter. What suburb are you in? We'll get someone out today. 👍"),
        container([
            heading("HOT LEAD", "div", GREEN, 11, "700", SANS, "left", ls=1),
            para('"need someone to replace a hot water system asap"', INK, 13, "left"),
        ], direction="column", gap_px=4, bg=ACCENT, radius=12, pad=px(11,13,11,13),
            extra={"margin": px(8,10,6,10)}),
    ], direction="column", gap_px=8, bg=CARD, radius=24, pad=px(6,6,16,6))
    phone = container([screen], direction="column", bg=INK, radius=34, pad=px(12),
                      extra={"_element_id": "ca-phone",
                             "box_shadow_box_shadow_type": "yes",
                             "box_shadow_box_shadow": {"horizontal": 0, "vertical": 30,
                             "blur": 60, "spread": -20, "color": "rgba(20,30,60,0.45)"}})
    notif = container([
        heading("New lead · 0418 234 567", "div", INK, 13, "600", SANS, "left"),
        para('"need a safety inspection before settlement"', MUTED, 13, "left"),
    ], direction="column", gap_px=2, bg=CARD, radius=16, pad=px(12,16,12,16),
        extra={"_element_id": "ca-notif", "box_shadow_box_shadow_type": "yes",
               "box_shadow_box_shadow": {"horizontal": 0, "vertical": 18, "blur": 40,
               "spread": -12, "color": "rgba(20,30,60,0.30)"}})
    replied = container([
        heading("Catch AI", "div", "#2f7dc0", 12, "700", SANS, "left", width_auto=True),
        heading("replied in 9s", "div", INK, 12, "600", SANS, "left", width_auto=True),
    ], direction="row", align="center", gap_px=5, wrap="nowrap", bg=WHITE, radius=999,
        pad=px(6, 14, 6, 14),
        extra={"_element_id": "ca-replied", "box_shadow_box_shadow_type": "yes",
               "box_shadow_box_shadow": {"horizontal": 0, "vertical": 10, "blur": 24,
               "spread": -8, "color": "rgba(20,30,60,0.25)"}})
    # Real <img> (not a CSS background) so it renders reliably; CSS makes it fill.
    van = container([image("%s/hero-plumber.jpg" % ASSET, width=100)],
                    direction="column", extra={"_element_id": "ca-van"})
    right = container([html_widget(HERO_CSS), notif, replied, van, phone],
                      direction="column", width=42,
                      extra={"_element_id": "ca-hero-visual", "width_tablet": sz(100, "%")})

    row = container([left, right], direction="row", align="center", justify="space-between", gap_px=40,
                    boxed=True, max_w=1200,
                    extra={"flex_direction_tablet": "column", "flex_gap": gap(48)})
    return section([row], bg=SKY, pad_y=96, pad_y_mob=64, max_w=1200,
                   inner_extra={"width": sz(1200)})

def stat(num, label):
    return container([
        heading(num, "div", WHITE, 52, "500", SERIF, "left", mobile=42),
        para(label, W70, 15, "left", lh=1.4),
    ], direction="column", gap_px=12, width=22,
        extra={"flex_align_items": "flex-start"})

def stats():
    row = container([
        stat("59,039", "missed calls recovered for Australian businesses so far today"),
        stat("1 in 3", "Calls to the average tradie go unanswered every single day"),
        stat("80%", "Of callers who get voicemail don't leave a message — they just call someone else"),
        stat("10s", "How long it takes us to text your missed caller back — every single time"),
    ], direction="row", gap_px=32, boxed=True, max_w=1200, wrap="wrap")
    return section([row], bg=INK, pad_y=72, pad_y_mob=56, inner_extra={"width": sz(1200)})

def step(num, title, body):
    circle = container([heading(num, "div", INK, 20, "500", SERIF, "center")],
                       direction="row", justify="center", align="center", bg=SKY2,
                       radius=999, width=44, width_unit="px",
                       extra={"height": sz(44), "min_height": sz(44),
                              "_element_width": "auto"}, gap_px=0, wrap="nowrap")
    return container([circle,
        heading(title, "h3", FG, 23, "500", SERIF, "left", lh=1.15),
        para(body, MUTED, 16, "left")],
        direction="column", gap_px=16, bg=CARD, radius=16, pad=px(34,32,34,32),
        border=BORDER, width=31, extra={"flex_align_items": "flex-start"})

def how():
    head = sec_head("How it works",
        heading("Set it up once.<br>We handle every missed call after that.",
                "h2", FG, 44, "500", SERIF, "center", lh=1.1, mobile=32),
        para("You keep your existing number. Calls you answer pass through completely "
             "normally. We only kick in the moment a call goes unanswered.",
             MUTED, 18, "center", lh=1.5))
    row = container([
        step("1", "Your phone rings. You can't get to it.",
             "You're on the tools, driving between jobs, in a consult room, or tied up with a customer. A potential job calls — and rings out. That's where we come in."),
        step("2", "Your caller gets a text in under 10 seconds.",
             "A friendly, professional text goes out from your business name. Plain English, in your voice. No robot language. It looks exactly like you sent it from your own phone."),
        step("3", "You see the conversation and call back the hot ones.",
             "When they reply, you get an instant notification with a link to the thread. Read what the job is — then only pick up the phone for the calls worth your time."),
    ], direction="row", gap_px=24, boxed=True, max_w=1200, wrap="wrap")
    return section([head, row], bg=BG, inner_gap=48, el_id="how", inner_extra={"width": sz(1200)})

def compare_card(tag, tag_bg, tag_color, rows, outcome, out_bg, out_color):
    kids = [pill(tag.upper(), tag_bg, tag_color, 12, "700", 1)]
    for h, d in rows:
        kids.append(container([
            heading(h, "div", WHITE, 16, "600", SANS, "left"),
            para(d, W55, 14.5, "left", lh=1.4),
        ], direction="column", gap_px=3,
            extra={"border_border": "solid",
                   "border_width": px(1,0,0,0),
                   "border_color": "rgba(255,255,255,0.08)",
                   "padding": px(14,0,14,0)}))
    kids.append(container([para("<strong>Outcome:</strong> " + outcome, out_color, 14.5, "left")],
                direction="column", bg=out_bg, radius=12, pad=px(14,16,14,16),
                extra={"margin": px(10,0,0,0)}))
    return container(kids, direction="column", gap_px=0,
                    bg="rgba(255,255,255,0.03)", radius=20, pad=px(34),
                    border="rgba(255,255,255,0.08)", width=47,
                    extra={"flex_align_items": "flex-start"})

def difference():
    head = sec_head("The difference",
        heading('What happens to a missed call — <i>with and without</i> Catch AI.',
                "h2", WHITE, 44, "500", SERIF, "center", lh=1.1, mobile=32),
        para("You can't always pick up. What happens next determines whether that caller "
             "becomes your job or your competitor's.", W70, 18, "center", lh=1.5),
        dark=True)
    without = compare_card("Without Catch AI", "rgba(190,60,60,0.28)", "#e79a9a",
        [("Your phone rings", "You're on a job and can't answer"),
         ("They hit voicemail", "A generic beep. Nothing personal."),
         ("80% hang up without leaving a message", "They're not going to wait around."),
         ("They Google the next tradie on the list", "Your competitor picks up. Or texts back first.")],
        "That job is gone. You never even knew it was there.",
        "rgba(120,40,40,0.28)", "#e6b0b0")
    with_ = compare_card("With Catch AI", "rgba(60,150,90,0.28)", "#a6e6bd",
        [("Your phone rings", "You're on a job and can't answer"),
         ("They get your text in 10 seconds", '"Hi! Sorry we missed you — what can we help with?"'),
         ("They reply with the job details", "They're talking to your business — not moving on."),
         ("You get notified instantly", "A tap shows you exactly what the job is.")],
        "You call back the ones worth your time. Job booked.",
        "rgba(40,110,70,0.28)", "#b6e8c6")
    row = container([without, with_], direction="row", gap_px=24, boxed=True,
                    max_w=1200, wrap="wrap")
    return section([head, row], bg=INK2, inner_gap=48, inner_extra={"width": sz(1200)})

def who_card(cat, title, body, img):
    return container([
        image("%s/%s" % (ASSET, img), width=100),
        container([
            heading(cat.upper(), "div", MUTED, 11.5, "600", SANS, "left", ls=1.2),
            heading(title, "h3", FG, 24, "500", SERIF, "left"),
            para(body, MUTED, 15.5, "left"),
        ], direction="column", gap_px=10, pad=px(26,26,30,26)),
    ], direction="column", gap_px=0, bg=CARD, radius=16, width=31,
        extra={"overflow": "hidden", "flex_align_items": "flex-start"})

def who():
    head = sec_head("Who it's for",
        heading("If you're on the tools,<br>you're missing calls.", "h2", FG, 44,
                "500", SERIF, "center", lh=1.1, mobile=32),
        para("Catch AI works for any trade or service business where the phone rings and "
             "no one can always pick up. Sound familiar?", MUTED, 18, "center", lh=1.5))
    cards = [
        who_card("Tradies", "Plumbers", "Knee-deep in a bathroom reno when a burst pipe enquiry calls. That's an $800 emergency callout handed to the next name on Google — before you could even dry your hands.", "who-plumber.jpg"),
        who_card("Tradies", "Electricians", "Up on a roof or inside a live switchboard — your phone might as well be in another suburb. By the time you're out, they've already called someone else and booked them in.", "who-electrician.jpg"),
        who_card("Tradies", "Locksmiths", "Locked-out callers ring three tradies and book the first one to reply. That first reply is now yours, automatically, in under 10 seconds — every single time.", "who-locksmith.jpg"),
        who_card("Professionals", "Real estate agents", "At an open home when your next listing enquiry calls. Miss that one call and you miss the appraisal — and everything that comes after it.", "who-realestate.jpg"),
        who_card("Service Businesses", "Health & beauty", "With a client on the table when a new booking enquiry rings. They book with whoever gets back to them first — and it's not going to be your voicemail.", "who-beauty.jpg"),
        who_card("Tradies", "Builders", "On a noisy site when a $50k renovation enquiry calls. Can't hear it. Can't answer. Can't even see you missed it for three hours. Catch AI catches it the second it rings out.", "who-builder.jpg"),
    ]
    row = container(cards, direction="row", gap_px=26, boxed=True, max_w=1200, wrap="wrap")
    return section([head, row], bg=MINT, inner_gap=48, el_id="who", inner_extra={"width": sz(1200)})

def price_card(tier, name, desc, price, feats, cta, dark=False, popular=False):
    fg = WHITE if dark else FG
    muted = W70 if dark else MUTED
    kids = []
    if popular:
        kids.append(pill("MOST POPULAR", LIME, INK, 12, "700", 0.8))
    kids += [
        heading(tier.upper(), "div", muted, 12, "600", SANS, "left", ls=1.2),
        heading(name, "h3", fg, 30, "500", SERIF, "left"),
        para(desc, muted, 15.5, "left"),
        container([
            heading(price, "div", fg, 52, "500", SERIF, "left", width_auto=True),
            para("per month · inc. GST", muted, 14, "left", width_auto=True),
        ], direction="row", align="flex-end", gap_px=10, wrap="nowrap"),
        icon_list(feats, color=fg, icon_color=(LIME if dark else SKY2)),
        button(cta, "#demo", (LIME if dark else INK), (INK if dark else WHITE),
               align="center", extra={"_element_width": "initial"}),
        para("No setup fee · No contract · Cancel any time", muted, 13, "center"),
    ]
    return container(kids, direction="column", gap_px=14,
                    bg=(INK if dark else CARD), radius=24, pad=px(40),
                    border=(INK if dark else BORDER), width=47,
                    extra={"flex_align_items": "flex-start"})

def pricing():
    head = sec_head("Pricing",
        heading("Two plans. No lock-in.<br>No setup fee.", "h2", FG, 44, "500",
                SERIF, "center", lh=1.1, mobile=32),
        para("Both plans are month-to-month. Cancel any time with 30 days notice. "
             "Setup takes 15 minutes and we do it with you on a call.", MUTED, 18,
             "center", lh=1.5))
    t1 = price_card("Tier 1", "Instant Text Back",
        "Every missed call gets a text back within 10 seconds. Simple and effective.",
        "$149",
        ["Text sent in under 10 seconds of a missed call",
         "In your business name and voice — not robot language",
         "Two-way SMS — they reply, you respond",
         "Instant notification when a customer texts back",
         "Simple web inbox — no app download needed",
         "Monthly leads-recovered report",
         "Works on any phone or number type"],
        "Try the demo first")
    t2 = price_card("Tier 2", "AI Qualifying",
        "The AI asks what the job is before you call back. You only talk to the ones worth your time.",
        "$249",
        ["Everything in Instant Text Back, plus:",
         "AI asks: What's the job? Which suburb? How urgent?",
         "Pre-qualified lead summary before you call back",
         "Filters tyre-kickers before they reach you",
         "Questions tailored to your trade or service type",
         "Book directly from the conversation",
         "Saves 2+ hours of follow-up calls every week"],
        "Try the demo free", dark=True, popular=True)
    row = container([t1, t2], direction="row", gap_px=28, boxed=True, max_w=940,
                    wrap="wrap", align="stretch")
    help_ = container([
        heading("Not sure which plan is right for you?", "div", FG, 22, "500", SERIF, "center"),
        para("Book a 15-minute call and we'll help you decide — no pressure.", MUTED, 16, "center"),
        button("Book a 15-minute call", "#demo", "rgba(0,0,0,0)", INK, align="center",
               extra={"border_border": "solid", "border_width": px(1),
                      "border_color": "rgba(0,0,0,0.18)"}),
    ], direction="column", align="center", gap_px=14,
        extra={"text_align": "center", "flex_align_items": "center"})
    return section([head, row, help_], bg=BG, inner_gap=48, el_id="pricing", inner_extra={"width": sz(1200)})

def tst_card(quote, name, role, initial):
    return container([
        heading("★★★★★", "div", LIME, 15, "400", SANS, "left", ls=2),
        para(quote, "rgba(255,255,255,0.9)", 16, "left", lh=1.6),
        container([
            container([heading(initial, "div", INK, 16, "600", SANS, "center")],
                      direction="row", justify="center", align="center", bg=AVATAR,
                      radius=999, width=40, width_unit="px",
                      extra={"height": sz(40), "min_height": sz(40), "_element_width": "auto"},
                      gap_px=0, wrap="nowrap"),
            container([
                heading(name, "div", WHITE, 15, "600", SANS, "left"),
                para(role, W55, 13, "left"),
            ], direction="column", gap_px=2, extra={"_element_width": "auto"}),
        ], direction="row", align="center", gap_px=12, wrap="nowrap",
            extra={"margin": px(8,0,0,0)}),
    ], direction="column", gap_px=16, bg="rgba(255,255,255,0.04)", radius=18,
        pad=px(32), border="rgba(255,255,255,0.08)", width=31,
        extra={"flex_align_items": "flex-start"})

def testimonials():
    head = sec_head("What clients say",
        heading("Tradies are recovering jobs<br>they didn't know they were losing.",
                "h2", WHITE, 44, "500", SERIF, "center", lh=1.1, mobile=32), dark=True)
    row = container([
        tst_card('"I had no idea how many calls I was missing every day. First month, I recovered 11 conversations I would have just lost. That\'s paid for itself ten times over."', "Dave M.", "Plumber · Parramatta, NSW", "D"),
        tst_card('"Set it up in 20 minutes on a Tuesday arvo. By Friday it had already replied to six callers while I was on jobs. Genuinely dead simple — I don\'t think about it at all now."', "Sarah K.", "Electrician · Brisbane, QLD", "S"),
        tst_card('"The AI qualifying is the best part. I used to call back every unknown number and waste half the morning. Now I only call the real jobs. Saves me two hours a week, easy."', "Marcus T.", "Locksmith · Melbourne, VIC", "M"),
    ], direction="row", gap_px=24, boxed=True, max_w=1200, wrap="wrap")
    disc = para("Testimonials are representative examples for illustration. Replace with "
                "your real clients' words as you collect them.", W55, 13.5, "center")
    return section([head, row, disc], bg=INK, inner_gap=44, inner_extra={"width": sz(1200)})

def faq():
    head = sec_head("FAQ",
        heading("Straight answers.", "h2", FG, 44, "500", SERIF, "center", mobile=32),
        max_w=760)
    items = [
        ("Does it replace my current phone number?", "No. You keep your existing mobile or landline exactly as it is. Calls you answer work completely normally — we never touch those. We only kick in when a call genuinely goes unanswered. Setting up the forwarding rule takes about 5 minutes and we walk you through it."),
        ("Will my customers know the text is automated?", "Most won't. The texts are written in plain, friendly language with your business name — they look exactly like you sent them from your own phone. We write the templates in your voice during the 15-minute setup call. We do include a legally required opt-out option in line with the Spam Act 2003, but the message itself is designed to feel personal, not robotic."),
        ("What if I actually pick up the call?", "Nothing happens. We only trigger a text when the call genuinely goes unanswered. If you pick up, the call passes through exactly as normal — no text is sent, no notification fires. Catch AI is completely invisible when you answer."),
        ("How do I reply to customers who text back?", "When a customer replies, you get a notification on your phone with a direct link. Tap it and you're in a simple inbox where you can read the full thread and reply. No app to download, no password to remember, works on any smartphone — including the one you already use for everything else."),
        ("Is this legal in Australia?", "Yes. We only send texts to people who called your number first — they initiated contact, so consent is clear. Every outbound text identifies your business by name and includes an opt-out option as required by the Spam Act 2003. We built compliance in from the start, not as an afterthought."),
        ("Is there a setup fee or contract?", "No setup fee. No contract. Both plans are month-to-month and you can cancel any time with 30 days written notice — no penalty, no fee, no fuss. We'd rather earn your business every month by delivering results than lock you in."),
        ("How long does setup take?", "About 15 minutes. We do a short onboarding call with you, set up the number forwarding, write your text templates together in your voice, and test it live before we finish. Most clients are fully live the same day they sign up."),
        ("What if the system has an outage?", "We monitor the system around the clock. If there's a disruption, we'll notify you immediately and work to restore service as fast as possible. In the meantime, your calls simply ring through as normal — no outgoing texts, but no missed calls either. We'll proactively reach out if anything affects your service."),
    ]
    tabs = []
    for q, a in items:
        tabs.append({"tab_title": q, "tab_content": "<p>%s</p>" % a, "_id": nid()[:7]})
    acc = W("accordion", {
        "tabs": tabs, "title_html_tag": "div",
        "selected_icon": {"value": "fas fa-plus", "library": "fa-solid"},
        "selected_active_icon": {"value": "fas fa-minus", "library": "fa-solid"},
        "title_color": FG, "tab_active_color": FG, "content_color": MUTED,
        "border_width": sz(1),
        "title_typography_typography": "custom", "title_typography_font_family": SERIF,
        "title_typography_font_size": sz(22), "title_typography_font_weight": "500",
        "content_typography_typography": "custom", "content_typography_font_family": SANS,
        "content_typography_font_size": sz(16), "content_typography_line_height": sz(1.6, "em"),
    })
    body = container([acc], direction="column", boxed=True, max_w=840, width=100)
    return section([head, body], bg=BG, inner_gap=48, el_id="faq",
                   inner_extra={"width": sz(1200)})

DEMO_FORM_HTML = """<div class="ca-demo-form">
  <label>Your name</label>
  <input type="text" placeholder="Dave">
  <label>Business name</label>
  <input type="text" placeholder="Dave's Plumbing">
  <label>Your mobile number</label>
  <input type="tel" placeholder="04__ ___ ___">
  <p class="ca-consent">By submitting, I agree to receive one demo call and text to this number to demonstrate the service. Reply STOP to opt out at any time.</p>
</div>
<style>
.ca-demo-form label{display:block;font:600 14px Inter,sans-serif;color:#161b24;margin:14px 0 6px}
.ca-demo-form input{width:100%;box-sizing:border-box;padding:14px 16px;border:1px solid #e0ded7;border-radius:12px;font:16px Inter,sans-serif;background:#f6f5f1;color:#161b24}
.ca-demo-form input:focus{outline:2px solid #73c0f0}
.ca-consent{font:13px Inter,sans-serif;color:#505561;margin:16px 0 0;line-height:1.5}
</style>"""

def demo_step(num, text):
    circle = container([heading(num, "div", WHITE, 14, "600", SANS, "center")],
                       direction="row", justify="center", align="center", bg=INK,
                       radius=999, width=30, width_unit="px",
                       extra={"height": sz(30), "min_height": sz(30), "_element_width": "auto"},
                       gap_px=0, wrap="nowrap")
    return container([circle, para(text, FG, 16, "left")],
                     direction="row", align="flex-start", gap_px=16, wrap="nowrap",
                     stack_mobile=False)

def demo():
    left = container([
        eyebrow("Try it now"),
        heading("Your next missed call doesn't have to be a lost job.", "h2", FG, 46,
                "500", SERIF, "left", lh=1.1, mobile=32),
        para("Try it on your own phone in 30 seconds. No account, no credit card, no commitment.",
             "#2b3340", 19, "left", lh=1.5),
        container([
            demo_step("1", "Enter your name, business name, and mobile number below."),
            demo_step("2", "Call our demo number — let it ring out, or decline it."),
            demo_step("3", "Check your texts. Reply like one of your customers would — watch what happens next."),
        ], direction="column", gap_px=20),
    ], direction="column", gap_px=24, width=52, extra={"flex_align_items": "flex-start", "width_tablet": sz(100,"%")})
    card = container([
        html_widget(DEMO_FORM_HTML),
        button("See the demo on my phone", "#", LIME, INK, align="center",
               extra={"_element_width": "initial"}),
        para("• No sign-up required&nbsp;&nbsp; • No credit card&nbsp;&nbsp; • One text, one call",
             MUTED, 13.5, "left"),
    ], direction="column", gap_px=16, bg=CARD, radius=24, pad=px(36), width=40,
        extra={"width_tablet": sz(100,"%"), "box_shadow_box_shadow_type": "yes",
               "box_shadow_box_shadow": {"horizontal": 0, "vertical": 30, "blur": 60,
               "spread": -26, "color": "rgba(20,30,60,0.35)"}})
    row = container([left, card], direction="row", align="center", gap_px=48,
                    boxed=True, max_w=1200,
                    extra={"flex_direction_tablet": "column"})
    return section([row], bg=SKY, pad_y=96, pad_y_mob=64, el_id="demo", inner_extra={"width": sz(1200)})

def foot_col(title, links):
    kids = [heading(title.upper(), "div", W55, 12, "600", SANS, "left", ls=1.2)]
    for t, u in links:
        kids.append(heading(t, "div", "rgba(255,255,255,0.82)", 15, "400", SANS, "left",
                            width_auto=True, extra={"link": {"url": u}}))
    return container(kids, direction="column", gap_px=12, width=17,
                     extra={"flex_align_items": "flex-start"})

def footer():
    about = container([
        container([
            container([heading("C", "div", INK, 15, "600", SANS, "center")],
                      direction="row", justify="center", align="center", bg=WHITE,
                      radius=999, width=30, width_unit="px",
                      extra={"height": sz(30), "min_height": sz(30), "_element_width": "auto"},
                      gap_px=0, wrap="nowrap"),
            heading("Catch AI", "div", WHITE, 22, "500", SERIF, "left", width_auto=True),
        ], direction="row", align="center", gap_px=10, wrap="nowrap"),
        para("Automatic missed-call text-back for Australian tradies and small businesses. "
             "Stop losing jobs to your voicemail.", W55, 15, "left", lh=1.5),
    ], direction="column", gap_px=18, width=30, extra={"flex_align_items": "flex-start"})
    cols = container([
        about,
        foot_col("Product", [("How it works", "#how"), ("Pricing", "#pricing"),
                             ("Try the demo", "#demo"), ("For plumbers", "#who"),
                             ("For electricians", "#who")]),
        foot_col("Company", [("About us", "#"), ("Contact", "#"), ("Blog", "#"),
                             ("Case studies", "#")]),
        foot_col("Legal", [("Privacy Policy", "#"), ("Terms of Service", "#"),
                           ("Acceptable Use", "#")]),
    ], direction="row", gap_px=48, boxed=True, max_w=1200, wrap="wrap",
        extra={"flex_align_items": "flex-start"})
    bottom = container([
        para("© 2025 Catch AI Australia · ABN [YOUR ABN] · Based in Australia", W55, 13.5, "left"),
        para("All texts comply with the Spam Act 2003 and include a mandatory opt-out.", W55, 13.5, "left"),
    ], direction="column", gap_px=6, boxed=True, max_w=1200,
        extra={"border_border": "solid", "border_width": px(1,0,0,0),
               "border_color": "rgba(255,255,255,0.1)", "padding": px(28,0,0,0),
               "margin": px(40,0,0,0), "width": sz(1200)})
    return section([cols, bottom], bg=INK, pad_y=72, pad_y_mob=56, inner_gap=0,
                   inner_extra={"width": sz(1200)})

# ================================================================ ASSEMBLE
elements = [header(), hero(), stats(), how(), difference(), who(), pricing(),
            testimonials(), faq(), demo(), footer()]

page_settings = {
    "background_background": "classic",
    "background_color": BG,
}

template = {
    "version": "0.4",
    "title": "Catch AI — Home",
    "type": "page",
    "page_settings": page_settings,
    "content": elements,
}

here = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(here, "catch-ai-elementor-template.json"), "w", encoding="utf-8") as f:
    json.dump(template, f, ensure_ascii=False, indent=1)
with open(os.path.join(here, "catch-ai-elementor-data.json"), "w", encoding="utf-8") as f:
    json.dump(elements, f, ensure_ascii=False)

# ---- global styles (colors + typography) for the applier
global_styles = {
    "system_colors": [
        {"_id": "primary",   "title": "Primary",   "color": INK},
        {"_id": "secondary", "title": "Secondary", "color": MUTED},
        {"_id": "text",      "title": "Text",      "color": FG},
        {"_id": "accent",    "title": "Accent",    "color": LIME},
    ],
    "custom_colors": [
        {"_id": "ca_sky",  "title": "Sky",        "color": SKY},
        {"_id": "ca_ink2", "title": "Ink 2",      "color": INK2},
        {"_id": "ca_mint", "title": "Mint",       "color": MINT},
        {"_id": "ca_bg",   "title": "Background",  "color": BG},
        {"_id": "ca_accent","title": "Accent Green","color": ACCENT},
        {"_id": "ca_card", "title": "Card",       "color": CARD},
        {"_id": "ca_border","title": "Border",     "color": BORDER},
    ],
    "system_typography": [
        {"_id": "primary",   "title": "Primary",   "typography_typography": "custom",
         "typography_font_family": SERIF, "typography_font_weight": "500"},
        {"_id": "secondary", "title": "Secondary", "typography_typography": "custom",
         "typography_font_family": SANS, "typography_font_weight": "500"},
        {"_id": "text",      "title": "Text",      "typography_typography": "custom",
         "typography_font_family": SANS, "typography_font_weight": "400"},
        {"_id": "accent",    "title": "Accent",    "typography_typography": "custom",
         "typography_font_family": SANS, "typography_font_weight": "600"},
    ],
}
with open(os.path.join(here, "catch-ai-global-styles.json"), "w", encoding="utf-8") as f:
    json.dump(global_styles, f, ensure_ascii=False, indent=1)

# ---- quick structural sanity check
def check(el, path="root"):
    assert "id" in el and "elType" in el and "settings" in el and "elements" in el, path
    for i, c in enumerate(el["elements"]):
        check(c, path + "/%s[%d]" % (el.get("widgetType") or el["elType"], i))
for i, e in enumerate(elements):
    check(e, "top[%d]" % i)

n_widgets = 0; n_containers = 0
def count(el):
    global n_widgets, n_containers
    if el["elType"] == "widget": n_widgets += 1
    else: n_containers += 1
    for c in el["elements"]: count(c)
for e in elements: count(e)
print("OK  sections=%d containers=%d widgets=%d total_ids=%d" %
      (len(elements), n_containers, n_widgets, _counter[0]-0x100000))
