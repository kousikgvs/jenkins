import unittest

from src.data_loader import load_customer_data
from src.preprocessing import preprocess_customer_data


class TestCustomerPipeline(unittest.TestCase):
    def test_loader_returns_expected_columns(self):
        data_frame = load_customer_data()

        self.assertEqual(
            list(data_frame.columns),
            ['customer_id', 'name', 'city', 'age', 'monthly_spend'],
        )
        self.assertEqual(len(data_frame), 3)

    def test_preprocessing_fills_missing_age_and_tags_segments(self):
        data_frame = load_customer_data()
        processed = preprocess_customer_data(data_frame)

        self.assertFalse(processed['age'].isna().any())
        self.assertEqual(processed.loc[0, 'city'], 'Hyderabad')
        self.assertEqual(processed.loc[0, 'spend_segment'], 'high')
        self.assertEqual(processed.loc[1, 'spend_segment'], 'standard')


if __name__ == '__main__':
    unittest.main()