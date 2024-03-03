import fontforge

font = fontforge.open("font.ttf")

# substitute `s` with `sacute`
font.addLookup("s_lookup", "gsub_single", (), ())
font.addLookupSubtable("s_lookup", "s_subtable")
font["s"].addPosSub("s_subtable", "sacute")
font["S"].addPosSub("s_subtable", "Sacute")

# substitute JSON with the above s_lookup
# fmt: off
font.addLookup("JSON_lookup", "gsub_contextchain", (),
               (("calt", (("DFLT",("dflt")),
                          ("bamu", ("dflt")),
                          ("cyrl", ("dflt")),
                          ("gjr2", ("dflt")),
                          ("grek", ("dflt")),
                          ("latn", ("AZE ", "CAT ", "CRT ", "KAZ ", "MOL ", "ROM ", "TAT ", "TRK ", "dflt")),
                          ("math", ("dflt")))),))
font.addContextualSubtable("JSON_lookup", "JSON_subtable", "coverage", "[J j] | [S s] @<s_lookup> | [O o] [N n]")
# fmt: on

# change fontname
font.fontname += "-JSON"
font.familyname += " JSON"
font.fullname += " JSON"

font.generate("patched_font.ttf")
