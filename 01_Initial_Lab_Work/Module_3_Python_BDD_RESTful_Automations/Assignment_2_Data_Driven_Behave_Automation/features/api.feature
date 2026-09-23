Feature: REST API Data Driven Automation

  Scenario Outline: Verify user details using different user IDs
    Given I send a GET request for user ID "<user_id>"
    When the API response is received
    Then the response status code should be 200
    And the response should contain user ID "<user_id>"

    Examples:
      | user_id |
      | 1       |
      | 2       |
      | 3       |