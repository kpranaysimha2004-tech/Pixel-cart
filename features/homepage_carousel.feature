Feature: Homepage Image Carousel
  Scenario: Navigate through homepage promotions
    Given the user is on the Demoblaze homepage
    When the user clicks the carousel next or previous arrow
    Then the next promotional banner should slide into view