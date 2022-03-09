# Created by juliusc at 3/3/22
Feature: Upload Photo
  # Enter feature description here

  Scenario: Verify photo is uploaded on feed
    Given User is logged in given a photo
    When User uploads photo
    Then Photo is successfully uploaded


