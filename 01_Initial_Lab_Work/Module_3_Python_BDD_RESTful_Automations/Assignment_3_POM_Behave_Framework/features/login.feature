Feature: SauceDemo Login using Page Object Model

  Scenario Outline: Login with different valid users
    Given I open the SauceDemo login page
    When I login using username "<username>" and password "<password>"
    Then I should see the Products page

    Examples:
      | username              | password     |
      | standard_user         | secret_sauce |
      | problem_user          | secret_sauce |