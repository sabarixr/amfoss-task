import os

from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
from datetime import date
from datetime import datetime
import csv


def get_livescore():
    global team_one, match_score1, match_over1, match_over2, match_score2, team_two, ti_me, match_summary
    site = 'https://www.espncricinfo.com/live-cricket-score'

    op = urlopen(site)
    rd = op.read()
    op.close()

    sp_page = soup(rd, 'html.parser')

    live_match = sp_page.find('div',
                              class_='ds-flex ds-flex-col ds-mt-2 ds-mb-2')

    details_match = live_match.find_all('div',
                                        class_='ci-team-score ds-flex ds-justify-between ds-items-center ds-text-typo ds-my-1')

    p_summery = sp_page.find('p', class_='ds-text-tight-s ds-font-regular ds-truncate ds-text-typo')

    exception_match = live_match.find_all('div',
                                          class_='ci-team-score ds-flex ds-justify-between ds-items-center ds-text-typo ds-opacity-50-my-1')

    # ----------------------------------------------------------------------------------------------------------------------
    if details_match:
        if details_match[0].find('p'):
            team_one = details_match[0].find('p').text if details_match[0].find('p') else ""

        if details_match[0].find('strong'):
            match_score1 = details_match[0].find('strong').text
        else:
            match_score1 = ""

        if details_match[0].find('span'):
            match_over1 = details_match[0].find('span').text
        else:
            match_over1 = ""
        # ----------------------------------------------------------------------------------------------------------------
        if details_match[1].find('p'):
            team_two = details_match[1].find('p').text
        elif exception_match:
            team_two = exception_match[0].find('p').text
        else:
            team_two = ""

        if details_match[1].find('strong'):
            match_score2 = details_match[1].find('strong').text
        elif exception_match:
            match_score2 = exception_match[0].find('strong').text
        else:
            match_score2 = ""

        if details_match[1].find('span'):
            match_over2 = details_match[1].find('span').text
        elif exception_match:
            match_over2 = details_match[1].find('span').text
        else:
            match_over2 = ""
        # --------------------------------------------------------------------------------------------------
        match_summary = p_summery.find('span').text
        ti_me = date.today()

        data = {
            "team_one": team_one,
            "match_score1": match_score1,
            "match_over1": match_over1,
            "team_two": team_two,
            "match_score2": match_score2,
            "match_over2": match_over2,
            "match_summary": match_summary,
            "time": ti_me

        }

        return data
    else:
        return {"error": "no live matches available! try again later"}


# solution = get_livescore()
# print(solution)

def livescore_file():
    da_ti = datetime.now()
    data = get_livescore()

    file_exists = os.path.exists('livescore.csv')

    with open('livescore.csv', mode='a', newline='') as csvfile:
        fieldnames = ["team1", "team2", "score1", "over1", "score2", "over2", "summary", "time"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # If the file doesn't exist, write the header row
        if not file_exists:
            writer.writeheader()

        writer.writerow({
            "team1": data["team_one"],
            "team2": data["team_two"],
            "score1": data["match_score1"],
            "over1": data["match_over1"],
            "score2": data["match_score2"],
            "over2": data["match_over2"],
            "summary": data["match_summary"],
            "time": da_ti
        })


def team_info():
    site2 = 'https://www.espncricinfo.com/cricketers/team/india-6'

    op2 = urlopen(site2)
    rd2 = op2.read()
    op2.close()

    sp_page2 = soup(rd2, 'html.parser')
    team_info_ind = sp_page2.find_all('span',
                                      class_='ds-text-compact-l ds-font-medium ds-text-typo hover:ds-text-typo-primary ds-block ds-cursor-pointer')

    with open('team_info.csv', 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)

        for span_tag in team_info_ind:
            text = span_tag.text.strip()
            csv_writer.writerow([text])
