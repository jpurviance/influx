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



var map = L.map('mapid').setView([30,0], 3);

L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

// L.marker([51.5, -0.09]).addTo(map)
//     .bindPopup('A pretty CSS3 popup.<br> Easily customizable.')
//     .openPopup();

//GLOBALS AHHHHH
var lastClickedCountry = null;
var lastWasBanned = false;


fetch("/api")
    .then(r => r.json())
    .then(dat => {

        var data = {};

        function onEachBannedFeature(feature, layer) {
            layer.on('click', function (e) {
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
                fetch('/api/reverse_visa?to=' + lastClickedCountry)
                    .then(r => r.json())
                    .then(dat => {
                        var data = dat.d;
                        var inf = "";
                        var countryData = null;
                        bannedCountries.eachLayer(function (layer) {
                            countryData = data[layer.feature.properties.name];
                            if (countryData == null) {
                                inf = "no data available"
                                inf = "Banned!!!"
                            } else if (countryData[0] == "") { // was 1
                                inf = "no data found";
                            } else {
                                inf = '<b>' + countryData[0] + '</b>';
                                if (countryData[1] != ""){
                                    inf = inf + '<br>' + countryData[1];
                                }
                            }
                            layer.bindPopup(inf).addTo(map).openPopup();
                        })
                        lastWasBanned = false;
                    });
            });
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

        function bannedStyle(feature) {
            return {
                fillColor: '#950101',
                weight: 2,
                opacity: 1,
                color: 'white',
                dashArray: '3',
                fillOpacity: 0.75
            };
        }

        function style(feature) {
            var styl = {
                weight: 2,
                opacity: 1,
                color: 'white',
                dashArray: '3',
                fillOpacity: 0.3
            };

            var fillCol = null;

            if (data[feature.properties.name] >= 0.875) {
                fillCol = '#800026';
            } else if (data[feature.properties.name] >= 0.75) {
                fillCol = '#BD0026';
            } else if (data[feature.properties.name] >= 0.625) {
                fillCol = '#E31A1C';
            } else if (data[feature.properties.name] >= 0.5) {
                fillCol = '#FC4E2A';
            } else if (data[feature.properties.name] >= 0.375) {
                fillCol = '#FD8D3C';
            } else if (data[feature.properties.name] >= 0.25) {
                fillCol = '#FEB24C';
            } else if (data[feature.properties.name] >= 0.125) {
                fillCol = '#FED976';
            } else if (data[feature.properties.name] >= 0) {
                fillCol = '#FFEDA0';
            }

            if (fillCol != null || !isBanned(feature.properties.name)) {
                styl.fillColor = fillCol;
            }

            return styl;
        }

        var data = dat.d;

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

    });

//click on any other country, show info to banned countries (in those countries)
//click on one country to another country, show info between the two