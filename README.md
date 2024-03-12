# **JŚON**

JSON, or JavaScript Object Notation, is a widely used data format in web applications. However, there has
been ongoing debate about the correct pronunciation of this acronym. In a 
[YouTube video](https://www.youtube.com/watch?v=uR-f4b0G9lo) featuring the creator of JSON, Douglas Crockford,
he revealed that it should be pronounced as "JŚON" ("shason" in French accent).

In celebration of this revelation and to ensure that everyone follows the CORRECT pronunciation of JŚON,
this script comes into action. It alters existing TTF or OTF font files by substituting any occurrence of
"JSON" with "JŚON", following the one and only CORRECT pronunciation.

## **Table of Contents** 🔎
1. [Prepatched Fonts](#prepatched-fonts-)
2. [Prerequisites](#prerequisites-)
3. [Usage](#usage-)
4. [Credits](#credits-)

## **Prepatched Fonts** 🤓
We've got some prepatched fonts for every one of you to use.
Go to [/patched-fonts](https://github.com/Eggrror404/json/tree/master/patched-fonts)
and you'll see some fonts modified from Google Fonts.

If something doesn't work - _don't let me know_.
Maybe re-patching it with the script would work :)

## **Prerequisites** 💻
To use this script, make sure you have the following tools installed:
- [FontForge](https://fontforge.org/)
- [Python](https://www.python.org/downloads/)

## **Usage** 🔧
```
usage: substitute.py [-h] [-o OUTPUT] [-n NAME] input_font

positional arguments:
  input_font            The TTF or OTF font to patch

options:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        The path to save the patched font (default: patched_font.ttf)
  -n NAME, --name NAME  Name of the patched font (default: original font name with `JSON`)

```
Replace `input_font` with the path to your TTF or OFT font file.
Optionally specify the OUTPUT and NAME arguments.

To run the script:
```
$ python substitute.py -o patched_font.ttf -n "JŚON Font" input.ttf
```
This command will patch the font `input.ttf`, output the patched font as `patched_font.ttf`, and
set its fontname to `JŚON Font`.

### Pro Tip!

Use the following script to patch all ttf files in a folder, recursively:
```bash
ls ./**/*.ttf | while read font; do
  python substitute.py -o ${font:0:${#font}-4}-JSON.ttf $font
done
```

## **Credits** 🌐
Thanks to [ToxicFrog/Ligaturizer](https://github.com/ToxicFrog/Ligaturizer)
under the [GPLv3 License](https://github.com/ToxicFrog/Ligaturizer/blob/master/LICENSE)
for showing font modifying with FontForge's Python bindings.
