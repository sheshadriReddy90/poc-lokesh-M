Feature: Register Account functionality


  @register1
  Scenario: Register with mandatory fields
    Given I navigate to Register Page
    When I enter below details into mandatory fields
         |name  |number    |password   |
         |ramesh|6303169446|Loki@12345 |
         |suresh|6303269446|Loki@12343 |
    And I click on Continue button
    Then Account should get created


  @register
  Scenario: Register without providing any details
    Given I navigate to Register Page
    When I dont enter anything into the fields
    And I click on Continue button
    Then Error warning message should be displayed
