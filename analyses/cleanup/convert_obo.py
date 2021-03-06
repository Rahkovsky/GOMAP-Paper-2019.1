# This script reads an OBO file using the obo_parser and outputs JSON files that are then used by the crystal scripts.
# The GO.json file looks like this:
# {
#   "parents": {
#     "GO:122335": ["GO:4433", "GO:5432"],
#     "GO:122341": ["GO:1243", "GO:1532"],
#     ...
#   },
#   "main_id" : {"GO:1443":"GO:532", "GO:2533":"GO:5234"}
#   "obsolete": ["GO:1432", "GO:4322", ...]
# }
#
# The GO_names.json file looks like this:
# {
#   "GO:43334":"Photosynthesis",
#   "GO:93743":"Something else",
#   ...
# }
#
# The GO_aspects.json file looks like this:
# {
#   "GO:43334":"P",
#   "GO:93743":"F",
#   ...
# }


import obo_parser
import json
import gzip

parents = {}
main_id = {}
obsolete = []
go_names = {}
go_aspects = {}
go_aspect_mapping = {
    "biological_process": "P",
    "molecular_function": "F",
    "cellular_component": "C"
}
with gzip.open("data/go.obo.gz") as obofile:
  parser = obo_parser.Parser(obofile)
  for stanza in parser:
    if not stanza.name == "Term":
      continue

    go_id = stanza.tags["id"][0]

    if 'is_a' in stanza.tags:
      parents[go_id] = stanza.tags['is_a']
    else:
      parents[go_id] = []

    if 'alt_id' in stanza.tags:
      for alt_id in stanza.tags['alt_id']:
        main_id[alt_id] = go_id

    if 'is_obsolete' in stanza.tags and stanza.tags['is_obsolete'][0] == "true":
      obsolete.append(go_id)
    else:
      go_names[go_id] = stanza.tags['name'][0]

    # Also save obsolete aspects bc they are used on non-cleaned annotations
    go_aspects[go_id] = go_aspect_mapping[stanza.tags['namespace'][0]]

with open('analyses/cleanup/results/GO.json', 'w') as f:
  f.write(json.dumps({"parents":parents,"main_id":main_id,"obsolete":obsolete},indent=2))

with open('analyses/cleanup/results/GO_names.json', 'w') as f:
  f.write(json.dumps(go_names,indent=2))

with open('analyses/cleanup/results/GO_aspects.json', 'w') as f:
  f.write(json.dumps(go_aspects,indent=2))
