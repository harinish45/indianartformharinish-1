# -*- coding: utf-8 -*-
with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Add Camera Views section in settings panel #sPanel
old_panel_snippet = '''      <h6>Time of day</h6>
      <div class="row" id="pTime">
        <button data-t="dawn">Dawn</button><button data-t="day">Day</button><button data-t="golden" class="on">Golden</button><button data-t="dusk">Dusk</button><button data-t="night">Night</button>
      </div>'''

new_panel_snippet = '''      <h6>Camera Views</h6>
      <div class="row" id="pViews">
        <button data-v="walk" class="on">Walk</button>
        <button data-v="drone">Drone</button>
        <button data-v="aerial">Aerial</button>
        <button data-v="shore">Shore</button>
        <button data-v="ganga">Ganges</button>
        <button data-v="rathas">Rathas</button>
      </div>
      <h6>Time of day</h6>
      <div class="row" id="pTime">
        <button data-t="dawn">Dawn</button><button data-t="day">Day</button><button data-t="golden" class="on">Golden</button><button data-t="dusk">Dusk</button><button data-t="night">Night</button>
      </div>'''

text = text.replace(old_panel_snippet, new_panel_snippet, 1)

# 2. Add quick Drone View toggle button in the bottom HUD right above other buttons
old_hud_btn = '<button class="hudbtn on" id="sSun">Raking light · on</button>'
new_hud_btn = '<button class="hudbtn" id="sDrone">🚁 Drone view</button>\n    <button class="hudbtn on" id="sSun">Raking light · on</button>'

text = text.replace(old_hud_btn, new_hud_btn, 1)

# Style for the new Drone button in HUD
old_style_hud = '#sSun{bottom:90px} #sTour{bottom:52px} #sLamp{bottom:14px}'
new_style_hud = '#sDrone{bottom:128px} #sSun{bottom:90px} #sTour{bottom:52px} #sLamp{bottom:14px}'
text = text.replace(old_style_hud, new_style_hud, 1)

# Update instructions text in bottom-left HUD to mention V for Views
text = text.replace('<b>T</b> tour · <b>N</b> night', '<b>V</b> drone · <b>T</b> tour · <b>N</b> night')

# 3. Add JS Camera Views logic
js_views_data = '''
  var VIEWS = {
    walk:   { p:[0, 1.7, 16],  yaw:0,     pitch:0,     name:"WALK VIEW" },
    drone:  { p:[0, 22, 38],   yaw:0,     pitch:-0.52, name:"DRONE OVERVIEW" },
    aerial: { p:[0, 52, 10],   yaw:0,     pitch:-1.38, name:"TOP-DOWN AERIAL" },
    shore:  { p:[-14, 9, -15], yaw:-2.1,  pitch:-0.28, name:"SHORE TEMPLE CINEMATIC" },
    ganga:  { p:[0, 4.2, -7],  yaw:0,     pitch:-0.05, name:"GANGES RELIEF CLOSEUP" },
    rathas: { p:[18, 7, -6],   yaw:1.2,   pitch:-0.32, name:"PANCHA RATHAS PERSPECTIVE" }
  };
  var currentView = "walk";
  function switchView(k){
    if(!VIEWS[k]) return;
    currentView = k;
    stopTour();
    var v = VIEWS[k];
    px = v.p[0]; py = v.p[1]; pz = v.p[2];
    yaw = v.yaw; pitch = v.pitch;
    lastX = null; lastY = null;
    $("#sDrone").classList.toggle("on", k==="drone");
    $("#sDrone").textContent = k==="drone" ? "🚁 Drone view · on" : "🚁 Drone view";
    document.querySelectorAll("#pViews button").forEach(function(b){ b.classList.toggle("on", b.dataset.v === k); });
    toast(v.name);
  }
'''

# Insert js_views_data and wire events
text = text.replace('var TIMES={', js_views_data + '\n  var TIMES={', 1)

# Wire the clicks and keyboard shortcuts
old_controls = '$("#sSun").addEventListener("click", function(){ setRake(!rakeOn); });'
new_controls = '''$("#sDrone").addEventListener("click", function(){ switchView(currentView==="drone" ? "walk" : "drone"); });
  $("#pViews").addEventListener("click", function(e){ var b=e.target.closest("button[data-v]"); if(b) switchView(b.dataset.v); });
  $("#sSun").addEventListener("click", function(){ setRake(!rakeOn); });'''
text = text.replace(old_controls, new_controls, 1)

# Add key shortcut 'v' for drone view
old_keys = 'if(k==="l") setRake(!rakeOn);'
new_keys = '''if(k==="v") switchView(currentView==="drone" ? "walk" : "drone");
    if(k==="l") setRake(!rakeOn);'''
text = text.replace(old_keys, new_keys, 1)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print('Added multiple camera views safely without disturbing anything else!')
