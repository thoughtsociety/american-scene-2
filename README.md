## American Scene : A new data story from ThoughtSociety.org

## ThoughtSociety.org 
Helps to digest open source data and encourages the user to find insights as a result.

The object is to make this process, interactive, easy and fast and to insulate the user from the ugly data wrangling, 
algorithm development and hard data science that is usually required to get there.

## Running in the cloud is one of the objectives

This was designed for four or more containers, 1 for each separate app and one for the Nginx proxy.
Users hit the proxy and everything gets internally routed to the multi-app containers by name. The sit within a docker local network on Ubuntu.

## Embeddable Graph Apps - Using SSL
In order to embed from the tsworker.com/appn.. URL in iFrames on Wordpress, SSL needed to be implemented in the Nginx container. 
Using LetsEncrypt free certs and an auto-renewal script, 
we are able to have carefree SSL certs that pass certification authority muster.

## The Blog
At www.thoughtsociety.org, we embed (in iFrames) all the graphs that are created with the Dash app. 
The main benefit of these is that we tell data stories that the user can interact with and mess around with 
the plotting controls.
This does not go so far as to allow operations on the data but 
simply a way to choose what data to plot against other available
datasets loaded up into S3 buckets in the cloud. 

## Futures
**Live Data Sources** Ultimately, the Dashboard apps will pull live data from opensources in 
the cloud and update on their own. When the user then interacts with those, the experience will be much more vivid
and alive. A simple interaction will be a history slider that allows the user to go back in time to older data
and compare things with current time-series available on the apps.  
    
**Accounts with personal preferences and saved history** Once all of this is scaled out and totally stable, we should
be able to add accounts with login, saved profiles and prefs as well as a research history. At some point, we could 
add the ability to select datasets that are of interest to the user where we can semi-automate 
the wrangling and aggregations without becoming Tableau. 

# Technology
## Dash

Dash Web Applications combine the full power and best features of Plot.ly, Python, React.js and Flask.

https://dash.plot.ly/gallery

A fork of 
https://github.com/ericcgu/Flask_Dash_Container

Added extra items to requirements.txt in order to get this to correctly build and run.
Demos a sample StockTicker app (renamed app.py) which originated 
on [Jose Portilla's Dash course in Udemy](https://www.udemy.com/interactive-python-dashboards-with-plotly-and-dash/learn/v4/overview).

### Multi-App-Container 

09/29/18 - Re-forked Ctindel's mods and deleted the current repo
10/05-18 - A fork of Multi-App-Dashboard with new names

This is essentially a fork of the Stock Ticker with two apps now. Second one is Eric's simple graph.

There are now 3 apps:  

* economy
* elections
* social

## Synopsis
A Nginx and Python Flask Container used for bootstrapping continuous deployment of Dash / Plot.ly Applications.
Requires :

* Docker
* Dash & Plot.ly
* Nginx
* Gunicorn
* Whatever other packages required to run our charts & analysis