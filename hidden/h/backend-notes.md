# Backend API notes (for storefront developers)

A short reference of the kind a backend team hands to a client team: conventions, the endpoints the storefront uses and the field names people get wrong. Written by hand, and every fact in it was checked against the backend source. It is deliberately not exhaustive.

## Conventions

- Base path `/api/v1`; paths below omit it. All endpoints accept the optional query parameters `store` (default `DEFAULT`) and `lang` (default `en`).
- Endpoints under `auth/` need the header `Authorization: Bearer <token>`. The anonymous cart and checkout endpoints have no `auth/` prefix.

## Cart (anonymous, identified by the cart `code` returned when it is created)

| Call | Body | Returns |
| --- | --- | --- |
| `POST cart` | `{product, quantity, voucher, attributes}` | the cart |
| `GET cart/{code}` | | the cart |
| `PUT cart/{code}` | the same body | the cart |
| `DELETE cart/{code}/product/{sku}?body=true` | | the cart |
| `POST cart/{code}/promo/{promo}` | | the cart |
| `GET cart/{code}/total` | | order totals |
| `POST cart/{code}/shipping` | `{postalCode, countryCode}` | shipping quote with `shippingOptions` |
| `POST cart/{code}/checkout` | checkout body (below) | order confirmation |

- In the cart body, `product` holds the product **sku** (a string), not a numeric id. A cart line is addressed by its sku in the `DELETE` URL for the same reason.
- `DELETE` returns 204 with no body unless `body=true` is given.
- The cart response has `code`, `subtotal`, `total`, `quantity`, `promoCode`, `products` (the lines) and `totals`.

## Checkout body

`{quoteId, shoppingCartId, currency, termsAccepted, orderNote, payment: {paymentType, transactionType, processor, cardToken, amount}}`. The chosen shipping option goes in `quoteId`; `processor` is the payment module and `cardToken` the payment token.

## Customer and login

| Call | Body | Returns |
| --- | --- | --- |
| `POST customer/login` | `{username, password}` | `{id, token}`; bad credentials give 401 `{"message":"Bad credentials"}` |
| `POST customer/register` | customer: `emailAddress, password, repeatPassword, userName, storeCode, gender, language, billing` | `{id, token}` |
| `GET auth/customer/profile` | | the customer |
| `GET auth/customer/refresh` | | `{id, token}` with a fresh token |
| `GET auth/customer/cart` | | the customer's cart |

## Orders

| Call | Returns |
| --- | --- |
| `GET auth/orders?page=0&count=100` | `{orders, pageCount, totalRecords, itemsOnPage, recordsFiltered}`; pages start at 0, `count` defaults to 100 |
| `GET auth/orders/{id}` | one order |

## Search and catalogue

| Call | Body or query | Returns |
| --- | --- | --- |
| `POST search` | `{query, size, offset}` | a list of matches |
| `POST search/autocomplete` | `{query, size, offset}` | suggestions |
| `GET products?category=&name=&page=&count=` | | a product list |
| `GET shipping/country` | | countries the store ships to |
