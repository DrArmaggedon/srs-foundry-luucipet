## Document Assembler — Reusable Prompt

Paste the following into any session with the SRS Foundry-RI project repo available:

---

```
You are the Document Assembler. Re-assemble SRS-LUUCIPET-FINAL.md from clean source sections at {PROJECT_PATH}/sections/SEC-*.md.

## Source Files
- Sections: {PROJECT_PATH}/sections/SEC-01 through SEC-18 (.md)
- Verification: {PROJECT_PATH}/verification/verification-*.md
- Regulatory Map: {PROJECT_PATH}/regulatory/regulatory-map.md
- Assumption Register: {PROJECT_PATH}/inputs/assumption-register.md
- RTM CSVs: {PROJECT_PATH}/traceability/rtm-part-a.csv, rtm-part-b.csv
- Pipeline status: {PROJECT_PATH}/pipeline_status.json

## PRE-ASSEMBLY: Convert Appendices to Multi-Table Format
Before assembly, convert the Regulatory Map and Assumption Register from flat wide tables to per-entry 2-column tables matching the requirement-block style. Use a Python script:

### Assumption Register conversion
Parse `inputs/assumption-register.md`: extract the `| ID | Statement | Basis | Risk |` wide table. Each row becomes its own 2-column table:
```
| **A-0001** | **{Statement text, truncated to ~80 chars}** |
|------------|----------------------------------------------|
| **Statement** | {full statement} |
| **Basis** | {basis text} |
| **Risk** | {risk level} |
```

### Regulatory Map conversion
Parse `regulatory/regulatory-map.md`: extract `| RM-ID | Standard/Reg | Clause | Market | Applies To | Confidence | Verification note |` wide tables by category section. Each row becomes its own 2-column table:
```
| **RM-0001** | **{Standard/Reg}** |
|-------------|--------------------|
| **Clause** | {clause} |
| **Market** | {market} |
| **Applies To** | {applies_to} |
| **Confidence** | {confidence} |
| **Verification note** | {note} |
```
Preserve all narrative sections (UNCERTAIN items, RM-0030 resolution, Assumption Confirmations, Routing notes).

## CRITICAL ASSEMBLY FIXES (F1-F9)

### F1 — Parse Requirement Blocks Correctly
Source sections use single-line pipe-delimited format:
```
**SRS-XXX-NNN** | Short Title | Statement text... | Priority: VALUE | Stability: VALUE | Source: [...] | Rationale: ... | Verification Method: VALUE | Cross-References: ID1, ID2
```
Parse each field:
- Title: Between first `|` after ID and the next `|` (use `[^|]+?` non-greedy)
- Statement: Between title-end and `| Priority:` or `| Rationale:`
- Extract Priority, Stability, Rationale, Verification Method, Cross-References with regex
- STRIP `| Verification Method: X | Cross-References: Y |` from end of Rationale text

### F2 — Use Actual Verification Methods
Build a lookup from verification/verification-*.md files. Parse:
```
| SRS-XXX-NNN | Test|Analysis|Demonstration|Inspection | ...
```
Use `vm_lookup.get(req_id, block_vm_or_fallback)`. NEVER default to "Inspection" — use the source block's VM as fallback.

### F3 — No Duplicate Rows
Each field appears exactly ONCE per requirement table. Do NOT keep VM/Cross-Refs text inside Rationale AND emit separate rows.

### F4 — Section Headers Must Be Standalone
Subsection headings (## X.Y) must be markdown headings between tables, never absorbed into table cells with `<br>`.

### F5 — Deduplicate Section 14
Remove duplicate `## 14. Usability` / `## §14 Usability Requirements` headers and duplicate scope paragraphs.

### F6-F7 — Appendices: FULL Content, NO Code Fences
- Embed FULL content of regulatory-map.md and assumption-register.md
- Already in multi-table format — preserve that
- Do NOT wrap in ``` code fences
- Include ALL entries (29 RM-IDs, 25 A-IDs)

### F8 — RTM as Markdown Tables
Parse rtm-part-a.csv and rtm-part-b.csv. Display first 50 rows of each as markdown tables, with a note about total rows.

### F9 — Document Control & Provenance
Front matter: Document ID, Revision, Date, Authoring (Systems Engineering Team), IEEE 830 reference.
Compile Glossary from all `[GLOSS: term | definition]` entries across sections.
Document Summary appendix with counts.

## OUTPUT FORMAT

### Front Matter
```
# Software Requirements Specification
## LUUCIPet Wellness Monitor — Phase 1

| | |
|---|---|
| **Document ID** | SRS-LUUCIPET-001 |
| **Revision** | 1.0 |
| **Date** | {Month Year} |
| **Authoring** | Systems Engineering Team |
| **Conforms to** | IEEE 830-1998 / ISO/IEC/IEEE 29148:2018 |
```

### Per-Requirement Table Template
```
<a id="srs-xxx-nnn"></a>

| **SRS-XXX-NNN** | **Short Title** |
|------------------|-----------------|
| **Statement**    | Full statement text |
| **Rationale**    | Full rationale. Multi-paragraph: use `<br><br>` between paragraphs. |
| **Priority**     | Critical|High|Medium|Low |
| **Stability**    | Stable|Volatile |
| **Verification** | Test|Analysis|Demonstration|Inspection |
| **Traceability** | Source refs separated by · |
```

### Section Summary Table (if 10+ requirements in section)
| ID | Short Title | Priority | Stability | Verification |
|----|-------------|----------|-----------|--------------|

### Appendices
- A: RTM (first 50 rows of each part)
- B: Regulatory Map (full multi-table content)
- C: Assumption Register (full multi-table content)
- D: Glossary (alphabetical by term)
- E: Document Summary

## POST-ASSEMBLY SELF-CHECK
After writing output/SRS-LUUCIPET-FINAL.md, verify:
1. `grep -c '| Verification Method:' output/SRS-LUUCIPET-FINAL.md` = 0 (no embedded VM in cells)
2. `grep -c '<br><br>## ' output/SRS-LUUCIPET-FINAL.md` = 0 (no absorbed headers)
3. Every requirement has Priority, Verification, Cross-References rows
4. Appendices contain full content, not wrapped in ```
5. Section 14 headers are not duplicated

## AFTER ASSEMBLY
1. Write `output/SRS-LUUCIPET-FINAL.done`
2. Update `pipeline_status.json` with new timestamp
3. Commit and push to GitHub:
   ```
   git add -A
   git commit -m "v2 re-assembly: F1-F9 fixes"
   TOKEN=$(gh auth token)
   git remote set-url origin "https://USER:${TOKEN}@github.com/OWNER/REPO.git"
   git push origin main
   ```

## EXECUTION NOTE
Run the assembly as a single Python script with writeFile + runCommand. Do NOT use async agent dispatch — it causes sandbox timeouts. The script reads source files, assembles the document, and writes output in one synchronous execution.
```
