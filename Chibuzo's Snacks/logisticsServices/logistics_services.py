class LogisticsServices:
    @staticmethod
    def calculate_riders_wage(successful_deliveries: int) -> int:
        BASE_PAY = 5000

        if successful_deliveries <= 0:
            return 0
        elif successful_deliveries < 50:
            return (successful_deliveries * 160) + BASE_PAY
        elif successful_deliveries <= 59:
            return (successful_deliveries * 200) + BASE_PAY
        elif successful_deliveries <= 69:
            return (successful_deliveries * 250) + BASE_PAY
        else:
            return successful_deliveries * 500 + BASE_PAY
