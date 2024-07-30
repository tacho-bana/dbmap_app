document.addEventListener('DOMContentLoaded', function () {
  fetch('http://127.0.0.1:8000/data')
      .then(response => response.json())
      .then(data => {
          var beerSelect = document.getElementById("beer-select");
          data.beers.forEach(beer => {
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
                      .filter(bb => bb.beer_id == selectedBeerId)
                      .map(bb => data.bars.find(bar => bar.id == bb.bar_id));
                  bars.forEach(bar => {
                      // 座標のパース（座標の順序を修正）
                      var latlng = bar.location
                          .replace("POINT(", "")
                          .replace(")", "")
                          .split(", ");
                      var lat = parseFloat(latlng[0]);
                      var lng = parseFloat(latlng[1]);

                      if (!isNaN(lat) && !isNaN(lng)) {
                          // マーカーを地図に追加
                          var marker = L.marker([lat, lng])
                              .addTo(map)
                              .bindPopup(
                                  `<b>${bar.name}</b><br><a href="${bar.url}" target="_blank">${bar.url}</a>`
                              );

                          // 店舗リストに追加
                          var barItem = document.createElement("div");
                          barItem.className = "bar-item";
                          barItem.innerHTML = `<b>${bar.name}</b><br><a href="${bar.url}" target="_blank">${bar.url}</a>`;
                          barItem.addEventListener("click", function () {
                              showBarBeers(bar.id, data);
                              marker.openPopup();
                              map.setView([lat, lng], 15); // クリック時にマップをズームしてマーカーを表示
                          });
                          barList.appendChild(barItem);
                      } else {
                          console.error("Invalid coordinates for bar:", bar);
                      }
                  });
              }
          });
      })
      .catch(error => console.error('Error fetching data:', error));
});

function showBarBeers(barId, data) {
  var selectedBarBeers = document.getElementById("selected-bar-beers");
  selectedBarBeers.innerHTML = "";

  var barBeers = data.bar_beers.filter(bb => bb.bar_id == barId);
  barBeers.forEach(barBeer => {
      var beer = data.beers.find(beer => beer.id == barBeer.beer_id);
      if (beer) {
          var beerItem = document.createElement("div");
          beerItem.className = "beer-item";
          beerItem.innerHTML = `<p>${beer.name}</p>`;
          selectedBarBeers.appendChild(beerItem);
      }
  });
}

// マップの初期設定
var map = L.map('map').setView([35.6895, 139.6917], 13); // 東京の緯度経度を使用
L.tileLayer("https://osm.gdl.jp/styles/osm-bright-ja/{z}/{x}/{y}.png", {
attribution:
  '&copy; <a href="https://osm.org/copyright">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>',
}).addTo(map);
