Feature: Cart Total Calculation
  Scenario: Validate the total price of multiple items
    Given the user has added multiple products to the cart
    When the user views the Cart page
    Then the total price should equal the sum of the individual product prices