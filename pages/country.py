class country:
    def __init__(self, page):
        self.page = page

        self.drp = page.locator('//select[@id="countrySelector"]')

    def country_click(self):

        self.drp.select_option("uae")
        self.page.wait_for_timeout(3000)

        self.drp.select_option("india")
        self.page.wait_for_timeout(3000)


        self.drp.select_option("usa")
        self.page.wait_for_timeout(3000)
        