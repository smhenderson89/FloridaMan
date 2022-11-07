<div id="top"></div>

<!-- PROJECT LOGO -->
<br />
<div align="center">

  <h3 align="center">FloridaMan - A Florida News Story Google Search Web Scarper</h3>
  https://floridaman.onrender.com/today
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#project-demo">Project Demo</a>
    </li>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- Project DEMO -->
## Project Demo

![890F1CC5-6E02-46BF-AA7D-8FCB9797CD1C](https://user-images.githubusercontent.com/53064568/200436355-f567cd04-80fe-40e1-be35-e286cbde927d.jpeg)

<!-- ABOUT THE PROJECT -->
## Project Inspiration

This website is my Final Project for [CS50 Edx Course 2020](https://www.edx.org/course/introduction-computer-science-harvardx-cs50x).
My goal was to create a website that would show a user their "Florida Man Horoscope", which I had learned about years back. A Florida Man Horoscope is created by typing in your date of birth into Google + "[Florida Man](https://letmegooglethat.com/?q=Dec+30+florida+man)" and the list of headlines that return are your horoscope. (Here's an [example](https://floridaman.onrender.com/random).)

Origin of the Meme: [Know Your Meme](https://knowyourmeme.com/memes/florida-man)

Wikipedia: [Link](https://en.wikipedia.org/wiki/Florida_Man)

To accomplish this I built a [web-scraper](https://en.wikipedia.org/wiki/Web_scraping) that would search for 'Florida Man' headlines and save the results from every day of the year (including leap year). I put those results into a database and any user can query them while searching the website.

<p align="right">(<a href="#top">back to top</a>)</p>

### Built With

* [Python](https://www.python.org/)
* [Sqlite3](https://www.sqlite.org/index.html)
* [Flask](https://flask.palletsprojects.com/en/1.1.x/)
* [Heroku](https://dashboard.heroku.com/apps)
* [Render](https://render.com/)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites

* Download Python ([link])(https://www.python.org/downloads/)
* Download Flask ([link](https://flask.palletsprojects.com/en/1.1.x/installation/))

### Installation

1. Clone the repo
   ```sh
   git clone gh repo clone smhenderson89/FloridaMan 
   ```
2. Setup virtual environment: 
  ```sh
  . venv/bin/activate
  ```
3. Install all pip package requirements:
#### Windows
  ```sh
  pip install -r requirements.txt
  ```
#### Mac
   ```sh
  pip3 install -r requirements.txt
   ```
4. Setup Environmental varialbe: 
  ```sh
  $env:FLASK_APP = "app"
  ```
5. Launch Website
  ```sh
  "python3 -m flask"
  ```
6. Go to location host location, should be running at localhost:5000

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->


<!-- ROADMAP -->
## Roadmap

I'm pretty happy with how the site turned out. There are some sretch goal ideas I have (making a twitter bot to post a new news story everyday, word cloud), but for now it was a great learning experience.

See the [open issues](https://github.com/smhenderson89/FloridaMan/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Scott Henderson
Github: [https://github.com/smhenderson89](https://github.com/smhenderson89)

Julia Szymanski
Github: [https://github.com/julszymanski](https://github.com/julszymanski)

Mike Woolf
Github: [https://github.com/mwoolf87](https://github.com/mwoolf87)


<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* The DigitalCrafts Teachers and Teaching Assistants

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[product-screenshot]: images/screenshot.png
