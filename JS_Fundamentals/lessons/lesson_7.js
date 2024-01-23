// Loops

// For Loop: 
// statement1 - start, 
// statement2 - how long to run/ when to stop
// statement3 - what do do after every cycle
// for (statement1; statement2; statement3){

// }

// 1. for i loop
for(let i=0; i<5; i++){
    (console.log('Hello World!' + i))
}

// 2. for of loop
var cars = ["Volvo", "Toyota", "Tesla"]
for(let car of cars){
    console.log(car)
    if(car == "Toyota"){
        break
    }
}

// 3. ES6 syntax for each loop
cars.forEach( car => {
    console.log(car)
})
