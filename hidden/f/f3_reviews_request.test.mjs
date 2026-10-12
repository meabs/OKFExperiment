import assert from "node:assert/strict";
const m = await import(process.cwd() + "/src/util/reviewsRequest.mjs");
const r = m.buildReviewsRequest({ productId: 42, store: "DEFAULT" });
assert.equal(r.method, "GET");
assert.match(r.path, /^product\/42\/reviews(\?|$)/, "the backend declares the singular path product/{id}/reviews");
assert.match(r.path, /store=DEFAULT/);
console.log("ok");
