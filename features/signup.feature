Feature: User Registration
  Scenario Outline: Register a new user account
    Given the user is on the Demoblaze homepage
    When the user opens the Sign Up modal
    And the user enters a unique "<username>" and "<password>"
    And the user submits the registration form
    Then a success alert should appear