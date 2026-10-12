import json,glob,collections,re,sys
d=sys.argv[1]
tot=collections.Counter();hit=collections.Counter();ex={}
for f in glob.glob(f'{d}/runs/*/*/codex/*/run.json'):
    r=json.load(open(f));a=r['arm']
    own=f"{d}/work/{r['question']}/{a}/codex/{r['rep']}"
    tot[a]+=1
    out=False
    for t in r['tool_calls']:
        c=t['text']
        for m in re.findall(r'/(?:private/)?tmp/[^\s"\'\\]+|/Users/[^/]+/[^\s"\'\\]*',c):
            if own in m or 'using-superpowers' in m or '/.agents/skills' in m: continue
            out=True;ex.setdefault(a,m[:170])
    if out: hit[a]+=1
for a in tot: print(f"{a:14} runs reaching outside their own workdir: {hit[a]:>2}/{tot[a]}   e.g. {ex.get(a,'')}")
