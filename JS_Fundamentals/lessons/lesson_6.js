// Conditional statement

// if(condition){
     // execute some code here
// }else{
     // execute some code here
// }

// If hour between 6 and 12 print ""Good Morning"
// If hour between 12 and18 print "Good Afternoon"
// Otherwise: Good evening

var hour = 5

if(6 <= hour && hour < 12){
    console.log("Good Morning.")
}else if(12 <= hour && hour < 18){
    console.log("Good Afternoon.")
}else{
    console.log("Good evening.")
}


var ageIsMoreThanEighteen = true
var isUSCitizen = false

if(ageIsMoreThanEighteen && isUSCitizen){
    console.log('Customer is eligable for DL')
}else{
    console.log('Customer is NOT eligible for DL')
}