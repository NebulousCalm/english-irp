const update_aqi_form = () =>{
    const city = document.getElementById('city');
    const state = document.getElementById('state');

    if(city && state) {
        document.getElementById('cityInput').value = city.innerHTML;
        document.getElementById('stateInput').value = state.innerHTML;
    }

    const wind_direction = document.getElementById('wind_direction').dataset.direction;
    document.getElementById('rotate').style.transform = `rotate(${wind_direction}deg)`;
}