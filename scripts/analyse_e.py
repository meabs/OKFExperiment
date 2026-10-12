"""Experiment E: for each arm, what happened on the questions whose guide entry was made wrong, and on the unchanged ones.
followed wrong = the answer gives the planted wrong callee and not the true one; true = the answer matches the true facts;
other = neither (e.g. the agent picked a different handler). hedged = the answer says it relies on a guess or is unverified."""
import json, glob, re, sys, collections, statistics as st
d = sys.argv[1]
wrong = {"e1_login": r"registerCustomer", "e3_cart_delete": r"modifyCartMulti", "e4_cart_add": r"replaceBasket", "e5_shipping": r"processOrder"}
hedge = re.compile(r"medium|heuristic|guess|unverified|not verified|can.?t (verify|confirm)|cannot (verify|confirm)|could not (verify|confirm)|may be (wrong|incorrect|inaccurate)|might be|not certain|uncertain|low confidence|inferred", re.I)
rows = [json.load(open(f)) for f in glob.glob(f"{d}/runs/*/*/codex/*/run.json")]
cnt = collections.defaultdict(lambda: collections.Counter()); tok = collections.defaultdict(list)
for r in rows:
    a, q = r["arm"], r["question"]; tok[a].append(r["tokens"]["total"])
    h = bool(hedge.search(r["answer"]))
    if q in wrong:
        c = cnt[a]; c["planted"] += 1
        if r.get("correct"): c["true"] += 1
        elif re.search(wrong[q], r["answer"]): c["followed_wrong"] += 1
        else: c["other"] += 1
        c["planted_hedged"] += h
        if re.search(wrong[q], r["answer"]) and not r.get("correct"): c["followed_wrong_hedged"] += h
    else:
        c = cnt[a]; c["control"] += 1; c["control_correct"] += bool(r.get("correct")); c["control_hedged"] += h
print("arm                 planted: followed-wrong / true / other   hedged(planted)  hedged-when-wrong   controls correct   hedged(controls)   tokens")
for a in ["plain", "labels", "labels_rule", "mislabelled_rule"]:
    c = cnt[a]
    if not c: continue
    print(f"{a:19} {c['followed_wrong']:>6} / {c['true']:>3} / {c['other']:>3}  of {c['planted']:<3}   {c['planted_hedged']:>6}        {c['followed_wrong_hedged']:>3} of {c['followed_wrong']:<3}        {c['control_correct']:>3}/{c['control']:<3}          {c['control_hedged']:>4}         {st.mean(tok[a])/1000:>5.0f}k")
