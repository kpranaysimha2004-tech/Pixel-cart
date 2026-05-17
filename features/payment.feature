Feature: Payment functionality

  Scenario: Place an order with valid payment details
    Given user opens the Demoblaze website
    And user adds a product to the cart
    And user opens the cart page
    When user clicks on place order button
    And user enters valid payment details
    And user clicks on purchase button
    Then order should be placed successfully

  Scenario: Place order without entering payment details
    Given user opens the Demoblaze website
    And user adds a product to the cart
    And user opens the cart page
    When user clicks on place order button
    And user clicks on purchase button without entering details
    Then user should see a validation message

  Scenario: Cancel payment from order form
    Given user opens the Demoblaze website
    And user adds a product to the cart
    And user opens the cart page
    When user clicks on place order button
    And user clicks on close button
    Then payment form should be closed