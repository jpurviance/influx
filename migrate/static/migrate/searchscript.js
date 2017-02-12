var searchBar = document.getElementById("search");
var countryNameEl = document.getElementById("countryname");

searchBar.onclick = function (e) {
    if (e.target.id == 'countrysearch') {
        var countryName = capitalizeEachWord(countryNameEl.value);
        fetch("/api/visa/?from=" + countryName)
            .then(r => r.json())
            .then(dat => colorCountries(dat.d));
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

countryNameEl.onkeyup = function (e) {
    if (e.which == 13) {
        var countryName = capitalizeEachWord(countryNameEl.value);
        console.log(countryName);
        fetch("/api/visa/?from=" + countryName)
            .then(r => r.json())
            .then(dat => colorCountries(dat.d));
    }
}