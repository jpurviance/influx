L.Map = L.Map.extend({
    openPopup: function (popup, latlng, options) {
        if (!(popup instanceof L.Popup)) {
            var content = popup;

            popup = new L.Popup(options).setContent(content);
        }

        if (latlng) {
            popup.setLatLng(latlng);
        }

        if (this.hasLayer(popup)) {
            return this;
        }

        // NOTE THIS LINE : COMMENTING OUT THE CLOSEPOPUP CALL
        //this.closePopup(); 
        this._popup = popup;
        return this.addLayer(popup);
    }
});

var map = L.map('mapid').setView([51.505, -0.09], 4);

L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

// L.marker([51.5, -0.09]).addTo(map)
//     .bindPopup('A pretty CSS3 popup.<br> Easily customizable.')
//     .openPopup();

//GLOBALS AHHHHH
var lastClickedCountry = null;
var lastWasBanned = false;

function onEachBannedFeature(feature, layer) {   
    layer.on('click', function(e) {
        var popupContent = "";
        var name = feature.properties.name;
        if (lastClickedCountry != null && !lastWasBanned) {
            popupContent = "this country (" + name + ") is banned, last clicked is " + lastClickedCountry;
        } else {
            popupContent = "this country (" + name + ") is banned, no last clicked";
        }

        lastWasBanned = true;
        layer.bindPopup(popupContent).addTo(map).openPopup();
    })
}

function onEachFeature(feature, layer) {
    layer.on('click', function (e) {
        lastClickedCountry = feature.properties.name;
        bannedCountries.eachLayer(function (layer) {
            layer.bindPopup(feature.properties.name).addTo(map).openPopup();
        })
        lastWasBanned = false;
    })
}

function isBanned(name) {
    var bannedCountryList = [
        "Syria",
        "Iraq",
        "Iran",
        "Sudan",
        "Yemen",
        "Somalia",
        "Libya"
    ];
    return bannedCountryList.indexOf(name) > -1;
}

function style(feature) {
    return {
        weight: 2,
        opacity: 0,
        color: 'white',
        dashArray: '3',
        fillOpacity: 0.3
    };
}

function bannedStyle(feature) {
    return {
        fillColor: '#800026',
        weight: 2,
        opacity: 1,
        color: 'white',
        dashArray: '3',
        fillOpacity: 0.3
    };
}

var countries = L.geoJson(countryData, {
    style: style,
    onEachFeature: onEachFeature,
    pointToLayer: function (feature, latlng) {
        return L.circleMarker(latlng, {
            radius: 8,
            fillColor: "#ff7800",
            color: "#000",
            weight: 1,
            opacity: 1,
            fillOpacity: 0.8
        });
    }
});

var bannedCountries = L.geoJson(countryData, {
    style: bannedStyle,
    onEachFeature: onEachBannedFeature,
    pointToLayer: function (feature, latlng) {
        return L.circleMarker(latlng, {
            radius: 8,
            fillColor: "#ff7800",
            color: "#000",
            weight: 1,
            opacity: 1,
            fillOpacity: 0.8
        });
    },
    filter: function (feature, layer) {
        return isBanned(feature.properties.name);
    }
});

countries.addTo(map);
bannedCountries.addTo(map);

//click on any other country, show info to banned countries (in those countries)
//click on one country to another country, show info between the two