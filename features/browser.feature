Feature: Profiling

  As a developer
  When using PhantomJS
  I want Aloe to be as fast as Lettuce

  Scenario: Search for speed
    Given I am on the test page
    When I fill in "foo" with "Bar?"
    And I fill in "bar" with "No Bar!"
    And I submit the only form
    Then I should see "Foobar!"
