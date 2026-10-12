#!/usr/bin/env bash
d="$1"; mkdir -p "$d/src/util"
cat > "$d/src/util/cartRequest.mjs" <<'J'
export function buildAddToCartRequest({ cartId, sku, quantity, voucher }) {
  const body = { product: sku, quantity };
  if (voucher) body.voucher = voucher;
  return cartId ? { method: "PUT", path: `cart/${cartId}`, body } : { method: "POST", path: "cart/", body };
}
J
cat > "$d/src/util/searchRequest.mjs" <<'J'
export function buildSearchRequest({ query, page, pageSize }) {
  return { method: "POST", path: "search/", body: { query, size: pageSize, offset: (page - 1) * pageSize } };
}
J
cat > "$d/src/util/reviewsRequest.mjs" <<'J'
export function buildReviewsRequest({ productId, store }) {
  return { method: "GET", path: `product/${productId}/reviews?store=${store}` };
}
J
cat > "$d/src/util/storeConfig.mjs" <<'J'
export function canPurchaseOnline(config) { return config.purchasingEnabled === true; }
J
