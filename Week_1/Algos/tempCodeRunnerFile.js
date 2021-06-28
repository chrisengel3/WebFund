

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
    var max = lifesAnswers.length - 1
    var min = 0
    var predict = Math.floor(Math.random() * (max - min) + min);
    return lifesAnswers[predict]
}

var prediction = magic8(lifesAnswers)
console.log(prediction)


