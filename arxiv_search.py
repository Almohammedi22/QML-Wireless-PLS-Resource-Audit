"""arXiv search for the QML physical-layer review (supplementary source, both tiers).

Usage:
    python arxiv_search.py            # run Tier 1 and Tier 2, write CSV and query files
    python arxiv_search.py --tier 2   # run one tier
    python arxiv_search.py --dry-run  # print the queries only, no network
    python arxiv_search.py --test     # three single requests that diagnose an HTTP 406

Standard library only. Follows the arXiv API terms: one request every 3 seconds.
The API searches free text only (no keyword field), so every term is matched in
the title or the abstract. It has no proximity operator, so the Scopus/Xplore
clause "quantum within 5 words of learning|neural|..." becomes a co-occurrence
of "quantum" with those words in the title or abstract.
"""
import argparse, csv, datetime, re, sys, time, urllib.parse, urllib.request
import xml.etree.ElementTree as ET

API = "https://export.arxiv.org/api/query"
PAGE = 500          # results per request (API maximum is 2000)
DELAY = 3.1         # seconds between requests
NS = {"a": "http://www.w3.org/2005/Atom",
      "os": "http://a9.com/-/spec/opensearch/1.1/",
      "ax": "http://arxiv.org/schemas/atom"}

QML_PHRASES = ["variational quantum", "parameterized quantum circuit", "quantum kernel",
               "quantum support vector", "hybrid quantum-classical", "quantum deep unfolding"]
QML_WITH_QUANTUM = ["learning", "neural", "reinforcement", "policy", "adversarial", "GAN", "transformer"]
WIRELESS = ["wireless", "radio", "physical layer", "physical-layer", "satellite", "UAV",
            "MIMO", "beamforming", "NOMA", "RIS", "mmWave"]
DESIGN = ["beamforming", "precoding", "beam prediction", "power allocation", "power control", "transmit power",
          "resource allocation", "reconfigurable intelligent surface",
          "intelligent reflecting surface", "stacked intelligent metasurface",
          "channel estimation", "UAV", "unmanned aerial vehicle"]
SECURITY = ["physical layer security", "physical-layer security", "secrecy", "eavesdropping",
            "eavesdropper", "wiretap", "physical layer authentication",
            "physical-layer authentication", "RF fingerprinting", "RF fingerprint",
            "radio frequency fingerprint", "emitter identification", "spoofing", "jamming",
            "jammer", "covert communication", "key generation"]

# Corpus studies with known arXiv versions; each run must retrieve these (protocol, Section 4).
EXPECTED = {1: {"2602.13238": "SIM-assisted PLS via QRL (Tier 1 preprint)",
                "2608.20240": "QUASAR SAR physical-layer authentication (Tier 1 preprint)"},
            2: {"2408.04747": "Hybrid quantum-classical NNs for downlink beamforming (TWC 2024)"}}


def term(t):
    t = f'"{t}"' if (" " in t or "-" in t) else t
    return f"(ti:{t} OR abs:{t})"


def group(terms):
    return "(" + " OR ".join(term(t) for t in terms) + ")"


def build_query(tier):
    qml = ("(" + group(QML_PHRASES) + " OR (" + term("quantum") + " AND "
           + group(QML_WITH_QUANTUM) + "))")
    third = DESIGN if tier == 2 else SECURITY
    return f"{qml} AND {group(WIRELESS)} AND {group(third)}"


HEADERS = {  # arXiv's API answers HTTP 406 to requests that do not ask for Atom explicitly
    "User-Agent": "qml-pls-review-search/1.1 (systematic literature search; Python urllib)",
    "Accept": "application/atom+xml",
    "Accept-Language": "en",
}


def fetch(query, start, n):
    url = API + "?" + urllib.parse.urlencode({
        "search_query": query, "start": start, "max_results": n,
        "sortBy": "submittedDate", "sortOrder": "ascending"})
    req = urllib.request.Request(url, headers=HEADERS)
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=120) as r:
                return r.read()
        except Exception as e:  # network error, HTTP 406 or 5xx: wait and retry
            if attempt == 3:
                sys.exit(f"\narXiv refused the request four times ({e}).\n"
                         "Wait 30 minutes and run the script again. "
                         "If it fails again, send a screenshot of this window.")
            wait = 30 * (attempt + 1)
            print(f"  request failed ({e}); retrying in {wait} s")
            time.sleep(wait)


def parse(xml_bytes):
    root = ET.fromstring(xml_bytes)
    total = int(root.findtext("os:totalResults", default="0", namespaces=NS))
    rows = []
    for e in root.findall("a:entry", NS):
        full_id = e.findtext("a:id", default="", namespaces=NS).rsplit("/abs/", 1)[-1]
        base, ver = re.match(r"^(.*?)(?:v(\d+))?$", full_id).groups()   # 2408.04747v2 -> 2408.04747, 2
        ver = ver or ""
        prim = e.find("ax:primary_category", NS)
        rows.append({
            "arxiv_id": base, "version": ver,
            "title": " ".join(e.findtext("a:title", default="", namespaces=NS).split()),
            "abstract": " ".join(e.findtext("a:summary", default="", namespaces=NS).split()),
            "authors": "; ".join(a.findtext("a:name", default="", namespaces=NS)
                                 for a in e.findall("a:author", NS)),
            "published": e.findtext("a:published", default="", namespaces=NS),
            "updated": e.findtext("a:updated", default="", namespaces=NS),
            "doi": e.findtext("ax:doi", default="", namespaces=NS),
            "journal_ref": e.findtext("ax:journal_ref", default="", namespaces=NS),
            "primary_category": prim.get("term") if prim is not None else "",
            "categories": "; ".join(c.get("term", "") for c in e.findall("a:category", NS)),
            "link": f"https://arxiv.org/abs/{base}",
        })
    return total, rows


def run(tier, fetcher=fetch, delay=DELAY):
    query = build_query(tier)
    rows, start, total, empty_retries = {}, 0, None, 0
    while total is None or start < total:
        if start:
            time.sleep(delay)
        total, page = parse(fetcher(query, start, PAGE))
        if not page and start < total:          # the API sometimes returns an empty page
            empty_retries += 1
            if empty_retries > 3:
                raise RuntimeError(f"empty page at start={start} of {total}")
            time.sleep(delay)
            continue
        empty_retries = 0
        for r in page:
            rows.setdefault(r["arxiv_id"], r)
        start += len(page)
    return query, total, list(rows.values())


def diagnose():
    """Three single requests that show why arXiv refuses the search. Makes no files."""
    tests = [("short, common query", "ti:electron"),
             ("short, rare query", 'abs:"variational quantum" AND abs:beamforming'),
             ("full Tier 2 query", build_query(2))]
    ok = {}
    for i, (name, q) in enumerate(tests):
        if i:
            time.sleep(DELAY)
        url = API + "?" + urllib.parse.urlencode({"search_query": q, "start": 0, "max_results": 1})
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=HEADERS), timeout=60) as r:
                ok[name] = True
                print(f"  {name} ({len(url)} characters): OK, HTTP {r.status}")
        except Exception as e:
            ok[name] = False
            print(f"  {name} ({len(url)} characters): FAILED, {e}")
    a, b, c = (ok[n] for n, _ in tests)
    if not a:
        print("\nResult: arXiv refuses even a simple request from this network. Try another network, "
              "such as a phone hotspot, and run the test again.")
    elif not b:
        print("\nResult: arXiv is throttling uncached requests from this network. Try another network, "
              "such as a phone hotspot, and run the test again.")
    elif not c:
        print("\nResult: only the long query is refused. Send this screenshot; the fix is to split the query.")
    else:
        print("\nResult: all three requests worked. Run the search again: python arxiv_search.py")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tier", type=int, choices=[1, 2])
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--test", action="store_true", help="diagnose an HTTP 406 refusal")
    args = ap.parse_args()
    if args.test:
        print("Testing the connection to arXiv (three requests, about 10 seconds) ...")
        return diagnose()
    today = datetime.date.today().isoformat()
    for tier in ([args.tier] if args.tier else [1, 2]):
        query = build_query(tier)
        if args.dry_run:
            print(f"Tier {tier} query ({len(query)} characters):\n{query}\n")
            continue
        print(f"Tier {tier}: searching arXiv ...")
        query, total, rows = run(tier)
        base = f"arxiv_T{tier}_{today}"
        with open(base + "_query.txt", "w", encoding="utf-8") as f:
            f.write(query + "\n")
        with open(base + ".csv", "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=list(rows[0]) if rows else ["arxiv_id"])
            w.writeheader()
            w.writerows(rows)
        found = {r["arxiv_id"] for r in rows}
        print(f"  API total {total}, unique records written {len(rows)} -> {base}.csv")
        for aid, label in EXPECTED[tier].items():
            print(f"  check {aid} ({label}): {'found' if aid in found else 'MISSING'}")
        if tier == 1 and not args.tier:
            time.sleep(DELAY)


if __name__ == "__main__":
    sys.exit(main())
