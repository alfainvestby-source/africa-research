# Skill: Corpus coverage & field promotion

**Purpose:** Decide which fields belong on **public Rightmove-like** UI vs **Admin** vs **Plus**, using confidence + coverage across the dossier corpus.

**Inputs:** All `docs/projects/*.md`, `docs/db/`, `decisions.md`  
**Outputs:** `docs/db/field-promotion.md` (living scoreboard), updates to must-have consensus, changelog notes  

**Rules:** Public only if high confidence AND high coverage (~½ missing → not public). Never invent data.
