import fontforge


def patch_font(font):
    print("Adding font substitution")

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


def replace_sfnt(font, key, value):
    font.sfnt_names = tuple(
        (row[0], key, value) if row[1] == key else row for row in font.sfnt_names
    )


def update_font_metadata(font, new_name):
    # Figure out the input font's real name (i.e. without a hyphenated suffix)
    # and hyphenated suffix (if present)
    old_name = font.familyname
    try:
        suffix = font.fontname.split("-")[1]
    except IndexError:
        suffix = None

    # Replace the old name with the new name whether or not a suffix was present.
    # If a suffix was present, append it accordingly.
    font.familyname = new_name
    if suffix:
        font.fullname = "%s %s" % (new_name, suffix)
        font.fontname = "%s-%s" % (new_name.replace(" ", ""), suffix)
    else:
        font.fullname = new_name
        font.fontname = new_name.replace(" ", "")

    print("Patching font %s as '%s'" % (old_name, new_name))

    # font.copyright = (font.copyright or "") + COPYRIGHT
    replace_sfnt(font, "UniqueID", "%s; Ligaturized" % font.fullname)
    replace_sfnt(font, "Preferred Family", new_name)
    replace_sfnt(font, "Compatible Full", new_name)
    replace_sfnt(font, "Family", new_name)
    replace_sfnt(font, "WWS Family", new_name)


def parse_args():
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument("input_font", help="The TTF or OTF font to patch")
    parser.add_argument(
        "-o",
        "--output",
        help="The path to save the patched font",
        default="patched_font.ttf",
    )
    parser.add_argument("-n", "--name", help="Name of the patched font", default="")

    return parser.parse_args()


def main():
    args = parse_args()

    font = fontforge.open(args.input_font)
    patch_font(font)
    update_font_metadata(font, args.name or ("%s JSON" % font.familyname))
    font.generate(args.output)

    print("Generated patched font at %s" % args.output)


if __name__ == "__main__":
    main()
