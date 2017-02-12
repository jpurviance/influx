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

function style(feature) {
    var styl = {
        weight: 2,
        opacity: 1,
        color: 'white',
        dashArray: '3',
        fillOpacity: 0.3
    };

    // var fillCol = '#ff0000';

    // if (fillCol != null) {
    //     styl.fillColor = fillCol;
    // }

    return styl;
}

function onEachFeature(feature, layer) {
    layer.on('click', function (e) {

    })
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

countries.addTo(map);

function colorCountries(data) {
    map.removeLayer(countries);

    console.log("cash me ousside how bow dah");

    function style(feature) {
        var styl = {
            weight: 2,
            opacity: 1,
            color: 'white',
            dashArray: '3',
            fillOpacity: 0.75
        };

        // var fillCol = '#ff0000';
        var dataArr = data[feature.properties.name];
        if (dataArr != null) {
            var fillCol = dataArr[dataArr.length - 1];

            if (fillCol != null || fillCol != "") {
                styl.fillColor = fillCol;
            }
        }


        return styl;
    }

    countries = L.geoJson(countryData, {
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

    countries.addTo(map);
}

//click on any other country, show info to banned countries (in those countries)
//click on one country to another country, show info between the two