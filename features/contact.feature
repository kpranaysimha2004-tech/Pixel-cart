Feature: Contact Functionality

Scenario: Verify contact form submission
Given user is on Demoblaze homepage
When user clicks on Contact link
And user enters valid contact details
And clicks Send message
Then success alert should be displayed