# Y2 2018 Summer: Databases Lab

Welcome to the databases lab! Please read all the instructions so you don't
get lost halfway through, but definitely feel free to ask for help if you
get stuck. Good luck, and have fun!

### Part 0: Setup

1. Before you start coding, make sure you clone the repository for this lab:
```
cd ~/Desktop
https://github.com/meet-projects/y2s18-databases
cd y2s18-databases
subl lab &
```

2. In this lab, we will create our own database. The only files that you will
need to modify are `knowledge_model.py` and `knowledge_databases.py`.

### Part 1: Creating a Database Model

1. That is, after realizing just
how easy it is to organize information, you decide to create a website to 
organize all the information in the world. To start off, you'd like to understand
what kind of topics people are interested in. Survey at least three people
around you and ask them what they want to learn about!

2. To start with, you decide to look on Wikipedia to find information on the relevant
topics. So, for each topic that has been chosen, find a Wikipedia article that
your friends can use to learn more about the topic. 

3. Read through the articles and give them a rating from 1-10, based off of how
much you liked them and what you've learned.

4. Now, after doing this, you have enough information to create a database of
the knowledge you've learned so far. The database should have:
- A primary key (what would this be for the set of articles?)
- The topic of the article (what did your friends want to learn about?)
- The title of the relevant article that you've chosen. This can be the same
as the topic of the article, but it does not have to be!
- Your rating of the article, from 1-10.
Edit `knowledge_model.py` and create a table, named `knowledge`, to create a table
which stores this information.

5. Add a `__repr__` function to your table. That is, when you want to print an instance
of the Knowledge class, which has primary key 1, a topic of weather, a title of rainbow,
and a rating of 9, the following should be printed:
```
If you want to learn about weather, you should look at the Wikipedia article called rainbow.
We gave this article a rating of 9 out of 10!
```

6. Bonus: If the article is rated lower than 7 out of 10, add the following message, when printing
the instance.
```
Unfortunately, this article does not have a better rating. Maybe, this is an article that should be
replaced soon!.
```

### Part 2: 