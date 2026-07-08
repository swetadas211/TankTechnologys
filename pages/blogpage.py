class blog:
    def __init__(self, page):
        self.page = page

        #BLOG
        self.BLOG=page.locator('(//a[@href="https://www.tranktechnologies.com/blog/"])[1]')

        ##SUBLOCATOR_BLOG
        self.APP=page.locator('//a[@href="/blog/category/app-development/"]')
        self.WEB=page.locator('//a[@href="/blog/category/web-development/"]')
        self.ST=page.locator('//a[@href="/blog/category/software-development/"]')
        self.DM=page.locator('//a[@href="/blog/category/digital-marketing/"]')
        self.EM=page.locator('//a[@href="/blog/category/email-marketing/"]')
        self.AI=page.locator('//a[@href="/blog/category/artificial-intelligence/"]')
        self.UI=page.locator('//a[@href="/blog/category/ui-ux-design/"]')

        self.BLOG_list=[self.APP,self.WEB,self.ST,self.DM,self.EM,self.AI,self.EM,self.UI]
        
    def blog_hover(self):
        self.BLOG.click()
        for i in self.BLOG_list:
            i.click()
            self.page.wait_for_timeout(2000)
            self.page.go_back()