# def test_untitled(self):
#     driver = self.driver
#     driver.get(self.base_url + "/users/53753")
#     driver.find_element_by_id("realname").clear()
#     driver.find_element_by_id("realname").send_keys(u"发发是去")
#     driver.find_element_by_id("idnumber").clear()
#     driver.find_element_by_id("idnumber").send_keys("11010519980505297x")
#     driver.find_element_by_id("captcha-button").click()
#     driver.find_element_by_css_selector("fieldset > input[type=\"text\"]").clear()
#     driver.find_element_by_css_selector("fieldset > input[type=\"text\"]").send_keys("5642")
#     driver.find_element_by_css_selector("button.confirm").click()
#     driver.find_element_by_css_selector("button.confirm").click()
#     driver.find_element_by_css_selector("button.confirm").click()
#     driver.find_element_by_css_selector("button.confirm").click()
#     driver.find_element_by_id("idcode").clear()
#     driver.find_element_by_id("idcode").send_keys("550621")
#     driver.find_element_by_id("idcode").clear()
#     driver.find_element_by_id("idcode").send_keys("550621")
#     driver.find_element_by_id("submission").click()
#     driver.find_element_by_id("submission").click()
#     driver.find_element_by_css_selector("span.two-step.hover").click()
import re
a = '200,000.00元'
a1 = a.replace(',','')
a3 = a1.replace('元','')
print(a1)
print(a3)
print(type(float(a3)))
a2 = re.sub('\D','.',a1)
print(a2)

def replacestr(gfa): #获得a的数字输出类型
    h = gfa.replace(',', '')
    print(h)
    h2 = float(h.replace('元',''))
    print(h2)
    h3 = '%.2f' % h2
    print(h3)
    print(type(h3))
    return h3
# replacestr(a)
print(replacestr(a))
