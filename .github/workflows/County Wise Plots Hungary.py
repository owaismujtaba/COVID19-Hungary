import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', -1)

url = "https://raw.githubusercontent.com/mollac/CoVid-19/master/korona_megyei.csv"


# Time series plots for all counties from starting to till date
def time_series_plots_all_counties():
    data = pd.read_csv(url, error_bad_lines=False)  # Get data from the url
    data = data.drop("Dátum", axis=1)  # Droping first column that is date
    counties = data.columns  # Get the list of all counties

    # Plotting every county in counties Note the graphs are on log scale
    for county in counties:
        plt.plot(np.log10(data[county]))
    plt.title("All counties time series plots")
    plt.legend(counties)
    plt.xlabel("Days")
    plt.ylabel("No of cases on log10 scale")
    plt.subplots_adjust(left=0.1,
                        bottom=0.1,
                        right=0.95,
                        top=0.9,
                        wspace=0.4,
                        hspace=0.35)
    # plt.savefig("E:\CountyHungary\TimeSerisAll.png", dpi=100)
    plt.show()
    plt.clf()


# Plotting the counties in four categories starting from min caess to max cases
def time_series_plots_grouping():
    data = pd.read_csv(url, error_bad_lines=False)
    data = data.drop("Dátum", axis=1)  # Droping first column that is date
    counties = data.columns
    sort = []
    label = 0
    for county in counties:
        sort.append([data[county].max(), label]) # Getting the end entry from each county and add to sort with its label
        label = label + 1

    sort = sorted(sort, key=lambda sort: sort[0]) # Sorting the counties in assending order


    plt.subplots_adjust(left=0.1,
                        bottom=0.1,
                        right=0.95,
                        top=0.9,
                        wspace=0.4,
                        hspace=0.35)
    fig, a = plt.subplots(2)

    legend = []
    a[0].set_title("Cases less than 2300")
    for i in range(0, 5):
        a[0].plot(data[counties[sort[i][1]]])
        legend.append(counties[sort[i][1]])
    a[0].legend(legend)

    a[1].set_title("Total Cases: 2301-3100")
    for i in range(5, 10):
        a[1].plot(data[counties[sort[i][1]]])
        legend.append(counties[sort[i][1]])
    a[1].legend(legend[5:])

    plt.subplots_adjust(left=0.1,
                        bottom=0.1,
                        right=0.95,
                        top=0.9,
                        wspace=0.4,
                        hspace=0.35)

    #plt.savefig('E:\CountyHungary/png1.png', dpi=600)

    fig, b = plt.subplots(2)

    b[0].set_title("Total Cases: 3101-5000")
    for i in range(10, 15):
        b[0].plot(data[counties[sort[i][1]]])
        legend.append(counties[sort[i][1]])
    b[0].legend(legend[10:])
    b[1].set_title("Total Cases: > 5000")

    for i in range(15, 20):
        b[1].plot(data[counties[sort[i][1]]])
        legend.append(counties[sort[i][1]])
    b[1].legend(legend[15:])

    plt.subplots_adjust(left=0.1,
                        bottom=0.1,
                        right=0.95,
                        top=0.9,
                        wspace=0.4,
                        hspace=0.35)
    #plt.savefig('E:\CountyHungary/png2.png', dpi=600)
    plt.show()
    plt.clf()


def sorted_counties_data():
    data = pd.read_csv(url, error_bad_lines=False)
    data = data.drop("Dátum", axis=1)
    counties = data.columns

    sort = []
    label = 0
    for i in counties:
        sort.append([data[i].max(), label])
        label = label + 1

    sort = sorted(sort, key=lambda sort: sort[0])

    sorted_labels = []
    sorted_values = []
    for i in range(0, len(sort)):
        sorted_values.append(sort[i][0])
        sorted_labels.append(counties[sort[i][1]])

    return sorted_values, sorted_labels


def pie_chart_all_counties():
    sorted_values, sorted_labels = sorted_counties_data()
    explode = np.zeros(len(sorted_labels))

    for i in range(len(sorted_labels) - 5, len(sorted_labels)):
        explode[i] = 0.1
    plt.title("Distribution of total cases")
    plt.pie(sorted_values, labels=sorted_labels, autopct='%1.1f%%', explode=explode)
    plt.tight_layout()

    #plt.savefig("E:\CountyHungary\PieChart.png", dpi=600)
    plt.show()
    plt.clf()


def time_series_plots_worst_five_counties_log10():
    # Time series plots of most five affected counties
    data = pd.read_csv(url, error_bad_lines=False)
    data = data.drop("Dátum", axis=1)

    # Gettting sorted labels from sorted counties function
    sorted_values, counties = sorted_counties_data()

    for county in counties[len(counties) - 5:len(counties)]:
        plt.plot(np.log10(data[county]))
    plt.title("Time series plots of top five counties")
    plt.legend(counties[len(counties) - 5:len(counties)])
    plt.xlabel("Days")
    plt.ylabel("Number of cases on log 10 scale")
    plt.tight_layout()

    #plt.savefig("E:\CountyHungary\TimeSeries5most.png", dpi=600)
    plt.show()
    plt.clf()



def plot_population_density_all_counties():
    # Source Wikipedia

    density = [3293, 190, 135, 106, 98, 98, 95, 94, 88, 87, 85, 80, 79, 77, 75, 69, 64, 62, 62, 52]
    density.reverse()
    counties = ['Budapest', 'Pest', 'Komárom-Esztergom', 'Győr-Moson-Sopron', 'Fejér', 'Csongrád',
                'Borsod-Abaúj-Zemplén',
                'Szabolcs-Szatmár-Bereg', 'Hajdú-Bihar', 'Baranya', 'Heves', ' Nógrád', 'Veszprém', 'Vas', 'Zala',
                'Jász-Nagykun-Szolnok', 'Békés', 'Bács-Kiskun', 'Tolna', 'Somogy']
    counties.reverse()
    plt.title("Population per square km")
    plt.barh(counties, density)
    plt.tick_params(axis='y', labelsize=8)
    plt.tight_layout()

    for index, value in enumerate(density):
        plt.text(value, index, str(value))
    plt.show()
    # plt.savefig("E:\CountyHungary\PopulationBar.png", dpi=600)
    plt.clf()


time_series_plots_all_counties()
time_series_plots_grouping()
time_series_plots_worst_five_counties_log10()
pie_chart_all_counties()
plot_population_density_all_counties()