// # ADICIONAR EVENT LISTENER
const btn = document.querySelector('#btn');

btn.addEventListener('click', (e) => {
  e.preventDefault();
  console.log('Clicou no botão');
});

// # EVENTOS COMUNS
// click, submit, input, keydown, keyup, mouseover, mouseout
