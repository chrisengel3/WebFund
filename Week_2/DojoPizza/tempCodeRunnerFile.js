var pizzaML = {
    crust : "deep dish",
    sauce : "traditional",
    cheese : "mozzarella",
    toppings : ['pepperoni', 'sausage']
}
var pizzaVG = {
    crust : 'hand tossed',
    sauce : 'marinara',
    cheese : ['mozzarella', 'feta'],
    toppings : ['mushrooms', 'olives', 'onions']
}
var pizzaCL = {
    crust : 'thin',
    sauce : 'alfredo',
    cheese : ['mozzarella', 'cheddar'],
    toppings : ['mushrooms', 'olives', 'onions']
}
var pizzaSP = {
    crust : 'GF',
    sauce : 'arrabiata',
    cheese : ['asiago', 'feta'],
    toppings : ['basil', 'mozzarella', 'pepperoni']
}

var pizzas = [pizzaML, pizzaVG, pizzaCL, pizzaSP]

function pizza(pizzas){
    var max = pizzas.length
    var min = 0
    var chefsChoice = Math.floor(Math.random() * (max - min) + min);
    return pizzas[chefsChoice]
}

var pizzaPick = pizza(pizzas)
console.log(pizzaPick)