import os
import urllib.request
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, PageBreak, KeepTogether, HRFlowable
)
from reportlab.pdfgen import canvas

BASE_URL = "https://image.qwenlm.ai/public_source/6c87be1b-829a-4fdc-8974-0709bd18cf94/"
IMAGE_MAP = {
    "shore":   BASE_URL + "05ead0c5a-5e02-4867-b527-2a24ec786b337208.png",
    "rathas":  BASE_URL + "45ead0c5a-5e02-4867-b527-2a24ec786b338463.png",
    "lion":    BASE_URL + "15ead0c5a-5e02-4867-b527-2a24ec786b338045.png",
    "ganga":   BASE_URL + "25ead0c5a-5e02-4867-b527-2a24ec786b332494.png",
    "varaha":  BASE_URL + "55ead0c5a-5e02-4867-b527-2a24ec786b333261.png",
    "krishna": BASE_URL + "15ead0c5a-5e02-4867-b527-2a24ec786b336339.png",
    "durga":   BASE_URL + "45ead0c5a-5e02-4867-b527-2a24ec786b334701.png",
    "bhima":   BASE_URL + "05ead0c5a-5e02-4867-b527-2a24ec786b335274.png",
    "arch":    BASE_URL + "35ead0c5a-5e02-4867-b527-2a24ec786b338432.png"
}

CACHE_DIR = "img_cache"
os.makedirs(CACHE_DIR, exist_ok=True)
LOCAL_IMAGES = {}
for k, url in IMAGE_MAP.items():
    local_p = os.path.join(CACHE_DIR, f"{k}.png")
    if not os.path.exists(local_p):
        try:
            print(f"Downloading {k}...")
            urllib.request.urlretrieve(url, local_p)
        except Exception as e:
            print(f"Failed to download {k}: {e}")
    if os.path.exists(local_p):
        LOCAL_IMAGES[k] = local_p

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super(NumberedCanvas, self).__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super(NumberedCanvas, self).showPage()
        super(NumberedCanvas, self).save()

    def draw_page_decorations(self, page_count):
        self.saveState()
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#555555"))
        
        # Draw header on pages 2..N
        if self._pageNumber > 1:
            self.drawString(54, 755, "SRM INSTITUTE OF SCIENCE & TECHNOLOGY · 21LEM301T INDIAN ART FORM")
            self.drawRightString(558, 755, "SCULPTURE THEMATIC ANALYSIS · MAHABALIPURAM")
            self.setStrokeColor(colors.HexColor("#C99A3F"))
            self.setLineWidth(0.75)
            self.line(54, 748, 558, 748)

        # Draw footer on all pages
        self.setStrokeColor(colors.HexColor("#D0D0D0"))
        self.setLineWidth(0.5)
        self.line(54, 45, 558, 45)
        self.drawString(54, 34, "CANDIDATE: HARINISH S V (RA2411030010137) · SECTION Y1")
        self.drawRightString(558, 34, f"PAGE {self._pageNumber} OF {page_count}")
        self.restoreState()

def build_pdf(filename="Sculpture_Thematic_Analysis_Mahabalipuram_Harinish.pdf"):
    doc = SimpleDocTemplate(
        filename,
        pagesize=letter,
        leftMargin=54,
        rightMargin=54,
        topMargin=54,
        bottomMargin=54
    )

    styles = getSampleStyleSheet()

    c_primary = colors.HexColor("#1A1A1E")
    c_gold = colors.HexColor("#9C6F19")
    c_teal = colors.HexColor("#185F5B")
    c_dark = colors.HexColor("#2C2C30")

    # Custom styles
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=20,
        leading=24,
        textColor=c_primary,
        alignment=1, # Center
        spaceAfter=6
    )
    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=11,
        leading=15,
        textColor=c_gold,
        alignment=1,
        spaceAfter=14
    )
    h1_style = ParagraphStyle(
        'Heading1_Custom',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=16,
        textColor=c_teal,
        spaceBefore=8,
        spaceAfter=4,
        keepWithNext=True
    )
    h2_style = ParagraphStyle(
        'Heading2_Custom',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=14,
        textColor=c_gold,
        spaceBefore=6,
        spaceAfter=3,
        keepWithNext=True
    )
    body_style = ParagraphStyle(
        'Body_Custom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=11.5,
        textColor=c_dark,
        alignment=4, # Justified
        spaceAfter=5
    )
    caption_style = ParagraphStyle(
        'Caption_Custom',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=7.5,
        leading=9.5,
        textColor=colors.HexColor("#555555"),
        alignment=1, # Center
        spaceBefore=3,
        spaceAfter=6
    )
    abstract_style = ParagraphStyle(
        'Abstract_Custom',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=8.5,
        leading=12,
        textColor=colors.HexColor("#222222"),
        alignment=4,
        leftIndent=14,
        rightIndent=14,
        spaceAfter=8
    )

    story = []

    # ==================== PAGE 1 ====================
    story.append(Paragraph("SRM INSTITUTE OF SCIENCE AND TECHNOLOGY", ParagraphStyle('InstHeader', fontName='Helvetica-Bold', fontSize=10, leading=13, alignment=1, textColor=colors.HexColor("#555555"))))
    story.append(Paragraph("FACULTY OF SCIENCE AND HUMANITIES · DEPARTMENT OF VISUAL COMMUNICATION / ARTS", ParagraphStyle('SubHeader', fontName='Helvetica', fontSize=8, leading=10, alignment=1, textColor=colors.HexColor("#777777"), spaceAfter=10)))
    story.append(HRFlowable(width="100%", thickness=1.5, color=c_gold, spaceAfter=14))
    
    story.append(Paragraph("Sculpture Thematic Analysis", title_style))
    story.append(Paragraph("Thematic, Iconographic, and Socio-Religious Discourse in the Rock-Cut Sculptures of Mahabalipuram (Mamallapuram)", subtitle_style))
    
    # Meta Ledger Table
    ledger_data = [
        [Paragraph("<b>Course Code & Title:</b>", body_style), Paragraph("21LEM301T — Indian Art Form", body_style),
         Paragraph("<b>Assessment Type:</b>", body_style), Paragraph("Assignment 5 (Course Outcome 2)", body_style)],
        [Paragraph("<b>Student Name:</b>", body_style), Paragraph("HARINISH S V", body_style),
         Paragraph("<b>Registration Number:</b>", body_style), Paragraph("RA2411030010137", body_style)],
        [Paragraph("<b>Section / Year:</b>", body_style), Paragraph("Section Y1 · 2026", body_style),
         Paragraph("<b>Maximum Marks:</b>", body_style), Paragraph("10 Marks", body_style)],
        [Paragraph("<b>Dynastic Epoch:</b>", body_style), Paragraph("Pallava Dynasty (c. 630 – 730 CE)", body_style),
         Paragraph("<b>UNESCO Ref:</b>", body_style), Paragraph("WHS Criteria (i), (ii), (iii), (vi) [No. 249]", body_style)]
    ]
    t_ledger = Table(ledger_data, colWidths=[110, 142, 110, 142])
    t_ledger.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#F9F8F5")),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#D5C8A8")),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor("#EAE4D2")),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t_ledger)
    story.append(Spacer(1, 10))

    story.append(Paragraph("<b>EXECUTIVE ABSTRACT & THEMATIC OBJECTIVE</b>", h2_style))
    story.append(Paragraph(
        "This critical research paper conducts an exhaustive thematic and iconographic investigation into the 7th- and 8th-century "
        "CE rock-cut and structural monuments of Mahabalipuram (Mamallapuram), situated on the Coromandel coast of Tamil Nadu. "
        "Excavated and carved during the reigns of the Pallava monarchs—predominantly Mahendravarman I, Narasimhavarman I 'Mamalla', "
        "and Narasimhavarman II Rajasimha—the site constitutes one of the most intellectually cohesive sculptural ensembles in world "
        "art history. Moving beyond simple descriptive taxonomies, this paper interrogates the semiotic grammar through which four "
        "overarching thematic imperatives are articulated: (1) <i>The Descent of Divine Grace (Anugraha)</i> as embodied in hydrological and "
        "celestial convergence; (2) <i>Cosmic Deliverance and Dynamic Theophanies</i> wherein gods act as militant restorers of cosmic equilibrium (Dharma); "
        "(3) <i>The Sanctification of the Vernacular and Empirical Naturalism</i> wherein agrarian and pastoral observation is elevated to sacred "
        "theology; and (4) <i>Imperial Ideology and Dynastic Signature</i> wherein the rock-cut chisel functions as statecraft. "
        "By critically decoding hierarchies of scale, ayudha (weapon/attribute) syntax, postural flexion (tribhanga, atibhanga), and subtractive monolithic "
        "choreography, this study demonstrates that Mahabalipuram is not merely an open-air gallery, but a fully unified, syntactically legible theological mountain.",
        abstract_style
    ))
    
    if "shore" in LOCAL_IMAGES:
        story.append(Image(LOCAL_IMAGES["shore"], width=490, height=140))
        story.append(Paragraph("<b>Figure 1:</b> The Shore Temple (c. 700–728 CE) at Mamallapuram, illustrating the transition from subtractive rock-cut monoliths to maritime structural architecture.", caption_style))

    story.append(PageBreak())

    # ==================== PAGE 2 ====================
    story.append(Paragraph("1. Geological Medium, Spatial Topography, and Subtractive Craft", h1_style))
    story.append(Paragraph(
        "The sculptural phenomenon of Mahabalipuram cannot be understood apart from its geological reality. Unlike the soft, sedimentary "
        "sandstones exploited at Badami and Aihole by the contemporary Western Chalukyas, or the volcanic basalt traps carved at Ajanta and Ellora, "
        "the sculptors of the Pallava workshop were confronted with regional <b>charnockite granite</b>. Charnockite is an intensely hard, "
        "metamorphic rock characterized by hypersthene quartz crystals, quartz-feldspar intergrowths, and an extreme resistance to cleavage. "
        "This geological intractability necessitated a revolutionary departure in stone-working methodology. Pallava artisans did not simply "
        "chip away stone; they practiced a rigorous <i>subtractive epistemology</i>.",
        body_style
    ))
    story.append(Paragraph(
        "In the monolithic excavation of the <i>mandapas</i> (cave shrines) and <i>rathas</i> (free-standing monoliths), the carver worked strictly "
        "from the apex downward (top-down quarrying). There was zero margin for structural error: an unintended fracture or cleavage shear "
        "would compromise the entire architectural entity, as no masonry could be inserted or patched. Analysis of unfinished surfaces across "
        "the outcrop—such as the partially carved boulders south of the Lighthouse—reveals a standardized workshop workflow: linear channel trenches "
        "were cut around the boulder perimeter, followed by the insertion of dry wooden pegs which, when saturated with coastal water, expanded to split off "
        "volumetric granite blocks. Next, master sculptors gridded the surface using mineral pigments, blocked out somatic silhouettes, and gradually chiseled "
        "fine drapery, jewelry, and iconographic attributes. Hence, every finished sculpture represents the latent anatomical form extracted from the mountain.",
        body_style
    ))

    story.append(Paragraph("2. Imperial Patronage and Ideology: The Lion of the Pallavas", h1_style))
    story.append(Paragraph(
        "Under Narasimhavarman I (who earned the title <i>Mamalla</i>, 'The Great Wrestler', following his triumph over the Western Chalukyan king "
        "Pulakeshin II at Vatapi in 642 CE), sculpture was deliberately transformed into dynastic statecraft. The Pallavas claimed descent from the divine "
        "Brahma-Kshatriya lineage through the sage Bharadvaja, Drona, and Ashvatthaman. This legendary pedigree was given physical form through "
        "the ubiquitous heraldic motif of the <b>Vyala (Simha-vyala)</b>.",
        body_style
    ))
    
    if "lion" in LOCAL_IMAGES:
        story.append(Image(LOCAL_IMAGES["lion"], width=490, height=130))
        story.append(Paragraph("<b>Figure 2:</b> Pillar porch in the Varaha Mandapa showing the crouching heraldic Vyala (lion-base), synthesizing structural support, royal insignia, and apotropaic guardianship.", caption_style))

    story.append(Paragraph(
        "In cave mandapas such as the Varaha, Mahishasuramardini, and Kotikal mandapas, the standard architectural pillar base is completely replaced "
        "by a crouching or rampant lion carved in high relief. The beast is depicted with arched feline vertebrae, bared fangs, stylized ringlet manes, "
        "and bulging ocular orbs. This motif operates simultaneously on three distinct semantic levels: First, as a <i>structural member</i>, where the "
        "muscular neck of the lion transfers the dead load of the monolithic architrave to the stylobate; second, as an <i>apotropaic sentinel</i>, guarding "
        "the sanctum sanctorum against malignant spiritual intrusions; and third, as the <i>unmistakable royal sign-manual</i> of the Pallava dynasty. "
        "By walking through these pillared verandas, the devotee entered sacred space directly over the body of the king's totemic animal.",
        body_style
    ))

    story.append(PageBreak())

    # ==================== PAGE 3 ====================
    story.append(Paragraph("3. Theme I — Cosmic Descent and Hydrological Polysemy (The Great Relief)", h1_style))
    story.append(Paragraph(
        "Dominating the northern sector of the central outcrop is the monumental open-air bas-relief measuring approximately 29 meters in length by "
        "13 meters in height, conventionally known as either <b>The Descent of the Ganges (Gangavatarana)</b> or <b>Arjuna's Penance</b>. "
        "This colossal composition is universally recognized as the magnum opus of early medieval Indian narrative sculpture. Rather than flattening "
        "the rock surface into a conventional framed tableau, the Pallava master-sculptor incorporated the physical geology of the boulder directly into "
        "the mythic discourse. A prominent, natural vertical fissure divides the boulder into two asymmetric halves.",
        body_style
    ))

    if "ganga" in LOCAL_IMAGES:
        story.append(Image(LOCAL_IMAGES["ganga"], width=490, height=140))
        story.append(Paragraph("<b>Figure 3:</b> The Great Open-Air Relief: The natural geological cleft serves as the celestial river Ganga, flanked by ascending Nagas, soaring Vidyadharas, and the life-sized elephant herd.", caption_style))

    story.append(Paragraph(
        "<b>Hydrological Function and Polysemic Narrative:</b> In antiquity, a masonry cistern situated atop the cliff collected rainwater, which was "
        "channeled through a sluice gate down the central cleft. As the water cascaded into the pool below, it animated the sculpted world. Carved inside "
        "the fissure are the undulating serpentine bodies of <i>Apara-Nagaraja</i> and his consort, hands folded in <i>anjali mudra</i>, undulating upward "
        "toward the source of life. The surrounding granite is populated by over a hundred figures: celestial Gandharvas and Vidyadharas hovering weightlessly "
        "in the upper ether; Siddhas, Kinnaras, and Apsaras; earthly sovereigns and ascetics; and a magnificent panoramic bestiary featuring lions, tigers, "
        "monkeys, and a naturalistic matriarchal elephant herd sheltering calves beneath their bellies.",
        body_style
    ))
    story.append(Paragraph(
        "Crucially, the relief embodies deliberate <b>shlesha (theological double entendre)</b>. To the left of the cleft stands a emaciated ascetic "
        "performing rigorous tapas—standing on one leg, arms upraised in <i>urdhva-bahu</i>, his ribcage protruding under taut skin. Immediately beside him "
        "appears the four-armed Bhagavan Shiva, accompanied by his dwarfish Ganas, granting a boon with his right hand in <i>varada mudra</i>. "
        "Within Shaiva theology, this depicts Bhagiratha undergoing austerities to persuade Shiva to cushion the devastating descent of Ganga in his matted locks. "
        "Simultaneously, within the epic Mahabharata tradition, this depicts the Pandava hero Arjuna performing penance on Mount Indrakila to obtain the "
        "celestial weapon <i>Pashupatastra</i> from Lord Shiva. This intentional dual reading functioned as imperial flattery: the Pallava king was simultaneously "
        "likened to Bhagiratha (who brings divine abundance to his subjects) and Arjuna (the peerless warrior conqueror).",
        body_style
    ))

    story.append(PageBreak())

    # ==================== PAGE 4 ====================
    story.append(Paragraph("4. Theme II — Dynamic Heroic Theophanies: Gods Restoring Dharma", h1_style))
    story.append(Paragraph(
        "Contrasting with the cosmic calm of the Great Relief are the interior panels of the rock-cut mandapas, which explore dramatic kineticism "
        "and heroic divine intervention. Two panels stand out as masterpieces of visual rhetoric: the <b>Bhu-Varaha panel</b> in the Varaha Mandapa "
        "and the <b>Mahishasuramardini panel</b> in Cave 26.",
        body_style
    ))

    # Dual image side by side
    im_w = 238
    im_h = 115
    if "varaha" in LOCAL_IMAGES and "durga" in LOCAL_IMAGES:
        t_duo = Table([
            [Image(LOCAL_IMAGES["varaha"], width=im_w, height=im_h), Image(LOCAL_IMAGES["durga"], width=im_w, height=im_h)],
            [Paragraph("<b>Figure 4:</b> Bhu-Varaha lifting Bhudevi.", caption_style), Paragraph("<b>Figure 5:</b> Mahishasuramardini in kinetic combat.", caption_style)]
        ], colWidths=[245, 245])
        t_duo.setStyle(TableStyle([
            ('ALIGN', (0,0), (-1,-1), 'CENTER'),
            ('VALIGN', (0,0), (-1,-1), 'TOP'),
            ('BOTTOMPADDING', (0,0), (-1,-1), 0),
            ('TOPPADDING', (0,0), (-1,-1), 0),
        ]))
        story.append(t_duo)

    story.append(Paragraph(
        "<b>Bhu-Varaha: The Tenderness of Cosmic Power:</b> In the Varaha Mandapa, the third avatara of Vishnu is depicted rescuing Mother Earth (Bhudevi) "
        "from the primeval abyssal ocean. The colossal boar-headed deity stands with his right leg firmly planted on the hooded coils of the subterranean naga "
        "king Shesha. What renders this composition profound is the psychological contrast: while Varaha's muscular torso embodies cosmic power capable "
        "of overturning tectonic depths, his boar snout nuzzles Bhudevi with profound delicacy. The goddess sits serenely on his flexed right knee, her small, "
        "graceful limbs conveying total surrender and absolute security. Here, cosmic protection (<i>rakshana</i>) is translated into intimate somatic empathy.",
        body_style
    ))
    story.append(Paragraph(
        "<b>Mahishasuramardini: The Architecture of Moral Combat:</b> In the adjacent mandapa, the battle between Durga and the buffalo-headed titan "
        "Mahishasura is organized with cinematic dynamism. Durga is mounted atop her roaring lion, her eight arms radiating in an arc of lethal weaponry—bow, "
        "trident, chakra, shankha, and sword. Her torso leans forward in a posture of aggressive certainty (<i>alidhasana</i>). In stark contrast to later "
        "Chola and medieval depictions where the demon is already decapitated, here Mahishasura remains a formidable adversary: holding an iron club, "
        "his muscular human frame crowned with heavy buffalo horns. However, his psychological defeat is already signaled through spatial syntax: he recoils "
        "backward toward the right edge of the frame, his demonic attendants stumbling in disarray as the divine aura sweeps across the composition.",
        body_style
    ))

    story.append(Paragraph("5. Theme III — The Sanctified Vernacular: Govardhana & Moral Satire", h1_style))
    story.append(Paragraph(
        "Nowhere is the Pallava workshop's humanism more vivid than in the <b>Krishna Mandapa</b>. Krishna is depicted lifting Mount Govardhana with his left hand "
        "to shield the pastoral community of Gokula from the torrential storms unleashed by Indra. Rather than focusing exclusively on the miracle, the sculptors "
        "consecrated the daily life of cowherds (Ayars). A cowherd milks a seated cow while the cow tenderly curls her tongue around her suckling calf; a milkmaid "
        "balances a woven stack of earthenware pots on her head; a farmer holds a child on his shoulder; and a pastoral musician plays a fluted pipe. "
        "Sacred divinity here does not annihilate the everyday; it provides a protective canopy beneath which ordinary human and animal life flourishes.",
        body_style
    ))

    story.append(PageBreak())

    # ==================== PAGE 5 ====================
    story.append(Paragraph("6. Iconographic Grammar: Semiotic Mechanics of Pallava Sculpture", h1_style))
    story.append(Paragraph(
        "The sculptures of Mahabalipuram operate according to a precise semiotic grammar that can be dissected through four structural mechanisms:",
        body_style
    ))

    # Semiotic table
    sem_data = [
        [Paragraph("<b>Grammatical Device</b>", body_style), Paragraph("<b>Visual Implementation</b>", body_style), Paragraph("<b>Thematic / Theological Meaning</b>", body_style)],
        [Paragraph("<b>Hierarchy of Scale</b>", body_style), Paragraph("Gods carved 2–3× larger than attending humans; demons sized proportionally to moral deficit.", body_style), Paragraph("Ontological reality: spiritual authority visually dominates mundane material space.", body_style)],
        [Paragraph("<b>Ayudha & Mudra Syntax</b>", body_style), Paragraph("Chakra (wheel) held edgewise (<i>prayoga</i>); Shankha; Abhaya (fearlessness) & Varada mudras.", body_style), Paragraph("Attributes identify sectarian identity; archaic edge-on disc signals early Pallava dating.", body_style)],
        [Paragraph("<b>Postural Flexion</b>", body_style), Paragraph("<i>Samabhanga</i> for central deities; <i>tribhanga</i> for consorts; <i>alidhasana</i> for active warfare.", body_style), Paragraph("Equilibrium represents absolute transcendence; flexion denotes dynamic cosmic engagement.", body_style)],
        [Paragraph("<b>Somatic Naturalism</b>", body_style), Paragraph("Accurate rendering of bovine muscle, elephant skin folds, and bone ribcages in ascetics.", body_style), Paragraph("Rejection of rigid geometric stylization in favor of living, breathing biological reality.", body_style)]
    ]
    t_sem = Table(sem_data, colWidths=[120, 180, 204])
    t_sem.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#EFEBE2")),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#C4B89A")),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor("#D8CFC0")),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t_sem)
    story.append(Spacer(1, 8))

    story.append(Paragraph("7. Architectural Taxonomy and Subtractive Prototyping: The Pancha Rathas", h1_style))
    story.append(Paragraph(
        "South of the main hill lies the extraordinary group of five monolithic shrines known colloquially as the <b>Pancha Rathas</b> "
        "(Dharmaraja, Bhima, Arjuna, Draupadi, and Nakula-Sahadeva). These structures are not functional temples—none possesses a consecration "
        "inscription or an altar with a ritually installed lingam—but rather full-scale, three-dimensional architectural textbooks carved from a single "
        "declining granite whaleback outcrop.",
        body_style
    ))

    if "rathas" in LOCAL_IMAGES:
        story.append(Image(LOCAL_IMAGES["rathas"], width=490, height=130))
        story.append(Paragraph("<b>Figure 6:</b> The Pancha Rathas: Top-down monolithic experimental prototypes testing the stepped vimana, barrel-vaulted sala, and apsidal gajaprishta forms in living granite.", caption_style))

    story.append(Paragraph(
        "Each ratha experiments with a different regional timber and thatch building tradition, translating perishable vernacular forms into eternal stone: "
        "<b>Draupadi Ratha</b> copies the four-cornered hut (<i>kutagara</i>) with curved bamboo thatch roof and corner relief figures of Durga; "
        "<b>Arjuna and Dharmaraja Rathas</b> embody the classic stepped pyramidal Dravida superstructure (<i>tritala vimana</i>) crowned by octagonal "
        "shikharas, embellished with miniature pavilions (<i>kutas</i> and <i>salas</i>) and projecting horseshoe arches (<i>kudus</i>); "
        "<b>Bhima Ratha</b> replicates the massive oblong, barrel-vaulted wagon roof (<i>valabhi/sala-shikhara</i>), anticipating the grand gopuram "
        "gateways of the high medieval era; and <b>Nakula-Sahadeva Ratha</b> showcases the apsidal (<i>gajaprishta</i>, or elephant-back) chaitya plan, "
        "deliberately paired with a colossal life-sized monolithic elephant standing adjacent in the sand. Here, the architectural workshop actively "
        "codified the formal grammar of the South Indian temple.",
        body_style
    ))

    story.append(PageBreak())

    # ==================== PAGE 6 ====================
    story.append(Paragraph("8. Cultural Significance: A Maritime Metropolis and Trans-Oceanic Echoes", h1_style))
    story.append(Paragraph(
        "Mahabalipuram was not an isolated monastic hermitage; it was the bustling premier naval emporium of the Pallava empire, known in Greco-Roman "
        "records as <i>Melange</i> and in Chinese accounts as a terminal of the Maritime Silk Route. Merchant flotillas sailed from this shore to Sri Lanka, "
        "the Srivijaya empire of Sumatra and Java, and the early kingdoms of Cambodia (Funan and Chenla). The sculptures carved here were visual ambassadors "
        "of Indian civilization.",
        body_style
    ))
    story.append(Paragraph(
        "The syncretic coexistence of major theological schools—Shaiva, Vaishnava, and Shakta sanctuaries sitting peacefully within paces of each "
        "other—mirrors the cosmopolitan tolerance of an international port. Furthermore, Pallava architectural and iconographic vocabulary traveled "
        "directly across the Bay of Bengal: the makara toranas, kirtimukha faces, and stepped vimana profiles seen at Mahabalipuram reappear with striking "
        "fidelity in the 8th-century Dieng Plateau candis of Central Java and the pre-Angkorian brick towers of Sambor Prei Kuk in Cambodia.",
        body_style
    ))

    story.append(Paragraph("9. Critical Conclusion: The Living Text of Living Basalt", h1_style))
    story.append(Paragraph(
        "The rock-cut sculptures of Mahabalipuram represent a watershed moment in the history of Asian art. By subjecting intractable charnockite "
        "granite to their conceptual will, the Pallava sculptors achieved a synthesis of theology, geology, and royal ambition that remains unparalleled. "
        "The thematic threads identified throughout this analysis—the descent of grace through geological fissure, the dynamic defense of moral order, "
        "the tender celebration of pastoral labor, and the codification of architectural form—are not disparate decorative choices. They constitute a "
        "fully unified philosophical universe. Thirteen centuries of salt-laden sea winds and monsoon rains have weathered the stone, but its iconographic "
        "sentence remains crystal clear: divinity is not remote from creation; it is carved into the very bones of the earth.",
        body_style
    ))

    story.append(Paragraph("<b>SCHOLARLY REFERENCES & ARCHIVAL SOURCES</b>", h2_style))
    refs = [
        "1. <b>Srinivasan, K. R.</b> (1964). <i>Cave-Temples of the Pallavas</i>. Architectural Survey of Temples, No. 1. New Delhi: Archaeological Survey of India (ASI).",
        "2. <b>Lockwood, Michael, Siromoney, Gift, & Dayanandan, P.</b> (1974). <i>Mahabalipuram Studies</i>. Madras: Christian Literature Society.",
        "3. <b>Dehejia, Vidya</b> (1997). <i>Indian Art</i>. Art & Ideas Series. London: Phaidon Press.",
        "4. <b>Harle, J. C.</b> (1994). <i>The Art and Architecture of the Indian Subcontinent</i>. Pelican History of Art. New Haven: Yale University Press.",
        "5. <b>Nagaswamy, R.</b> (2008). <i>Mahabalipuram: Monumental Legacy</i>. New Delhi: Oxford University Press.",
        "6. <b>UNESCO World Heritage Centre</b> (1984). <i>Group of Monuments at Mahabalipuram</i>. Advisory Body Evaluation, Ref. 249."
    ]
    for r in refs:
        story.append(Paragraph(r, ParagraphStyle('RefItem', parent=body_style, fontSize=7.5, leading=10, leftIndent=12, spaceAfter=2)))

    story.append(Spacer(1, 10))
    story.append(HRFlowable(width="100%", thickness=1, color=c_gold, spaceAfter=8))
    
    # Sign-off block
    sign_data = [
        [Paragraph("<b>Candidate Signature:</b> Harinish S V", body_style), Paragraph("<b>Faculty Evaluation:</b> ____________________", body_style)],
        [Paragraph("<b>Date of Submission:</b> October 2026", body_style), Paragraph("<b>Marks Awarded:</b> ______ / 10 Marks", body_style)]
    ]
    t_sign = Table(sign_data, colWidths=[250, 254])
    t_sign.setStyle(TableStyle([
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
    ]))
    story.append(t_sign)

    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"Successfully generated {filename}")

if __name__ == "__main__":
    build_pdf()
