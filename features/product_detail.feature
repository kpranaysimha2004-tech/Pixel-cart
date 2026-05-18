Feature: Product Detail Page

  Scenario: View product details
    Given user opens the Demoblaze website
    When user clicks on "Samsung galaxy s6"
    Then user should see product name
    And user should see product price
    And user should see product description
    And user should see "Add to cart" button