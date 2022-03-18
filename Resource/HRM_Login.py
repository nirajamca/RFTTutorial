from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
import CommonFunctions as CF
import AccessorRepository as AR

@keyword
def Open_Browser_To_Login_Page():
    myData = CF.fncGetData('HRM_Login')
    uURL = myData['Option1']

    # Create instance of SeleniumLibrary
    sl = BuiltIn().get_library_instance('SeleniumLibrary')

    # Create a handle for Chrome Webdriver and launch
    sl.create_webdriver('Chrome')

    # Maximize Chrome Window
    sl.maximize_browser_window()

    # Launch Orange HRM Demo site URL
    sl.go_to(uURL)
    BuiltIn().sleep(3)

    # Verify that the page is launched with title
    sl.title_should_be('OrangeHRM')

@keyword
def Enter_Login_Details():
    myData = CF.fncGetData('HRM_Login')
    uUsername = myData['Option2']
    uPassword = myData['Option3']

    # Create instance of SeleniumLibrary
    sl = BuiltIn().get_library_instance('SeleniumLibrary')

    # Enter Login Credentials
    sl.input_text(AR.idtxtLoginUsername, uUsername)
    sl.input_text(AR.idtxtLoginPassword, uPassword)
    BuiltIn().sleep(3)

@keyword
def Submit_Credentials():
    # Create instance of SeleniumLibrary
    sl = BuiltIn().get_library_instance('SeleniumLibrary')

    # Click Login Button
    sl.click_button(AR.idbtnLoginLogin)
    BuiltIn().sleep(3)

@keyword
def HRM_page_should_be_open():
    # Create instance of SeleniumLibrary
    sl = BuiltIn().get_library_instance('SeleniumLibrary')

    # Verify if the page is launched with correct title
    sl.title_should_be('OrangeHRM')





