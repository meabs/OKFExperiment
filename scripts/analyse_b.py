import json,glob,collections,re,sys
d=sys.argv[1]
rows=[json.load(open(f)) for f in glob.glob(f'{d}/runs/*/*/codex/*/run.json')]
stale={'inherit':r'\bArgument\b','callers':r'parse_args','complete':r'_resolve_context\b'}
truth={'inherit':'PositionalParameter','callers':'_ordered_params','complete':'_resolve_completion_context'}
tab=collections.defaultdict(lambda:[0,0,0]); ctl=collections.defaultdict(lambda:[0,0]); per=collections.defaultdict(lambda:collections.defaultdict(int))
for r in rows:
    q=r['question'];a=r['answer']
    if q in stale:
        t=tab[r['arm']];t[2]+=1
        ht=bool(re.search(truth[q],a)); sf=(not ht) and bool(re.search(stale[q],a))
        t[0]+=sf; t[1]+=ht; per[r['arm']][q]+=sf
    else:
        c=ctl[r['arm']];c[1]+=1;c[0]+=bool(r.get('correct'))
print('arm       stale-followed  found-truth  n(drift)   control-correct  stale by question')
for arm in ['noflag_confirm','none','noflag','native','tags','banner','all','targeted','blanket']:
    t=tab[arm];c=ctl[arm];print(f"{arm:9} {t[0]:>6}   {t[1]:>9}   {t[2]:>6}   {c[0]}/{c[1]}   {dict(per[arm])}")
