# superapp

## json-processing.py
The lambda function is event driven. It picks up files named .json expected to be 'product' and puts them in dynamodb table.

```json
{
    "product_id": 1,
    "name": "screwdriver",
    "manufacturer": "Bosch",
    "location": ["store1"],
    "barcode": "1212-1232-1232-3433"
}