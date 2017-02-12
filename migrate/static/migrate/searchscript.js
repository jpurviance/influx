var searchBar = document.getElementById("search");
var countryNameEl = document.getElementById("countryname");

searchBar.onclick = function (e) {
    if (e.target.id == 'countrysearch') {
        colorCountries(null);
    }
}

countryNameEl.onkeyup = function (e) {
    if (e.which == 13) {
        colorCountries(null);
    }
}