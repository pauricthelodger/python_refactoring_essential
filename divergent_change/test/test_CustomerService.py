import unittest

from divergent_change.src.CustomerService import (
    CustomerService,
    EmailValidator,
)


class TestCustomerService(unittest.TestCase):

    def setUp(self):
        self.service = CustomerService()
        self.email_validator = EmailValidator()

    # -------------------------
    # is_valid_email tests
    # -------------------------

    def test_is_valid_email_returns_false_when_email_is_none(self):
        self.assertFalse(self.email_validator.is_valid_email(None))

    def test_is_valid_email_returns_false_when_email_is_empty(self):
        self.assertFalse(self.email_validator.is_valid_email(""))

    def test_is_valid_email_returns_false_when_missing_at_symbol(self):
        self.assertFalse(self.email_validator.is_valid_email("invalid.email.com"))

    def test_is_valid_email_returns_false_when_missing_local_part(self):
        self.assertFalse(self.email_validator.is_valid_email("@domain.com"))

    def test_is_valid_email_returns_false_when_missing_domain(self):
        self.assertFalse(self.email_validator.is_valid_email("user@"))

    def test_is_valid_email_returns_true_when_email_is_valid_with_tag(self):
        self.assertTrue(self.email_validator.is_valid_email("user.name+tag@example.com"))

    def test_is_valid_email_returns_true_when_simple_valid_email(self):
        self.assertTrue(self.email_validator.is_valid_email("user@example.com"))

    # -------------------------
    # format_display_name tests
    # -------------------------

    def test_format_display_name_trims_and_uppercases_last_name(self):
        result = self.service.format_display_name(" John ", " smith ")
        self.assertEqual("John SMITH", result)

    def test_format_display_name_handles_empty_strings(self):
        result = self.service.format_display_name("", "")
        self.assertEqual(" ", result)

    def test_format_display_name_handles_single_character_names(self):
        result = self.service.format_display_name("A", "b")
        self.assertEqual("A B", result)

    # -------------------------
    # calculate_loyalty_points tests
    # -------------------------

    def test_calculate_loyalty_points_returns_zero_when_no_purchases(self):
        self.assertEqual(0, self.service.calculate_loyalty_points(0))

    def test_calculate_loyalty_points_calculates_correctly_for_positive_values(self):
        self.assertEqual(50, self.service.calculate_loyalty_points(5))

    def test_calculate_loyalty_points_handles_large_numbers(self):
        self.assertEqual(100_000, self.service.calculate_loyalty_points(10_000))

    def test_calculate_loyalty_points_allows_negative_values(self):
        self.assertEqual(-50, self.service.calculate_loyalty_points(-5))

    # -------------------------
    # determine_account_status tests
    # -------------------------

    def test_determine_account_status_returns_inactive_when_over_365_days(self):
        self.assertEqual("INACTIVE", self.service.determine_account_status(366))

    def test_determine_account_status_returns_dormant_when_between_31_and_365(self):
        self.assertEqual("DORMANT", self.service.determine_account_status(100))

    def test_determine_account_status_returns_active_when_30_days_or_less(self):
        self.assertEqual("ACTIVE", self.service.determine_account_status(30))
        self.assertEqual("ACTIVE", self.service.determine_account_status(0))

    def test_determine_account_status_treats_negative_days_as_active(self):
        self.assertEqual("ACTIVE", self.service.determine_account_status(-10))


if __name__ == "__main__":
    unittest.main()
