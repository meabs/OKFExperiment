import json,glob,collections,re,sys,statistics as st
d=sys.argv[1]
stale={'x1_cart_add':r'\bvoucher\b','x3_cart_delete':r'\{sku\}','x4_login':r'\bSignInForm\b','x6_config':r'\breadSettings\b'}
truth={'x1_cart_add':r'discountCode','x3_cart_delete':r'itemCode','x4_login':r'LoginPayload','x6_config':r'readPublicSettings'}
allowed_bases=None
def outside(r):
    own=f"{d}/work/{r['question']}/{r['arm']}/codex/{r['rep']}"
    for t in r['tool_calls']:
        for m in re.findall(r'/(?:private/)?tmp/[^\s"\'\\]+|/Users/[^/]+/[^\s"\'\\]*',t['text']):
            if own in m or 'using-superpowers' in m: continue
            if r['arm']=='source_drift' and m.rstrip('/').endswith('/cx/pr1') or '/cx/pr1/' in m and r['arm']=='source_drift': continue
            return True
    return False
rows=[json.load(open(f)) for f in glob.glob(f'{d}/runs/*/*/codex/*/run.json')]
def table(rows,label):
    tab=collections.defaultdict(lambda:[0,0,0]);ctl=collections.defaultdict(lambda:[0,0]);tok=collections.defaultdict(list)
    for r in rows:
        a=r['arm'];q=r['question'];tok[a].append(r['tokens']['total'])
        if q in stale:
            t=tab[a];t[2]+=1;ht=bool(re.search(truth[q],r['answer']));t[0]+=(not ht) and bool(re.search(stale[q],r['answer']));t[1]+=ht
        else:
            c=ctl[a];c[1]+=1;c[0]+=bool(r.get('correct'))
    print(f"\n{label}\narm              followed-stale  found-truth  n(drift)   controls-correct   mean-tokens")
    for a in ['source_drift','bundle_nosent','bundle_sent','bundle_t_sent']:
        if a in tab or a in ctl:
            t=tab[a];c=ctl[a];print(f"{a:16} {t[0]:>8}   {t[1]:>9}   {t[2]:>6}   {c[0]:>6}/{c[1]:<3}        {st.mean(tok[a])/1000:>6.0f}k")
table(rows,'ALL RUNS')
clean=[r for r in rows if not outside(r)]
print(f"\nruns reaching outside their own workdir (other than the drifted backend path in source_drift): {len(rows)-len(clean)} of {len(rows)}")
table(clean,'EXCLUDING THOSE RUNS')
