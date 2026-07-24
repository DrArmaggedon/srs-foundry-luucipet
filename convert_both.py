import re

# === Assumption Register ===
with open('/mnt/srs_foundry_luucipet/inputs/assumption-register.md', 'r') as f:
    content = f.read()

lines = content.split('\n')
header_lines = []
for i, line in enumerate(lines):
    if line.startswith('| ID | Statement'):
        break
    header_lines.append(line)

# Parse flat table
data = []
for line in lines[i+2:]:
    line = line.strip()
    if not line or not line.startswith('|'):
        break
    parts = [p.strip() for p in line.split('|')]
    if len(parts) >= 5:
        data.append({'id': parts[1], 'statement': parts[2], 'basis': parts[3], 'risk': parts[4]})

out = header_lines + ['']
for r in data:
    title = r['statement'][:77] + '...' if len(r['statement']) > 80 else r['statement']
    out.append(f'| **{r["id"]}** | **{title}** |')
    out.append('|------------|' + '-' * max(len(title), 10) + '|')
    out.append(f'| **Statement** | {r["statement"]} |')
    out.append(f'| **Basis** | {r["basis"]} |')
    out.append(f'| **Risk** | {r["risk"]} |')
    out.append('')

with open('/mnt/srs_foundry_luucipet/inputs/assumption-register.md', 'w') as f:
    f.write('\n'.join(out))
print(f'Assumptions: {len(data)} entries converted')

# === Regulatory Map ===
with open('/mnt/srs_foundry_luucipet/regulatory/regulatory-map.md', 'r') as f:
    content = f.read()

lines = content.split('\n')
out2 = []
i = 0
in_table = False
header_cols = []
table_rows = []

def flush():
    global table_rows, header_cols
    if not table_rows:
        return []
    r = []
    for row in table_rows:
        rid = row.get('RM-ID', '')
        std = row.get('Standard/Reg', '')
        r.append(f'| **{rid}** | **{std}** |')
        r.append('|-------------|' + '-' * max(len(std), 10) + '|')
        for col in header_cols:
            if col in ('RM-ID', 'Standard/Reg'):
                continue
            r.append(f'| **{col}** | {row.get(col, "")} |')
        r.append('')
    table_rows = []
    return r

while i < len(lines):
    line = lines[i]
    if line.startswith('|') and not in_table:
        if i+1 < len(lines) and re.match(r'^\|[\s\-:|]+\|', lines[i+1]):
            in_table = True
            header_cols = [c.strip() for c in line.split('|') if c.strip()]
            i += 2
            continue
    if in_table:
        if line.startswith('|'):
            cols = [c.strip() for c in line.split('|') if c.strip()]
            if len(cols) == len(header_cols):
                table_rows.append(dict(zip(header_cols, cols)))
            i += 1
            continue
        else:
            out2.extend(flush())
            in_table = False
            header_cols = []
            continue
    # Fix RM-0031 bold doubling
    if '****RM-0031****' in line:
        line = line.replace('****RM-0031****', '**RM-0031**')
    out2.append(line)
    i += 1

if table_rows:
    out2.extend(flush())

result = '\n'.join(out2)
with open('/mnt/srs_foundry_luucipet/regulatory/regulatory-map.md', 'w') as f:
    f.write(result)
print(f'Regulatory: {result.count("| **RM-")} RM-ID entries')
