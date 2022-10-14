# Website Data
website_name = 'website.com'  # Your Website URL
wordpress_token = 'xxxx xxxx xxxx xxxx xxxx xxxx'  # WordPress Authorize Token PassWord, it will have under user profile
wordpress_username = 'username'  # WordPress Admin Username
author = '1'
Job_status = 'draft'  # or You can keep 'publish'
job_apply_url = 'Indeed'  #

# Search Data
country = 'us'  # US is American Extension
city = 'Connecticut'
job_search = 'Insurance'  # Input Job Category for Indeed Search
location_radius = '100'  # 0, 5, 10, 15, 25, 50, 100 Kilometers, this option is not for US
job_update = '14'  # 1 = 24 Hours, 3 = 3 Days, 7 = 7 Days, 14 = 14 Days
jobs = 10  # How many jobs you want to publish from Indeed
exclude_jobs = 5  # How many jobs do you want to exclude from the first list of Indeed

# Schema Data For Google
post_code = '000000'  # US Postcode is 6 digits, so here is 6 Zero
currency = 'USD'  # INR is India Currency Code Letter symbol
Salary_minimum_amount = '1500'  # Minimum salary for every post, this is for Schema
Salary_maximum_amount = '5000'  # Maximum salary for every post, this is for Schema
job_category_id = '134'  # WordPress Category ID number
year = '2022'  # Current Year
expire_time = 2  # Months

from bs4 import BeautifulSoup as bs
from random import choice
from datetime import date
from datetime import datetime
import base64
from time import sleep
from dateutil.relativedelta import relativedelta
import cloudscraper
import requests
scraper = cloudscraper.create_scraper()

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome()
action = ActionChains(driver)


if country.upper() == 'US':
    # Page Condition
    job_search = job_search.replace(' ', '%20')
    page = int(jobs // 15) * 10
    page_i = 0
    page_list = []
    while page_i < page + 1:
        url = f'https://www.indeed.com/jobs?q={job_search}&l={city}&fromage={job_update}&start={str(page_i)}&vjk'
        page_list.append(url)
        page_i = page_i + 10

    # All Job Url Scrapping
    url_list = []
    for page_url in page_list:
        sleep(5)
        # Scrapping
        driver.get(page_url)
        html = driver.page_source
        soup = bs(html, 'html.parser')
        job = soup.find_all('a', {"class": "jcs-JobTitle"})
        for job_data in job:
            single_job = "https://www.indeed.com/viewjob?jk=" + job_data.get('data-jk')
            url_list.append(single_job)
else:
    # Page Condition
    job_search = job_search.replace(' ', '%20')
    page = int(jobs // 15) * 10
    page_i = 0
    page_list = []
    while page_i < page + 1:
        url = f'https://{country}.indeed.com/jobs?q={job_search}&l={city}&radius={location_radius}&fromage={job_update}&forceLocation=1&start={str(page_i)}&vjk'
        page_list.append(url)
        page_i = page_i + 10

    # All Job Url Scrapping
    url_list = []
    for page_url in page_list:
        sleep(5)
        # Scrapping
        driver.get(page_url)
        html = driver.page_source
        soup = bs(html, 'html.parser')
        job = soup.find_all('a', {"class": "jcs-JobTitle"})
        print(job)
        for job_data in job:
            single_job = "https://" + country + ".indeed.com/viewjob?jk=" + job_data.get('data-jk')
            url_list.append(single_job)

inputcount = exclude_jobs + 1
url_dicts = {}
input_all_list = []

inputcount = exclude_jobs + 1
url_dicts = {}
input_all_list = []
for ur_l in url_list[exclude_jobs:jobs]:
  url_dicts[str(inputcount)] = ur_l
  print('number '+str(inputcount) + '. ----->>>>> URL: '+ ur_l)
  input_all_list.append(str(inputcount))
  inputcount += 1

# Job Publishing Command
input_jobs = input('\nInput numbers, that Jobs do you want to publish. Each number separate with ( , ) comma, and space or serial isn\'t matter.\nOr Input 00 for posting all Jobs>>\nInput Here : ')

if input_jobs == '00':
  jobs_input = input_all_list
else:
  jobs_input = input_jobs.replace(' ','').split(sep=',')

print('>>')
print('>>')
print('>>')

# Start scrapping job body for Job posting and --- Job Posting Loop Start
for jobposting in jobs_input:
    url = url_dicts[jobposting]

    driver.get(url)
    html = driver.page_source
    job_soup = bs(html, 'html.parser')

    job_position_raw = job_soup.find('h1').text.strip().split(' ')
    if len(job_position_raw) > 2:
        job_position_raw = job_position_raw[0:2]
        job_position = ' '.join(job_position_raw)
    else:
        job_position = ' '.join(job_position_raw)

    copmpany_name_raw = job_soup.find('div', {'class': 'jobsearch-CompanyInfoContainer'}).text.replace('reviews','').replace('0','').replace('1', '').replace('2', '').replace('3', '').replace('4', '').replace('5', '').replace('6', '').replace('7','').replace('8', '').replace('9', '').replace(',', '').title().split(sep=' ')
    if len(copmpany_name_raw) > 2:
        copmpany_name_raw = copmpany_name_raw[0:2]
        copmpany_name = ' '.join(copmpany_name_raw)
    else:
        copmpany_name = copmpany_name_raw
        copmpany_name = ' '.join(copmpany_name_raw)

    if 'Confidential' in copmpany_name:
        copmpany_name = 'A Reputed Company'
    else:
        copmpany_name = copmpany_name

    try:
        job_location = job_soup.find('div', {'class': 'jobsearch-JobInfoHeader-subtitle'}).find_all('div')[1].text.strip()
    except:
        job_location = city

    if job_apply_url.upper() == 'INDEED':
        try:
            apply_url = job_soup.find('div', {'id': 'applyButtonLinkContainer'}).find('a').get('href')
        except:
            apply_url = url
    else:
        apply_url = job_apply_url

    try:
        job_type = job_soup.find('div', {'class': 'jobsearch-JobDescriptionSection-sectionItem'}).find('div')[1].text.strip()
    except:
        job_type = 'Full-Time'

    # Indeed list
    indeed_des = job_soup.find('div', {"id": "jobDescriptionText"}).find_all('li')
    if len(indeed_des) > 0:
        indeed_lst = []
        for x in indeed_des:
            indeed_lst.append(str(x))
        indeed_lst.sort()
        indeed_list = ' '
        for x_lst in indeed_lst:
            indeed_list += ' ' + x_lst  # Indeed list
    else:
        indeed_list = ''  # Indeed list

    # Job Intro Data
    looking = choice(['looking', 'searching', 'finding', 'seeking'])
    position = choice(['position', 'post', 'designation', 'vacancy', 'employment'])
    reputed = choice(['reputed', 'famous', 'popular', 'giant', 'top', 'best', 'remarkable', 'corporate'])
    company = choice(['company', 'organization', 'agency', 'hiring agency', 'employer'])
    interested = choice(['interested', 'like', 'love', 'want to get'])
    career = choice(['career', 'profession', 'corporate career', 'corporate life', 'job profession'])
    Recently = choice(['Recently', 'At present', 'Currently'])
    published = choice(['published', 'revealed', 'expressed', 'disclosed', 'circulated', 'publicized'])
    circular = choice(['circular', 'notice', 'news', 'advertisement', 'notification'])
    eligible = choice(['eligible', 'appropriate', 'perfect', 'best', 'suitable', 'top', 'capable', 'skilled', 'efficient','dedicated', 'committed'])
    candidate = choice(['candidate', 'applicant', 'worker', 'job candidate', 'manpower', 'staff', 'employee', 'officiary'])
    will_get = choice(['are going to get', 'are getting', 'will get'])
    details = choice(['details', 'in details', 'full information', 'details information'])
    job = choice(['job', 'work', 'employment'])
    follow = choice(['follow', 'read', 'check', 'check out', 'learn more'])
    collected = choice(['collected', 'sourced', 'picked', 'generated'])
    Indeed = choice(['Indeed\'s official', 'hiring Websites', 'employment Websites', 'hiring Agencies'])
    page = choice(['page', 'web page'])
    represented = choice(['represented', 'republished', 'published'])
    only = choice(['only', 'just', ''])
    location = choice(['location', 'place', 'region', 'territory', 'area', 'locus'])
    responsibility = choice(['responsibility', 'duty'])
    everything = choice(['everything', 'all', 'entire info', 'all info', 'all data', 'all information', 'entire information','entire data'])
    mentioned = choice(['mentioned', 'added', 'written', 'discussed'])
    here = choice(['here', 'in this page', 'this page', 'in this post', 'in this website', 'in this circular', 'in this news'])
    data = choice(['data', 'info', 'information', 'details'])
    Warning = choice(['Warning', 'Alert', 'Caution', 'Reminder', 'Notice', 'Note'])
    judge = choice(['judge', 'consider', 'observe', 'analysis', 'check out'])
    yourself = choice(['yourself', 'your responsibility', 'your knowledge', 'your observation', 'your study'])
    cheated = choice(['cheated', 'beguiled', 'deceived', 'swindled'])
    company_and_etc = choice([company + ' ' + details + ', offered salary, ' + position + ', ' + job + ' ' + location + ', ' + responsibility + ', ',
                              'Offered salary, ' + position + ', ' + job + ' ' + location + ', ' + responsibility + ', ' + company + ' ' + details + ', ',
                              company + ' ' + details + ', offered salary, ' + job + ' ' + location + ', ' + responsibility + ', ' + position + ', ',
                              company + ' ' + details + ', offered salary, ' + position + ', ' + responsibility + ', ' + job + ' ' + location + ', ',
                              responsibility + ', offered salary, ' + position + ', ' + job + ' ' + location + ', ' + company + ' ' + details + ', ',
                              responsibility + ', offered salary, ' + job + ' ' + location + ', ' + company + ' ' + details + ', ' + position + ', ',
                              responsibility + ', offered salary, ' + job + ' ' + location + ', ' + position + ', ' + company + ' ' + details + ', ',
                              company + ' ' + details + ', ' + responsibility + ', offered salary, ' + job + ' ' + location + ', ' + position + ', ',
                              position + ', ' + company + ' ' + details + ', ' + responsibility + ', offered salary, ' + job + ' ' + location + ', ',
                              job + ' ' + location + ', ' + position + ', ' + company + ' ' + details + ', ' + responsibility + ', offered salary, ',
                              'Offered salary, ' + job + ' ' + location + ', ' + position + ', ' + company + ' ' + details + ', ' + responsibility + ', ',
                              'Offered salary, ' + company + ' ' + details + ', ' + responsibility + ', ' + job + ' ' + location + ', ' + position + ', ',
                              ])
    # Schema Description
    sentence1 = choice(['Are you ' + looking + ' for ' + job_position + ' ' + position + ' in a ' + reputed + ' ' + company + '? ',
                        'Do you ' + looking + ' for ' + job_position + ' ' + position + ' in a ' + reputed + ' ' + company + '? ',
                        'Do you intersted to build your ' + career + ' as an ' + job_position + ' ' + position + ' in a ' + reputed + ' ' + company + '? '])
    sentence2 = Recently + ', ' + copmpany_name + ' has ' + published + ' a ' + job_position + ' ' + position + ' job ' + circular + '. And they are ' + looking + ' for the ' + eligible + ' ' + candidate + ' for their ' + company + '.'
    sentence3 = ' On this ' + circular + ' page, you ' + will_get + ' ' + details + '. Also, if you ' + interested + ' apply for this ' + job_position + ' ' + position + ' follow this.'
    schemameta = '<p>' + sentence1 + sentence2 + sentence3 + '</p>'

    # Job Intro
    intro_sen1 = choice([Recently + ' ' + copmpany_name + ' has ' + published + ' a job ' + circular + '. They are ' + looking + ' for a ' + eligible + ' ' + job_position + '. ',
                        copmpany_name + ' ' + Recently + ' ' + published + ' a job ' + circular + '. They are ' + looking + ' for a ' + eligible + ' ' + job_position + '. ',
                        ])
    intro_sen2 = choice(['If you ' + interested + ' a ' + job + ' in the ' + job_position + ' ' + position + ' you can ' + follow + ' this ' + job + ' ' + circular + '. ',
                         'You can ' + follow + ' this ' + job + ' ' + circular + ', if you ' + interested + ' a ' + job + ' in the ' + job_position + ' ' + position + '. ',
                          ])
    intro_sen3 = choice(['This ' + circular + ' has been ' + collected + ' from ' + Indeed + ' ' + page + ' of this ' + company + ' profile. ',
                         'From ' + Indeed + ' ' + page + ' of this ' + company + ' profile, this ' + circular + ' has been ' + collected + '. ',
                         'From ' + Indeed + ' ' + page + ', this ' + circular + ' has been ' + collected + '. ',
                         ])
    intro_sen4 = choice(['Here has ' + represented + ' that ' + circular + ' ' + only + ', so you can apply for this ' + job + '. ','So you can apply for this ' + job + '. ',
                         'You can apply for this ' + job + ', cause here has ' + represented + ' that ' + circular + ' ' + only + '. ',
                         'Here has ' + represented + ' that ' + circular + ' ' + only + '. ',
                         ])
    intro_sen5 = choice(['Also, ' + company_and_etc + ' etc ' + everything + ' has been ' + mentioned + ' ' + here + '. ',])
    intro_sen6 = choice([
                        'Since this ' + data + ' has been ' + collected + ' from the official ' + page + ' you can trust this ' + data + '. ',
                        'You can keep trusted in this ' + data + ', cause this ' + data + ' has been ' + collected + ' from the official ' + page + '. ',
                        'You can trust this ' + data + ', cause this ' + data + ' has been ' + collected + ' from the official ' + page + '. ',
                        'So you can keep trusted in this ' + data + '. ',
                        'So you can trust this ' + data + '. ',
                        ])
    intro_sen7 = choice([
                        Warning + ': Before applying for this ' + job + ' you have to ' + judge + ' ' + everything + ' from ' + yourself + '. We have no ' + responsibility + ' if you become ' + cheated + '. ',
                        Warning + ': We have no ' + responsibility + ' if you become ' + cheated + '. So before applying for this ' + job + ' you have to ' + judge + ' ' + everything + ' from ' + yourself + '. ',
                        ])

    intro = '<p>' + intro_sen1 + intro_sen2 + '</p><p>' + intro_sen3 + intro_sen4 + '</p><p>' + intro_sen5 + intro_sen6 + '</p><p class="warning-p">' + intro_sen7 + '</p>'

    # Bsci Job Data
    see = choice(['see', 'check out', 'read', 'look'])
    basic = choice(['basic', 'primary', '', 'main', 'key'])
    interested = choice(['interested', 'like', 'love', 'want to get', 'want to'])
    apply = choice(['apply', 'submit resume'])
    you_will = choice(['you will get', 'are going to get', 'you will see', 'are going to see'])
    decide = choice(['decide', 'make decision', 'take decision'])
    suitable = choice(['suitable', 'worthy', 'perfect', 'best', 'good', 'valuable', 'great'])
    these = choice(['these', 'this'])
    duties = choice(['duties', 'tasks', 'responsibilities', 'duty'])
    take = choice(['take', 'start', 'choose'])
    have = choice(['have', 'must have'])
    instruction = choice(['instruction', 'directions', 'requirement', 'responsibility', 'duty'])
    switching = choice(['switching', 'leaving', 'changing', 'altering'])
    present = choice(['present', 'current', 'running', 'recent'])
    checks = choice(['check', 'check out', 'find out', 'analysis', 'observe'])
    handle = choice(['handle', 'manage'])
    pressure = choice(['pressure', 'work pressure', 'job pressure', 'duty pressure'])

    bd1 = see.capitalize() + ' this ' + basic + ' Job description ' + data + ' if you ' + interested + ' ' + apply + ' for this job. '
    bd2random1 = 'Here ' + you_will + ' the ' + company + ' name, Job ' + position + ', Salary amount, Job ' + location + ', and Job Type ' + data + ' etc. '
    bd2random2 = 'Here ' + you_will + ' the Job ' + position + ', Salary amount, Job ' + location + ', ' + company + ' name, and Job Type ' + data + ' etc. '
    bd2random3 = 'Here ' + you_will + ' the ' + company + ' name, Salary amount, Job ' + location + ', Job ' + position + ', and Job Type ' + data + ' etc. '
    bd2random4 = 'Here ' + you_will + ' the Job ' + position + ', Salary amount, Job ' + location + ', Job Type, and ' + company + ' name ' + data + ' etc. '
    bd2random5 = 'Here ' + you_will + ' the Salary amount, Job ' + location + ', ' + company + ' name, Job ' + position + ', and Job Type ' + data + ' etc. '
    bd2random6 = 'Here ' + you_will + ' the Job ' + location + ', Salary amount, Job ' + position + ', ' + company + ' name, and Job Type ' + data + ' etc. '
    bd2random7 = 'Here ' + you_will + ' the Job Type, Job ' + location + ', ' + company + ' name, Job ' + position + ', and Salary amount ' + data + ' etc. '
    bd2random8 = 'Here ' + you_will + ' the Salary amount, Job ' + position + ', Job ' + location + ', ' + company + ' name, and Job Type ' + data + ' etc. '
    bd2random9 = 'Here ' + you_will + ' the Job ' + position + ', Job ' + location + ', ' + company + ' name, Job Type, and Salary amount ' + data + ' etc. '
    bd2random10 = 'Here ' + you_will + ' the Job ' + position + ', Job ' + location + ', ' + company + ' name, Job Type, and Salary amount, ' + data + ' etc. '
    bd2 = choice([bd2random1, bd2random2, bd2random3, bd2random4, bd2random5, bd2random6, bd2random7, bd2random8, bd2random9,bd2random10])
    bd3 = 'By checking this ' + data + ' you can ' + decide + ' whether this job is ' + suitable + ' for you or not. '

    bdfinalrandom1 = '<p>' + bd1 + bd2 + '</p><p> ' + bd3 + '</p>'
    bdfinalrandom2 = '<p>' + bd1 + '</p><p>' + bd3 + bd2 + '</p>'
    bdfinalrandom3 = '<p>' + bd2 + '</p><p>' + bd1 + bd3 + '</p>'
    bdfinalrandom4 = '<p>' + bd2 + '</p><p>' + bd3 + bd1 + '</p>'

    basic_description = choice([bdfinalrandom1, bdfinalrandom2, bdfinalrandom3, bdfinalrandom4])
    basic_job_details = '<h2><strong>' + job.title() + ' Details:</strong></h2>' + basic_description + '<ul><li>' + company.title() + ' Name: ' + copmpany_name + '</li><li>' + job.title() + ' ' + position.title() + ': ' + job_position + '</li><li>Salary ' + data.title() + ': ' + choice(['Check on', 'See on', 'Check out', 'See','Check']) + ' the apply page</li><li>' + location.title() + ': ' + city + '</li><li>Job-Type: ' + job_type + '</li></ul>'

    # Indeed List
    if len(indeed_list) > 0:
        indeedlist1 = '<p> Be carefully ' + see + ' ' + these + ' job ' + duties + '. Cause if you ' + take + ' this job you ' + have + ' to obey this ' + instruction + '. </p>'
        indeedlist12 = '<p> So be carefully ' + see + ' ' + these + ' job ' + duties + '. Cause if you ' + take + ' this job you ' + have + ' to obey this ' + instruction + '. </p>'
        indeedlist2 = '<p> Before ' + switching + ' your ' + present + ' job ' + checks + ' whether this ' + responsibility + ' is ' + suitable + ' or not for you. If you can ' + take + ' ' + handle + ' this ' + pressure + ' then go ahead. </p>'
        indeedlistfinal1 = indeedlist1 + indeedlist2
        indeedlistfinal2 = indeedlist2 + indeedlist12
        job_indeed = '<h2><strong>' + job.title() + ' ' + responsibility.title() + ':</strong></h2>' + choice([indeedlistfinal1, indeedlistfinal2]) + '<ul>' + indeed_list + '</ul>'
    else:
        job_indeed = ''

    # Necessary Qualifications
    Good = choice(['Good', 'Strong', 'Enough', 'Perfect', 'Best'])
    skill = choice(['skill', 'ability', 'efficiency', 'proficiency', 'knowledge'])
    ability = choice(['ability', 'capability', 'efficiency'])
    person = choice(['person', 'guy', 'worker', 'candidate', 'applicant'])
    management = choice(['management', 'leading', 'leadership'])
    improve = choice(['improve', 'bright', 'shine', 'enhance'])
    reputation = choice(['reputation', 'fame', 'quality'])
    offering = choice(['offering', 'proposing', 'providing', 'referring', 'mentioning'])
    appropriate = choice(['appropriate', 'perfect', 'best', 'suitable', 'high', 'top'])
    chance = choice(['chance', 'challenge', 'scope', 'opportunity', 'benefit'])
    regularly = choice(['regularly', 'frequently', 'often', 'continually'])
    performance = choice(['performance', 'skill', 'dedication', 'work'])

    q1 = choice(['<li>' + Good + ' communication ' + skill + ' in English.</li>',
                 '<li>' + Good + ' ' + skill + ' in English.</li>'
                 ])
    q2 = choice(['<li>' + Good + ' team player.</li>',
                 '<li>Working ' + ability + ' with team.</li>',
                 '<li>Team m' + management + ' ' + skill + '.</li>',
                 '<li>' + Good + ' understanding about teamwork.</li>',
                 ])
    q3 = choice(['<li>Working under pressure.</li>',
                 '<li>' + ability.title() + ' to work under pressure.</li>',
                 '<li>Under pressure working ' + ability + '.</li>',
                 '<li>' + ability.title() + ' to handle working pressure. </li>',
                 ])
    q4 = choice(['<li>Dedicated & Honest ' + person + '.</li>',
                 '<li>Honest & Dedicated ' + person + '.</li>',
                 ])
    q5 = '<li>' + Good + ' ' + management + ' ' + skill + '.</li>'
    q6 = '<li>Maintaining punctuality.</li>'

    # Random Choice Permutation
    qc1 = choice([q1, q2, q3, q4, q5, q6])
    while True:
        qc2 = choice([q1, q2, q3, q4, q5, q6])
        if qc2 != qc1:
            break
    while True:
        qc3 = choice([q1, q2, q3, q4, q5, q6])
        if qc3 != qc1 and qc3 != qc2:
            break
    while True:
        qc4 = choice([q1, q2, q3, q4, q5, q6])
        if qc4 != qc1 and qc4 != qc2 and qc4 != qc3:
            break
    while True:
        qc5 = choice([q1, q2, q3, q4, q5, q6])
        if qc5 != qc1 and qc5 != qc2 and qc5 != qc3 and qc5 != qc4:
            break
    while True:
        qc6 = choice([q1, q2, q3, q4, q5, q6])
        if qc6 != qc1 and qc6 != qc2 and qc6 != qc3 and qc6 != qc4 and qc6 != qc5:
            break

    q_merge = qc1 + ' ' + qc2 + ' ' + qc3 + ' ' + qc4 + ' ' + qc5 + ' ' + qc6
    q_description = '<p> You can ' + checks + ' also this. Not only for this job, if you ' + interested + ' join any ' + company + ' you ' + have + ' to ' + follow + ' this ' + instruction + '. Cause these ' + skill + ' will ' + improve + ' your corporate ' + career + '. </p>'
    Qualifications = '<h2><strong>Necessary Qualifications:</strong></h2>' + q_description + '<ul>' + q_merge + '</ul>'

    # Company Information
    companyp1 = '<p> ' + copmpany_name + ' is a giant ' + company + ' in ' + city + '. They are providing their service in ' + city + ' with a proper ' + reputation + '. They are always ready to hire the ' + eligible + ' ' + candidate + ' for their team. </p> '
    companyp2 = '<p> And they are also ' + offering + ' an ' + appropriate + ' salary according to ' + performance + '. So you can take a ' + chance + ' to work with them. Also, ' + follow + ' their career page to ' + regularly + ' get job updates. </p>'

    about_company = '<h2><strong>About Company:</strong></h2>' + companyp1 + companyp2

    # Apply Button
    job_apply_button = '<div class="jobapply_div"><a class="jobapply_a" href="' + apply_url + '">Apply Now</a></div>'

    # Schema data for SEO
    start_date = str(date.today())
    end_date = str(datetime.today() + relativedelta(months=expire_time)).split(' ')[0]

    schema = r'<script type="application/ld+json">{"@context" :"https://schema.org/","@type" : "JobPosting","title" : "' + job_position + ' job circular by ' + copmpany_name + '","description" : "' + schemameta.replace('\n','') + '","datePosted" : "' + start_date + '","validThrough" : "' + end_date + '","employmentType" : "Full-Time","hiringOrganization" : {"@type" : "Organization","name" : "' + copmpany_name + '"},"jobLocation": {"@type": "Place","address": {"@type": "PostalAddress","streetAddress": "' + copmpany_name + '","addressLocality": "' + city + '","addressRegion": "' + location + '","postalCode": "' + post_code + '","addressCountry":"' + country + '"}},"baseSalary": {"@type":"MonetaryAmount","currency": "' + currency + '","value": {"@type": "QuantitativeValue","minValue": ' + Salary_minimum_amount + ',"maxValue": ' + Salary_maximum_amount + ',"unitText":"Month"}}}</script>'

    post_body = '<div class="job-body">' + intro + basic_job_details + job_indeed + Qualifications + about_company + job_apply_button + '</div>' + schema

    user = wordpress_username
    website_url = 'https://' + website_name
    wp_title = job_position + ' job in ' + city
    content = post_body
    slug_r = job_position + ' job in ' + copmpany_name
    slug = slug_r.replace(':', ' ').replace('/', ' ').replace('|', ' ').replace('(', ' ').replace(')', ' ').replace('  ', ' ').replace(' ', '-').replace('--', '-')
    pythonapp = wordpress_token

    json_url = website_url + '/wp-json/wp/v2'  # the url of the wp access location
    token = base64.standard_b64encode((user + ':' + pythonapp).encode('utf-8'))  # we have to encode the usr and pw
    headers = {'Authorization': 'Basic ' + token.decode('utf-8')}

    post = {'title': wp_title,
            'slug': slug,
            'status': Job_status,
            "content": content,
            "categories": job_category_id,
            "author": author,
            }

    r = scraper.post(json_url + '/posts', headers=headers, json=post)
    if r.status_code == 201:
        print('number ' + jobposting + '. : ' + wp_title + ' : https://' + website_name + '/' + slug + ' Has Been Posted')
    else:
        print('number ' + jobposting + '. : ' + wp_title + ' : https://' + website_name + '/' + slug + ' Not Posted -- Probably Hosting error')
        print(r.status_code, ' Error')