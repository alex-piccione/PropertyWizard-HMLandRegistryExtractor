
// index on "hm-price-data-raw" collection

db.getCollection("hm-price-data-raw").createIndex(
    {
        "transaction_id": 1
    },
    {"unique": true}
)


// indexes on "hm-sale" collection

db.getCollection('hm-sale').createIndex(
    {
        "raw_data_id": 1
    },
    {"unique": true}
)


db.getCollection('hm-sale').createIndex(
    {
        "post_code": 1, "address": 1, "date": 1, "transaction_category": 1
    },
    {"unique": true}
)

db.getCollection('hm-sale').createIndex(
    {
        "post_code": 1,
    }
)

db.getCollection('hm-sale').createIndex(
    {
        "partial_post_code": 1,
    }
)
