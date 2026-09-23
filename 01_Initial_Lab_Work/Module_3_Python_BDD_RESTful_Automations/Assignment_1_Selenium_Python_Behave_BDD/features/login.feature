Feature: SauceDemo Login

  Scenario: Successful login with valid credentials
    Given I open the SauceDemo website
    When I enter valid username and password
    And I click the login button
    Then I should see the products page