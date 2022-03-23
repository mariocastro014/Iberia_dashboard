function getData() {
  var data = fetch('/incident-critic', {
    method: "GET"
  }).then(function(response){
    response.json().then(function(data){
        console.log(data)
    })
  })
};