var filterBar = document.getElementById("filter");
var countryNameEl = document.getElementById("countryname");

var countryLocDict = {
    "United States": [39.83, -98.58],
    "Saudi Arabia": [23.89, 45.08],
    "India": [20.6, 78.96],
    "Russia": [61.52, 105.32],
    "China": [35.86, 104.2],
    "Canada": [56.13, -106.35],
    "Mexico": [23.63, -102.6]
}

var panToCountry = function (e) {
    var countryName = capitalizeEachWord(countryNameEl.value);
    console.log("move to country " + countryName);
    var latlng = coordinateData[countryName];
    console.log(latlng);
    if (latlng != null) {
        console.log(latlng);
        map.panTo(latlng);
    }
}

function capitalizeFirstLetter(string) {
    return string.charAt(0).toUpperCase() + string.slice(1);
}

function capitalizeEachWord(string) {
    return string
        .split(' ')
        .map(capitalizeFirstLetter)
        .join(' ')
}

filterBar.onclick = function (e) {
    if (e.target.dataset.filterType === "hotcountry") {
        var countryName = capitalizeEachWord(e.target.innerText);
        console.log("move to country " + countryName);
        var latlng = countryLocDict[countryName];
        console.log(latlng);
        map.panTo(latlng);
    }

    if (e.target.id == 'countrysearch') {
        panToCountry();
    }
}

countryNameEl.onkeyup = function (e) {
    if (e.which == 13) {
        panToCountry();
    }
}