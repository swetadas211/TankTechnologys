class technology:
    def __init__(self, page):
        self.page = page

        self.tech = page.locator("(//a[text()='Technologies'])[1]")
        self.ecommerce = page.locator("//strong[text()='eCommerce Development']")
        self.mobileApp = page.locator("//strong[text()='Mobile App Development']")
        self.AI = page.locator("//strong[text()='Artificial Intelligence']")
        self.tech_list = [self.ecommerce, self.mobileApp, self.AI]

        #Ecommerce Development
        self.MD = page.locator('(//a[@href="https://www.tranktechnologies.com/magento-development"])[1]')
        self.OC = page.locator('(//a[@href="https://www.tranktechnologies.com/opencart-development"])[1]')
        self.CD = page.locator('(//a[@href="https://www.tranktechnologies.com/codeigniter-development"])[1]')
        self.WPD = page.locator('(//a[@href="https://www.tranktechnologies.com/wordpress-development"])[1]')
        self.BC = page.locator('(//a[@href="https://www.tranktechnologies.com/big-commerce"])[1]')
        self.SD = page.locator('(//a[@href="https://www.tranktechnologies.com/shopify-development"])[1]')
        self.CSCD = page.locator('(//a[@href="https://www.tranktechnologies.com/cs-cart-development"])[1]')
        self.NJS = page.locator('(//a[@href="https://www.tranktechnologies.com/node-js-development"])[1]')
        self.NC = page.locator('(//a[@href="https://www.tranktechnologies.com/nopcommerce-design-and-development-company"])[1]')
        self.WC = page.locator('(//a[@href="https://www.tranktechnologies.com/woocommerce-development"])[1]')
        self.LD = page.locator('(//a[@href="https://www.tranktechnologies.com/laravel-development"])[1]')
        self.PD = page.locator('(//a[@href="https://www.tranktechnologies.com/prestashop-development"])[1]')
        self.DD = page.locator('(//a[@href="https://www.tranktechnologies.com/drupal-development"])[1]')
        self.WD = page.locator('(//a[@href="https://www.tranktechnologies.com/wix-development"])[1]')
        self.JD = page.locator('(//a[@href="https://www.tranktechnologies.com/joomla-development"])[1]')
        self.RJSD = page.locator('(//a[@href="https://www.tranktechnologies.com/react-js-development"])[1]')
        self.EJSD = page.locator('(//a[@href="https://www.tranktechnologies.com/express-js-development"])[1]')
        self.ecommerce_list = [self.MD,self.OC,self.CD,self.WPD,self.BC,self.SD,self.CSCD,self.NJS,self.NC,
                                self.WC,self.LD,self.PD,self.DD,self.WD, self.JD,self.RJSD,self.EJSD,]
        
        #MobileApp Developament
        self.RNAD = page.locator('(//a[@href="https://www.tranktechnologies.com/react-native-mobile-app-development"])[1]')
        self.EMAD = page.locator('(//a[@href="https://www.tranktechnologies.com/enterprise-mobile-app-development"])[1]')
        self.AMAD = page.locator('(//a[@href="https://www.tranktechnologies.com/xamarin-mobile-app-development"])[1]')
        self.KMAD = page.locator('(//a[@href="https://www.tranktechnologies.com/kotlin-mobile-app-development"])[1]')
        self.FMAD = page.locator('(//a[@href="https://www.tranktechnologies.com/flutter-mobile-app-development"])[1]')
        self.IMAD = page.locator('(//a[@href="https://www.tranktechnologies.com/ionic-mobile-app-development"])[1]')
        self.SMAD = page.locator('(//a[@href="https://www.tranktechnologies.com/swift-mobile-app-development"])[1]')
        self.ABD = page.locator('(//a[@href="https://www.tranktechnologies.com/appointment-booking-development"])[1]')
        self.mobile_list = [self.RNAD,self.EMAD,self.AMAD,self.KMAD,self.FMAD,self.IMAD,self.SMAD,self.ABD]

    def tech_hover(self):
        for i in self.tech_list:
            self.tech.hover()
            i.hover()
            self.page.wait_for_load_state('load')

    def ecommerce_click(self):
        for i in self.ecommerce_list:
            self.page.wait_for_load_state('load')
            self.tech.hover()
            self.ecommerce.hover()
            i.click()
            self.page.wait_for_load_state('load')

    def mobileApp_click(self):
        for i in self.mobile_list:
            self.page.wait_for_load_state('load')
            self.tech.hover()
            self.mobileApp.hover()
            i.click()
            self.page.wait_for_load_state('load')
