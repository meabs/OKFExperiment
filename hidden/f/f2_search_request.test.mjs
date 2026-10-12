import assert from "node:assert/strict";
const m = await import(process.cwd() + "/src/util/searchRequest.mjs");
const r = m.buildSearchRequest({ query: "shoes", page: 3, pageSize: 20 });
assert.equal(r.method, "POST"); assert.match(r.path, /^search\/?$/);
assert.equal(r.body.query, "shoes"); assert.equal(r.body.size, 20); assert.equal(r.body.offset, 40);
const first = m.buildSearchRequest({ query: "x", page: 1, pageSize: 10 });
assert.equal(first.body.offset, 0);
console.log("ok");
