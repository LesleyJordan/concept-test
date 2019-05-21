@wip
Feature:
    To keep track of the animes that I have watched
    As a user
    I want to add an anime to my MAL

    Background: 
        Given I am currently on the homepage of MyAnimeList.net
        And I pressed Ok on the pop-up that appears
        And I am logged into my account
            | username     | password                 |
            | LesleyTester | Testwachtwoordlesley!123 |

    @happyflow
    Scenario Outline:
        When I search for <anime>
        And I select the <anime> from the results
        And I press the Add to My List
        And I press the Add button    
        Then <anime> is added to my list

    Examples: search anime
        | anime                |
        | Death Note           |
        | Elfen Lied           |

    @quickadd
    Scenario Outline:
        When I search for <anime>
        And I press the (quick) Add button at <anime>
        And I confirm the quick add   
        Then <anime> is added to my list

    Examples: quickadd anime
        | anime                |
        | Fullmetal Alchemist  |
        
    @nosearchresult
    Scenario Outline:
        When I search for <anime> 
        Then the <anime> is not found on MAL
        
    Examples: nono anime
        | anime                |
        | Babi Pangang         |