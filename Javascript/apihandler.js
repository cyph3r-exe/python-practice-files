const URL = "https://cat-fact.herokuapp.com/facts";

const getFacts = async () => {
    console.log('geting facts ......');
    let promise = fetch(URL);
    console.log((await promise).status);
    let firstData = (await promise).json();
    console.log(firstData);

};