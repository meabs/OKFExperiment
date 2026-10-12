import assert from "node:assert/strict";
const m = await import(process.cwd() + "/src/util/storeConfig.mjs");
assert.equal(m.canPurchaseOnline({ purchasingEnabled: true, displayShipping: false }), true);
assert.equal(m.canPurchaseOnline({ purchasingEnabled: false }), false);
assert.equal(m.canPurchaseOnline({}), false);
console.log("ok");
