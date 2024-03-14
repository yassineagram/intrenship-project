Feature: Test Scenarios for Reelly

Scenario:  Verify each product contains the Out of Stocks tag.

    Given I navigate to: https://soft.reelly.io/sign-in
    When I input username: ''
    When I input password: ''
    When I click button: Continue
    When I click "off plan”button at the left side menu.
    Then I see URL contains text: off plan
    When I click on button: "filter" and filter by sale status of “Out of Stocks”.
    Then I click button "Apply filter"
    Then I Verify each product contains the Out of Stocks tag.

