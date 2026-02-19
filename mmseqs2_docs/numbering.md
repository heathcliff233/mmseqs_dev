```{=typst}
#set heading(numbering: "1.1.1")

#let doc_callout(title, fill_color, body) = block(
  fill: fill_color,
  stroke: 0.6pt + rgb("#c5ccd3"),
  inset: (x: 10pt, y: 8pt),
  radius: 5pt,
  breakable: true,
)[
  #text(weight: "semibold")[#title]
  #v(0.35em)
  #body
]

#let doc_note(body) = doc_callout([Note], rgb("#eef3f8"), body)
#let doc_perf(body) = doc_callout([Performance], rgb("#e8f6ff"), body)
#let doc_warning(body) = doc_callout([Warning], rgb("#fff3df"), body)
#let doc_tip(body) = doc_callout([Tip], rgb("#ecf9ef"), body)
```
