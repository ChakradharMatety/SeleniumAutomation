Feature:    OrangeHRM Logo DataDriven

  Background: Common Steps
        Given launch chrome browser
        When open orange hrm homepage
        Then Verify that the logo present on page


  Scenario Outline: Login to OrangeHRM with valid parameters
#    Given launch chrome browser
#    When open orange hrm homepage
#    Then Verify that the logo present on page
    When Enter the username "<username>" and password "<password>"
    Then Verify text present on Dashboard page after login

    Examples:
      | username | password |
      | admin    | admin123 |
      | admin123 | admin    |
      | admin    | adminxyz |