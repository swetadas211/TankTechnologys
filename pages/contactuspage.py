class contact:
    def __init__(self,page):
        self.page=page

        self.CONT=page.locator('(//a[@href="https://www.tranktechnologies.com/contact-us"])[1]')
    

        self.NAME=page.locator('(//input[@placeholder="Your Name"])[2]')
        self.EMAIL=page.locator('(//input[@type="email"])[2]')
        self.COMPANY=page.locator('(//input[@name="company"])[2]')
        self.SELECT=page.locator('(//select[@name="service"])[2]')
        self.PHONE=page.locator('(//input[@name="phone"])[2]')
        self.MESSAGE=page.locator('(//textarea[@name="message"])[2]')
        
    def fill_contact(self):
        self.CONT.click()
        self.NAME.fill("SWETA DAS")
        self.EMAIL.fill("swetadas211@gmail.com")
        self.COMPANY.fill("YS")
        self.SELECT.select_option("Web Development")
        self.PHONE.fill('9876543356')
        self.MESSAGE.fill("Done")
        
        self.page.wait_for_timeout(3000)
