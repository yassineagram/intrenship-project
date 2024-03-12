
Feature: Target.com


  Scenario Outline: User can search for a product on target
    Given Open Target main page
    When Search for <search_word>
    Then Search results for <expected_result> are shown
    Examples:
    |search_word    |expected_result
    |Shoes          |Shoes
    |Gift           |Gift



