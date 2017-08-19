import unittest

from extractor.saleDataProcessor import SaleDataProcessor
from extractor.entities.saleRawData import SaleRawData


class SaleDataProcessorTest(unittest.TestCase):

    def _get_complete_address(self):

        test_cases = []
        test_cases.append({  # PAON and SAON are defined
            "saon": "saon",
            "paon": "paon",
            "street": "street",
            "locality": "locality",
            "expected_address": "paon, saon street locality"
        }),
        test_cases.append({  # PAON is not defined
            "saon": "saon",
            "paon": "",
            "street": "street",
            "locality": "",
            "expected_address": "saon street"
        }),
        test_cases.append({  # real case 1
            "saon": "46",
            "paon": "FLAT 4",
            "street": "EGERTON GARDENS",
            "locality": "",
            "expected_address": "FLAT 4, 46 EGERTON GARDENS"
        })

        processor = SaleDataProcessor()

        for case in test_cases:
            raw_data = self._create_sale_raw_data(case["paon"], case["saon"], case["street"], case["locality"])

            # execute
            address = processor._get_complete_address(raw_data)

            self.assertEqual(address, case["expected_address"], case["expected_address"])

    def _get_partial_post_code(self):

        test_cases = []
        test_cases.append({"input": "", "expected_result": ""})
        test_cases.append({"input": "AB1", "expected_result": "AB1"})
        test_cases.append({"input": "AB1 2CD", "expected_result": "AB1"})
        test_cases.append({"input": "AB1", "expected_result": "AB1"})
        test_cases.append({"input": "SE17 3AW", "expected_result": "SE17"})
        test_cases.append({"input": "RG1 1NA", "expected_result": "RG1"})
        test_cases.append({"input": "NW1 5LA", "expected_result": "NW1"})
        test_cases.append({"input": "EC2A 3ET", "expected_result": "EC2A"})

        processor = SaleDataProcessor()

        for case in test_cases:
            result = processor._get_partial_post_code(case["input"])
            self.assertEqual(result, case["expected_result"], case["input"])

    def _create_sale_raw_data(self, paon, saon, street, locality):

        data = SaleRawData(None, None, None, None, None, None, None,
                           paon, saon, street, locality,
                           None, None, None, None, None)
        return data
