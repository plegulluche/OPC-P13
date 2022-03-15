//AUTOCOMPLETE FUNCTION WITH AUTOCOMPLETE-JS LIBRARY
new Autocomplete('#autocomplete', {

                search : input =>{
                    const url = `/search/?city=${input}`
                    return new Promise((resolve,reject) =>{
                        fetch(url)
                        .then(response => response.json())
                        .then(data => {
                            resolve(data.data)
                        
                        }).catch(error => {
                            reject(error)
                        })
                    })
                }
            })

//SELECTORS
const inputField = document.querySelector('#input-text');
const submitButton = document.querySelector('#submit');
const imgSelector = document.querySelector('#img')
const firstCardGroupSelector = document.querySelector('#firstcardgroup')
const secondCardGroupSelector = document.querySelector('#secondcardgroup')

//FOR THIS SELECTOR WE ARE USING JS-COOKIE LIBRARY
const csrftoken = Cookies.get('csrftoken');


//LISTENERS 
submitButton.addEventListener('click', getInput)

//CONST

const nbForCloudy = [2,3,4,5]
const nbCloudSun = [1,235]
const nbSun = [0]
const nbSunSnow = [220,221,222]
const nbSunRain = [210,211,212]
const nbCloudRain = [10,11,13,16,30,31,12,14,15,32,40,41,42,43,44,45,46,47,48]
const nbStorm = [100,101,102,103,104,105,106,107,108,120,121,122,
                123,124,125,126,127,128,130,131,132,133,134,135,136,137,138]
const nbSnow = [20,21,22,60,61,62,63,64,65,66,67,68,70,71,72,73,74,75,76,77,78,142]
const days = ["Dimanche","Lundi","Mardi","Mercredi","Jeudi","Vendredi","Samedi"]

//FUNCTIONS

function createMeteoCard(daystr,imagecode,tmin,tmax,cardnumber) {
    let divCard = document.createElement("div");
    divCard.setAttribute('class','card');
    divCard.innerHTML = `<div class="card-header">${daystr}</div><img src="\{\% static 'images/${imagecode}.svg' \%\}"  class="card-img-top"><div class='card-footer'><small class='text-muted'>Min : ${tmin}°/Max : ${tmax}°</small></div>`;
    if (cardnumber > 7) {
        secondCardGroupSelector.appendChild(divCard);
    }else {
        firstCardGroupSelector.appendChild(divCard);
    }
}

function getFirstDayAsNumber() {
    let today = new Date();
    let dayAsNumb = today.getDay();
    return dayAsNumb;
}


function arrayForWeek() {
    let today = new Date();
    let todayAsNumb = today.getDay();
    let baseWeekArray = [1,2,3,4,5,6,7]
    let temp_array = []
    let day_str_array = []
    while (temp_array.length < 14) {
        for (number in baseWeekArray) {
            if (number >= todayAsNumb) {
                temp_array.push(number)
            }
        }
        for (number in baseWeekArray) {
            if (number < todayAsNumb) {
                temp_array.push(number)
            }
    }}
    temp_array.forEach(function(item,index) {
        day_str_array.push(days[parseInt(item)])
    })
    return day_str_array
}



function getImgCode(weathercode) {
    console.log(typeof weathercode,weathercode)
    if (nbForCloudy.includes(weathercode)) {
        console.log("TRUE")
        return 1;
    } else if (nbCloudSun.includes(weathercode)) {
        console.log("TRUE")
        return 2;
    } else if (nbSunSnow.includes(weathercode)) {
        console.log("TRUE")
        return 3;
    } else if (nbSunRain.includes(weathercode)) {
        console.log("TRUE")
        return 4;
    } else if (nbCloudRain.includes(weathercode)) {
        console.log("TRUE")
        return 5;
    } else if (nbStorm.includes(weathercode)) {
        console.log("TRUE")
        return 6;
    } else if (nbSnow.includes(weathercode)) {
        console.log("TRUE")
        return 7;
    } else {
        console.log("TRUE")
        return 8;
    } 
}

//CREATE IMG CARD FOOTER 
function createCardFooter(tmin,tmax) {
    let divCard = document.createElement("div");
    divCard.setAttribute('class','card-footer');
    let smallTag = document.createElement('small');
    smallTag.setAttribute('class','text-muted');
    smallTag.textContent = `${tmin}//${tmax}`;
    divCard.appendChild(smallTag)
}

//ASYNC REQUEST FOR METEO DATA TO BACKEND
function getInput(event) {
    event.preventDefault();
    fetch('meteo-week/',{
        method:'POST',
        mode: 'same-origin',
        body:inputField.value,
        headers: {

            "X-CSRFToken": csrftoken,
            
          }
        
    })
    .then(response => {
        return response.json()
    })
    .then(data => {
        let meteo = data.meteo_week;
        let obj_array = [
            meteo.day0,meteo.day1,meteo.day2,
            meteo.day3,meteo.day4,meteo.day5,
            meteo.day6,meteo.day7,meteo.day8,
            meteo.day9,meteo.day10,meteo.day11,
            meteo.day12,meteo.day13
            ]
        obj_array.forEach(day => {
            console.log(typeof day['weather'])
            console.log(day['weather'])
            let weekArray = arrayForWeek()
            console.log(weekArray)
            let image = getImgCode(day['weather'])
            console.log(day['weather'])
            createMeteoCard(weekArray[day['day']],image,day['tmin'],day['tmax'],day['day'])
            for (let key in day) {
                console.log(`${key}: ${day[key]}`);

            }
        })
        
        
        
    }).catch(error => {
        console.log(error);
    })
    
}