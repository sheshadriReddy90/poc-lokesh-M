Feature: Search functionality

  @search
  Scenario: Search for a valid product
    Given I got navigated to Home page
    When I enter valid product say "Apple iphone 14 pro max 256gb gold" into the Search box field
    And I click on Search button
    Then Valid product should get displayed in Search results

  @search
  Scenario: Search for an invalid product
    Given I got navigated to Home page
    When I enter invalid product say "424424sssssssss" into the Search box field
    And I click on Search button
    Then Proper message should be displayed in Search results

  @search
  Scenario: Search without entering any product
    Given I got navigated to Home page
    When I dont enter anything into Search box field
    And I click on Search button
    Then Proper message should be displayed in Search results on search page
