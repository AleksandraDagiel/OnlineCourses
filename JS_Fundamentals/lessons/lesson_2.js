// Concatination and Interpolation
var price = 50
var itemName = "Cup"

//concatination
var messageToPrint = "The price for your " + itemName +  "is " + price +  "dollars"
console.log(messageToPrint)

//interpolation
var messageToPrint2 = `The price for your ${itemName} is ${price} dollars`
console.log(messageToPrint2)