Feature: Product navigation functionality

  Scenario: Open product details page
    Given user is on the Demoblaze home page
    When user clicks on a product image
    Then product details page should be displayed

  Scenario: Return to home page from product page
    Given user is on product details page
    When user clicks on Home button
    Then user should navigate back to home page