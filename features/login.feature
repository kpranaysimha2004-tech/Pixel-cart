Feature: Login functionality

  Scenario: Successful login with valid credentials
    Given user opens the Demoblaze website
    When user clicks on login button
    And user enters valid username and password
    And user clicks on login submit button
    Then user should login successfully

  Scenario: Login with invalid credentials
    Given user opens the Demoblaze website
    When user clicks on login button
    And user enters invalid username and password
    And user clicks on login submit button
    Then user should see login error message

  Scenario: Login with empty username and password
    Given user opens the Demoblaze website
    When user clicks on login button
    And user leaves username and password empty
    And user clicks on login submit button
    Then user should see validation message