import os
import subprocess
import shutil

cwd = os.getcwd().replace('\\', '/')
img_shore = f'file:///{cwd}/img_cache/shore.png'
img_rathas = f'file:///{cwd}/img_cache/rathas.png'
img_ganga = f'file:///{cwd}/img_cache/ganga.png'
img_varaha = f'file:///{cwd}/img_cache/varaha.png'
img_durga = f'file:///{cwd}/img_cache/durga.png'
img_arch = f'file:///{cwd}/img_cache/arch.png'

html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Sculpture Thematic Analysis — Mahabalipuram</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@fontsource/marcellus@5/index.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@fontsource/alegreya-sans@5/400.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@fontsource/alegreya-sans@5/500.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@fontsource/alegreya-sans@5/700.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@fontsource/alegreya-sans@5/400-italic.css">
<style>
@page {{
  size: A4;
  margin: 12mm 15mm;
}}
:root {{
  --disp: 'Marcellus', Georgia, serif;
  --body: 'Alegreya Sans', system-ui, sans-serif;
  --pink: #242220;
  --gold: #b38226;
  --rust: #9e432c;
  --teal: #1f7a75;
}}
* {{ margin:0; padding:0; box-sizing:border-box; }}
body {{
  font-family: var(--body);
  color: var(--pink);
  background: #ffffff;
  line-height: 1.5;
  font-size: 13.5px;
  -webkit-print-color-adjust: exact;
  print-color-adjust: exact;
}}
.sheet {{
  page-break-after: always;
  padding: 8px 0 16px 0;
  position: relative;
  min-height: 94vh;
  display: flex;
  flex-direction: column;
}}
.sheet:last-child {{
  page-break-after: auto;
}}
.rhead {{
  display: flex;
  justify-content: space-between;
  font-size: 8.5px;
  letter-spacing: .24em;
  text-transform: uppercase;
  color: #7a776e;
  border-bottom: 1.5px solid var(--pink);
  padding-bottom: 6px;
  margin-bottom: 14px;
}}
h3 {{
  font-family: var(--disp);
  font-size: 22px;
  color: #1a1816;
  margin: 10px 0 6px;
  line-height: 1.2;
}}
.sheet h3:first-of-type {{ margin-top: 0; }}
h4 {{
  font-size: 10.5px;
  letter-spacing: .22em;
  text-transform: uppercase;
  color: var(--rust);
  margin: 12px 0 6px;
  font-weight: 700;
}}
p {{
  font-size: 13px;
  line-height: 1.6;
  margin-bottom: 8px;
  text-align: justify;
}}
p.abs {{
  font-style: italic;
  color: #4c4a44;
  background: #f8f6f0;
  border-left: 3px solid var(--gold);
  padding: 10px 14px;
  margin-bottom: 12px;
  font-size: 12.5px;
}}
.rledg {{
  margin: 10px 0 14px;
  font-size: 12.5px;
  background: #faf9f6;
  border: 1px solid #e2ded5;
  padding: 8px 14px;
}}
.rledg div {{
  display: flex;
  gap: 12px;
  padding: 4px 0;
  border-bottom: 1px dotted rgba(43,43,46,.25);
}}
.rledg div:last-child {{ border-bottom: none; }}
.rledg b {{
  min-width: 140px;
  font-size: 9.5px;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: #6a675e;
}}
.rledg span {{
  font-weight: 600;
  color: #1a1816;
}}
.rfig {{
  margin: 10px auto;
  border: 1px solid #d5cfc4;
  padding: 6px;
  background: #fcfbf9;
  text-align: center;
  max-width: 96%;
}}
.rfig img {{
  width: 100%;
  max-height: 220px;
  object-fit: cover;
  display: block;
}}
.rfig .rc {{
  font-size: 10px;
  font-style: italic;
  color: #5c5a52;
  padding-top: 5px;
  line-height: 1.4;
}}
.refs {{
  font-size: 11.5px;
  line-height: 1.6;
  margin-left: 18px;
}}
.refs li {{
  margin-bottom: 5px;
}}
.pnum {{
  margin-top: auto;
  padding-top: 12px;
  text-align: center;
  font-size: 9.5px;
  letter-spacing: .3em;
  color: #8c8980;
  border-top: 1px solid #eae6de;
}}
</style>
</head>
<body>

<!-- PAGE 1 -->
<section class="sheet">
  <div class="rhead"><span>Sculpture Thematic Analysis · Mahabalipuram</span><span>21LEM301T · CO2 · 10 MARKS</span></div>
  <h3>Sculpture Thematic Analysis: The Rock-Cut Sculptures of Mahabalipuram</h3>
  <p class="abs">This presentation reads the open-air reliefs, cave shrines and monolithic rathas of Mahabalipuram as one legible program, identifying four recurring themes — the descent of divine grace, gods in narrative action, the sanctification of everyday life, and royal piety — and examining the iconographic language of scale, register, attribute and gesture through which those themes are communicated.</p>
  <div class="rledg">
    <div><b>Submitted by</b><span>HARINISH S V (Registration No: RA2411030010137)</span></div>
    <div><b>Course & Section</b><span>21LEM301T — Indian Art Form · Section Y1 · Assignment 5</span></div>
    <div><b>Institution</b><span>SRM Institute of Science and Technology · Faculty of Science and Humanities</span></div>
  </div>
  <figure class="rfig">
    <img src="{img_shore}" alt="Shore Temple">
    <figcaption class="rc">Fig. 1 — Shore Temple, Mamallapuram: structural granite architecture growing out of the rock-cut tradition.</figcaption>
  </figure>
  <div class="pnum">— PAGE 1 OF 6 —</div>
</section>

<!-- PAGE 2 -->
<section class="sheet">
  <div class="rhead"><span>Sculpture Thematic Analysis · Mahabalipuram</span><span>21LEM301T · CO2 · 10 MARKS</span></div>
  <h3>1. The Site and Its Method</h3>
  <p>Mamallapuram, the Pallava port on the Coromandel coast, was carved <strong>c. 630–730 CE</strong> almost entirely from one outcrop of charnockite granite. Three formats speak one language here: <strong>open-air reliefs</strong>, <strong>cave shrines (mandapas)</strong> and <strong>monolithic rathas</strong>. A UNESCO World Heritage Site since 1984, it remains the clearest primary text of early South Indian iconography.</p>
  <p>Because the whole complex rises from one outcrop, stylistic change across the site can be read like stratigraphy: earlier soft modelling hardens into the crisp ornament of the late mandapas.</p>
  <h3>2. Patronage: The Lion of the Pallavas</h3>
  <p>Under <strong>Narasimhavarman I 'Mamalla'</strong> and his successors, sculpture became state theology: the king's title and the god's image share the same stone. The seated lion at every pillar base is at once <strong>structural support, dynastic signature and protective deity</strong>. Port wealth funded workshops across generations — the site preserves its own artistic evolution in place.</p>
  <p>The vyala pillar base is the site's signature: a heraldic animal converted into load-bearing ornament, binding dynastic identity to sacred architecture.</p>
  <figure class="rfig">
    <img src="{img_rathas}" alt="Pancha Rathas">
    <figcaption class="rc">Fig. 2 — Pancha Rathas: monolithic prototypes cut top-down from single boulders.</figcaption>
  </figure>
  <div class="pnum">— PAGE 2 OF 6 —</div>
</section>

<!-- PAGE 3 -->
<section class="sheet">
  <div class="rhead"><span>Sculpture Thematic Analysis · Mahabalipuram</span><span>21LEM301T · CO2 · 10 MARKS</span></div>
  <h3>3. Theme I — The Sacred Descends: The Descent of the Ganges</h3>
  <p>A natural cleft in the boulder <strong>becomes the river</strong>: geology recruited into theology, with nagas and naginis rising inside it. Hundreds of figures — gods, sages, kings, animals — walk in <strong>one direction</strong>: composition itself performs pilgrimage. The double reading (<strong>Arjuna's penance</strong> / <strong>Bhagiratha bringing Ganga down</strong>) is deliberate polysemy, not confusion.</p>
  <p>The relief's genius is temporal: it depicts not an event but a process — descent — and uses the site's hydrology (water channelled through the cleft) to complete the narrative seasonally.</p>
  <figure class="rfig">
    <img src="{img_ganga}" alt="Descent of the Ganges">
    <figcaption class="rc">Fig. 3 — The great open-air relief; the natural cleft performs the river.</figcaption>
  </figure>
  <div class="pnum">— PAGE 3 OF 6 —</div>
</section>

<!-- PAGE 4 -->
<section class="sheet">
  <div class="rhead"><span>Sculpture Thematic Analysis · Mahabalipuram</span><span>21LEM301T · CO2 · 10 MARKS</span></div>
  <h3>4. Theme II — Gods in Action</h3>
  <p><strong>Varaha rescuing Bhudevi</strong>: the earth personified as a woman, gently held — protection (rakshana) made visible in one gesture. In the same cave <strong>Trivikrama</strong> strides the cosmos: three steps measure earth, sky and heaven. Adjacent, <strong>Durga as Mahishasuramardini</strong> fights the buffalo demon — the goddess as warrior, eight-armed, lion-mounted.</p>
  <p>The Varaha panel is the site's most tender composition: the boar's foreleg cradles the goddess with a care that softens the cosmic scale of the myth.</p>
  <h3>5. Theme III — The Everyday Sanctified</h3>
  <p><strong>Krishna lifting Govardhana</strong> shelters cowherds and cattle — pastoral labour raised to myth without losing its sweat. Cows turning toward calves, milkmaids balancing pots: <strong>observation of daily life</strong> enters sacred stone. On the great relief a <strong>cat stands in mock penance</strong> with mice at its feet — humour as a theological footnote.</p>
  <p>The pastoral register at Mamallapuram is unusually empirical for its date: cattle anatomy, rope tension and pot-carrying posture are recorded, not stylised.</p>
  <figure class="rfig">
    <img src="{img_varaha}" alt="Varaha Mandapa">
    <figcaption class="rc">Fig. 4 — Varaha mandapa: Vishnu lifting Bhudevi; tenderness at cosmic scale.</figcaption>
  </figure>
  <div class="pnum">— PAGE 4 OF 6 —</div>
</section>

<!-- PAGE 5 -->
<section class="sheet">
  <div class="rhead"><span>Sculpture Thematic Analysis · Mahabalipuram</span><span>21LEM301T · CO2 · 10 MARKS</span></div>
  <h3>6. Iconographic Language: How the Stone Says It</h3>
  <p><strong>Hierarchy of scale</strong>: the divine is largest; attendants step down; the demon shrinks as he falls. <strong>Ayudhas and mudras are grammar</strong> — bow, trident, conch and the abhaya hand each fix a figure's meaning. <strong>Registers and pilasters</strong> frame narrative like verses; deliberate emptiness works as pause and emphasis.</p>
  <p>Once the grammar is fixed — scale for status, attribute for identity, direction for intent — even damaged panels at the site remain legible.</p>
  <h3>7. Artistic Significance: Thinking in Subtraction</h3>
  <p>The rathas are <strong>working models</strong>: experiments in translating timber and brick forms into monolithic stone. <strong>Unfinished faces preserve the workshop sequence</strong> — squared blocking first, imagery last. Pallava fluidity in hard granite <strong>anticipates the structural Dravida temple</strong> of the following century.</p>
  <p>Tool-marks on unfinished boulders record decisions: the carver blocks volumes before committing to iconography, exactly as a modern sculptor would.</p>
  <figure class="rfig">
    <img src="{img_durga}" alt="Mahishasuramardini">
    <figcaption class="rc">Fig. 5 — Mahishasuramardini panel: scale, attribute and gesture as grammar.</figcaption>
  </figure>
  <div class="pnum">— PAGE 5 OF 6 —</div>
</section>

<!-- PAGE 6 -->
<section class="sheet">
  <div class="rhead"><span>Sculpture Thematic Analysis · Mahabalipuram</span><span>21LEM301T · CO2 · 10 MARKS</span></div>
  <h3>8. Cultural Significance: A Port That Carved for the Sea</h3>
  <p>As a port, Mamallapuram <strong>exported its iconography with its cargo</strong> — echoes reach Java and the Khmer world. <strong>Shaiva, Vaishnava and Shakta shrines stand side by side</strong>: synthesis rather than sectarianism. The Shore Temple's vimanas doubled as a <strong>seamark</strong>: sculpture in civic and maritime service.</p>
  <p>Lakshmi, sea-born and elephant-crowned, is the fitting deity of a port: abundance arriving by water is the town's lived theology.</p>
  <h3>9. Conclusion: The Legible Mountain</h3>
  <p>Four themes — <strong>descent, divine action, sanctified everyday, royal piety</strong> — form one coherent program. The site's iconographic language became the <strong>grammar of later South Indian temple art</strong>. Mahabalipuram remains a <strong>primary text</strong>: stone that can be read, argued with, and re-read.</p>
  <p>The analysis closes where it began: with a mountain that a century of carvers turned into a sentence, and that thirteen centuries of viewers have continued to parse.</p>
  <h4>References</h4>
  <ol class="refs">
    <li>Srinivasan, K. R. <i>Cave Temples of the Pallavas.</i> New Delhi: Archaeological Survey of India, 1964.</li>
    <li>Lockwood, Michael. <i>Mamallapuram (Mahabalipuram).</i> Madras: New Era Publications, 1993.</li>
    <li>Dehejia, Vidya. <i>Indian Art.</i> London: Phaidon Press, 1997.</li>
    <li>UNESCO World Heritage Centre. “Group of Monuments at Mahabalipuram,” WHS 249, inscribed 1984.</li>
  </ol>
  <figure class="rfig">
    <img src="{img_arch}" alt="Archival photograph">
    <figcaption class="rc">Fig. 6 — The great relief in a 19th-century photograph: continuity of reading.</figcaption>
  </figure>
  <div class="pnum">— PAGE 6 OF 6 —</div>
</section>

</body>
</html>
'''

output_html = "report_exact.html"
with open(output_html, "w", encoding="utf-8") as f:
    f.write(html_content)
print(f"Created {output_html} successfully!")

# Now print to PDF using Edge / Chrome headless
edge_exe = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
if not os.path.exists(edge_exe):
    edge_exe = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

output_pdf = "Sculpture_Thematic_Analysis_Mahabalipuram_Harinish.pdf"
abs_html = os.path.abspath(output_html)

cmd = [
    edge_exe,
    "--headless",
    "--disable-gpu",
    "--no-pdf-header-footer",
    f"--print-to-pdf={output_pdf}",
    abs_html
]

print("Rendering PDF via headless browser engine...")
subprocess.run(cmd, check=True)
print(f"Generated {output_pdf} successfully! Size: {os.path.getsize(output_pdf)} bytes")
