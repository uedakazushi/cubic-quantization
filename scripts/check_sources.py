"""Standalone TeX source graph and references sanity check; not a proof or LaTeX compile."""
from pathlib import Path
from collections import Counter
import re
ROOT=Path(__file__).resolve().parents[1]
seen=set(); parts=[]
def clean(s):
    return "\n".join(re.split(r"(?<!\\)%",x,1)[0] for x in s.splitlines())
def visit(p):
    p=p.resolve()
    assert p.is_relative_to(ROOT) and p.is_file(), f"Missing/external input: {p}"
    assert p not in seen, f"Repeated or circular input: {p}"
    seen.add(p)
    s=clean(p.read_text(encoding="utf-8")); parts.append(s)
    for x in re.findall(r"\\(?:input|include)\{([^}]+)\}",s):
        q=ROOT/x
        visit(q if q.suffix else q.with_suffix(".tex"))
visit(ROOT/"papers/cubic-quantization.tex")
s="\n".join(parts)
labels=Counter(re.findall(r"\\label\{([^}]+)\}",s))
dups=[x for x,n in labels.items() if n>1]
refs=set(re.findall(r"\\(?:ref|eqref|pageref|autoref)\{([^}]+)\}",s))
missing=refs-set(labels)
cites=set(x.strip() for raw in re.findall(r"\\cite(?:\[[^]]*\])*\{([^}]+)\}",s) for x in raw.split(","))
keys=set(re.findall(r"\\bibitem(?:\[[^]]*\])?\{([^}]+)\}",s))
assert not dups, f"Duplicate labels: {dups}"
assert not missing, f"Unresolved refs: {sorted(missing)}"
assert not (cites-keys),f"Unresolved cites: {sorted(cites-keys)}"
print(f"OK: {len(seen)} files, {len(labels)} labels, {len(cites)} citations.")
print("LIMIT: source integrity only; no proof, runtime or typesetting verification.")
