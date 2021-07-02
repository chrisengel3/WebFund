async function getDitto(){
    var response = await fetch("https://pokeapi.com/api/v2/pokemon/ditto")
    var data = await response.json
    console.log(data)
}

getDitto()