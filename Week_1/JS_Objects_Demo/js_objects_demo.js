var string = "whateveryouwantbaby"

var chrisPizza = {
    "crust" : "thin crust",
    "sauce" : "arrabiata",
    "cheese" : "three cheese blend",
    "toppings" : ['spicy pep', 'basil', 'red pep flakes'],
    "slices" : 8,
    "vegetarian" : false,
    "pizzaInfo" : function() {
        console.log("crust: " + this.crust)
        console.log("sauce: " + this.sauce)
        console.log("cheese: " + this.cheese)
        console.log("toppings: " + this.toppings)
        console.log("slices: " + this.slices)
        console.log("vegetarian: " + this.vegetarian)
    }
}
chrisPizza.pizzaInfo()


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