let dbname = 'cardDB';
let sl = "http://localhost:8000/product/api/single/";
let ml = "http://localhost:8000/product/api/plural/";

function addToCart(id) {
    let str = "6:1,7:2";
    fetch(ml+str)
        .then((response) => {
            return response.text();
        }).then((res) => {
            console.log(res);
        })
}
/*
let ind = items.findIndex(it => it.id == id);
items.splice(ind, 1);
fetch(url)
    .then((response) => {
        return response.text();
    })
    .then((res) => {
        products = JSON.parse(res);
        loadData();
    })
*/




