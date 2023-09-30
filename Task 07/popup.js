document.addEventListener('DOMContentLoaded', function () {
   const currentDate = new Date().getHours();
   let greetingMessage;

   if (currentDate >= 0 && currentDate < 6) {
       greetingMessage = 'Good Morning :)';
   } else if (currentDate >= 6 && currentDate < 12) {
       greetingMessage = 'Good Morning :)';
   } else if (currentDate >= 12 && currentDate < 18) {
       greetingMessage = 'Good Afternoon';
   } else {
       greetingMessage = 'Good Evening :)';
   }

   const greetingElement = document.getElementById("greetingMessage");
   greetingElement.textContent = greetingMessage;
});

document.getElementById("getWeatherBtn").addEventListener("click", getWeather);

function getWeather() {
  const locationInput = document.getElementById("locationInput").value;
  const apiKey = "b547460e07c7a4c16b455b7d4ee913ee";
  const apiUrl = `https://api.openweathermap.org/data/2.5/weather?q=${locationInput}&appid=${apiKey}`;

  fetch(apiUrl)
    .then(response => {
      if (!response.ok) {
        throw new Error('Network Error');
      }
      return response.json();
    })
    .then(data => {
      const weatherInfo = document.getElementById("weatherInfo");
      const location = document.getElementById("location");
      location.textContent = data.name;
      const temperature = document.getElementById("temperature");
      temperature.textContent = Math.round((data.main.temp - 273.15) * 100) / 100;;
      const weatherDescription = document.getElementById("weatherDescription");
      weatherDescription.textContent = data.weather[0].description;
      const humidity= document.getElementById("humidity");
      humidity.textContent = data.main.humidity;
      const weather = document.getElementById("weather");
      weather.textContent = data.weather[0].main;



    })
    .catch(error => {
      const weatherInfo = document.getElementById("weatherInfo");
      weatherInfo.innerHTML = `<p>Failed to fetch weather data. Please check the location.</p>`;
    });
}
