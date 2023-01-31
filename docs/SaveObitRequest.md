# SaveObitRequest

Request to save Obit

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**manufacturer** | **str** | Waiting more specific details from Rohi | 
**part_number** | **str** | Manufacturer provided. In cases where no part number is provided for the product, use model, or the most specific ID available from the manufacturer. MWCN2LL/A (an iPhone 11 Pro, Silver, 256GB, model A2160) | 
**serial_number** | **str** | Serial number hashed with sha256 hash function | 
**documents** | [**[DeviceDocument]**](DeviceDocument.md) |  | [optional] 
**address** | **str** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


