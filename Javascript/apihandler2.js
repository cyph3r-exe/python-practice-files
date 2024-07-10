const URL = "https://cat-fact.herokuapp.com/facts";

const iWantFacts = async () => {
    console.log('geting facts ......');
    let response = await fetch(URL);
    let data = response.json();
    console.log(data[0].text);
};