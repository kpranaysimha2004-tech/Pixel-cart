Feature: Cart functionality

  Scenario: Add product to cart successfully
    Given user opens the Demoblaze website
    When user selects a product
    And user clicks on Add to cart button
    Then product should be added to cart successfully

  Scenario: Verify added product in cart page
    Given user adds a product to the cart
    When user opens the cart page
    Then added product should be visible in cart

  Scenario: Delete product from cart
    Given user adds a product to the cart
    When user opens the cart page
    And user clicks on delete button
    Then product should be removed from cart

  Scenario: Add multiple products to cart
    Given user opens the Demoblaze website
    When user adds multiple products to cart
    And user opens the cart page
    Then all selected products should be displayed