
![Barlow Screenshot](https://raw.githubusercontent.com/jpt/barlow/master/documentation/barlow.gif)

# Barlow

Barlow is a slightly rounded, low-contrast, grotesk type family designed by [Jeremy Tribby](https://tribby.com). Drawing from the visual style of the California public, Barlow shares qualities with the state's car plates, highway signs, busses, and trains.

The family includes 54 styles in three widths and nine weights, as well as italics, suitable for large and small digital and print use. Customizable weights and widths are available via the included variable font (GX) file.

Barlow is named after internet pioneer, EFF co-founder, songwriter, and activist [John Perry Barlow](https://en.wikipedia.org/wiki/John_Perry_Barlow), in tribute to his lasting [impact on the information superhighway](https://www.eff.org/cyberspace-independence). Please consider making a donation to the [John Perry Barlow Wellness Trust](https://www.johnperrybarlow-wellnesstrust.com/).

## Download

[Download the project](https://github.com/jpt/barlow/archive/master.zip) and find the OpenType font files in the `fonts/otf` directory. A good way to play with it as a web font (`fonts/woff`) is on [Pablo Impallari's font testing site](http://www.impallari.com/testing/).

## Variable font support

Variable font support is currently experimental, both in the Barlow typeface and in the general ecosystem of tooling and rendering; please open an issue if you find a bug (other than a lack of rounding)!

#### Building the variable Font

Building the GX file requires Glyphs. First, move the contents of the `tools` folder in this repo to your local Glyphs Scripts folder (`Scripts->Open Script Folder`) and refresh your Glyphs scripts (`Option + Scripts->Reload Scripts`). Save a copy of Barlow.glyphs as Barlow-GX.glyphs. Run the `Brace Layer Decompose` script, and then the `Brace Layer VF Designspace Fix` script. The font is now ready for GX export from Glyphs.

## Acknowledgements

Thank you Lukas Schneider (@lukas____s) of [Revolver Type](http://revolvertype.com/tools/cadencer.html) for donating the LS Cadencer spacing tool. Thank you Dave Crossland (@davelab6) and Thomas Phinney (@tphinney) of [Crafting Type](http://craftingtype.com) for the guidance and early feedback. Thank you Hugh D'Andrade (@hughillustration) for holding me to a high standard from the start.

And thank you, Barlow, most of all, for a legacy that will carry our future into a brighter place. 

## License

This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available in the bundled [OFL.txt](https://github.com/jpt/barlow/blob/master/OFL.txt) file, and is also available with a FAQ at: http://scripts.sil.org/OFL
