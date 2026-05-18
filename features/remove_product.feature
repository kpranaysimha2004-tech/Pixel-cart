Feature: Remove product from cart

  Scenario: Remove added product from cart
    Given user is on the Demoblaze home page
    When user selects a product
    And user adds the product to cart
    And user navigates to cart page
    And user clicks on Delete button
    Then product should be removed from cart