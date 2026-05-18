Feature: User Logout

  Scenario: Logout successfully
    Given user is logged in to Demoblaze
    When user clicks on "Log out" in navbar
    Then user should see "Log in" option in navbar
    And user should not see "Log out" option