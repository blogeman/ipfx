import json
import sys

import ipfx.stimulus as stm
import ipfx.qc_protocol as qcp
import allensdk.core.json_utilities as ju
import os.path

stimulus_ontology_file = stm.DEFAULT_STIMULUS_ONTOLOGY_FILE

input_nwb_file = sys.argv[1]
output_dir = sys.argv[2]

d = {}

print("output_dir: %s" %output_dir)
d['input_nwb_file'] = input_nwb_file
d['output_nwb_file'] = os.path.join(output_dir, "output.nwb")
d['qc_fig_dir'] = os.path.join(output_dir,"qc_figs")
d['qc_criteria'] = ju.read(qcp.DEFAULT_QC_CRITERIA_FILE)
d['manual_sweep_states'] = []

with open(os.path.join(output_dir, 'pipeline_input.json'), 'w') as f:
    f.write(json.dumps(d, indent=2))