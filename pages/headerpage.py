from config import url
class header:
    def __init__(self,page):
     self.page=page

     self.freeQutoe=page.locator("(//a[text()='Get a Free Quote'])[1]")

     self.name=page.locator('//input[@placeholder="Your Name"]')
     self.mail=page.locator('//input[@placeholder="Your Mail"]')
     self.service=page.locator('//select[@name="service"]')
     self.company=page.locator('//input[@placeholder="Your Company"]')
     self.phone=page.locator('//input[@placeholder="Your Phone"]')
     self.message=page.locator('//textarea[@placeholder="Message"]') 

     self.cross=page.locator('//div[@class="cm-close-btn"]')

    def freeQutoe_fill(self):

        self.page.goto(url)
        self.page.wait_for_load_state("load")

        self.freeQutoe.click()

        self.name.fill("sweta")
        self.mail.fill("swetadas211@gmail.com")
        self.service.select_option("Web Development")
        self.company.fill("ys")
        self.phone.fill("987643456")
        self.message.fill("added all details")
        self.page.wait_for_timeout(3000)
        self.cross.click()



