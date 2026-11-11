#!/usr/bin/env python3
"""Fetch the FULL text of an Act or statutory instrument from legislation.gov.uk in one request.

Usage:
  legislation_fetch.py https://www.legislation.gov.uk/ukpga/2006/45            # current version, clean text
  legislation_fetch.py ukpga/2006/45 --version enacted                          # as originally passed
  legislation_fetch.py ukpga/2006/45 --version 2010-01-01                       # as it stood on a date
  legislation_fetch.py ukpga/2006/45 --notes                                    # explanatory notes
  legislation_fetch.py ukpga/2006/45 --format xml -o act.xml                    # raw XML
  legislation_fetch.py ukpga/2006/45 --format pdf -o act.pdf                    # PDF
  legislation_fetch.py ukpga/2006/45 --section 4                                # one section

Prints the version date and any "changes outstanding" note to stderr, and the text to stdout
(or writes to -o). Always record the version date with any quote.
"""
import argparse, re, sys
from _common import get, die, strip_tags, looks_blocked

def norm(ref):
    ref = ref.strip()
    ref = re.sub(r"^https?://(www\.)?legislation\.gov\.uk/", "", ref)
    ref = re.sub(r"/(contents|data\.\w+|enacted|made)?/?$", "", ref)
    return ref.strip("/")

def build(ref, version, notes, fmt, section):
    path = f"https://www.legislation.gov.uk/{ref}"
    if section:
        path += f"/section/{section}"
    if notes:
        path += "/notes"
    elif version == "enacted":
        path += "/enacted" if not ref.startswith(("uksi", "wsi", "nisr", "ssi")) else "/made"
    elif version and version != "current":
        path += f"/{version}"
    return path + f"/data.{fmt}"

def xml_to_text(x):
    # Drop footnote/commentary markers and metadata so the statute reads as prose.
    x = re.sub(r"<ukm:Metadata.*?</ukm:Metadata>", "", x, flags=re.S)
    x = re.sub(r"<Commentaries>.*?</Commentaries>", "", x, flags=re.S)
    x = re.sub(r"<CommentaryRef[^>]*/>", "", x)
    x = re.sub(r"<(Pnumber)>", r"\n<\1>", x)
    x = re.sub(r"<(Title|Number)>", r"\n\n<\1>", x)
    x = re.sub(r"</(P1|P2|P3|P1para|P2para|P3para|Pblock|P1group|Text)>", "\n", x)
    return strip_tags(x)

if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("ref", help="URL or path like ukpga/2006/45")
    ap.add_argument("--version", default="current", help="current | enacted | YYYY-MM-DD")
    ap.add_argument("--notes", action="store_true", help="explanatory notes instead of the Act")
    ap.add_argument("--format", default="text", choices=["text", "xml", "pdf", "html"])
    ap.add_argument("--section", default=None)
    ap.add_argument("-o", "--output", default=None)
    args = ap.parse_args()
    ref = norm(args.ref)
    fmt = "xml" if args.format == "text" else args.format
    url = build(ref, args.version, args.notes, fmt, args.section)
    status, ctype, body = get(url, delay=5.0)
    if looks_blocked(status, body) or status != 200:
        die(f"{url} returned HTTP {status}")
    print(f"# fetched {url} ({len(body)} bytes)", file=sys.stderr)
    if fmt == "xml":
        x = body.decode("utf-8", "ignore")
        title = re.search(r"<dc:title>(.*?)</dc:title>", x)
        valid = re.search(r"<dct:valid>(.*?)</dct:valid>", x)
        start = re.search(r'RestrictStartDate="([^"]+)"', x)
        unapplied = len(re.findall(r"<ukm:UnappliedEffect", x))
        print(f"# title: {title.group(1) if title else '?'}", file=sys.stderr)
        print(f"# version in force from: {(valid or start).group(1) if (valid or start) else 'unknown'}", file=sys.stderr)
        if unapplied:
            print(f"# WARNING: {unapplied} outstanding change(s) not yet applied to this text", file=sys.stderr)
        data = xml_to_text(x).encode() if args.format == "text" else body
    else:
        data = body
    if args.output:
        open(args.output, "wb").write(data)
        print(f"# written to {args.output}", file=sys.stderr)
    else:
        sys.stdout.buffer.write(data if fmt != "pdf" else b"(binary PDF: use -o)\n")
