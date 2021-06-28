
var ronniePizza = {
    "crust" : "thin crust",
    "sauce" : "alfredo",
    "cheese" : "white cheddar",
    "toppings" : ['macaroni', 'bacon', 'avocado'],
    "slices" : 0,
    "vegetarian" : false,
    "pizzaInfo" : function() {
        console.log(this)
        console.log("crust: " + this.crust)
        console.log("sauce: " + this.sauce)
        console.log("cheese: " + this.cheese)
        console.log("toppings: " + this.toppings)
        console.log("slices: " + this.slices)
        console.log("vegetarian: " + this.vegetarian)
    }
}
ronniePizza.pizzaInfo()