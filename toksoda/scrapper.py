from selenium import webdriver
from fake_useragent import UserAgent


ua = UserAgent()
ua_chrome = 'User-Agent=' + str(ua.chrome)
options = webdriver.ChromeOptions()

# options.add_argument('headless')
# options.add_argument('window-size=1920x1080')
options.add_argument('disable-gpu')
options.add_argument(ua_chrome)
options.add_argument('lang=ko_KR')



driver = webdriver.Chrome('lib/chromedriver',chrome_options=options)
driver.get('about:blank')
driver.get('http://www.nate.com')

driver.execute_script("Object.defineProperty(navigator, 'plugins', {get: function() {return[1,2,3,4,5];},});")
driver.execute_script("Object.defineProperty(navigator, 'languages', {get: function() {return ['ko-KR', 'ko']}})")
driver.execute_script("const getParameter = WebGLRenderingContext.getParameter;WebGLRenderingContext.prototype.getParameter = function(parameter) {if (parameter === 37445){return 'NVIDIA Corporation'} if (parameter === 37446){return 'NVIDIA GeForce GTX 980 Ti OpenGL Engine';}return getParameter(parameter);};")

#driver.quit()
