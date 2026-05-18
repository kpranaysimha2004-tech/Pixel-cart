Feature: Product Category Filtering

Scenario: Verify phones category displays phone products
Given user is on Demoblaze homepage
When user clicks on Phones category
Then only phone products should be displayed

Scenario: Verify laptops category displays laptop products
Given user is on Demoblaze homepage
When user clicks on Laptops category
Then only laptop products should be displayed

Scenario: Verify monitors category displays monitor products
Given user is on Demoblaze homepage
When user clicks on Monitors category
Then only monitor products should be displayed