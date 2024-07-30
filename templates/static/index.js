var map = L.map("map").setView([35.6074, 139.7358], 15);

L.tileLayer("https://osm.gdl.jp/styles/osm-bright-ja/{z}/{x}/{y}.png", {
  attribution:
    '&copy; <a href="https://osm.org/copyright">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>',
}).addTo(map);

fetch("../data.json")
  .then((response) => response.json())
  .then((data) => {
    var beerSelect = document.getElementById("beer-select");
    data.beers.forEach((beer) => {
      var option = document.createElement("option");
      option.value = beer.id;
      option.text = beer.name;
      beerSelect.add(option);
    });

    beerSelect.addEventListener("change", function () {
      var selectedBeerId = this.value;
      var barList = document.getElementById("bar-list");
      var selectedBarBeers = document.getElementById("selected-bar-beers");
      barList.innerHTML = "";
      selectedBarBeers.innerHTML = "";
      map.eachLayer(function (layer) {
        if (layer instanceof L.Marker) {
          map.removeLayer(layer);
        }
      });

      if (selectedBeerId) {
        var bars = data.bar_beers
          .filter((bb) => bb.beer_id == selectedBeerId)
          .map((bb) => data.bars.find((bar) => bar.id == bb.bar_id));
        bars.forEach((bar) => {
          var latlng = bar.location
            .replace("POINT(", "")
            .replace(")", "")
            .split(", ");
          var marker = L.marker([parseFloat(latlng[0]), parseFloat(latlng[1])])
            .addTo(map)
            .bindPopup(
              `<b>${bar.name}</b><br><a href="${bar.url}" target="_blank">${bar.url}</a>`
            );
          var barItem = document.createElement("div");
          barItem.className = "bar-item";
          barItem.innerHTML = `<b>${bar.name}</b><br><a href="${bar.url}" target="_blank">${bar.url}</a>`;
          barItem.addEventListener("click", function () {
            showBarBeers(bar.id);
            marker.openPopup();
          });
          barList.appendChild(barItem);
        });
      }
    });

    function showBarBeers(barId) {
      var selectedBarBeers = document.getElementById("selected-bar-beers");
      selectedBarBeers.innerHTML = "";
      var barBeers = data.bar_beers
        .filter((bb) => bb.bar_id == barId)
        .map((bb) => data.beers.find((beer) => beer.id == bb.beer_id));

      if (barBeers.length > 0) {
        var heading = document.createElement("h4");
        heading.textContent = "提供ビール:";
        selectedBarBeers.appendChild(heading);
        var beerList = document.createElement("ul");
        barBeers.forEach((beer) => {
          var beerItem = document.createElement("li");
          beerItem.textContent = beer.name;
          beerList.appendChild(beerItem);
        });
        selectedBarBeers.appendChild(beerList);
      }
    }
  });