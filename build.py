"""Generates the static HTML pages with a shared header and footer.
Run:  python3 build.py   (edit page content below, then re-run)"""
from pathlib import Path

ROOT = Path(__file__).parent
PAGES = [
    ("index.html", "Home"),
    ("about.html", "About Us"),
    ("goal7.html", "Goal 7"),
    ("engineering.html", "Engineering Solutions"),
    ("economic.html", "Economic Impact"),
    ("sources.html", "Sources"),
    ("disclaimer.html", "Disclaimer"),
]

def c(n):  # citation link to the Sources page
    return f'<a class="cite" href="sources.html#src{n}" aria-label="Source {n}">[{n}]</a>'

def layout(file, title, desc, body):
    cur = ' aria-current="page"'
    nav = "\n".join(
        f'        <li><a href="{f}"{cur if f == file else ""}>{t}</a></li>'
        for f, t in PAGES)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title} | Powering Tomorrow – SDG 7</title>
  <meta name="description" content="{desc}">
  <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>☀️</text></svg>">
  <link rel="stylesheet" href="css/styles.css">
</head>
<body>
  <a class="skip" href="#main">Skip to main content</a>
  <header class="site-header">
    <nav class="nav container" aria-label="Main">
      <a class="brand" href="index.html"><span class="brand-badge" aria-hidden="true">7</span> Powering Tomorrow</a>
      <button class="nav-toggle" aria-expanded="false" aria-controls="nav-links">☰ Menu</button>
      <ul class="nav-links" id="nav-links">
{nav}
      </ul>
    </nav>
  </header>
  <main id="main">
{body}
  </main>
  <footer class="site-footer">
    <div class="container footer-grid">
      <p>© <span id="year">2026</span> Powering Tomorrow — a student project on UN Sustainable Development Goal 7.</p>
      <p><a href="sources.html">Sources</a> · <a href="disclaimer.html">Disclaimer</a> · <a href="https://sdgs.un.org/goals/goal7" rel="noopener">UN SDG 7</a></p>
    </div>
  </footer>
  <script src="js/main.js"></script>
</body>
</html>
"""

def banner(eyebrow, h1, text):
    return f"""    <div class="page-banner"><div class="container">
      <p class="eyebrow">{eyebrow}</p>
      <h1>{h1}</h1>
      <p>{text}</p>
    </div></div>"""

content = {}

# ---------------- HOME ----------------
content["index.html"] = ("Home", "A public guide to UN Sustainable Development Goal 7: affordable, reliable, sustainable and modern energy for all.", f"""    <section class="hero">
      <div class="container">
        <p class="eyebrow">UN Sustainable Development Goal 7</p>
        <h1>Affordable and clean energy for everyone</h1>
        <p class="lead">Electricity lights classrooms, keeps vaccines cold and powers small businesses. Yet hundreds of millions of people still live without it. This site explains why Goal 7 matters, how engineers are solving the problem, and what it means for the economy.</p>
        <a class="btn" href="goal7.html">Learn about Goal 7</a>
        <a class="btn alt" href="engineering.html">See the solutions</a>
      </div>
    </section>

    <section>
      <div class="container">
        <h2>The energy gap at a glance</h2>
        <div class="grid">
          <div class="card stat"><strong>685<span> M</span></strong><p>people had no access to electricity in 2022 {c(2)}</p></div>
          <div class="card stat"><strong>2.1<span> B</span></strong><p>people still cook with polluting fuels such as wood, charcoal or kerosene {c(2)}</p></div>
          <div class="card stat"><strong>3.2<span> M</span></strong><p>deaths per year linked to household air pollution from cooking {c(5)}</p></div>
          <div class="card stat"><strong>16.2<span> M</span></strong><p>people worked in renewable energy worldwide in 2023 {c(6)}</p></div>
        </div>
      </div>
    </section>

    <section class="tint">
      <div class="container">
        <h2>Explore the site</h2>
        <div class="grid">
          <article class="card"><div class="icon" aria-hidden="true">🎯</div><h3><a href="goal7.html">Goal 7 explained</a></h3><p>The five targets, where the world stands today, and who is being left behind.</p></article>
          <article class="card"><div class="icon" aria-hidden="true">🛠️</div><h3><a href="engineering.html">Engineering solutions</a></h3><p>Solar mini-grids, wind, clean cookstoves, batteries and efficiency — how they work.</p></article>
          <article class="card"><div class="icon" aria-hidden="true">💡</div><h3><a href="economic.html">Economic impact</a></h3><p>Falling costs, new jobs and the price of doing nothing.</p></article>
          <article class="card"><div class="icon" aria-hidden="true">👥</div><h3><a href="about.html">About our group</a></h3><p>Meet the students behind this project and what each of us researched.</p></article>
        </div>
      </div>
    </section>""")

# ---------------- ABOUT ----------------
members = [
    ("AJ", "Alex Johnson", "Project lead &amp; Goal 7 research", "Coordinated the team, wrote the Goal 7 page and checked every statistic against the original reports."),
    ("PS", "Priya Sharma", "Engineering solutions", "Researched solar mini-grids, clean cookstoves and battery storage for the Engineering Solutions page."),
    ("ML", "Marcus Lee", "Economic analysis", "Studied cost trends and green jobs data from IRENA and the IEA for the Economic Impact page."),
    ("SO", "Sofia Okafor", "Web design &amp; sources", "Designed and built the website, checked accessibility, and managed the citation list."),
]
cards = "\n".join(f"""          <article class="card member"><div class="avatar" aria-hidden="true">{i}</div><h3>{n}</h3><p class="role">{r}</p><p>{d}</p></article>""" for i, n, r, d in members)
content["about.html"] = ("About Us", "Meet the student group behind the Powering Tomorrow SDG 7 project.", banner("About us", "Meet the team", "We are a group of students who chose Goal 7 because energy quietly underpins almost every other Sustainable Development Goal — health, education, jobs and climate.") + f"""
    <section>
      <div class="container">
        <h2>Group members</h2>
        <div class="grid">
{cards}
        </div>
      </div>
    </section>
    <section class="tint">
      <div class="container prose">
        <h2>Why we chose this goal</h2>
        <p>When a clinic has no reliable power, it cannot refrigerate vaccines. When a student has no light after sunset, homework stops. We wanted to understand why, in a world with abundant sunshine and wind, so many people still lack basic energy — and what practical, affordable fixes already exist.</p>
        <h2>How we worked</h2>
        <p>Each member researched one area using reports from the United Nations, the International Energy Agency (IEA), the International Renewable Energy Agency (IRENA), the World Bank and the World Health Organization. All figures on this site link to the <a href="sources.html">Sources</a> page.</p>
      </div>
    </section>""")

# ---------------- GOAL 7 ----------------
targets = [
    ("7.1", "By 2030, ensure universal access to affordable, reliable and modern energy services."),
    ("7.2", "By 2030, increase substantially the share of renewable energy in the global energy mix."),
    ("7.3", "By 2030, double the global rate of improvement in energy efficiency."),
    ("7.a", "By 2030, enhance international cooperation to facilitate access to clean energy research and technology, and promote investment in energy infrastructure."),
    ("7.b", "By 2030, expand infrastructure and upgrade technology for supplying modern and sustainable energy services in developing countries."),
]
rows = "\n".join(f"            <tr><th scope=\"row\">{t}</th><td>{d}</td></tr>" for t, d in targets)
content["goal7.html"] = ("Goal 7", "What UN Sustainable Development Goal 7 means, its targets, and global progress so far.", banner("The goal", "Goal 7: Affordable and Clean Energy", "“Ensure access to affordable, reliable, sustainable and modern energy for all.” — one of 17 goals adopted by every UN member state in 2015 " + c(1) + ".") + f"""
    <section>
      <div class="container two-col">
        <div class="prose">
          <h2>What does it actually mean?</h2>
          <p>Goal 7 is about more than switching to renewables. It asks for four things at once: energy that people can <strong>afford</strong>, that is <strong>reliable</strong> enough to depend on, that is <strong>sustainable</strong> for the planet, and that is <strong>modern</strong> — electricity and clean cooking rather than open fires.</p>
          <p>Energy is often called the “golden thread” of development because it connects to health, education, gender equality, jobs and climate action.</p>
        </div>
        <aside class="callout">
          <h3>Who is left behind?</h3>
          <p>Around 80% of people without electricity live in sub-Saharan Africa, many in rural areas far from the grid {c(2)}. Women and girls often spend hours each week collecting firewood for cooking.</p>
        </aside>
      </div>
    </section>
    <section class="tint">
      <div class="container">
        <h2>The five targets</h2>
        <div class="table-wrap">
          <table>
            <caption>Official SDG 7 targets (summarised from the UN {c(1)})</caption>
            <thead><tr><th scope="col">Target</th><th scope="col">What it aims for</th></tr></thead>
            <tbody>
{rows}
            </tbody>
          </table>
        </div>
      </div>
    </section>
    <section>
      <div class="container">
        <h2>Where are we now?</h2>
        <div class="grid">
          <div class="card"><h3>⚡ Electricity access</h3><p>Global access reached about 91% in 2022, but the number of people without power rose for the first time in a decade, to 685 million {c(2)}.</p></div>
          <div class="card"><h3>🔥 Clean cooking</h3><p>About 74% of people have clean cooking, leaving 2.1 billion relying on polluting fuels {c(2)}.</p></div>
          <div class="card"><h3>🌱 Renewables</h3><p>Renewables supplied under one-fifth of total final energy consumption in 2021 — far below what is needed {c(2)}.</p></div>
          <div class="card"><h3>📉 Efficiency</h3><p>Efficiency is improving at under half the 2.6% annual rate the target requires {c(2)}.</p></div>
        </div>
        <p class="note">On current trends, the world is not on track to meet Goal 7 by 2030 {c(1)} {c(2)}.</p>
      </div>
    </section>""")

# ---------------- ENGINEERING ----------------
sols = [
    ("☀️", "Solar home systems &amp; mini-grids", "A rooftop panel, battery and LED lights can power a home far from the grid. Mini-grids link panels and batteries to serve a whole village, often cheaper and faster than extending national power lines to remote areas " + c(4) + ".", "Remote and rural communities"),
    ("🌬️", "Wind power", "Turbines convert moving air into electricity. Onshore wind is now one of the cheapest sources of new power in many countries " + c(3) + ".", "Windy coastal and open regions"),
    ("🔋", "Battery storage", "Sun and wind vary. Lithium-ion and emerging chemistries store surplus power for evening use, making renewables reliable. Battery costs have fallen sharply over the last decade " + c(4) + ".", "Grids with lots of solar or wind"),
    ("🍲", "Clean cookstoves", "Improved biomass, LPG, biogas and electric induction stoves cut smoke indoors and reduce firewood use, directly tackling household air pollution " + c(5) + ".", "Households cooking on open fires"),
    ("💧", "Small hydropower", "Run-of-river turbines generate steady power from streams without large dams, suiting hilly areas.", "Mountain and river valley communities"),
    ("🏠", "Energy efficiency", "LED lighting, insulation, efficient motors and smart meters deliver the same service with less energy — often the cheapest “source” of energy of all " + c(4) + ".", "Everywhere"),
]
scards = "\n".join(f"""          <article class="card"><div class="icon" aria-hidden="true">{i}</div><h3>{t}</h3><p>{d}</p><p class="note"><strong>Best for:</strong> {b}</p></article>""" for i, t, d, b in sols)
content["engineering.html"] = ("Engineering Solutions", "Engineering technologies helping achieve SDG 7: solar, wind, storage, clean cooking and efficiency.", banner("Engineering", "Engineering solutions", "Engineers are not waiting for one big breakthrough — many proven technologies already exist. The challenge is designing them to be affordable, durable and right for local conditions.") + f"""
    <section>
      <div class="container">
        <h2>Key technologies</h2>
        <div class="grid">
{scards}
        </div>
      </div>
    </section>
    <section class="tint">
      <div class="container two-col">
        <div class="prose">
          <h2>Case study: a solar mini-grid</h2>
          <p>Picture a rural village 40 km from the nearest power line. Extending the grid could take years. Instead, engineers install:</p>
          <ol>
            <li><strong>Solar arrays</strong> sized to the village’s daytime demand.</li>
            <li><strong>A battery bank</strong> to supply lights, phones and fridges after dark.</li>
            <li><strong>An inverter and local distribution lines</strong> to deliver power to homes, shops and a clinic.</li>
            <li><strong>Pay-as-you-go smart meters</strong> so families buy only what they can afford, often by mobile money.</li>
          </ol>
          <p>The World Bank and IEA identify mini-grids and stand-alone solar as the least-cost way to connect a large share of people still without power {c(2)} {c(4)}.</p>
        </div>
        <aside class="callout">
          <h3>Design challenges</h3>
          <ul>
            <li>Dust, heat and humidity shorten equipment life</li>
            <li>Local technicians must be trained for repairs</li>
            <li>Batteries need responsible recycling</li>
            <li>Systems must grow as demand grows</li>
          </ul>
        </aside>
      </div>
    </section>""")

# ---------------- ECONOMIC ----------------
content["economic.html"] = ("Economic Impact", "The economics of SDG 7: falling renewable costs, green jobs, and the cost of energy poverty.", banner("Economics", "Economic impact", "Clean energy used to be the expensive option. Today it is often the cheapest — and energy access unlocks income, productivity and jobs.") + f"""
    <section>
      <div class="container two-col">
        <div>
          <h2>Renewables have become cheaper</h2>
          <p>According to IRENA, the global average cost of electricity from new solar PV fell by about 90% between 2010 and 2023, and around 81% of new renewable capacity added in 2023 produced power more cheaply than fossil-fuel alternatives {c(3)}.</p>
          <p class="note">Chart: approximate fall in average cost of new electricity, 2010–2023 {c(3)}.</p>
          <div class="bars" role="img" aria-label="Bar chart: solar PV costs fell about 90 percent, onshore wind about 70 percent, offshore wind about 63 percent between 2010 and 2023.">
            <div class="bar"><span>Solar PV</span><div class="bar-track"><div class="bar-fill" data-width="90%">−90%</div></div></div>
            <div class="bar"><span>Onshore wind</span><div class="bar-track"><div class="bar-fill" data-width="70%">−70%</div></div></div>
            <div class="bar"><span>Offshore wind</span><div class="bar-track"><div class="bar-fill" data-width="63%">−63%</div></div></div>
          </div>
        </div>
        <aside class="callout">
          <h3>What this means for households</h3>
          <p>Families using kerosene lamps can spend a significant share of their income on fuel. A small solar kit, paid in instalments, can cost less over time while giving brighter, safer light.</p>
        </aside>
      </div>
    </section>
    <section class="tint">
      <div class="container">
        <h2>Jobs and growth</h2>
        <div class="grid">
          <div class="card stat"><strong>16.2<span> M</span></strong><p>renewable energy jobs worldwide in 2023 {c(6)}</p></div>
          <div class="card stat"><strong>7.1<span> M</span></strong><p>of those jobs were in solar PV — the largest employer {c(6)}</p></div>
          <div class="card"><h3>Productive use</h3><p>Reliable power lets farmers run irrigation pumps and grain mills, tailors use electric machines and shops stay open after dark — turning energy into income.</p></div>
          <div class="card"><h3>Investment gap</h3><p>Clean energy investment is growing fast but remains concentrated in advanced economies and China; developing economies need far more finance {c(4)}.</p></div>
        </div>
      </div>
    </section>
    <section>
      <div class="container prose">
        <h2>The cost of doing nothing</h2>
        <p>Energy poverty has hidden costs: illness and early deaths from smoky kitchens {c(5)}, lost school and work hours, spoiled food and medicines, and exposure to volatile fossil-fuel prices. Investing in Goal 7 is therefore not only an environmental choice — it is an economic one.</p>
        <p>To explore the data yourself, try the interactive charts at Our World in Data {c(7)}.</p>
      </div>
    </section>""")

# ---------------- SOURCES ----------------
sources = [
    ("United Nations Department of Economic and Social Affairs. (n.d.). <em>Goal 7: Ensure access to affordable, reliable, sustainable and modern energy for all.</em> United Nations.", "https://sdgs.un.org/goals/goal7", "Goal definition, targets, overall progress."),
    ("IEA, IRENA, UNSD, World Bank &amp; WHO. (2024). <em>Tracking SDG 7: The Energy Progress Report 2024.</em> World Bank.", "https://trackingsdg7.esmap.org/", "Electricity access, clean cooking, renewables share, efficiency."),
    ("International Renewable Energy Agency. (2024). <em>Renewable Power Generation Costs in 2023.</em> IRENA.", "https://www.irena.org/Publications/2024/Sep/Renewable-Power-Generation-Costs-in-2023", "Cost declines for solar and wind."),
    ("International Energy Agency. (2024). <em>World Energy Outlook 2024.</em> IEA.", "https://www.iea.org/reports/world-energy-outlook-2024", "Mini-grids, storage, efficiency, investment trends."),
    ("World Health Organization. (2024). <em>Household air pollution</em> [Fact sheet]. WHO.", "https://www.who.int/news-room/fact-sheets/detail/household-air-pollution-and-health", "Health impacts of polluting cooking fuels."),
    ("International Renewable Energy Agency &amp; International Labour Organization. (2024). <em>Renewable Energy and Jobs: Annual Review 2024.</em> IRENA.", "https://www.irena.org/Publications/2024/Oct/Renewable-energy-and-jobs-Annual-review-2024", "Global renewable employment figures."),
    ("Ritchie, H., Rosado, P., &amp; Roser, M. (n.d.). <em>Energy.</em> Our World in Data.", "https://ourworldindata.org/energy", "Further interactive data for readers."),
]
items = "\n".join(f"""          <li id="src{i}">{t} <a href="{u}" rel="noopener">{u}</a><span class="used">Used for: {w}</span></li>""" for i, (t, u, w) in enumerate(sources, 1))
content["sources.html"] = ("Sources", "References cited on the Powering Tomorrow SDG 7 website.", banner("References", "Sources", "Every statistic on this site is linked to one of the sources below. References follow APA 7th edition style.") + f"""
    <section>
      <div class="container prose">
        <ol class="sources">
{items}
        </ol>
        <p class="note">All links were checked when the site was built. Figures may be updated in later editions of these reports.</p>
      </div>
    </section>""")

# ---------------- DISCLAIMER ----------------
content["disclaimer.html"] = ("Disclaimer", "Disclaimer for the Powering Tomorrow student SDG 7 website.", banner("Legal", "Disclaimer", "Please read this before relying on any information on this site.") + """
    <section>
      <div class="container prose">
        <h2>Educational project</h2>
        <p>This website was created by students as an academic assignment about UN Sustainable Development Goal 7. It is for educational purposes only and is not professional, engineering, financial or policy advice.</p>
        <h2>No affiliation</h2>
        <p>We are not affiliated with, endorsed by, or speaking on behalf of the United Nations, the International Energy Agency, IRENA, the World Bank, the World Health Organization or any other organisation mentioned. The SDG name and colour are used for educational identification only, in line with the UN’s guidelines for non-commercial use.</p>
        <h2>Accuracy of information</h2>
        <p>We have made every effort to summarise our sources accurately, and every figure is cited on the <a href="sources.html">Sources</a> page. However, statistics change as new reports are published, and some values have been rounded or simplified for a general audience. Please consult the original sources for the latest and most precise data.</p>
        <h2>External links</h2>
        <p>This site links to external websites. We are not responsible for their content, availability or privacy practices.</p>
        <h2>Images and names</h2>
        <p>Icons are standard emoji characters. Group member details on the About Us page are provided by the project team.</p>
      </div>
    </section>""")

for file, title in PAGES:
    t, desc, body = content[file]
    (ROOT / file).write_text(layout(file, t, desc, body), encoding="utf-8")
    print("wrote", file)
