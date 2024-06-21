function calcularMassaGorda() {
    var peso = parseInt(document.getElementById('weigth').value, 10);
    var percGordura = parseInt(document.getElementById('percFat').value, 10);
    document.getElementById('fat').innerHTML =  (percGordura/100) * peso;
  }
function calcularMassaMuscular() {
    var peso = parseInt(document.getElementById('weigth').value, 10);
    var percMusculo = parseInt(document.getElementById('percMuscle').value, 10);
    document.getElementById('muscle').innerHTML = (percMusculo/100) * peso;
  }