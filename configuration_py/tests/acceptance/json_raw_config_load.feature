@wip
Feature: Loading config from raw JSON file
  In order to use JSON configs in my application,
  As developer
  I want to load config for current environment
  from raw JSON files

  Scenario: Load raw config by using default config name
    Given we have "application.json" config in "config" folder with the content:
      '''
      {
      "development":{
          "debug": true
        }
      }
      '''
      And environment set to "development"
    When we load default config from folder "config"
    Then "development" configuration loaded
      And it should looks like dictionary

  Scenario: Load raw config by using custom config name
    Given we have "database.json" config in "config" folder with the content:
      '''
      {
        "development":{
          "debug": true
        }
      }
      '''
      And environment set to "development"
    When we load "database" config from folder "config"
    Then "development" configuration loaded

  Scenario: Load raw config for the different environments
    Given we have "application.json" config in "config" folder with the content:
      '''
      {
        "development":{
          "debug": true
        },
        "test":{
          "debug": true
        }
      }
      '''
    When environment set to "development"
     And we load "application" config from folder "config"
    Then "development" configuration loaded
    When environment set to "test"
      And we load "application" config from folder "config"
    Then "test" configuration loaded

  Scenario: Load raw config for the different environments passed by code
    Given we have "application.json" config in "config" folder with the content:
      '''
      {
        "development":{
          "debug": true
        },
        "test":{
          "debug": true
        }
      }
      '''
    When we load "application" config from folder "config" with "development" environment
    Then "development" configuration loaded
    When we load "application" config from folder "config" with "test" environment
    Then "test" configuration loaded