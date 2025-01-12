from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest



class NewVisitorTest(unittest.TestCase) :
    def setUp(self) -> None:
        self.brower = webdriver.Chrome(executable_path="C:/Users/bottlechrome/Documents/GitHub/DeepDive/crawling/chromedriver.exe")
        self.brower.implicitly_wait(3)
    
    def tearDown(self) -> None:
        self.brower.quit()
    
    def test_can_start_a_list_and_retrieve_it_later(self) :

        self.brower.get('http://localhost:8000')
        self.assertIn('To-Do', self.brower.title )
        
        header_text = self.brower.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        inputbox = self.brower.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'),'작업 아이템 입력')
        inputbox.send_keys('공작깃털 사기')

        inputbox.send_keys(Keys.ENTER)
        


        table = self.brower.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(any(row.text == '1: 공작깃털 사기' for row in rows),"신규 작업이 테이블에 표시되지 않는다.")

        self.fail("Finished the test!")

if __name__ == '__main__' :
    unittest.main(warnings='ignore')

