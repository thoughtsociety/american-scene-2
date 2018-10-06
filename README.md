## American Scene : A new data story from ThoughtSociety.org

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

```
economy:
        container_name: economy
        restart: always
        build: ./economy
        ports:
        - "8500:8500"
        command: gunicorn -w 1 -b :8500 economy:server
```
## Synopsis
A Nginx and Python Flask Container used for bootstraping continuous deployment of Dash / Plot.ly Applications.
Requires :


    
    

## What is Dash? mmmm

Dash Web Applications combine the full power and best features of Plot.ly, Python, React.js and Flask.

https://dash.plot.ly/gallery