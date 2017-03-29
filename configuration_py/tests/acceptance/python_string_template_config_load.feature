@wip
Feature: Loading config from yaml in python string template
  In order to use generated YAML configs in my application,
  As developer
  I want to load config for current environment
  from YAML files generated from python string templates

  Scenario: Load templated yaml config by using default config name
    Given we have "application.yaml.tmpl" config in "config" folder with the content:
      """
      development:
        debug: True
      """
    And environment set to "development"
    When we load default config from folder "config"
    Then "development" configuration loaded
    And it should looks like dictionary

  Scenario: Load templated yml config by using default config name
    Given we have "application.yml.tmpl" config in "config" folder with the content:
      """
      development:
        debug: True
      """
    And environment set to "development"
    When we load default config from folder "config"
    Then "development" configuration loaded

  Scenario: Load templated yaml config with passed variable into template
    Given we have "application.yml.tmpl" config in "config" folder with the content:
      """
      development:
        debug: True
      """
    And environment set to "development"
    When we load "application" config from folder "config" with context:
      """
      {'debug': True}
      """
    Then "development" configuration loaded
    And "debug" is set to "True"