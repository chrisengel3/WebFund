var floor = Math.floor() 
var ceil = Math.ceil()
var random = Math.random()

function d6(){
    var max = 6
    var min = 1
    var roll = math.floor(math.random() + (max - min + 1) + min);
        return roll

}

var playerRoll = d6()
console.log(playeRoll)



var lifesAnswers = [
    "It is certain.",
    "It is decidedly so.",
    "Without a doubt.",
    "Yes – definitely.",
    "You may rely on it.",
    "As I see it, yes.",
    "Most likely.",
    "Outlook good.",
    "Yes.",
    "Signs point to yes.",
    "Reply hazy, try again.",
    "Ask again later.",
    "Better not tell you now.",
    "Cannot predict now.",
    "Concentrate and ask again.",
    "Don't count on it.",
    "My reply is no.",
    "My sources say no.",
    "Outlook not so good.",
    "Very doubtful."
];

function magic8(lifesAnswers){
    var max = lifesAnswers.length
    var min = 0
    var predict = Math.floor(Math.random() * (max - min) + min);
    return lifesAnswers[predict]
}

var prediction = magic8(lifesAnswers)
console.log(prediction)



