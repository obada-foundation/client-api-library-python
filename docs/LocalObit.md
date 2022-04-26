# LocalObit


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**owner** | **str** | Owner is the person/entity that owns the obit and the physical asset it represents. | 
**obit_status** | **str** | Represent available Obit statuses:   - FUNCTIONAL   - NON_FUNCTIONAL   - DISPOSED   - STOLEN   - DISABLED_BY_OWNER  | 
**manufacturer** | **str** | Waiting more specific details from Rohi | 
**part_number** | **str** | Manufacturer provided. In cases where no part number is provided for the product, use model, or the most specific ID available from the manufacturer. MWCN2LL/A (an iPhone 11 Pro, Silver, 256GB, model A2160) | 
**serial_number** | **str** | Serial Number | 
**modified_at** | **datetime** |  | 
**metadata** | [**[LocalObitMetadataInner]**](LocalObitMetadataInner.md) | Get description from Rohi | [optional] 
**documents** | [**[LocalObitDocumentsInner]**](LocalObitDocumentsInner.md) | To generate this link, take an SHA-256 hash of the document, and link to it as https://www.some-website.com?h1&#x3D;hash-of-document. Note this does not yet adhere to the hashlink standard.  | [optional] 
**structured_data** | [**[LocalObitStructuredDataInner]**](LocalObitStructuredDataInner.md) | Same as metadata but bigger. Key (string) &#x3D;&gt; Value (string) (hash per line sha256(key + value)) | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


