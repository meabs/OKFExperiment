import shutil, pathlib
W = pathlib.Path(__file__).parent
HINT = f"Run tests with `{W}/pyv/bin/python -m pytest` (the `ledgerlib` package this service uses is installed there).\n"
OKF = "\n# Repository knowledge\n\n`okf/` is an Open Knowledge Format bundle about this service. `okf/references/ledger-lib/` is the bundle of the separate `ledgerlib` repository it depends on. Start at `okf/index.md`. Use it to find your way around.\n"
TRUST = "\nEach concept's `generated` field says how it was produced. A concept with no `verified` entry is unverified: machine-written and not reviewed by a person.\n"
STALE = "\nA concept whose `stale_after` time has passed is stale: re-check it against the source before relying on it.\n"
SRC = f"\nThe `ledgerlib` library's repository is checked out at `{W}/ledger-lib` (read-only reference).\n"
ARMS = {"none": HINT, "source": HINT + SRC, "fresh": HINT + OKF + TRUST, "fresh_tags": HINT + OKF + TRUST, "stale": HINT + OKF + TRUST, "stale_tags": HINT + OKF + TRUST + STALE}
ov = W / "overlays_c"
shutil.rmtree(ov, ignore_errors=True)
arms = []
for arm, text in ARMS.items():
    d = ov / arm
    d.mkdir(parents=True)
    if arm not in ("none", "source"):
        shutil.copytree(W / "bundles" / f"c_{arm}", d / "okf")
    (d / "AGENTS.md").write_text(text, encoding="utf-8")
    arms.append(f'[[arms]]\nname = "{arm}"\noverlay = "{d}"\n' + ('uses = "okf/"\n' if arm not in ("none", "source") else 'uses = "ledger-lib"\n' if arm == "source" else ""))
def q(id, prompt):
    return f'[[questions]]\nid = "{id}"\nrepo = "svc"\nverify = "bash $OKF_EXP/verify_c.sh {id}"\nprompt = """{prompt}"""\n'
qs = [
 q("c1", "In this service, add `InvoiceService.refund_invoice(invoice_id, reason)`: it refunds the whole invoice through the ledger and returns the id of the refund entry. Calling it again for an invoice that is already refunded must return the same entry id and must not post a second refund. An unknown invoice raises InvoiceNotFound. Keep existing tests passing. Do not add tests."),
 q("c2", "In this service, add `InvoiceService.refund_invoice_partial(invoice_id, amount, reason)` where amount is a Decimal in currency units: it refunds that part of the invoice through the ledger and returns the id of the refund entry. A refund larger than the invoice total must be rejected by the ledger's own error and leave the balance unchanged, and an invoice can be refunded only once. Keep existing tests passing. Do not add tests."),
 q("c3", "In this service, add `InvoiceService.customer_balance(customer)` returning what the ledger says the customer owes, as a Decimal in currency units (0 for an unknown customer). Keep existing tests passing. Do not add tests."),
]
toml = f'''name = "okf-crossrepo-v2"
[defaults]
reps = 4
parallel = 3
timeout = 900
baseline = "none"
prompt_suffix = "Answer briefly and say which tools or files you used."
[[repos]]
name = "svc"
source = "{W / 'invoice-service'}"
''' + "\n".join(arms) + f'''
[[agents]]
name = "codex"
model = "gpt-5.6-luna"
edits = true
args = ["--ignore-user-config", "-c", "model_reasoning_effort=\\"medium\\""]
env = {{ OKF_EXP = "{W / 'exp'}", OKF_PY = "{W / 'pyv/bin/python'}" }}

''' + "\n".join(qs)
(W / "trial_c2.toml").write_text(toml, encoding="utf-8")
