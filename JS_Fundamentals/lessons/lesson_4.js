// 1. Relational or comparison operators

var result = 10 > 5
console.log(result)

// 2. Equality operators

var x = 1 
console.log(x == 1)       // ok
console.log(x == "1")    // ok, lose comparison
console.log(x === "1")  // nok, strict comparison, checks data type
console.log(x === 1)   // ok 