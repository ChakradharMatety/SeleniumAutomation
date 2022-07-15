Feature:    MultipleTimes

  Scenario Outline:
    Given launch chrome browser
    When open orange hrm homepage
    Then Verify that the logo present on page
    Then close browser
    Examples:
    |iterations|
    |  1       |
    |  2       |