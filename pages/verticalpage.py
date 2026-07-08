class vertical:                #It contains all the locators and reusable methods
    def __init__(self, page):  #constructor
        self.page = page       #page object is stored in self.page so it can be used throughout the class.
        self.ver = page.locator("(//a[text()='Verticals'])[1]")

        self.TR = page.locator("//strong[text()='Trading']")
        self.RE = page.locator("//strong[text()='Retail and Ecommerce']")
        self.HC = page.locator("//strong[text()='Healthcare']")
        self.FT = page.locator("//strong[text()='Fintech']")
        self.custom_App = page.locator("//strong[text()='Custom App']")
        self.ver_list = [self.TR, self.RE, self.HC, self.FT, self.custom_App]

        ##TRADING
        self.ST=page.locator('(//a[@class="mm-active"])[1]')
        self.PT=page.locator("//a[text()='Paper Trading']")
        self.CFD=page.locator("(//a[text()='CFD Trading'])[1]")
        self.TAD=page.locator('(//a[@href="https://www.tranktechnologies.com/stock-trading-development-in-massachusetts"])[1]')
        self.AT= page.locator("(//a[text()='Algo Trading'])[1]")
        self.CT=page.locator('(//a[@href="https://www.tranktechnologies.com/custom-trading-software-development-company"])[1]')
        self.WT=page.locator("(//a[text()='Web Portal Trading'])[1]")
        self.TR_list=[self.ST,self.PT,self.CFD,self.TAD,self.AT,self.CT,self.WT]

        ##RETAIL & ECOMMERCE
        self.EW=page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-web-development-company"])[2]') 
        self.AD=page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-app-development"])[1]')
        self.RE_list=[self.EW,self.AD]

        #HEALTHCARE
        self.DIET=page.locator('(//a[@href="https://www.tranktechnologies.com/diet-and-nutrition-app-developement"])[1]')
        self.HTA=page.locator('(//a[@href="https://www.tranktechnologies.com/health-tracking-app"])[1]')
        self.HC_list=[self.DIET,self.HTA]

        #Fintech
        self.posSD=page.locator('(//a[@href="https://www.tranktechnologies.com/pos-software-development-company"])[1]')
        self.crypto=page.locator('(//a[@href="https://www.tranktechnologies.com/cryptocurrency-mobile-app-development-company"])[1]')
        self.FT_list=[self.posSD,self.crypto]

        #Custom App
        self.desktop_dev=page.locator('(//a[@href="https://www.tranktechnologies.com/desktop-application-development-company"])[1]')
        self.crm=page.locator('(//a[@href="https://www.tranktechnologies.com/custom-crm-development-company"])[1]')
        self.hrm=page.locator('(//a[@href="https://www.tranktechnologies.com/hrm-application-development-company"])[1]')
        self.erp=page.locator('(//a[@href="https://www.tranktechnologies.com/erp-app-development-company"])[1]')
        self.travel=page.locator('(//a[@href="https://www.tranktechnologies.com/travel-mobile-app-development-company"])[1]')
        self.elearn=page.locator('(//a[@href="https://www.tranktechnologies.com/e-learning-mobile-app-development-company"])[1]')
        self.dating=page.locator('(//a[@href="https://www.tranktechnologies.com/dating-app-development-company"])[1]')
        self.realestate=page.locator('(//a[@href="https://www.tranktechnologies.com/real-estate-mobile-app-development-company"])[1]')
        self.crmDevUsa=page.locator('(//a[@href="https://www.tranktechnologies.com/usa/custom-crm-development-company-usa"])[1]')                   
        self.customApp_list=[self.desktop_dev,self.crm,self.hrm,self.erp,self.travel,self.elearn,self.dating,self.realestate,self.crmDevUsa]



    def mouse_hover(self):     #method call,used to define a function inside a class.
        for i in self.ver_list:
            self.ver.hover()
            i.hover()
            self.page.wait_for_load_state('load')

    def trading_click(self):
        for i in self.TR_list:
            self.ver.hover()
            self.TR.hover()
            i.click()
            self.page.wait_for_load_state('load')

    def retail_click(self):
        for i in self.RE_list:
            self.ver.hover()
            self.RE.hover()
            i.click()
            self.page.wait_for_load_state('load')
            self.page.go_back()

    def healthcare_click(self):
        for i in self.HC_list:
            self.ver.hover()
            self.HC.hover()
            i.click()
            self.page.wait_for_load_state('load')

    def fintech_click(self):
        for i in self.FT_list:
            self.page.wait_for_load_state('load')
            self.ver.hover()
            self.FT.hover()
            i.click()
            self.page.wait_for_load_state('load')

    def customApp_click(self):
        for i in self.customApp_list:
            self.ver.hover()
            self.custom_App.hover()
            i.click()
            self.page.wait_for_load_state('load')
