class Util:
    @staticmethod
    def monthly_payment(principal, year, interest):
        """
        Calculates Monthly Payment Amount for Loan of given Principal, Years and Rate of Interest by the user.
        :param principal: Principal Amount taken as a Loan by the user.
        :param year: Years of Loan provided by the user.
        :param interest: Rate of Interest of Loan provided by user.
        :return: Monthly payment for Loan Payment.
        """
        n = 12 * year
        r = interest / (12 * 100)

        payment = (principal * r) / (1 - ((1 + r) ** (-n)))
        return round(payment, 2)


def main():
    try:
        principal = float(input("Enter the principle loan amount: "))
        year = float(input("Number of years would it take to pay off: "))
        interest = float(input("Percent of Interest : "))
        payment_instance = Util()
        payment = payment_instance.monthly_payment(principal, year, interest)
        print("Monthly Payment = ", payment)
    except Exception as e:
        print("{} is raised.".format(str(e)))


if __name__ == "__main__":
    main()
