Feature:    OrangeHRM Logo

  Background: Common Steps
        Given launch chrome browser
        When open orange hrm homepage
        Then Verify that the logo present on page


  Scenario: logo present on OrangeHRM home page
#    Given launch chrome browser
#    When open orange hrm homepage
#    Then Verify that the logo present on page
    When Enter the username "admin" and password "admin123"
#    When Enter the username and password
#      |user |pwd|
#      |admin|abc|
    Then Verify text present on Dashboard page after login
    Then close browser


