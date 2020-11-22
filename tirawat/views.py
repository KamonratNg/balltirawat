from django.shortcuts import render
from django.http import HttpResponse
from collections import OrderedDict
from tirawat.fusioncharts import FusionCharts

# Create your views here.

def Home(request):
	return render(request,'tirawat/home.html')

def About(request):
	return render(request,'tirawat/about.html')

def Research(request):
	return render(request,'tirawat/research.html')

def Service(request):
	return render(request,'tirawat/service.html')

def Contact(request):
	return render(request,'tirawat/contact.html')

def Index(request):
	return render(request,'tirawat/index.html')

def Portfolio(request):
	return render(request,'tirawat/portfolio.html')

def Team(request):
	return render(request,'tirawat/team.html')

def myFirstMap(request):

    # Chart data is passed to the `dataSource` parameter, as dict, in the form of key - value pairs.
    dataSource = OrderedDict()

    # The `mapConfig` dict contains key - value pairs data
    # for chart attribute
    mapConfig = OrderedDict()
    mapConfig["animation"] = "0"
    mapConfig["usehovercolor"] = "1"
    mapConfig["showlegend"] = "1"
    mapConfig["legendposition"] = "BOTTOM"
    mapConfig["legendborderalpha"] = "0"
    mapConfig["legendbordercolor"] = "#ffffff"
    mapConfig["legendallowdrag"] = "0"
    mapConfig["legendshadow"] = "0"
    mapConfig["caption"] = "Website Visits for the month of March 2018"
    mapConfig["connectorcolor"]= "000000"
    mapConfig["fillalpha"]= "80"
    mapConfig["hovercolor"]= "CCCCCC"
    mapConfig["theme"] = "fusion"

    # Map color range data
    colorDataObj = {
        "minvalue": "0",
        "code": "#FFE0B2",
        "gradient": "1",
        "color": [{
            "minValue": "0.5",
            "maxValue": "1",
            "code": "#FFD74D"
        }, {
            "minValue": "1.0",
            "maxValue": "2.0",
            "code": "#FB8C00"
        }, {
            "minValue": "2.0",
            "maxValue": "3.0",
            "code": "#E65100"
        }]
    }

    dataSource["chart"] = mapConfig
    dataSource["colorrange"] = colorDataObj
    dataSource["data"] = []

    # Map data array
    mapDataArray = [
        ["001", "2834", "1"],
        ["003", "3182", "1"],
        ["005", "3280", "1"],
        ["007", "911", "1"],
        ["009", "292", "1"],
        ["011", "530", "1"],
        ["013", "2515", "1"],
        ["015", "728", "1"],
        ["017", "1974", "1"],
        ["019", "848", "1"],
        ["021", "3278", "1"],
        ["023", "4463", "1"],
        ["025", "1198", "1"],
        ["027", "378", "1"],
        ["029", "2610", "1"],
        ["031", "1200", "1"],
        ["033", "3820", "1"],
        ["035", "940", "1"],
        ["037", "3416", "1"],
        ["039", "4004", "1"],
        ["041", "1604", "1"],
        ["043", "4011", "1"],
        ["045", "3203", "1"],
        ["047", "3775", "1"],
        ["049", "2721", "1"],
        ["051", "3417", "1"],
        ["053", "1530", "1"],
        ["055", "412", "1"],
        ["057", "3434", "1"],
        ["059", "1670", "1"],
        ["061", "1274", "1"],
        ["063", "4339", "1"],
        ["065", "2073", "1"],
        ["067", "1018", "1"],
        ["069", "3967", "1"],
        ["071", "3401", "1"],
        ["073", "3307", "1"],
        ["075", "1938", "1"],
        ["077", "489", "1"],
        ["079", "3207", "1"],
        ["081", "2295", "1"],
        ["083", "2747", "1"],
        ["085", "1114", "1"],
        ["087", "3400", "1"],
        ["089", "784", "1"],
        ["091", "1673", "1"],
        ["093", "4274", "1"],
        ["095", "4509", "1"],
        ["097", "3862", "1"],
        ["099", "1356", "1"],
        ["101", "4126", "1"],
        ["103", "1314", "1"],
        ["105", "1807", "1"],
        ["107", "4026", "1"],
        ["109", "3456", "1"],
        ["111", "1393", "1"],
        ["113", "1500", "1"],
        ["115", "2218", "1"]
    ]

    # Iterate through the data in `mapDataArray` and insert in to the `dataSource["data"]` list.
    #The data for the `data` should be in an array wherein each element 
    #of the array is a JSON object# having the `id`, `value` and `showlabel` as keys.
    for i in range(len(mapDataArray)):
        dataSource["data"].append({
            "id": mapDataArray[i][0],
            "value": mapDataArray[i][1],
            "showLabel": mapDataArray[i][2]
        })

    # Create an object for the world map using the FusionCharts class constructor
    # The chart data is passed to the `dataSource` parameter.
    fusionMap = FusionCharts("maps/world", "myFirstMap", "650", "450", "myFirstmap-container", "json", dataSource)

    # returning complete JavaScript and HTML code, which is used to generate map in the browsers.
    return render(request, 'tirawat/map.html', {
        'output': fusionMap.render()
    })