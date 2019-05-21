from behave import *
from splinter import Browser
from hamcrest import *
from bs4 import BeautifulSoup
import logging
import time

#given
@given(u'I am currently on the homepage of MyAnimeList.net')
def step_impl(context):
    context.browser.visit(context.basicurl)

@given(u'I am logged into my account')
def step_impl(context):
    try:
        context.execute_steps(u''' 
        Given I pressed the Login button
        When I filled out user_name field with %s
        And I filled out password field with %s
        And I pressed the login button 
    '''%(context.table[0]['username'], context.table[0]['password']))
    except:
        pass

@given(u'I pressed Ok on the pop-up that appears')
def step_impl(context):
    try:
        elem = context.browser.find_by_text('OK')
        elem.click() #this will click the element
        time.sleep(1)
    except:
        time.sleep(1) 

@given(u'I pressed the Login button')
def step_impl(context):
    button = context.browser.find_by_id('malLogin')
    button.click()

#when
@when(u'I filled out {field} field with {fieldinput}')
def step_impl(context, field, fieldinput):
    context.browser.fill(field, fieldinput)

@when(u'I select {fieldinput} from {field} field')
def step_impl(context, field, fieldinput):
    context.browser.select(field, fieldinput)

@when(u'I pressed the login button')
def step_impl(context):
    button = context.browser.find_by_name('sublogin')
    button.click()

@when(u'I press the Update button')
def step_impl(context):
    button = context.browser.find_by_name('myinfo_submit')
    button.click()

@when(u'I search for {anime}')
def step_impl(context, anime):
    search_bar = context.browser.find_by_id('topSearchText')
    search_bar.click() #de balk aanklikken voordat ik het vul
    context.browser.fill('keyword', anime)
    context.browser.find_by_id('topSearchButon').click()

@when(u'I select the {anime} from the results')
def step_impl(context, anime):
    anime_list = context.browser.find_by_css('article')
    anime_list.find_by_text(anime).click()

@when(u'I press the (quick) Add button at {anime}')
def step_impl(context, anime):
    anime_list = context.browser.find_by_css('article')
    anime = anime_list.find_by_text(anime)
    anime.find_by_xpath('//../../../a[3]').click()

@when(u'I confirm the quick add')
def step_impl(context):
    add_anime = context.browser.find_by_css('iframe')
    soup = BeautifulSoup(add_anime.last.outer_html)
    anime_url = soup.find('iframe')['src']
    context.browser.visit(anime_url)
    time.sleep(1)
    context.browser.find_by_xpath('//*[@id="dialog"]/tbody/tr/td/div[3]/input').click()
    context.browser.find_by_text('Go to Anime Page').click()

@when(u'I press the Add to My List')
def step_impl(context):
    time.sleep(0.5)
    context.browser.find_by_id('showAddtolistAnime').click()

@when(u'I press the Add button')
def step_impl(context):
    time.sleep(0.5)
    context.browser.find_by_name('myinfo_submit').click()

@when(u'I go to my MAL')
def step_impl(context):
    menu = context.browser.find_by_id('header-menu')
    menu.find_by_css('a').click()
    menu.find_by_text('Anime List').click()

@when(u'I select the {anime} from my MAL')
def step_impl(context, anime):
    context.browser.find_by_text('All Anime').click()
    anime_list = context.browser.find_by_css('table')
    anime_list.find_by_text(anime).click()

#then
@then(u'I logged into my MAL account with {username}')
def step_impl(context, username):
    assert_that(str(context.browser.html), contains_string(username))
    assert_that(str(context.browser.html), contains_string('My Panel'))

@then(u'I am not logged into my MAL account')
def step_impl(context):
    assert_that(str(context.browser.html), contains_string('Your username or password is incorrect.'))

@then(u'{anime} is added to my list')
def step_impl(context, anime):
    context.execute_steps(u'''
    When I go to my MAL
    ''')
    assert_that(str(context.browser.html), contains_string(anime))

@then(u'the {anime} is not found on MAL')
def step_impl(context, anime):
    anime_list = context.browser.find_by_css('article')
    #assert_that(str(anime_list), contains_string(anime))

@then(u'the {anime} is updated on my list, the {score}, {status} and {episode} are updated')
def step_impl(context, anime, score, status, episode):
    context.execute_steps(u'''
    When I go to my MAL
    ''')
    context.browser.find_by_text(status).click()
    assert_that(context.browser.html, contains_string(anime)) #assert that anime is listed under correct status
    anime_list = context.browser.find_by_css('tbody')
    first = True
    for item in anime_list:
        if first == False:
            cellen = item.text.split('\n')
            if cellen[0].endswith(anime):
                assert_that(cellen[2].split(' ')[0], equal_to(score))
                assert_that(cellen[3].split(' ')[0], equal_to(episode))
        first = False