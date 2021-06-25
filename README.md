# Volumetric Monitor: Comprehensive Comparison
This ModelOpCenter monitor detects discrepancies between two assets based on their record counts & identifiers.

## Required Assets

| Type          | Number | Description                                           |
| ------------- | ------ | ----------------------------------------------------- |
| Baseline Data | **1**  | First dataset to compare |
| Sample Data   | **1**  | Second dataset to compare |

## Monitor Output

```JSON
{
    "identifiers_match": <boolean>,
    "record_count_difference": <record_count_difference>,

    "volumetrics":[
        {
            "test_name": "Identifier Comparison",
            "test_category": "volumetrics",
            "test_type": "identifier_comparison",
            "test_id": "volumetrics_identifier_comparison",
            "values": {
                "identifiers_match": <boolean>,
                "dataframe_1": {
                    "identifier_columns": <id_columns_array>,
                    "record_count": <dataframe_1_record_count>,
                    "unique_identifier_count": <dataframe_1_unique_identifier_count>,
                    "extra_identifiers": {
                        "total": <number_of_extra_identifiers>,
                        "breakdown": <breakdown_of_extra_identifiers>
                    }
                },
                "dataframe_2": {
                    "identifier_columns": <id_columns_array>,
                    "record_count": <dataframe_1_record_count>,
                    "unique_identifier_count": <dataframe_2_unique_identifier_count>,
                    "extra_identifiers": {
                        "total": <number_of_extra_identifiers>,
                        "breakdown": <breakdown_of_extra_identifiers>
                    }
                }
            }
        },
        {
            "test_name": "Count Comparison",
            "test_category": "volumetrics",
            "test_type": "count_comparison",
            "test_id": "volumetrics_count_comparison",
            "values": {
                "dataframe_1_record_count": 8,
                "dataframe_2_record_count": 6,
                "record_count_difference": 2
            }
        }
    ]
}
```

## Assumptions & Requirements
 - Underlying `BUSINESS_MODEL` being monitored has an **extended input schema** asset.
 - Input data contains at least one `identifier` column.

## Execution
1. `init` function extracts **extended** input schema (corresponding to the `BUSINESS_MODEL` being monitored) from job JSON.
2. **Monitoring parameters** are set based on the schema above. `identifier_columns` are determined accordingly.
3. `metrics` function runs **identifier_comparison** and **count_comparison** volumetrics test.
4. Test results are returned under the list of `volumetrics` tests.
