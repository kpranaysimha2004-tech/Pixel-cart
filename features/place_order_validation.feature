Feature: Place order form validation

  Scenario: Try placing order with empty details
    Given user is on the cart page
    When user clicks on Place Order button
    And user leaves all fields empty
    And user clicks on Purchase button
    Then validation message should be displayed

  Scenario: Enter valid order details
    Given user is on the place order popup
    When user enters valid name
    And user enters valid country
    And user enters valid city
    And user enters valid card details
    And user enters valid month and year
    And user clicks on Purchase button
    Then order should be placed successfully