# Created by yassine at 2/5/24
Feature: Feature: Target.com


  Scenario: User can open Target Circle page
      Given Open Target main page
      When Open Target Circle
      Then Target Circle are shown
      Then verify there are 5 benefit boxes