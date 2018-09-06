#!/usr/bin/python3

# Author: Marius Avram - Software Developer
# Website: mariusavram.com
# Github: github.com/mariusavram91

# Email: me@mariusavram.com
# Skype: mariusavram91
# Phone: +353 83 179 9605

# To run the script: python3 python_cv.py
# For more details about my experience please go to:
# http://mariusavram.com/projects/ or http://ie.linkedin.com/in/mariusavram91

import unittest
# from developers import marius


class MariusAvram:
    def __init__(self):
        self.about_me = " \
        I am Marius, a Software Developer currently based in\n \
        Berlin. I started my career in 2012 as an Intern after finishing a\n \
        vocational training course in Madrid. In 2013 I started working as\n \
        a developer. The company I was working for moved to Dublin shortly\n \
        after I started and I was asked to move. I was up for taking on a\n \
        challenge, so I moved. After three years working in Dublin, I\n \
        decided to look for another challenge and headed to Berlin. At the\n \
        beginning of 2018 I travelled for a few months through\n \
        Latin America and came back to Berlin.\n \
        \n \
        I am currently using Ubuntu as OS, I prefer Gnome Classic to other\n \
        desktop environments. I enjoy using Vim to write code, it is very\n \
        efficient. Vim + Tmux + Oh My Zsh is a match made in heaven.\n"

        self.jobs = [
            {
                'company': 'DCMN',
                'title': 'Software Developer',
                'tasks': 'PHP, Ruby',
                'location': 'Berlin, Germany; & Remote',
                'date_start': '10/2016',
                'date_end': '02/2018'
            },
            {
                'company': 'Kimera',
                'title': 'Cofounder & Software Developer',
                'tasks': 'Python',
                'location': 'Remote',
                'date_start': '05/2015',
                'date_end': '01/2017'
            },
            {
                'company': 'Coder Dojo SWICN',
                'title': 'Volunteer Mentor',
                'tasks': 'HTML, CSS, Javascript, Python, Scratch',
                'location': 'Dublin, Ireland',
                'date_start': '05/2015',
                'date_end': '05/2016'
            },
            {
                'company': 'Learning Data',
                'title': 'Software Developer',
                'tasks': 'PHP, Python, Javascript',
                'location': 'Dublin, Ireland; & Remote',
                'date_start': '07/2013',
                'date_end': '05/2016'
            },
            {
                'company': 'ClaSS Information Services',
                'title': 'Software Developer',
                'tasks': 'PHP & Support',
                'location': 'Madrid, Spain & Remote',
                'date_start': '01/2013',
                'date_end': '07/2013'
            },
            {
                'company': 'Wireless Mundi',
                'title': 'Intern',
                'tasks': 'Testing, Translations, & PHP',
                'location': 'Madrid, Spain',
                'date_start': '04/2012',
                'date_end': '07/2012'
            }
        ]

        self.education = {
            'school': 'La Inmaculada',
            'title': 'Telecommunications Technology Technician',
            'degree': 'CFGS Sistemas de Telecomunicacion e Informaticos',
            'skills': 'C, PHP, Networking',
            'location': 'Getafe, Spain',
            'year_start': 2010,
            'year_end': 2012
        }

        self.skills = [
            'Python',
            'PHP',
            'Javascript',
            'MySQL',
            'PostgreSQL',
            'Git',
            'Ansible',
            'Linux',
            'HTML',
            'Kanban',
            'Django',
            'TDD',
        ]

        self.languages = [
            'English',
            'Spanish',
            'Romanian',
        ]

        self.interests = [
            'Traveling',
            'Films',
            'Reading',
            'Open Source',
            'Painting',
            'Photography',
            'Pizza',
            'Ukulele',
        ]

    def cv(self):
        print("**************************************************************")
        print()
        print("Marius Avram, Software Developer, Berlin (me@mariusavram.com)")
        print()

        print(self.about_me)
        print()

        print("Experience")
        for job in self.jobs:
            print(job['company'])
            print("\t" + job['title'])
            print("\t" + job['date_start'] + "-" + job['date_end'])
            print("\t" + job['tasks'])
            print("\t" + job['location'])
        print()

        print("Skills")
        print(", ".join(skill for skill in self.skills))
        print()

        print("Languages")
        print(", ".join(language for language in self.languages))
        print()

        print("Interests")
        print(", ".join(interest for interest in self.interests))
        print()

        print("**************************************************************")
        print()


class Application:
    def __init__(self):
        self.company = None
        self.position = None
        self.contact = None
        self.location = None
        self.why_I_like_you = ''
        self.why_you_like_me = ''

    def apply(self, company_is_awesome, recruiter_likes_my_cv):
        MariusAvram().cv()

        if company_is_awesome and recruiter_likes_my_cv:
            Application().interview()

        print("Thanks!")

    def interview(self):
        success = True
        hired = True

        if success:
            print("We're hiring Marius! :)")
            return hired
        return


class ApplicationTest(unittest.TestCase):
    def setup(self):
        pass

    def test_hired(self):
        expect = True
        self.assertTrue(expect)


if __name__ == '__main__':
    application = Application()
    application.company = "Company Gmbh"
    application.position = "Python Developer advertised on Website"
    application.contact = "John Smith"
    application.location = "Berlin"
    application.why_I_like_you = "..."
    application.why_you_like_me = "..."

    company_is_awesome = True
    recruiter_likes_my_cv = True

    application.apply(company_is_awesome, recruiter_likes_my_cv)

    unittest.main()
