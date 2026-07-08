class footer:
    def __init__(self, page):
        self.page = page

        # WEB_DEVELOPMENT
        self.WEB=page.locator("//a[text()='Web Development']")
        self.CMS = page.locator("//a[text()='CMS Website Development']")
        self.CWD = page.locator("//a[text()='Custom Web Portal Development']")
        self.WEB_LIST = [self.WEB,self.CMS, self.CWD]

        self.arrow1=page.locator('(//i[@class="fa fa-chevron-down text-red-2"])[1]')
        self.WEDD=page.locator("//a[text()='Website Development']")

        # UI/UX DESIGN
        self.MAD = page.locator("//a[text()='Mobile App Design']")
        self.RWD = page.locator("//a[text()='Responsive Web Design']")
        self.BID = page.locator("//a[text()='Brand Identity Design']")
        self.UI_LIST = [self.MAD, self.RWD, self.BID]

        # APP DEVELOPMENT
        self.IOS = page.locator("//a[text()='iOS App Development']")
        self.HMD = page.locator("//a[text()='Hybrid Mobile App Development']")
        self.CAD = page.locator("//a[text()='Cross-Platform App Development']")
        self.PWD = page.locator("//a[text()='Progressive Web App Development']")
        self.APP_LIST = [self.IOS, self.HMD, self.CAD, self.PWD]

        # Additional app links
        self.arrow2=page.locator('(//i[@class="fa fa-chevron-down text-red-2"])[2]')
        self.APD = page.locator("(//a[text()='Android App Development'])[1]")
        self.AD = page.locator("(//a[text()='App Development'])[2]")
        self.AD_LIST = [self.APD, self.AD]

        # GRAPHICS DESIGNING
        self.LD = page.locator("//a[text()='Logo Design']")
        self.BD = page.locator("//a[text()='Banner Design']")
        self.PD = page.locator("//a[text()='Packaging Design']")
        self.BCD = page.locator("//a[text()='Business cards Design']")
        self.GP_LIST = [self.LD, self.BD, self.PD, self.BCD]

    def web_development_click(self):
        for i in self.WEB_LIST:
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()

    def ecommerce_click(self):
            self.arrow1.click()
            self.WEDD.click()
            self.page.wait_for_load_state("load")
            
    def ecommerce_click(self):
            self.arrow1.click()
            with self.page.context.expect_page() as new_page_info:self.WEDD.click()
            new_tab = new_page_info.value
            new_tab.wait_for_load_state("load")
            new_tab.close()
        

    def ui_ux_design_click(self):
        for i in self.UI_LIST:
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()

    def app_development_click(self):
        for i in self.APP_LIST:
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()

    def additional_app_links_click(self):
        for i in self.AD_LIST:
            self.arrow2.click()
            i.click()
            self.page.wait_for_load_state("load")
            
    def graphics_designing_click(self):
        for i in self.GP_LIST:
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()

    