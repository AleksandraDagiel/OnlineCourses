// 1.Object

var customer = {
    firstName: 'John',
    lastName: 'Smith'
}

console.log(customer.firstName)

// Dot notation
customer.firstName = "Mike"
// Bracket notation
customer['lastName'] = "Silver"
console.log(customer['firstName'], customer.lastName)
console.log(`${customer.firstName} ${customer.lastName}`)

// 2. Arrays
var car =["Volvo", "Toyota", "Tesla"]
console.log(car[0])
car[1] = "BMW"
console.log(car[1])