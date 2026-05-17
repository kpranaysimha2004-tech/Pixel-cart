Feature: Product category search functionality

  Scenario: View phone products
    Given user opens the Demoblaze website
    When user clicks on Phones category
    Then all phone products should be displayed

  Scenario: View laptop products
    Given user opens the Demoblaze website
    When user clicks on Laptops category
    Then all laptop products should be displayed

  Scenario: View monitor products
    Given user opens the Demoblaze website
    When user clicks on Monitors category
    Then all monitor products should be displayed

  Scenario: Open a product from category
    Given user opens the Demoblaze website
    When user clicks on Phones category
    And user selects a phone product
    Then product details page should open