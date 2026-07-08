class navmenu:
    def __init__(self,page):
        self.page=page

        self.aboutus=page.locator("(//a[text()='Contact us'])[1]")
        self.portfolio=page.locator("//a[text()='Portfolio']")

    def nav_click(self):
        self.aboutus.click()
        self.page.wait_for_timeout(2000)

        self.page.go_back()
        self.portfolio.click()