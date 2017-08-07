#MenuTitle: Brace Layer Decompose
# -*- coding: utf-8 -*-

__doc__="""
Copies brace layers in components to parent glyphs
"""

import GlyphsApp, re, string

font = Glyphs.font
brace = re.compile("^{\s*\d+\s*,\s*\d+\s*}$")

letters = string.ascii_uppercase + string.ascii_lowercase
letter_clones = []

for glyph in font.glyphs:
  if glyph.name in letters and len(glyph.name) == 1:
    for i, layer in enumerate(glyph.layers):
      for component in layer.components:
        if glyph.layers[i].name == font.masters[0].name:
          if component.componentName not in letters:
            for component_layer in font.glyphs[component.componentName].layers:
              if brace.match(component_layer.name):
                newBraceLayer = GSLayer()
                newBraceLayer.name = component_layer.name
                font.glyphs[glyph.name].layers.append(newBraceLayer)
                newBraceLayer.reinterpolate() 
          elif component.componentName in letters:
            letter_clones.append([glyph,component.componentName])
         
for glyph, letter in letter_clones:
  for layer in font.glyphs[letter].layers:
    if brace.match(layer.name):
      newBraceLayer = GSLayer()
      newBraceLayer.name = layer.name
      glyph.layers.append(newBraceLayer)
      newBraceLayer.reinterpolate()
      
for glyph in font.glyphs:
  for layer in glyph.layers:
    layer.decomposeComponents()