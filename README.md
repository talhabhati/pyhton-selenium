# python-selenium-automation/
│
├── drivers/              # Browser drivers (if required)
├── scripts/              # Selenium automation scripts
├── screenshots/          # Screenshots captured during execution
├── pytest_tests/         # PyTest test cases
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation

# Create Virtual Environment
##
``` py
python -m venv venv
source venv/bin/activate     # Linux / Mac
venv\Scripts\activate        # Windows
```

# Install Dependencies
##
```bash
pip install selenium
pip install webdriver-manager
pip install pytest
```

# 🌐 Browser Automation Examples
## Open Website in Chrome
``` py
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.google.com")
driver.maximize_window()
driver.close()
```
## Open Website in Firefox / Edge
``` py
driver = webdriver.Firefox()
driver = webdriver.Edge()
```

# 🔍 Selenium Locators Covered

## Selenium supports 8 locators, all demonstrated in this project:
1. ID
2. Name
3. CSS Selector
4. XPath
5. Tag Name
6. Class Name
7. Link Text
8. Partial Link Text

Example:
``` py
from selenium.webdriver.common.by import By
driver.find_element(By.ID, "user-name").send_keys("standard_user")
```
# ⏳ Synchronization (Waits)
## Implicit Wait
```py
driver.implicitly_wait(10)
 ```
## Explicit Wait
``` py
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

wait = WebDriverWait(driver, 20)
wait.until(EC.element_to_be_clickable((By.ID, "login-button")))
```
# 🧭 XPath & CSS Selectors
1. XPath Types
2. Absolute XPath
3. Relative XPath
4. Dynamic XPath
5. XPath Axes (parent, child, sibling, ancestor)

### Example:
``` py
//input[@id='Password']
//input[contains(@id,'Pass')]
```
## CSS Selectors
``` py
#id
tagname.classname
input[id^='user']
input[id$='Email']
```
# 🖱️ Mouse & Keyboard Actions

1. Mouse hover
2. Right click
3. Double click
4. Drag and drop

``` py
from selenium.webdriver import ActionChains
actions = ActionChains(driver)
actions.move_to_element(element).perform()
```
# 📸 Screenshots
## Full Page Screenshot
``` py
driver.save_screenshot("login.png")
```
## Element Screenshot
``` py
element.screenshot("element.png")
```

