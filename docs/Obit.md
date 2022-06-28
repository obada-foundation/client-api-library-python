# Obit

OBADA record.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**manufacturer** | **str** | Waiting more specific details from Rohi | 
**part_number** | **str** | Manufacturer provided. In cases where no part number is provided for the product, use model, or the most specific ID available from the manufacturer. MWCN2LL/A (an iPhone 11 Pro, Silver, 256GB, model A2160) | 
**did** | **str** | OBADA decentralized identifier | [optional] 
**usn** | **str** | Test An 8-12 character “URL Shortened” obit. Create the USN by Base(58) encoding the OBIT ID. Take the first 8 characters. Check for duplicates. With 16 million OBITs there is a 40% chance of collision. If so, add 4 characters. Repeat as necessary until a unique USN is generated.  | [optional] 
**owner** | **str** | Owner is the person/entity that owns the obit and the physical asset it represents. Format is a DID like did:obada:owner:1234. However in the current version only test numbers will be used. | [optional] 
**serial_number_hash** | **str** | Serial number hashed with sha256 hash function | [optional] 
**trust_anchor_token** | **str** | JWT token from the trust anchor | [optional] 
**documents** | [**[Document]**](Document.md) | Documents that are attached to Obit | [optional] 
**checksum** | **str** | Hash calculated by SHA256 (previous Obit checksum + Obit data).  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


