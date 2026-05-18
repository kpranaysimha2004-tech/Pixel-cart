Feature: About us functionality

  Scenario: Open About us video popup
    Given user is on the Demoblaze home page
    When user clicks on About us link
    Then About us popup should be displayed

  Scenario: Close About us popup
    Given user opens About us popup
    When user clicks on Close button
    Then popup should be closed successfully