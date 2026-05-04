"""Appends the missing tail to enrich_chapters.py"""
from pathlib import Path

SCRIPT = Path("/sessions/trusting-peaceful-wozniak/mnt/Sviluppo Bambino/output/assi-strutturali/enrich_chapters.py")

# Read current content, keep only up to line 215
with open(SCRIPT, encoding="utf-8") as f:
    lines = f.readlines()

# Find the line with mkdir (that's our safe cut point)
cut = 215
with open(SCRIPT, "w", encoding="utf-8") as f:
    f.writelines(lines[:cut])

# Now append the tail
tail = (
    '    print("\\n--- " + asse_dir.name, flush=True)\n'
    '\n'
    '    for cap in sorted(asse_dir.iterdir()):\n'
    '        if cap.suffix != ".md":\n'
    '            continue\n'
    '        content = cap.read_text(encoding="utf-8")\n'
    '        enriched, n_a, n_b = enrich(content)\n'
    '        (out_asse / cap.name).write_text(enriched, encoding="utf-8")\n'
    '        total_f += 1\n'
    '        total_a += n_a\n'
    '        total_b += n_b\n'
    '        name_short = cap.name[:60]\n'
    '        line_out = "  " + name_short.ljust(60) + "  a:" + str(n_a).rjust(2) + "  b:" + str(n_b).rjust(2)\n'
    '        print(line_out, flush=True)\n'
    '\n'
    'print("=" * 60)\n'
    'print("File: " + str(total_f) + " | Foto autori: " + str(total_a) + " | Copertine: " + str(total_b))\n'
)

with open(SCRIPT, "a", encoding="utf-8") as f:
    f.write(tail)

# Verify
with open(SCRIPT, encoding="utf-8") as f:
    final_lines = f.readlines()
print("Script finale: " + str(len(final_lines)) + " righe")
print("Ultime 5 righe:")
for ln in final_lines[-5:]:
    print("  " + repr(ln.rstrip()))
