// Functions
// Declarative function
function helloOne(){
    console.log("Hello one!")
}
helloOne()

// Anonymus function
var helloTwo = function(){
    console.log("Hello two!")
}
helloTwo()

// ES6 function syntax or arrow function
var helloThree = () => {
    console.log("Hello three!")
}
helloThree()

// Function with arguments
function printName(name, lastName){
    console.log(name + ' ' + lastName)
}
printName("John", "Smith")

// Function with return
function multiplyByTwo(number){
    var result = number * 2
    return result
}
var myResult = multiplyByTwo(5)
console.log(myResult)

// Import function (added "type": "module", to package.json
// and export in function from another method)
import { printAge } from '../helpers/printHelper.js'
printAge(5)

// Import everything
import * as helper from '../helpers/printHelper.js'
helper.printAge(4)