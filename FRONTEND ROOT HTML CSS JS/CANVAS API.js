// # SETUP CANVAS
const canvas = document.getElementById('meuCanvas');
const ctx = canvas.getContext('2d');

// # RETÂNGULO
ctx.fillStyle = 'red';
ctx.fillRect(10, 10, 100, 100);

// # CÍRCULO
ctx.beginPath();
ctx.arc(200, 50, 40, 0, 2 * Math.PI);
ctx.stroke();
