var map = L.map('mapid').setView([51.505, -0.09], 4);

L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

L.marker([51.5, -0.09]).addTo(map)
    .bindPopup('A pretty CSS3 popup.<br> Easily customizable.')
    .openPopup();

function getColor(d) {
    // return d > 1000 ? '#800026' :
    //        d > 500  ? '#BD0026' :
    //        d > 200  ? '#E31A1C' :
    //        d > 100  ? '#FC4E2A' :
    //        d > 50   ? '#FD8D3C' :
    //        d > 20   ? '#FEB24C' :
    //        d > 10   ? '#FED976' :
    //                   '#FFEDA0';
    if (d === 'Afghanistan') {
        return '#800026';
    } else {
        return '#FFEDA0';
    }
}

function style(feature) {
    return {
        fillColor: getColor(feature.properties.name),
        weight: 2,
        opacity: 1,
        color: 'white',
        dashArray: '3',
        fillOpacity: 0.7
    };
}


L.geoJson(countryData, {style: style}).addTo(map);