import requests
import json
from tkinter import *
    
def getListOfCountries():
    r = requests.get("https://api.covid19api.com/countries")
    j = r.json()
    countries = []
    for eachCountry in j:
        countries.append(eachCountry['Country'])
    return sorted(countries)

def getCountryApi(country):
    r = requests.get("https://api.covid19api.com/countries")
    j = r.json()
    for eachCountry in j:
        if eachCountry['Country'] == country:
            return eachCountry['Slug']



def getCountryStats(*args):
    countryName = getCountryApi(tkvar.get())
    URL="https://api.covid19api.com/live/country/"+countryName
    r = requests.get(URL)
    j = r.json()
    if len(j) == 0:
        confirmedLabel['text'] = 'NO DATA'
        recoveredLabel['text'] = 'NO DATA'
        deathsLabel['text'] = 'NO DATA'
        activeLabel['text']  = 'NO DATA'
    else:
        data = j[len(j) - 1]
        confirmedLabel['text'] = data['Confirmed']
        recoveredLabel['text'] = data['Recovered']
        deathsLabel['text'] = data['Deaths']
        activeLabel['text']  = data['Active']


root = Tk()
root.title("Covid tracker")

# Add a grid
mainframe = Frame(root)
mainframe.grid(column=0,row=0, sticky=(N,W,E,S) )
mainframe.columnconfigure(0, weight = 1)
mainframe.rowconfigure(0, weight = 1)
mainframe.pack(pady = 100, padx = 100)

# Create a Tkinter variable
tkvar = StringVar(root)

# Dictionary with options
choices = getListOfCountries()
tkvar.set('Select a Country') # set the default option

popupMenu = OptionMenu(mainframe, tkvar, *choices)
Label(mainframe, text="Choose A country").grid(row = 1, column = 1)
popupMenu.grid(row = 2, column =1)

    
noOfConfirmed=0
noOfRecovered=0
noOfActive=0
noOfDeaths=0
# link function to change dropdown
tkvar.trace('w', getCountryStats)
confirmedLabel = Label(mainframe, text=str(noOfConfirmed))
deathsLabel = Label(mainframe, text= str(noOfDeaths))
recoveredLabel = Label(mainframe, text=str(noOfRecovered))
activeLabel = Label(mainframe, text=str(noOfActive))
Label(mainframe, text="Deaths: ").grid(row = 4, column = 1)
Label(mainframe, text="Confirmed: ").grid(row = 5, column = 1)
Label(mainframe, text="Recovered: ").grid(row = 6, column = 1)
Label(mainframe, text="Active: ").grid(row = 7, column = 1)

deathsLabel.grid(row=4, column=2)
confirmedLabel.grid(row=5, column=2)
recoveredLabel.grid(row=6, column=2)
activeLabel.grid(row=7, column=2)
# on change dropdown value


root.mainloop()
