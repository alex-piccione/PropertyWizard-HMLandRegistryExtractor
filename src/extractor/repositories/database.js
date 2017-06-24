
// index on "hm-price-data-raw" collection

db.getCollection("hm-price-data-raw").createIndex(
    {
        "transaction_id": 1
    },
    {"unique": true}
)