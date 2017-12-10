#MenuTitle: Brace Layer VF Designspace Fix
# -*- coding: utf-8 -*-

__doc__="""
Adds brace layers at edges of designspace to allow for VF export
"""

import GlyphsApp, re, string

font = Glyphs.font
brace = re.compile("{\s*(\d+)\s*,\s*(\d+)\s*}")
axes = []
matches = {}

weight_low = 22
weight_high = 188
width_low = 300
width_high = 500

def addBrace(weight,width,glyph):
  print "adding", weight, width, glyph
  newBraceLayer = GSLayer()
  newBraceLayer.name = 'GX {' + str(weight) + ', ' + str(width) + '}'
  glyph.layers.append(newBraceLayer)
  newBraceLayer.reinterpolate() 


for glyph in font.glyphs:
  if glyph.name:
    gn = str(glyph.name)
    axes = []
    weight = 0
    width = 0
    for i, layer in enumerate(glyph.layers):
      if layer.name:
        if brace.match(layer.name):
          axes = brace.findall(layer.name)
          weight = int(axes[0][0])
          width = int(axes[0][1])
          try:
            matches[gn]
          except KeyError:
            matches[gn] = []
            matches[gn].insert(0, glyph)
          try:
            matches[gn][1]
          except IndexError:
            matches[gn].insert(1, [])
          
          matches[gn][1].append([width,weight])

for gn, array in matches.iteritems():
  weights = {}
  widths = {}

  for weight, width in array[1]:
    weight = str(weight)
    width = str(width)

    try:
      weights[weight]
    except KeyError:
      weights[weight] = {}
      weights[weight].update({width: {}})

    weights[weight].update({width: {}})

  for width, wts in weights.iteritems():
    for weight in wts:

      width = int(width)
      weight = int(weight)
      
      if width > width_low and width < width_high:
        if weight == weight_low or weight == weight_high:
          #print gn, "extreme weight, non extreme width (this is a master)", weight, width, array[0]

          if weight == weight_low:
            if [width, weight_high] not in matches[gn][1]:
              #print "*** NEEDED", weight_high, width
              matches[gn][1].append([width, weight_high])
              addBrace(weight_high, width, array[0])
          elif weight == weight_high:
            if [width, weight_low] not in matches[gn][1]:
              #print "*** NEEDED", weight_low, width
              matches[gn][1].append([width, weight_low])
              addBrace(weight_low, width, array[0])
     
        else:
          #print gn, "non extreme weight, non extreme width", weight, width, array[0]
          
          if [width_high, weight] not in matches[gn][1]:
            #print "*** NEEDED", weight, width_high
            matches[gn][1].append([width_high, weight])
            addBrace(weight, width_high, array[0])
   
          if [width_low, weight] not in matches[gn][1]:
            #print "*** NEEDED", weight, width_low
            matches[gn][1].append([width_low, weight])
            addBrace(weight, width_low, array[0])
            
      elif width == width_low or width == width_high:
        if weight > weight_low and weight < weight_high:
          #print gn, "non extreme weight, extreme width", weight, width, array[0]
          
          if width == width_low:
            if [width_high, weight] not in matches[gn][1]:
              #print "*** NEEDED", weight, width_high
              matches[gn][1].append([width_high, weight])
              addBrace(weight, width_high, array[0])

          elif width == width_high:
            if [width_low, weight] not in matches[gn][1]:
              #print "*** NEEDED", weight, width_low
              matches[gn][1].append([width_low, weight])
              addBrace(weight, width_low, array[0])
