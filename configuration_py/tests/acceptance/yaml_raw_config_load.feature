Feature: Loading config from raw YAML file
  In order to use YAML configs in my application,
  As developer
  I want to load config for current environment
  from raw YAML files

  Scenario: load raw config by using default config name
    Given we have "application.yaml" config in "config" folder with the content:
      """
      development:
        debug: True
      """
      And environment set to "development"
    When we load default config from folder "config"
    Then it should looks like dictionary
      And "development" configuration loaded

  Scenario: load raw config by using custom config name
    Given we have "database.yaml" config in "config" folder with the content:
      """
      development:
        host: local
      """
      And environment set to "development"
    When we load "database" config from folder "config"
    Then "development" configuration loaded

  Scenario: load raw config by using config name with the short extension
    Given we have "database.yml" config in "config" folder with the content:
      """
      development:
        host: local
      """
    And environment set to "development"
    When we load "database" config from folder "config"
    Then "development" configuration loaded

  Scenario: load raw config from the custom config folder
    Given we have "application.yaml" config in "custom" folder with the content:
      """
      development:
        debug: True
      """
      And environment set to "development"
    When we load default config from folder "custom"
    Then "development" configuration loaded

  Scenario: load raw config for the different environments
    Given we have "application.yaml" config in "config" folder with the content:
      """
      development:
        debug: True
      test:
        debug: True
      """
    When environment set to "development"
     And we load "application" config from folder "config"
    Then "development" configuration loaded
    When environment set to "test"
      And we load "application" config from folder "config"
    Then "test" configuration loaded

  Scenario: load raw config for the different environments passed by code
    Given we have "application.yaml" config in "config" folder with the content:
      """
      development:
        debug: True
      test:
        debug: True
      """
    When we load "application" config from folder "config" with "development" environment
    Then "development" configuration loaded
    When we load "application" config from folder "config" with "test" environment
    Then "test" configuration loaded

  Scenario: load raw config by the full file name
    Given we have "application.yaml" config in "config" folder with the content:
    """
    development:
      debug: True
    test:
      debug: True
    """
    When we load "application.yaml" config from folder "config" with "development" environment
    Then "development" configuration loaded