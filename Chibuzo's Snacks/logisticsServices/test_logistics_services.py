import unittest

from logisticsServices.logistics_services import LogisticsServices


class LogisticsServicesTest(unittest.TestCase):
    def test_given_0_successful_deliveries_when_calculated_then_riders_wage_is_0(self):
        self.assertEqual(0, LogisticsServices.calculate_riders_wage(0))

    def test_given_25_successful_deliveries_when_calculated_then_riders_wage_is_9000(self):
        self.assertEqual(9000, LogisticsServices.calculate_riders_wage(25))

    def test_given_49_successful_deliveries_when_calculated_then_riders_wage_is_12840(self):
        self.assertEqual(12840, LogisticsServices.calculate_riders_wage(49))

    def test_given_50_successful_deliveries_when_calculated_then_riders_wage_is_15000(self):
        self.assertEqual(15000, LogisticsServices.calculate_riders_wage(50))

    def test_given_55_successful_deliveries_when_calculated_then_riders_wage_is_16000(self):
        self.assertEqual(16000, LogisticsServices.calculate_riders_wage(55))

    def test_given_60_successful_deliveries_when_calculated_then_riders_wage_is_20000(self):
        self.assertEqual(20000, LogisticsServices.calculate_riders_wage(60))

    def test_given_65_successful_deliveries_when_calculated_then_riders_wage_is_21250(self):
        self.assertEqual(21250, LogisticsServices.calculate_riders_wage(65))

    def test_given_70_successful_deliveries_when_calculated_then_riders_wage_is_40000(self):
        self.assertEqual(40000, LogisticsServices.calculate_riders_wage(70))

    def test_given_80_successful_deliveries_when_calculated_then_riders_wage_is_45000(self):
        self.assertEqual(45000, LogisticsServices.calculate_riders_wage(80))
