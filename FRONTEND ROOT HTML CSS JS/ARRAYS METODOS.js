// # MÉTODOS ARRAY
const arr = [1, 2, 3, 4];

arr.push(5); // Adiciona no fim
arr.pop(); // Remove do fim

const dobro = arr.map(x => x * 2);
const pares = arr.filter(x => x % 2 === 0);
const soma = arr.reduce((acc, x) => acc + x, 0);
const busca = arr.find(x => x > 2);
