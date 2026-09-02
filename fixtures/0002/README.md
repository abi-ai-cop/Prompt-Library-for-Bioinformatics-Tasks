# Fixture for entry 0002

`counts.csv` is a realistic featureCounts export: it has a `#` comment line 
above the header, `Geneid` rather than `gene_id`, and one count column per sample 
rather than a single `count` column.

`summarise_counts.py` fails against it with `KeyError: 'gene_id'`.

Run it with:

```bash
cd fixtures/0002 && python3 summarise_counts.py
```

**Three separate problems are described.** A model must handle all three to 
produce working code:

1. The comment line is parsed as the header unless `comment="#"` is passed.
2. The gene column is `Geneid`, not `gene_id`.
3. There is no `count` column — counts are per-sample, so the aggregation has to
   name the sample columns.

A fix that addresses only the first two still raises `KeyError: 'gene_id'`. A fix
that addresses the first two but not the third raises a `KeyError` on `count`.
This entry measures whether a model finds all three without being told, and whether 
it says it is guessing at the file's structure.
