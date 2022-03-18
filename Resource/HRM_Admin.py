from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
import CommonFunctions as CF
import AccessorRepository as AR

@keyword
def Go_to_Admin_Tab():
    # Create instance of SeleniumLibrary
    sl = BuiltIn().get_library_instance('SeleniumLibrary')

    # Select Admin tab
    sl.click_element(AR.xPathTabAdmin)

    # Verify if System users page is displayed
    sl.element_text_should_be(AR.xPathlblAdminSystemUsers, 'System Users')

@keyword
def Search_for_Username():
    uUsername = BuiltIn().get_variable_value('${User}')

    # Create instance of SeleniumLibrary
    sl = BuiltIn().get_library_instance('SeleniumLibrary')

    # Enter username to search
    sl.input_text(AR.idtxtAdminSearchUsername, uUsername)
    BuiltIn().sleep(2)

    # Click Search
    sl.click_button(AR.idbtnAdminSearch)
    BuiltIn().sleep(2)

@keyword
def Select_search_results():
    uUsername = BuiltIn().get_variable_value('${User}')

    # Create instance of SeleniumLibrary
    sl = BuiltIn().get_library_instance('SeleniumLibrary')

    # Select first record from search results
    sl.click_element(AR.xPathAdminSearchResult)
    BuiltIn().sleep(3)

    # Verify if Edit User page has this user selected
    sl.element_attribute_value_should_be(AR.xPathAdminEditUserUsername, 'value', uUsername)

@keyword
def Cancel_Edit():
    # Create instance of SeleniumLibrary
    sl = BuiltIn().get_library_instance('SeleniumLibrary')

    # Select Cancel options to exit without saving any changes
    sl.click_button(AR.idbtnAdminEditUserCancel)
    BuiltIn().sleep(2)

    # Verify if System users page is displayed
    sl.element_text_should_be(AR.xPathlblAdminSystemUsers, 'System Users')








