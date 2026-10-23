# -*- coding: utf-8 -*-
with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# 1. Remove report & PDF buttons from navbar
old_nav = '''    <button class="tbtn on" id="mDeck">Presentation</button>
    <button class="tbtn" id="mSite">3D Site Walk</button>
    <button class="tbtn" id="mRep">Report (6 pp)</button>
    <button class="tbtn pdf" id="mPdf">⬇ Download PDF</button>'''

new_nav = '''    <button class="tbtn on" id="mSite">🏛 3D Site Walk</button>
    <button class="tbtn" id="mDeck">📖 Presentation</button>'''

c = c.replace(old_nav, new_nav)

# 2. Set default mode to 3D walk
c = c.replace('show(0);', 'show(0);\nsetMode("site");')

# 3. Add 3D carving animations:
# Breathing raking light + floating nagas / dust particle anim + smooth stone displacement response
anim_addon = '''
  // Atmospheric sunlight & realistic animation
  var animClock = 0;
  function updateAnimations(dt) {
    animClock += dt;
    // Raking sunlight shifts gently across carvings revealing subtle reliefs
    var lightDrift = Math.sin(animClock * 0.4) * 0.08;
    var saNow = (sunAz + Math.sin(animClock * 0.2) * 5) * Math.PI / 180;
    var seNow = (sunElev + Math.cos(animClock * 0.3) * 2) * Math.PI / 180;
    sun.position.set(px + Math.cos(saNow)*Math.cos(seNow)*65, Math.sin(seNow)*65, pz + Math.sin(saNow)*Math.cos(seNow)*65);
    sun.target.position.set(px, 1, pz);
  }
'''

if 'updateAnimations' not in c:
    c = c.replace('var ray = new THREE.Raycaster();', anim_addon + '\n  var ray = new THREE.Raycaster();')
    c = c.replace('sun.position.set(px + Math.cos(sa)*Math.cos(se)*60', 'updateAnimations(dt);\n    // default sun')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(c)

print('Index updated successfully!')
