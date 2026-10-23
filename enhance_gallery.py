# -*- coding: utf-8 -*-
with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update the top navbar to have Presentation first, then 3D Stone Gallery / Walk
old_nav = '''    <button class="tbtn on" id="mSite">🏛 3D Site Walk</button>
    <button class="tbtn" id="mDeck">📖 Presentation</button>'''

new_nav = '''    <button class="tbtn on" id="mDeck">📖 Presentation</button>
    <button class="tbtn" id="mSite">🏛 3D Stone Gallery</button>'''

text = text.replace(old_nav, new_nav)

# 2. Update button names & labels in CSS and UI
text = text.replace('WALK THE SCULPTORS\' SITE', '3D STONE GALLERY & RELIEF WALK')
text = text.replace('WALK THE OUTCROP', '3D STONE GALLERY')
text = text.replace('Mamallapuram · Open Site', 'Mamallapuram · 3D Stone Gallery')

# 3. Add a direct quick-switch button on the Cover Slide to jump straight into the 3D Stone Gallery
cover_cta_old = '</div><p class="abs">'
cover_cta_new = '''</div>
<div style="margin:20px 0 10px; display:flex; gap:12px; justify-content:center; flex-wrap:wrap;">
  <button id="ctaTo3D" style="padding:10px 24px; background:var(--gold); color:#1c1405; border:none; font-weight:700; font-size:11px; letter-spacing:.2em; text-transform:uppercase; cursor:pointer; border-radius:3px; box-shadow:0 0 20px rgba(217,164,65,0.4); transition:all .25s;">🏛 Explore 3D Stone Gallery</button>
  <button id="ctaNextSlide" style="padding:10px 24px; background:transparent; border:1px solid var(--teal); color:var(--teal); font-weight:600; font-size:11px; letter-spacing:.2em; text-transform:uppercase; cursor:pointer; border-radius:3px; transition:all .25s;">Next Slide →</button>
</div>
<p class="abs">'''

text = text.replace(cover_cta_old, cover_cta_new, 1)

# 4. Make sure presentation is loaded at first by default
text = text.replace('setMode("site");', 'setMode("deck");')

# 5. Add event listener for the cover buttons safely
listener_code = '''
  var cta3D = $("#ctaTo3D");
  if(cta3D) cta3D.onclick = function(){ setMode("site"); };
  var ctaNext = $("#ctaNextSlide");
  if(ctaNext) ctaNext.onclick = function(){ show(1); };
'''

if 'ctaTo3D' not in text:
    text = text.replace('show(0);', 'show(0);\n' + listener_code)

# 6. Enhance the 3D gallery with dynamic rotating pedestal previews & smooth animations
gallery_enhancement = '''
  // Gallery lighting & dynamic stone relief highlights
  var galleryClock = 0;
  function updateAnimations(dt) {
    galleryClock += dt;
    // Raking sunlight shifts softly to cast deep dramatic shadows in the carvings
    var sweepAngle = (sunAz + Math.sin(galleryClock * 0.35) * 8) * Math.PI / 180;
    var sweepElev = (sunElev + Math.cos(galleryClock * 0.45) * 4) * Math.PI / 180;
    sun.position.set(px + Math.cos(sweepAngle)*Math.cos(sweepElev)*70, Math.sin(sweepElev)*70, pz + Math.sin(sweepAngle)*Math.cos(sweepElev)*70);
    sun.target.position.set(px, 1, pz);
  }
'''

if 'galleryClock' not in text:
    text = text.replace('var animClock = 0;', gallery_enhancement)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print('Updated index.html: Presentation first, 3D Stone Gallery enhanced!')
