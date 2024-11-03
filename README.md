# Comic Wish List
This application provides the serious collector a quick tool to create a wish list and give pricing ranges in order to get the grail and not overpay. First appearance of Wolverine's daughter(X-23) is in NYX #3  ranges from $300 - $500, but what price for what grade?  Pop open this app and look at your recorded research.  A graded 9.8 has 3 prices with an average of $496, a 9.4 averaged $600 a 9.0 avg $350.  The book you are looking at is a 9.6 and they are asking $375, score!!  Thank you comic wish list :)

## Installation Instructions
```bash
docker-build .
docker-compose run django bash
python manage.py migrate
python manage.py createsuperuser

## Getting Started
To run my awesome app simply,
```bash
docker-compose up
```
Simple in app menus to Add, Edit and Delete with a quick search capability

# License
This project is licensed under [MIT License](./License)

# Home Page Mockup
![alt text](https://github.com/wein-uno/comicwishlist/blob/main/images/ComicWishList-Mockup.jpg "Home Page Mockup")

# C4 Diagram
![alt text](https://github.com/wein-uno/comicwishlist/blob/main/images/ErikWeinmeisterC4-ComicApp.jpg "C4 Diagram")

# Use Case
As a serious comic book collector, I want to have a list of my most wanted comics with with 3 price comparison for 3 different grades so I can determine a reasonable price to pay while hunting for these comic books.

## Acceptance criteria
For each comic, I need the title, comic id number and fields for three different grades with three prices under each grade.  I should be able to add new entries, edit existing entries and delete an entry.  The list will be displayed in alphabetical order.  After each price there will be a calculation which is the price divided by the grade to determine a price/point.

## Mis-user stories
Malicious actors and kids can have the same effect of deleting all the data. Price fields will display in dollar and cent format with checks to only allow numbers.  Ruin my day Ryan could cause the application to crash by putting in wrong data, like text in a number field.  Newbie Neuman may not know what the new grades are compared to what his grandpa wrote down, a guess of an 8.7 will lead to inaccurate results and bad buying decisions.

## Mitigation Criteria
Deletion will require confirmation to assist in mis-clicks.  This app will perform periodic copies of the data to ensure against accidental deletion and malicious deletion of data.  Price fields will display in dollar and cent format with checks to only allow numbers.  Grades will have predefined drop down selection list to abide by standard comic grades, this will have a tip on each grade to match the old grading word scores.

[![alt text](https://github.com/wein-uno/comicwishlist/blob/main/images/ComicWishList-Mockup.jpg "Use Case")


