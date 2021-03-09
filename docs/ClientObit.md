# ClientObit


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**obit_did** | **str** |  | [optional] 
**usn** | **str** |  | [optional] 
**owner_did** | **str** |  | [optional] 
**obit_status** | **str** | Represent available Obit statuses:   - FUNCTIONAL   - NON_FUNCTIONAL   - DISPOSED   - STOLEN   - DISABLED_BY_OWNER  | [optional] 
**manufacturer** | **str** |  | [optional] 
**part_number** | **str** |  | [optional] 
**serial_number_hash** | **str** |  | [optional] 
**modified_at** | **datetime** |  | [optional] 
**root_hash** | **str** |  | [optional] 
**metadata** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Get description from Rohi | [optional] 
**documents** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | To generate this link, take an SHA-256 hash of the document, and link to it as https://www.some-website.com?h1&#x3D;hash-of-document. Note this does not yet adhere to the hashlink standard.  | [optional] 
**structured_data** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Same as metadata but bigger. Key (string) &#x3D;&gt; Value (string) (hash per line sha256(key + value)) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


