# -*- coding: utf-8 -*-
with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Make all button lookups safe so no TypeError: Cannot read properties of null occurs
replacements = [
    ('$("#mDeck").classList.toggle("on", m==="deck");', 'var md=$("#mDeck"); if(md) md.classList.toggle("on", m==="deck");'),
    ('$("#mSite").classList.toggle("on", m==="site");', 'var ms=$("#mSite"); if(ms) ms.classList.toggle("on", m==="site");'),
    ('$("#mRep").classList.toggle("on", m==="rep");', 'var mr=$("#mRep"); if(mr) mr.classList.toggle("on", m==="rep");'),
    ('$("#mPdf").classList.toggle("on", m==="rep");', 'var mp=$("#mPdf"); if(mp) mp.classList.toggle("on", m==="rep");'),
    ('$("#mDeck").onclick = function(){ setMode("deck"); };', 'if($("#mDeck")) $("#mDeck").onclick = function(){ setMode("deck"); };'),
    ('$("#mSite").onclick = function(){ setMode("site"); };', 'if($("#mSite")) $("#mSite").onclick = function(){ setMode("site"); };'),
    ('$("#mRep").onclick  = function(){ setMode("rep"); };', 'if($("#mRep")) $("#mRep").onclick = function(){ setMode("rep"); };'),
    ('$("#mPdf").onclick = downloadPDF;', 'if($("#mPdf")) $("#mPdf").onclick = downloadPDF;'),
    ('$("#pdfGo").onclick = downloadPDF;', 'if($("#pdfGo")) $("#pdfGo").onclick = downloadPDF;'),
    ('$("#pdfBack").onclick = function(){ setMode("deck"); };', 'if($("#pdfBack")) $("#pdfBack").onclick = function(){ setMode("deck"); };')
]

for old, new in replacements:
    text = text.replace(old, new)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print('Successfully patched null guards!')
