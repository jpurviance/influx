var searchBar = document.getElementById("search");
var countryNameEl = document.getElementById("countryname");

searchBar.onclick = function (e) {
    if (e.target.id == 'countrysearch') {
        var countryName = countryNameEl.value;
        fetch("/api/visa/?from=" + countryName)
            .then(r => r.json())
            .then(dat => colorCountries(dat.d));
    }
}

countryNameEl.onkeyup = function (e) {
    if (e.which == 13) {
        fetch("/api/visa/?from=" + countryName)
            .then(r => r.json())
            .then(d => colorCountries(d));
    }
}