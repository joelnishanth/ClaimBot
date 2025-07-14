import argparse
import requests
import os

SCANNER_URL = os.getenv('SCANNER_CONTEXT_URL', 'http://scanner_context:8001')
DMCA_URL = os.getenv('DMCA_CONTEXT_URL', 'http://dmca_context:8002')

parser = argparse.ArgumentParser(description='ClaimBot Orchestrator')
parser.add_argument('--shop-url', required=True)
parser.add_argument('--auto-generate', action='store_true')
parser.add_argument('--output-dir', default='dmca_notices')
args = parser.parse_args()

resp = requests.post(f'{SCANNER_URL}/scan', json={'shop_url': args.shop_url})
violations = resp.json().get('violations', [])
print(f'Found {len(violations)} possible violations')

if args.auto_generate:
    os.makedirs(args.output_dir, exist_ok=True)
    for v in violations:
        r = requests.post(f'{DMCA_URL}/generate', json={'violation_id': v.get('id', 'unknown')})
        notice = r.json().get('notice', '')
        filename = os.path.join(args.output_dir, f"{v.get('id','violation')}.md")
        with open(filename, 'w') as f:
            f.write(notice)
        print(f'Generated notice for {v.get("id")}')
