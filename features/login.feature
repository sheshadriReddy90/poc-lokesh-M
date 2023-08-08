 Feature: Login Functionality

  @login
  Scenario Outline: Login with valid phone number and password
    Given I navigated to Login page
    When I enter valid phone number as "<number>" and valid password as "<password>" into the fields
    And I click on Login button
    Then I should get logged in
    Examples:
      |number       |password      |
      |8105000676   |Loki@1234     |
#      |6303169446   |srikala120    |
#      |8019713239   |Harish@AMAZON |

  @login
  Scenario Outline: Login with valid phone number and invalid password
    Given I navigated to Login page
    When I enter valid phone number as "<number>" and invalid password as "<password>" into the fields
    And I click on Login button
    Then I should get a proper warning message on password page
    Examples:
      |number       |password      |
      |8105000676   |Loki@125534     |
      |6303169446   |srikala12055    |
      |8019713239   |Harish@AMAZON33 |

  @login
  Scenario: Login with invalid phone number
    Given I navigated to Login page
    When I enter invalid phone number
    Then I should get a proper warning message on phone number page

  @login
  Scenario: Login without entering any phone number
    Given I navigated to Login page
    When I dont enter anything into phone number field
    Then I should get a proper warning message for  failure