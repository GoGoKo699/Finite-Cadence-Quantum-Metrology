"""Run every finite scientific check; fail immediately on an unsuccessful check."""
from pathlib import Path
import json
import subprocess
import sys
import numpy
import scipy

here=Path(__file__).resolve().parent
scripts=['check_algebra.py','check_exact_cycle.py','check_grid_upper.py',
         'check_physical_choi.py','check_fast_separation.py']
rows=[]
for script in scripts:
    result=subprocess.run([sys.executable,str(here/script)],capture_output=True,text=True)
    if result.returncode:
        print(result.stdout);print(result.stderr,file=sys.stderr)
        raise SystemExit(result.returncode)
    rows.append({'script':script,'status':'pass','summary':json.loads(result.stdout)})
    print('PASS '+script,flush=True)
report={'scope':'Finite deterministic numerical checks; analytical proofs remain authoritative.',
        'numpy':numpy.__version__,'scipy':scipy.__version__,'checks':rows,'status':'pass'}
(here/'results').mkdir(exist_ok=True)
(here/'results'/'summary.json').write_text(json.dumps(report,indent=2)+'\n')
