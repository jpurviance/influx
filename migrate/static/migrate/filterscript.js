var filterBar = document.getElementById("filter");

var countryLocDict = {
    "United States": [39.83, -98.58],
    "Saudi Arabia": [23.89, 45.08],
    "India": [20.6, 78.96],
    "Russia": [61.52, 105.32],
    "China": [35.86, 104.2],
    "Canada": [56.13, -106.35],
    "Mexico": [23.63, -102.6]
}

filterBar.onclick = function(e) {
    if (e.target.dataset.filterType === "hotcountry") {
        console.log("move to country " + e.target.innerText);
        var latlng = countryLocDict[e.target.innerText];
        console.log(latlng);
        map.panTo(latlng);
    }
}