Feature: Empty cart validation

  Scenario: Verify cart is empty initially
    Given user is on the Demoblaze home page
    When user clicks on Cart option
    Then cart page should display no products

  Scenario: Verify cart becomes empty after deleting products
    Given user has products in cart
    When user removes all products from cart
    Then cart should become empty