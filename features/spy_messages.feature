Feature: encode or decode a secret message
As a secret spy
I should be able to encode and decode messages
So that I can chat with my spy friends like a pro.

Scenario: I can successfully encode a secret message
    Given I open the url "https://www.hanginghyena.com/solvers_a/caesar-cipher-decoder"
    When I select the option with the value "1" for element "#shift-amount"
    When I clear the inputfield "#letters"
    When I add "Cutler" to the inputfield "#letters"
    When I click on the button "#submit"
    When I pause for 100ms
    Then I expect that element "#decoded_message" contains the text "Dvumfs"

Scenario: I can successfully decode a secret message
    Given I open the url "https://www.hanginghyena.com/solvers_a/caesar-cipher-decoder"
    When I select the option with the value "D" for element "#decoder-setting"
    When I select the option with the value "1" for element "#shift-amount"
    When I clear the inputfield "#letters"
    When I add "Dvumfs" to the inputfield "#letters"
    When I click on the button "#submit"
    When I pause for 100ms
    Then I expect that element "#decoded_message" contains the text "Cutler"